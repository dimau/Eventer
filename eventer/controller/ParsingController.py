# -*- coding: utf-8 -*-

# Add directories to PYTHONPATH for cron
import sys
sys.path.append('/home/dimau777/projects/eventer/')
sys.path.append('/home/dimau777/projects/eventer/eventer/')
sys.path.append('/home/dimau777/projects/eventer/eventer/answer_maker/')
sys.path.append('/home/dimau777/projects/eventer/eventer/controller/')
sys.path.append('/home/dimau777/projects/eventer/eventer/model/')
sys.path.append('/home/dimau777/projects/eventer/eventer/parser/')
sys.path.append('/home/dimau777/projects/eventer/eventer/utility/')
sys.path.append('/home/dimau777/projects/eventer/eventer/view/')
from AbstractController import AbstractController
import argparse
import logging
# it's needed for operation relationship between User, Event and Rating
from Event import Event
from User import User
from Rating import Rating


class ParsingController(AbstractController):

    def __init__(self):
        self.session = None
        self.source = None
        self.log_level = None
        self.mode = None

    def main(self):
        # Extracting parameters from command line
        args = self._extracting_parameters_from_command_line()
        self.source = args['source']
        self.log_level = args['log']
        self.mode = args['mode']

        # Launch logging with giving level
        self._launch_logging("parsing.log", self.log_level)

        # Check source, mode for parsing after launching of logging
        self._checking_parameters_for_parsing(self.source, self.mode)

        # Start session with database
        self.session = self._create_session_with_db()

        # Create concrete parser and do parse source
        parser = self._create_parser()
        parser.main()

    @staticmethod
    def _extracting_parameters_from_command_line():
        """
        Extracting parameters from command line
        We are expecting launch from cron by command like:
        python /home/dimau777/projects/eventer/eventer/controller/ParsingController.py --source=KudaGo --log=info --mode=only_new
        :return:
        """
        result_args = {
            'source': None,
            'log': "INFO",
            'mode': None
        }
        parser = argparse.ArgumentParser(description='parser of arguments of command line for parsing launch')
        parser.add_argument('-s', '--source', action='store', dest='source', help='codename source for parsing')
        parser.add_argument('--log', action='store', dest='log', help='level of logging for this launch')
        parser.add_argument('--mode', action='store', dest='mode', help='mode of parsing - only_new or full')
        args = parser.parse_args()
        if args.source and args.source in ['KudaGo', 'YandexAfishaCinema', 'YandexAfishaTheater']:
            result_args['source'] = args.source
        if args.log and args.log.upper() in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
            result_args['log'] = args.log.upper()
        if args.mode and args.mode in ['only_new', 'full', 'full_with_updating']:
            result_args['mode'] = args.mode
        return result_args

    @staticmethod
    def _checking_parameters_for_parsing(source, mode):
        if not source:
            logging.error("Invalid parameter with source name for parsing: --source")
            raise ValueError("Invalid parameter with source name for parsing: --source")
        if not mode:
            logging.error("Invalid parameter with mode for parsing: --mode")
            raise ValueError("Invalid parameter with mode for parsing: --mode")
        logging.info('start of parsing source: %s, mode: %s', source, mode)

    def _create_parser(self):
        """
        Provides right concrete parser object for source name
        :return:
        """
        logging.debug('Enter to the method, source: %s', self.source)
        if self.source == "KudaGo":
            from KudaGoParser import KudaGoParser
            parser = KudaGoParser(self.session, self.mode)
            return parser
        if self.source == "YandexAfishaCinema":
            from YandexAfishaCinemaParser import YandexAfishaCinemaParser
            parser = YandexAfishaCinemaParser(self.session, self.mode)
            return parser
        if self.source == "YandexAfishaTheater":
            from YandexAfishaTheaterParser import YandexAfishaTheaterParser
            parser = YandexAfishaTheaterParser(self.session, self.mode)
            return parser
        logging.error('Wrong source parameter!')
        raise ValueError("source parameter is wrong: " + str(self.source))


if __name__ == '__main__':
    controller = ParsingController()
    controller.main()
