import datetime
import logging


class AbstractView:

    @staticmethod
    def convert_timestamp_to_date_and_time(source_timestamp):
        logging.debug('Enter to the method')
        source_datetime = AbstractView._convert_utc_timestamp_to_local_timestamp(source_timestamp)
        source_datetime = datetime.datetime.fromtimestamp(source_datetime)
        source_date = source_datetime.day
        source_month = source_datetime.month
        source_hours = source_datetime.hour
        source_minutes = source_datetime.minute
        pretty_text_datetime = "{0} {1} в {2}:{3}".format(AbstractView._convert_date_to_normal_format(source_date),
                                                          AbstractView._convert_month_to_russian_name(source_month),
                                                          AbstractView._convert_minutes_to_normal_format(source_hours),
                                                          AbstractView._convert_minutes_to_normal_format(source_minutes)
                                                          )
        return pretty_text_datetime

    @staticmethod
    def _convert_utc_timestamp_to_local_timestamp(utc_timestamp):
        logging.debug('Enter to the method')
        return utc_timestamp + 3600 * 3  # only for Moscow 3 hours plus from UTC

    @staticmethod
    def _convert_month_to_russian_name(month):
        logging.debug('Enter to the method')
        source_month = str(month)
        converter = {
            "1": "января",
            "2": "февраля",
            "3": "марта",
            "4": "апреля",
            "5": "мая",
            "6": "июня",
            "7": "июля",
            "8": "августа",
            "9": "сентября",
            "10": "октября",
            "11": "ноября",
            "12": "декабря",
            "01": "января",
            "02": "февраля",
            "03": "марта",
            "04": "апреля",
            "05": "мая",
            "06": "июня",
            "07": "июля",
            "08": "августа",
            "09": "сентября"
        }
        return converter.get(source_month, None)

    @staticmethod
    def _convert_minutes_to_normal_format(minutes):
        logging.debug('Enter to the method')
        source_minutes = str(minutes)
        if len(source_minutes) == 2:
            return source_minutes
        return "0" + source_minutes

    @staticmethod
    def _convert_date_to_normal_format(source_date):
        logging.debug('Enter to the method')
        return str(int(source_date))
