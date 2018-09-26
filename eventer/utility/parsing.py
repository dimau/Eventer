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
import argparse
import logging
# it's needed for operation relationship between User, Event and Rating
from Event import Event
from User import User
from Rating import Rating

# Extracting parameters from command line
# We are expecting launch from cron by command like: 'python eventer/utility/parsing.py --source=KudaGo --log=INFO'
parser = argparse.ArgumentParser(description='parser of arguments of command line for parsing launch')
parser.add_argument('-s', '--source', action='store', dest='source',
                    help='codename source for parsing (KudaGo for example)')
parser.add_argument('--log', action='store', dest='loglevel', help='level of logging for this launch')
args = parser.parse_args()

# Check for logging level
log_level = args.loglevel if args.loglevel else "INFO"
numeric_level = getattr(logging, log_level.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError("Invalid log level: {}".format(log_level))

# Logging tuning
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(module)s - %(funcName)s - %(message)s',
                    level=numeric_level,
                    filename='/var/log/eventer/parsing.log'
                    )

# Check for source for parsing
if not args.source:
    logging.error("There is NOT parameter with source name for parsing: --source")
    raise ValueError("There is NOT parameter with source name for parsing: --source")
logging.info('start of parsing %s', args.source)

# Start session with database
user_for_mysql = os.environ.get("USERMYSQL", None)
if not user_for_mysql:
    logging.error("Cannot find environment variable USERMYSQL")
    raise KeyError("Cannot find environment variable USERMYSQL")
password_for_mysql = os.environ.get("PASSWORDMYSQL", None)
if not password_for_mysql:
    logging.error("Cannot find environment variable PASSWORDMYSQL")
    raise KeyError("Cannot find environment variable PASSWORDMYSQL")
name_of_database_for_mysql = os.environ.get("DATABASEMYSQL", None)
if not name_of_database_for_mysql:
    logging.error("Cannot find environment variable DATABASEMYSQL")
    raise KeyError("Cannot find environment variable DATABASEMYSQL")
engine = sqlalchemy.create_engine(
    "mysql://" + user_for_mysql + ":" + password_for_mysql + "@localhost/" + name_of_database_for_mysql + "?charset=utf8", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Create concrete parser and do parse source
parser = ParserFactory.create_parser(args.source, session)
parser.main()
