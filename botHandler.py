from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, ChatMigrated, NetworkError)
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

import logging
import time
import requests
import json
import os
from decorated_messages import BotMessages as msg
from ocr import OCRSpace, OCR_Supported_Languages
import keyboards as kb
from translate import TranslationHandlerClass, Translation

version = '0.3.1811'

# Example of your code beginning
#           Config vars
bot_token = os.environ['TELEGRAM_TOKEN']
ocr_space_api_token = os.environ['OCR_SPACE_TOKEN']
#

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def replyToLastMessage(*args):
    #bot, update, theReply
    bot, update, theReply = args
    bot.send_message(chat_id=update.message.chat_id, text=theReply, 
                    reply_to_message_id=update.message.message_id)

def sendMessage(*args):
    #bot, message
    bot, update, message = args
    bot.send_message(chat_id=update.message.chat_id, text=message)


def start(bot, update):
    sendMessage(bot, update, msg.welcome_message)

def unkown(bot, update):
    replyToLastMessage(bot, update, "I don't recognise that command:(")

def notPhoto(bot, update):
    replyToLastMessage(bot, update, "Not an image. Please upload images only.")

def isPhoto(bot, update):
    sendMessage(bot, update, "Received the image. Please wait for processing. I'll send you the contents of the text in the image shortly.")
    #print(photo) #log
    photo = update.message.photo[-1]
    start_time = time.time()
    #print(bot.getFile(photo.file_id))
    hostURL = bot.getFile(photo.file_id).file_path
    #print(hostURL)

    print(OCR_Supported_Languages.SelectedLang)
    ocr_handler_obj = OCRSpace(api_key = ocr_space_api_token, language = OCR_Supported_Languages.SelectedLang)
    res = ocr_handler_obj.ocr_space_url(url=hostURL)
    elapsed_time = time.time()
    text_to_translate = None
    #print(res)
    try:
        text_to_translate = res["ParsedResults"][0]["ParsedText"]
        sendMessage(bot, update, text_to_translate)
        sendMessage(bot, update, "Time taken : {0:.3g} seconds".format(elapsed_time - start_time))
    except BadRequest:
        sendMessage(bot, update, "No letters of currently selected language detected")
        text_to_translate = None
        
    Translation.text = text_to_translate
    if text_to_translate is not None and OCR_Supported_Languages.SelectedLang is not OCR_Supported_Languages.English:
        sendMessage(bot, update, "Send /tr to translate this to english")

def go_translate(bot, update):
    tObj = TranslationHandlerClass()
    translatedText = tObj.translate()
    if translatedText is not None:
        sendMessage(bot, update, translatedText)
    else:
        print('No text')

def getVer(bot, update):
    replyToLastMessage(bot, update, "v{}".format(version))

def readPrivacyStatement(bot, update):
    sendMessage(bot, update, msg.privacy_message)  

def err_callback(bot, update, error):
    try:
        raise error
    except Unauthorized as e:
        # remove update.message.chat_id from conversation list
        print(e)
    except BadRequest as e:
        # handle malformed requests - read more below!
        print(e)
    except TimedOut as e:
        # handle slow connection problems
        print(e)
    except NetworkError as e:
        # handle other connection problems
        print(e)
    except ChatMigrated as e:
        # the chat_id of a group has changed, use e.new_chat_id instead
        print(e)
    except TelegramError as e:
        # handle all other telegram related errors
        print(e)

def inlnKb(bot, update):
    #check query data and pass messages accordingly
    query = update.callback_query
    if query.data == 'AtoE':
        bot.answer_callback_query(query.id)
        bot.edit_message_text(chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text = "Choose",
        reply_markup=kb.AtoE())
    
    elif query.data == 'FtoK':
        bot.answer_callback_query(query.id)
        bot.edit_message_text(chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text = "Choose",
        reply_markup=kb.FtoK())

    elif query.data == 'LtoZ,#':
        bot.answer_callback_query(query.id)
        bot.edit_message_text(chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text = "Choose",
        reply_markup=kb.LtoZandNumbers())

    else:
        print("Nope") 

def langSelect(bot, update):
    print("Inside lang select")
    query = update.callback_query
    bot.answer_callback_query(query.id)
    if query.data == 'num':
        OCR_Supported_Languages.SelectedLang = OCR_Supported_Languages.Arabic
    else:
        OCR_Supported_Languages.SelectedLang = query.data
    print(OCR_Supported_Languages.SelectedLang)
    bot.send_message(chat_id=update.callback_query.message.chat_id, 
        text="I'll search for {} in the image now".format(OCR_Supported_Languages.ExpandedLang[query.data]))

def setLanguage(bot, update):
    #set language for ocr
    sendMessage(bot, update, "The current language is {}".format(OCR_Supported_Languages.ExpandedLang[OCR_Supported_Languages.SelectedLang]))
    bot.send_message(chat_id=update.message.chat_id, text=msg.langSelection_message, reply_markup=kb.alphabeticalSelection())

def backToMainPage(bot, update):
    bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg.langSelection_message, reply_markup=kb.alphabeticalSelection())

def allcommands(bot, update):
    sendMessage(bot, update, msg.available_commands)

def startBot():
    updater = Updater(token=bot_token)
    dispatcher = updater.dispatcher

    #COMMAND HANDLERS
    hStart = CommandHandler('start', start)
    dispatcher.add_handler(hStart)

    hVer = CommandHandler(('ver', 'version', 'v'), getVer)
    dispatcher.add_handler(hVer)

    hPrivacy = CommandHandler('privacy', readPrivacyStatement)
    dispatcher.add_handler(hPrivacy)

    hLangSett = CommandHandler('lang', setLanguage)
    dispatcher.add_handler(hLangSett)

    hAllCommands = CommandHandler(('command', 'commands'), allcommands)
    dispatcher.add_handler(hAllCommands)

    hTranslate = CommandHandler('tr', go_translate)
    dispatcher.add_handler(hTranslate)

    #goes last, after all command handlers
    hUnknown = MessageHandler(Filters.command, unkown)
    dispatcher.add_handler(hUnknown)

    #GENERAL MESSAGE HANDLERS
    hNotImage = MessageHandler(~Filters.photo, notPhoto)
    dispatcher.add_handler(hNotImage)

    hImage = MessageHandler(Filters.photo, isPhoto)
    dispatcher.add_handler(hImage)

    #CALLBACKQUERY HANDLERS (FOR KEYBOARD)
    dispatcher.add_handler(CallbackQueryHandler(inlnKb, pattern=r'^.{4,}$')) #callback data from Main KB is >=4 characters
    dispatcher.add_handler(CallbackQueryHandler(langSelect, pattern=r'^.{3}$')) #languages are generally all 3 characters
    dispatcher.add_handler(CallbackQueryHandler(backToMainPage, pattern='bk')) 
    
    #ERROR HANDLING
    dispatcher.add_error_handler(err_callback) 

    updater.start_polling()