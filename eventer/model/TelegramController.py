# -*- coding: utf-8 -*-

import argparse
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from User import User
from Router import Router
from TelegramView import TelegramView
# it's needed for operation relationship between User, Event and Rating
from Event import Event
from Rating import Rating


class TelegramController:

    def __init__(self, session_with_db=None):
        self.session = session_with_db

    def extract_telegram_user_id(self, update_from_telegram):
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
    def get_user(self, update_from_telegram, session):
        """
        Function to get user from our database by its telegram id
        :param update_from_telegram:
        :param session:
        :return:
        """
        logging.debug("Enter to the method")
        user_telegram_id = self.extract_telegram_user_id(update_from_telegram)
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

    def start_command(self, bot, update_from_telegram):
        """
        Handler for first command - start
        :param bot:
        :param update_from_telegram:
        :return:
        """
        user_message_text = "start"
        type_user_message = "start"
        logging.info('User starts work with chat-bot: start_command')
        user = self.get_user(update_from_telegram, session)
        text_answer, buttons_answer, message_buttons, image_preview = self.handle_request(user_message_text, type_user_message, user)
        if message_buttons:
            buttons_answer = message_buttons
        status_of_sending_message = bot.send_message(chat_id=update_from_telegram.message.chat_id,
                                                     parse_mode='HTML',
                                                     text=text_answer,
                                                     reply_markup=buttons_answer,
                                                     disable_web_page_preview=image_preview)
        logging.info("Status of sending message from telegram: %s", status_of_sending_message)

    def text_message(self, bot, update_from_telegram):
        """
        Handler for text message from telegram user
        :param bot:
        :param update_from_telegram:
        :return:
        """
        user_message_text = update_from_telegram.message.text
        type_user_message = "text_message"
        logging.info('User write text message: %s', user_message_text)
        user = self.get_user(update_from_telegram, session)
        text_answer, buttons_answer, message_buttons, image_preview = self.handle_request(user_message_text, type_user_message, user)
        if message_buttons:
            buttons_answer = message_buttons
        status_of_sending_message = bot.send_message(chat_id=update_from_telegram.message.chat_id,
                                                     parse_mode='HTML',
                                                     text=text_answer,
                                                     reply_markup=buttons_answer,
                                                     disable_web_page_preview=image_preview)
        logging.info("Status of sending message from telegram: %s", status_of_sending_message)

    def callback_button_request(self, bot, update_from_telegram):
        """
        Handler for requests from pushing message buttons (callback buttons or inline buttons)
        We suppose that push this button have to be the same like you write name of the button to the chat with bot
        :param bot:
        :param update_from_telegram:
        :return:
        """
        # Take a callback data from pushed button as a message text
        user_message_text = update_from_telegram.callback_query.data
        type_user_message = "callback_button_message"
        logging.info('User push message button: %s', user_message_text)

        # Take user and data for answer
        user = self.get_user(update_from_telegram, session)
        text_answer, buttons_answer, message_buttons, image_preview = self.handle_request(user_message_text,
                                                                                          type_user_message, user)
        # First priority for buttons showed with message
        if message_buttons:
            buttons_answer = message_buttons

        # After the user presses an inline button, Telegram clients will display a progress bar until you call answer.
        # It is, therefore, necessary to react by calling telegram.Bot.answer_callback_query even if no notification
        # to the user is needed (e.g., without specifying any of the optional parameters).
        update_from_telegram.callback_query.answer()

        # Real answer for user
        status_of_sending_message = bot.send_message(chat_id=update_from_telegram.callback_query.message.chat_id,
                                                     parse_mode='HTML',
                                                     text=text_answer,
                                                     reply_markup=buttons_answer,
                                                     disable_web_page_preview=image_preview)
        logging.info("Status of sending message from telegram: %s", status_of_sending_message)

    def handle_request(self, user_message_text, type_user_message, user):
        router = Router(user_message_text=user_message_text, session_with_db=self.session, user=user,
                        type_user_message=type_user_message)
        logging.debug("Router has been created: %s", router)
        answer_maker = router.get_answer_maker()
        logging.info('Answer maker is: %s', answer_maker)
        data_for_answer = answer_maker.get_answer()
        logging.info('Data for answer from answer maker: %s', data_for_answer)
        text_answer = TelegramView.make_text_answer_from_data(data_for_answer)
        logging.debug('Text for answer: %s', text_answer)
        buttons_answer = TelegramView.get_buttons_for_message(data_for_answer)
        message_buttons = TelegramView.make_message_buttons(data_for_answer)
        image_preview = TelegramView.is_not_allowed_images_preview(data_for_answer)
        return text_answer, buttons_answer, message_buttons, image_preview


if __name__ == "__main__":

    # Параметры для конфига системы
    telegram_token = "524706088:AAGq3De-XCF-vb3-Z5NvScaoULoMAlosYO4"

    # Extracting parameters from command line
    # We are expecting launch by command like: 'python eventer/model/TelegramController.py --log=INFO'
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

    # Start session with database
    user_for_mysql = "eventer"
    password_for_mysql = "Nhgbf86jmnIK"
    engine = sqlalchemy.create_engine(
        "mysql://" + user_for_mysql + ":" + password_for_mysql + "@localhost/eventer?charset=utf8", echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    controller = TelegramController(session)

    # Создаем обработчики событий для телеграма
    start_command_handler = CommandHandler('start', controller.start_command)
    text_message_handler = MessageHandler(Filters.text, controller.text_message)
    callback_button_handler = CallbackQueryHandler(controller.callback_button_request)
    # Добавляем обработчики событий для телеграма в диспетчер
    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(text_message_handler)
    dispatcher.add_handler(callback_button_handler)
    # Запускаем бесконечный цикл получения и обработки новых сообщений из телеграма
    updater.start_polling(clean=True)
    # Останавливаем бота, если были нажаты Ctrl + C
    updater.idle()
