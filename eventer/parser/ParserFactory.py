class ParserFactory:
    """
    Factory provides right concrete parser object for source name (from cron script originally)
    """

    @staticmethod
    def create_parser(source, session):
        print("ParserFactory:__init__(): enter, source: " + str(source))
        if source == "KudaGo":
            from KudaGoParser import KudaGoParser
            parser = KudaGoParser(session)
            return parser

        print("ParserFactory:__init__(): wrong source parameter: " + str(source))
        raise ValueError("source parameter is wrong: " + str(source))
