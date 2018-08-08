# -*- coding: utf-8 -*-

import argparse
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from User import User
from Router import Router
from TelegramView import TelegramView
# it's needed for operation relationship between User, Event and Rating
from Event import Event
from Rating import Rating

# Параметры для конфига системы
telegram_token = "524706088:AAGq3De-XCF-vb3-Z5NvScaoULoMAlosYO4"

# Extracting parameters from command line
# We are expecting launch by command like: 'python eventer/telegram_bot.py --log=INFO'
parser = argparse.ArgumentParser(description='parser of arguments of command line for telegram bot launch')
parser.add_argument('--log', action='store', dest='loglevel', help='level of logging for this launch')
args = parser.parse_args()

# Check for logging level
log_level = args.loglevel if args.loglevel else "INFO"
numeric_level = getattr(logging, log_level.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError("Invalid log level: {}".format(log_level))

# Logging tuning
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(module)s - %(funcName)s - %(message)s',
                    level=numeric_level
                    # filename='/tmp/telegram_bot.log'
                    )

# Создаем основные объекты для работы с телеграмом
updater = Updater(token=telegram_token)
dispatcher = updater.dispatcher

# Запуск сессии с базой данных
user_for_mysql = "eventer"
password_for_mysql = "Nhgbf86jmnIK"
engine = sqlalchemy.create_engine(
    "mysql://" + user_for_mysql + ":" + password_for_mysql + "@localhost/eventer?charset=utf8", echo=False)
Session = sessionmaker(bind=engine)
session = Session()


def extract_telegram_user_id(update_from_telegram):
    """
    Extract telegram user id from Update
    :param update_from_telegram:
    :return: str or None
    """
    if update_from_telegram.effective_user:
        user_telegram_id = str(update_from_telegram.effective_user.id)
    else:
        user_telegram_id = None
    return user_telegram_id


# Initialize user
def get_user(update_from_telegram, session):
    logging.debug("Enter to the method")
    user_telegram_id = extract_telegram_user_id(update_from_telegram)
    logging.info('user telegram id has extracted = %s', user_telegram_id)
    user = session.query(User).filter(User._telegram_id == user_telegram_id).first()
    logging.info('user from database: %s', user)
    if not user:
        user = User(telegram_id=user_telegram_id)
        session.add(user)
        session.commit()
        user = session.query(User).filter(User._telegram_id == user_telegram_id).first()
        logging.info('Create a new user in database: %s', user)
    return user


# Handler for first command - start
def start_command(bot, update_from_telegram):
    logging.info('User starts work with chat-bot: start_command')
    user = get_user(update_from_telegram, session)
    router = Router(user_message_text="start", session_with_db=session, user=user, type_user_message="start")
    answer_maker = router.get_answer_maker()
    bot.send_message(chat_id=update_from_telegram.message.chat_id,
                     text=answer_maker.get_answer())


# Handler for text message
def text_message(bot, update_from_telegram):
    user_message_text = update_from_telegram.message.text
    logging.info('User write text message: %s', user_message_text)
    user = get_user(update_from_telegram, session)

    # Handle request
    router = Router(user_message_text=user_message_text, session_with_db=session, user=user,
                    type_user_message="text_message")
    logging.debug("Router has been created: %s", router)
    answer_maker = router.get_answer_maker()
    logging.info('Answer maker is: %s', answer_maker)
    data_for_answer = answer_maker.get_answer()
    logging.info('Data for answer from answer maker: %s', data_for_answer)
    text_answer = TelegramView.make_text_answer_from_data(data_for_answer)
    logging.debug('Text for answer: %s', text_answer)
    buttons_answer = TelegramView.get_buttons_for_message(data_for_answer)
    image_preview = TelegramView.is_not_allowed_images_preview(data_for_answer)
    status_of_sending_message = bot.send_message(chat_id=update_from_telegram.message.chat_id,
                                                 parse_mode='HTML',
                                                 text=text_answer,
                                                 reply_markup=buttons_answer,
                                                 disable_web_page_preview=image_preview)
    logging.info("Status of sending message from telegram: %s", status_of_sending_message)


# Создаем обработчики событий для телеграма
start_command_handler = CommandHandler('start', start_command)
text_message_handler = MessageHandler(Filters.text, text_message)
# Добавляем обработчики событий для телеграма в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Запускаем бесконечный цикл получения и обработки новых сообщений из телеграма
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
