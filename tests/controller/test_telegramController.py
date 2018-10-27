from AbstractTestClass import AbstractTestClass
from TelegramController import TelegramController
from AbstractView import AbstractView
import datetime


class TestTelegramController(AbstractTestClass):

    def test_text_message_all_events_cinema_today(self, session, clear_data):
        # Fulfilling the database for future making answer - film tomorrow
        start_time = datetime.datetime.now().timestamp() + 86200
        finish_time = datetime.datetime.now().timestamp() + 86300
        event = self.create_event_yandexafishacinema_cinema_venom(start_time, finish_time)
        session.add(event)
        session.commit()
        # Creating objects that I will use in calling method under testing
        controller = TelegramController()
        controller.session = session
        test_bot = TestBot()
        test_update_from_telegram = TestUpdateFromTelegram(text="Куда сходить в кино завтра",
                                                           chat_id=234,
                                                           effective_user_id=555,
                                                           channel_post=None)
        # Check result of calling "_text_message" method (this method pass result to the 'test_bot' object)
        controller._text_message(test_bot, test_update_from_telegram)
        assert test_bot.text == AbstractView.convert_timestamp_to_date_and_time(start_time) + \
               "<a href='https://afisha.yandex.ru/13Iaf1251.jpg' target='_blank'>.</a>\n" \
               "<a href='https://afisha.yandex.ru/moscow/cinema/venom-2018' target='_blank'>Веном</a>"


class TestUpdateFromTelegram:

    def __init__(self, text, chat_id, effective_user_id, channel_post):
        self.message = TestMessage(text, chat_id)
        self.effective_user = TestEffectiveUser(effective_user_id)
        self.channel_post = channel_post


class TestMessage:

    def __init__(self, text, chat_id):
        self.text = text
        self.chat_id = chat_id


class TestEffectiveUser:

    def __init__(self, effective_user_id):
        self.id = effective_user_id


class TestBot:

    def __init__(self):
        self.chat_id = None
        self.parse_mode = None
        self.text = None
        self.reply_markup = None
        self.disable_web_page_preview = None

    def send_message(self, chat_id=None, parse_mode=None, text=None, reply_markup=None, disable_web_page_preview=None):
        self.chat_id = chat_id
        self.parse_mode = parse_mode
        self.text = text
        self.reply_markup = reply_markup
        self.disable_web_page_preview = disable_web_page_preview
