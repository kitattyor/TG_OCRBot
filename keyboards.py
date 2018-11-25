from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from ocr import OCR_Supported_Languages as lang

def alphabeticalSelection():
    kb_markup = [[InlineKeyboardButton('A-E', callback_data='AtoE')], 
                [InlineKeyboardButton('F-K', callback_data='FtoK')], 
                [InlineKeyboardButton('L-Z, and numbers', callback_data='LtoZ,#')]]
    return InlineKeyboardMarkup(kb_markup)

def AtoE():
    kb_markup = [[InlineKeyboardButton("Arabic", callback_data=lang.Arabic), InlineKeyboardButton("Bulgarian", callback_data=lang.Bulgarian)],
    [InlineKeyboardButton("Chinese Simplified", callback_data=lang.Chinese_Simplified), InlineKeyboardButton("Chinese Traditional", callback_data=lang.Chinese_Traditional)],
    [InlineKeyboardButton("Croatian", callback_data=lang.Croatian), InlineKeyboardButton("Danish", callback_data=lang.Danish)],
    [InlineKeyboardButton("Dutch", callback_data=lang.Dutch), InlineKeyboardButton("English", callback_data=lang.English)],
    [InlineKeyboardButton("🔙", callback_data="bk")]]
    return InlineKeyboardMarkup(kb_markup)

def FtoK():
    kb_markup = [[InlineKeyboardButton("Finnish", callback_data=lang.Finnish), InlineKeyboardButton("French", callback_data=lang.French)],
    [InlineKeyboardButton("German", callback_data=lang.German), InlineKeyboardButton("Greek", callback_data=lang.Greek)],
    [InlineKeyboardButton("Hungarian", callback_data=lang.Hungarian), InlineKeyboardButton("Korean", callback_data=lang.Korean)],
    [InlineKeyboardButton("Italian", callback_data=lang.Italian), InlineKeyboardButton("Japanese", callback_data=lang.Japanese)],
    [InlineKeyboardButton("🔙",callback_data="bk")]]
    return InlineKeyboardMarkup(kb_markup)

def LtoZandNumbers():
    kb_markup = [[InlineKeyboardButton("Norwegian", callback_data=lang.Norwegian), InlineKeyboardButton("Polish", callback_data=lang.Polish)],
    [InlineKeyboardButton("Portuguese", callback_data=lang.Portuguese), InlineKeyboardButton("Russian", callback_data=lang.Russian)], 
    [InlineKeyboardButton("Slovenian", callback_data=lang.Slovenian), InlineKeyboardButton("Spanish", callback_data=lang.Spanish)],
    [InlineKeyboardButton("Swedish", callback_data=lang.Swedish), InlineKeyboardButton("Turkish", callback_data=lang.Turkish)],
    [InlineKeyboardButton("0-9", callback_data="num")],
    [InlineKeyboardButton("🔙", callback_data="bk")]]
    return InlineKeyboardMarkup(kb_markup)