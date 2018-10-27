from AbstractTestClass import AbstractTestClass
from TelegramController import TelegramController
from AbstractView import AbstractView
from Rating import Rating
from User import User
import datetime


class TestTelegramController(AbstractTestClass):

    def test_telegram_text_message_find_events_cinema_tomorrow(self, session, clear_data):
        # Fulfilling the database for future making answer - film tomorrow
        start_time = datetime.datetime.now().timestamp() + 86200
        finish_time = datetime.datetime.now().timestamp() + 86300
        event = self.create_event_yandexafishacinema_cinema_venom(start_time, finish_time)
        session.add(event)
        session.commit()
        # Creating objects that I will use in calling method under testing
        controller = TelegramController()
        controller.session = session
        test_bot = BotTest()
        test_update_from_telegram = UpdateFromTelegramTest(text="Куда сходить в кино завтра",
                                                           chat_id=234,
                                                           effective_user_id=555,
                                                           channel_post=None)
        # Check result of calling "_text_message" method (this method pass result to the 'test_bot' object)
        controller._text_message(test_bot, test_update_from_telegram)
        assert test_bot.text == AbstractView.convert_timestamp_to_date_and_time(start_time) + \
               "<a href='https://afisha.yandex.ru/13Iaf1251.jpg' target='_blank'>.</a>\n" \
               "<a href='https://afisha.yandex.ru/moscow/cinema/venom-2018' target='_blank'>Веном</a>"

    def test_telegram_text_message_fallback(self, session, clear_data):
        # Creating objects that I will use in calling method under testing
        controller = TelegramController()
        controller.session = session
        test_bot = BotTest()
        test_update_from_telegram = UpdateFromTelegramTest(text="Белиберда",
                                                           chat_id=234,
                                                           effective_user_id=555,
                                                           channel_post=None)
        # Check result of calling "_text_message" method (this method pass result to the 'test_bot' object)
        controller._text_message(test_bot, test_update_from_telegram)
        assert test_bot.text == "Что-то я вас не понял, так какие события вас интересуют и когда?"

    def test_telegram_text_message_show_favorites_for_new_user(self, session, clear_data):
        # Creating objects that I will use in calling method under testing
        controller = TelegramController()
        controller.session = session
        test_bot = BotTest()
        test_update_from_telegram = UpdateFromTelegramTest(text="Избранное",
                                                           chat_id=234,
                                                           effective_user_id=555,
                                                           channel_post=None)
        # Check result of calling "_text_message" method (this method pass result to the 'test_bot' object)
        controller._text_message(test_bot, test_update_from_telegram)
        assert test_bot.text == "Здесь будет список мероприятий, которые тебе понравились"

    def test_telegram_text_message_show_favorites_for_old_user(self, session, clear_data):
        # Fulfilling the database for future making answer - film tomorrow
        start_time = datetime.datetime.now().timestamp() + 86200
        finish_time = datetime.datetime.now().timestamp() + 86300
        event = self.create_event_yandexafishacinema_cinema_venom(start_time, finish_time)
        session.add(event)
        rating = Rating(user_id=1, event_id=1, like=1)
        session.add(rating)
        session.commit()
        # Creating objects that I will use in calling method under testing
        controller = TelegramController()
        controller.session = session
        test_bot = BotTest()
        test_update_from_telegram = UpdateFromTelegramTest(text="Избранное",
                                                           chat_id=234,
                                                           effective_user_id=555,
                                                           channel_post=None)
        # Check result of calling "_text_message" method (this method pass result to the 'test_bot' object)
        controller._text_message(test_bot, test_update_from_telegram)
        assert test_bot.text == "Вот список мероприятий, которые тебе понравились\n\n" \
            "⭐ <a href='https://afisha.yandex.ru/moscow/cinema/venom-2018' target='_blank'>Веном</a> " + \
            AbstractView.convert_timestamp_to_date_and_time(start_time)

    def test_telegram_text_message_greeting(self, session, clear_data):
        # Creating objects that I will use in calling method under testing
        controller = TelegramController()
        controller.session = session
        test_bot = BotTest()
        test_update_from_telegram = UpdateFromTelegramTest(text="Привет",
                                                           chat_id=234,
                                                           effective_user_id=555,
                                                           channel_post=None)
        # Check result of calling "_text_message" method (this method pass result to the 'test_bot' object)
        controller._text_message(test_bot, test_update_from_telegram)
        assert test_bot.text == "Привет, дорогой друг! Какие мероприятия тебя интересуют?"

    def test_telegram_text_message_help(self, session, clear_data):
        # Creating objects that I will use in calling method under testing
        controller = TelegramController()
        controller.session = session
        test_bot = BotTest()
        test_update_from_telegram = UpdateFromTelegramTest(text="Помощь",
                                                           chat_id=234,
                                                           effective_user_id=555,
                                                           channel_post=None)
        # Check result of calling "_text_message" method (this method pass result to the 'test_bot' object)
        controller._text_message(test_bot, test_update_from_telegram)
        assert "Я подскажу, куда сходить в Москве" in test_bot.text

    def test_telegram_text_message_like_or_dislike_for_long_queue_events(self, session, clear_data):
        # Fulfilling the database for future making answer - adding two events
        start_time = datetime.datetime.now().timestamp() + 86200
        finish_time = datetime.datetime.now().timestamp() + 86300
        event1 = self.create_event_yandexafishacinema_cinema_venom(start_time, finish_time)
        session.add(event1)
        event2 = self.create_event_kudago_exhibition_face2face()
        session.add(event2)
        # Adding information about last_queue_events like if this user have already tried to find events
        user = User(telegram_id=777, name="Dima")
        user.last_queue_events = [2, 1]
        session.add(user)
        session.commit()
        # Creating objects that I will use in calling method under testing
        controller = TelegramController()
        controller.session = session
        test_bot = BotTest()
        test_update_from_telegram = UpdateFromTelegramTest(text="Нравится",
                                                           chat_id=234,
                                                           effective_user_id=777,
                                                           channel_post=None)
        # Check result of calling "_text_message" method (this method pass result to the 'test_bot' object)
        controller._text_message(test_bot, test_update_from_telegram)
        assert test_bot.text == AbstractView.convert_timestamp_to_date_and_time(start_time) + \
               "<a href='https://afisha.yandex.ru/13Iaf1251.jpg' target='_blank'>.</a>\n" \
               "<a href='https://afisha.yandex.ru/moscow/cinema/venom-2018' target='_blank'>Веном</a>"

    def test_telegram_text_message_like_or_dislike_for_one_event_in_queue_events(self, session, clear_data):
        # Fulfilling the database for future making answer - adding one event
        event = self.create_event_yandexafishacinema_cinema_venom()
        session.add(event)
        # Adding information about last_queue_events like if this user have already tried to find events
        user = User(telegram_id=777, name="Dima")
        user.last_queue_events = [1]
        session.add(user)
        session.commit()
        # Creating objects that I will use in calling method under testing
        controller = TelegramController()
        controller.session = session
        test_bot = BotTest()
        test_update_from_telegram = UpdateFromTelegramTest(text="Нравится",
                                                           chat_id=234,
                                                           effective_user_id=777,
                                                           channel_post=None)
        # Check result of calling "_text_message" method (this method pass result to the 'test_bot' object)
        controller._text_message(test_bot, test_update_from_telegram)
        assert test_bot.text == "Больше не осталось подходящих событий, поищем что-то еще?"

    def test_telegram_text_message_like_or_dislike_for_zero_event_in_queue_events(self, session, clear_data):
        # Adding information about last_queue_events with zero events
        user = User(telegram_id=777, name="Dima")
        user.last_queue_events = []
        session.add(user)
        session.commit()
        # Creating objects that I will use in calling method under testing
        controller = TelegramController()
        controller.session = session
        test_bot = BotTest()
        test_update_from_telegram = UpdateFromTelegramTest(text="Нравится",
                                                           chat_id=234,
                                                           effective_user_id=777,
                                                           channel_post=None)
        # Check result of calling "_text_message" method (this method pass result to the 'test_bot' object)
        controller._text_message(test_bot, test_update_from_telegram)
        assert test_bot.text == "Больше не осталось подходящих событий, поищем что-то еще?"


class UpdateFromTelegramTest:

    def __init__(self, text, chat_id, effective_user_id, channel_post):
        self.message = MessageTest(text, chat_id)
        self.effective_user = EffectiveUserTest(effective_user_id)
        self.channel_post = channel_post


class MessageTest:

    def __init__(self, text, chat_id):
        self.text = text
        self.chat_id = chat_id


class EffectiveUserTest:

    def __init__(self, effective_user_id):
        self.id = effective_user_id


class BotTest:

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
