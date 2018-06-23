"""
import telegram
bot = telegram.Bot(token='524706088:AAGq3De-XCF-vb3-Z5NvScaoULoMAlosYO4')
print(bot.get_me())
"""


from telegram.ext import Updater
updater = Updater(token='524706088:AAGq3De-XCF-vb3-Z5NvScaoULoMAlosYO4')
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                  level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Я чат-ботик, здравствуй, гуманоид")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Бро, " + update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


updater.start_polling()