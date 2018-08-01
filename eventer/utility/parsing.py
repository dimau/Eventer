# -*- coding: utf-8 -*-

# Add directories to PYTHONPATH for cron
import sys
sys.path.append('/home/dimau777/projects/eventer/')
sys.path.append('/home/dimau777/projects/eventer/eventer/')
sys.path.append('/home/dimau777/projects/eventer/eventer/model/')
sys.path.append('/home/dimau777/projects/eventer/eventer/utility/')
sys.path.append('/home/dimau777/projects/eventer/eventer/view/')
sys.path.append('/home/dimau777/projects/eventer/eventer/parser/')
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from ParserFactory import ParserFactory
# it's needed for operation relationship between User, Event and Rating
from Event import Event
from User import User
from Rating import Rating


# Parameters for future config file
user_for_mysql = "eventer"
password_for_mysql = "Nhgbf86jmnIK"

# Create a session with database
engine = sqlalchemy.create_engine("mysql://" + user_for_mysql + ":" + password_for_mysql + "@localhost/eventer?charset=utf8", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Take a source for parsing from argument
# We are expecting launch from cron by command like: 'python eventer/utility/parsing.py KudaGo'
if len(sys.argv) == 1:
    print("ERROR parsing.py: we don't have parameter with source name for parsing")
source = sys.argv[1]
print("parsing.py: start of parsing " + source)

# Create concrete parser and do parse source
parser = ParserFactory.create_parser(source, session)
parser.main()
