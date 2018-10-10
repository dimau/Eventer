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
import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from ParserFactory import ParserFactory
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

    def main(self):
        # Extracting parameters from command line
        args = self._extracting_parameters_from_command_line()
        self.log_level = args.log_level if args.log_level else "INFO"
        self.source = args.source

        # Launch logging with giving level
        self._launch_logging("parsing.log", self.log_level)

        # Check source for parsing and get it
        self._checking_source_for_parsing(self.source)

        # Start session with database
        self.session = self._create_session_with_db()

        # Create concrete parser and do parse source
        parser = ParserFactory.create_parser(self.source, self.session)
        parser.main()

    @staticmethod
    def _extracting_parameters_from_command_line():
        """
        Extracting parameters from command line
        We are expecting launch from cron by command like:
        python /home/dimau777/projects/eventer/eventer/controller/ParsingController.py --source=KudaGo --log=info
        :return:
        """
        parser = argparse.ArgumentParser(description='parser of arguments of command line for parsing launch')
        parser.add_argument('-s', '--source', action='store', dest='source',
                            help='codename source for parsing (KudaGo for example)')
        parser.add_argument('--log', action='store', dest='log_level', help='level of logging for this launch')
        args = parser.parse_args()
        return args

    @staticmethod
    def _checking_source_for_parsing(source):
        if not source:
            logging.error("There is NOT parameter with source name for parsing: --source")
            raise ValueError("There is NOT parameter with source name for parsing: --source")
        logging.info('start of parsing %s', source)


if __name__ == '__main__':
    controller = ParsingController()
    controller.main()
