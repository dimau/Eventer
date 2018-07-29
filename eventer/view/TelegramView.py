# from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram import ReplyKeyboardMarkup, KeyboardButton


class TelegramView:

    @staticmethod
    def _simple_text_message(message_data):
        return ""

    @staticmethod
    def make_text_answer_from_data(data_for_answer):
        text_answer = ""
        text_answer += data_for_answer.get("text", "")
        if "img" in data_for_answer.keys():
            text_answer += "<a href='" + data_for_answer["img"] + "' target='_blank'>.</a>"
        if "url" in data_for_answer.keys():
            text_answer += """
<a href='""" + data_for_answer["url"] + "' target='_blank'>Подробнее про событие</a>"
        return text_answer

    @staticmethod
    def get_buttons_for_message(data_for_answer):
        """
        Return object with buttons for message
        status:
            none_event - other type of messages
            one_event - message about one event where user will have opportunity to chose like or dislike
        :param data_for_answer:
        :return:
        """
        not_like_button = KeyboardButton("\U0001F44E")
        like_button = KeyboardButton("\U0001F44D")
        favorites_button = KeyboardButton("Избранное")
        all_categories_button = KeyboardButton("Все категории")
        if data_for_answer.get("status", "unknown") == "one_event":
            all_buttons = ReplyKeyboardMarkup([[like_button, not_like_button], [favorites_button, all_categories_button]],
                                              resize_keyboard=True,
                                              one_time_keyboard=True)
        else:
            all_buttons = ReplyKeyboardMarkup([[favorites_button, all_categories_button]],
                                              resize_keyboard=True,
                                              one_time_keyboard=True)
        return all_buttons
