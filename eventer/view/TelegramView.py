from telegram import ReplyKeyboardMarkup, KeyboardButton
from AbstractView import AbstractView
import logging


class TelegramView(AbstractView):

    @staticmethod
    def _simple_text_message(message_data):
        return ""

    @staticmethod
    def make_text_answer_from_data(data_for_answer):
        logging.debug('Enter to the method')
        text_answer = ""
        if "datetime" in data_for_answer.keys():
            text_answer += AbstractView.convert_timestamp_to_date_and_time(data_for_answer["datetime"])
        if "price_min" in data_for_answer.keys() and "price_max" in data_for_answer.keys() and data_for_answer['price_min'] == data_for_answer['price_max']:
            text_answer += " " + str(data_for_answer['price_min']) + " руб"
        elif "price_min" in data_for_answer.keys():
            text_answer += " от " + str(data_for_answer['price_min']) + " руб"
        if "img" in data_for_answer.keys():
            text_answer += "<a href='" + data_for_answer["img"] + "' target='_blank'>.</a>"
        if "url" in data_for_answer.keys():
            text_answer += "\n<a href='" + data_for_answer["url"] + "' target='_blank'>" + data_for_answer.get("text", "") + "</a>"
        else:
            text_answer += data_for_answer.get("text", "")
        if "list_of_events" in data_for_answer.keys():
            for event in data_for_answer["list_of_events"]:
                text_answer += "\n\n\U0001F31F" + \
                               " <a href='" + event.url + \
                               "' target='_blank'>" + \
                               event.title.capitalize() + \
                               "</a> " + \
                               str(AbstractView.convert_timestamp_to_date_and_time(event.start_time))
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
        logging.debug('Enter to the method')
        not_like_button = KeyboardButton("\U0001F44E")  # table of unicode symbols http://www.fileformat.info/info/unicode/char/1F44D/index.htm
        like_button = KeyboardButton("\U0001F44D")
        favorites_button = KeyboardButton("Избранное")
        all_categories_button = KeyboardButton("Помощь")
        if data_for_answer.get("status", "unknown") == "one_event":
            all_buttons = ReplyKeyboardMarkup([[like_button, not_like_button], [favorites_button, all_categories_button]],
                                              resize_keyboard=True,
                                              one_time_keyboard=True)
        else:
            all_buttons = ReplyKeyboardMarkup([[favorites_button, all_categories_button]],
                                              resize_keyboard=True,
                                              one_time_keyboard=True)
        return all_buttons

    @staticmethod
    def is_not_allowed_images_preview(data_for_answer):
        """
        Return flag that we have to allow to show image preview inside message or not
        :param data_for_answer:
        :return:
        """
        logging.debug('Enter to the method')
        if 'img' in data_for_answer.keys():  # only in this key we can show image preview
            return False
        return True


