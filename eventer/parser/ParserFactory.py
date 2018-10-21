import logging


class ParserFactory:
    """
    Factory provides right concrete parser object for source name (from cron script originally)
    """

    @staticmethod
    def create_parser(source, session):
        logging.debug('Enter to the method, source: %s', source)
        if source == "KudaGo":
            from KudaGoParser import KudaGoParser
            parser = KudaGoParser(session)
            return parser
        if source == "YandexAfishaCinema":
            from YandexAfishaCinemaParser import YandexAfishaCinemaParser
            parser = YandexAfishaCinemaParser(session)
            return parser
        if source == "YandexAfishaTheater":
            from YandexAfishaTheaterParser import YandexAfishaTheaterParser
            parser = YandexAfishaTheaterParser(session)
            return parser

        logging.error('Wrong source parameter!')
        raise ValueError("source parameter is wrong: " + str(source))
