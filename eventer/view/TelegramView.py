from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
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
        if "price_min" in data_for_answer.keys() and "price_max" in data_for_answer.keys() and data_for_answer['price_min'] == data_for_answer['price_max']:
            string_price = " " + str(data_for_answer['price_min']) + " руб"
        elif "price_min" in data_for_answer.keys():
            string_price = " от " + str(data_for_answer['price_min']) + " руб"
        else:
            string_price = ""
        if "datetime" in data_for_answer.keys():
            max_number_of_datetime = 5
            for item in data_for_answer["datetime"]:
                if max_number_of_datetime == 0:
                    break
                text_answer += AbstractView.convert_timestamp_to_date_and_time(item) + string_price + "\n"
                max_number_of_datetime -= 1
            text_answer = text_answer[:-1]  # Remove last symbol "\n"
        if "img" in data_for_answer.keys():
            text_answer += "<a href='" + data_for_answer["img"] + "' target='_blank'>.</a>"
        if "url" in data_for_answer.keys():
            text_answer += "\n<a href='" + data_for_answer["url"] + "' target='_blank'>" + data_for_answer.get("text", "") + "</a>"
        else:
            text_answer += data_for_answer.get("text", "")
        if "list_of_events" in data_for_answer.keys():
            for event in data_for_answer["list_of_events"]:
                text_answer += "\n\n\u2B50" + \
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
        \U0001F44E - THUMBS DOWN SIGN
        \U0001F44D - THUMBS UP SIGN
        """
        logging.debug('Enter to the method')
        not_like_button = KeyboardButton("\u27A1 Следующее")  # table of unicode symbols http://www.fileformat.info/info/unicode/char/1F44D/index.htm
        like_button = KeyboardButton("\u2764 Запомнить")
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
    def make_message_buttons(data_for_answer):
        buttons_list = []
        logging.debug('Enter to the method')
        if 'message_buttons' not in data_for_answer.keys():
            return None
        max_buttons_in_line = 3
        counter_buttons_in_line = 0
        buttons_line = []
        for button in data_for_answer['message_buttons']:
            if counter_buttons_in_line == max_buttons_in_line:
                counter_buttons_in_line = 0
                buttons_list.append(buttons_line)
                buttons_line = []
            buttons_line.append(InlineKeyboardButton(text=button, callback_data=button))
            counter_buttons_in_line += 1
        if buttons_line:
            buttons_list.append(buttons_line)
        all_buttons = InlineKeyboardMarkup(buttons_list)
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


