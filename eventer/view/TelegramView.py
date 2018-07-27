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
        not_like_button = KeyboardButton("\U0001F44E")
        like_button = KeyboardButton("\U0001F44D")
        favorites_button = KeyboardButton("Избранное")
        all_categories_button = KeyboardButton("Все категории")
        if data_for_answer["intent"] == "Find events" and data_for_answer["status"] == "one_event":
            all_buttons = ReplyKeyboardMarkup([[like_button, not_like_button], [favorites_button, all_categories_button]],
                                              resize_keyboard=True,
                                              one_time_keyboard=True)
        else:
            all_buttons = ReplyKeyboardMarkup([[favorites_button, all_categories_button]],
                                              resize_keyboard=True,
                                              one_time_keyboard=True)
        return all_buttons

"""
@staticmethod
    def get_buttons_for_message():
        not_like_button = InlineKeyboardButton("Это не интересно", callback_data="not_like_button")
        like_button = {"text": "Это интересно", "callback_data": "like_button"}
        all_buttons = InlineKeyboardMarkup([[not_like_button]])
        return all_buttons
"""
