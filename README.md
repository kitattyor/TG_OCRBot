# TG_OCRBot

#### How do I use this bot? 

This is a telegram bot. Download telegram for your device [here](https://telegram.org/) and set up an account. Search for ocrTltorBot on telegram or click here [@ocrTltorBot](https://www.t.me/ocrTltorBot) if you are using telegram on your browser.

##### What does this bot do?

This bot extracts text (or numbers) from the images sent to it in 20+ languages using the [OCR.SPACE API](https://ocr.space/). It can also translate the received text to English (if it is in some other language). The translation is done using the Microsoft Translator Text API.

###### Useful commands:

* /start - To start the bot 
* /v or /ver or /version - to check the version number
* /lang - to set the language for OCR
* /tr - to translate the OCRed text to English (if in some other language)

This service runs on [Heroku](https://www.heroku.com/). 

##### For developers

To run this bot on your local system, first get API keys from [@BotFather](https://www.t.me/botfather), [OCR.SPACE](https://ocr.space/) and [Microsoft Azure](https://azure.microsoft.com/en-us/). Store the keys in your system environment variables with the following commands on Windows.

```
setx TELEGRAM_TOKEN <tg_token>
setx OCR_SPACE_TOKEN <ocr_space_token>
setx MS_TRANSLATOR_KEY <translator_key>
```

(On MacOS or Linux systems, you'd need to edit the ~/.bash_profile file. Please refer to the relevant documentation)

Then run bot.py

##### Further improvements:

* Multiple language selection for translation of OCRed text.
* More work can be done on the UX to make usage simpler.
* Add user questionnaire (eg: ask if the OCR and translation were Perfect, Acceptable or Terrible) to be used as a log.  
* Create searchable PDF option

Licensed under the [MIT License](LICENSE)