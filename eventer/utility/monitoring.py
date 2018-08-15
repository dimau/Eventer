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
import logging
import argparse
import requests

# requests.post(r'https://api.telegram.org/bot613901896:AAENrUVZ1vkk3WOf-gUZnNochIOnbse_fJE/sendMessage',
#               dict(chat_id=46457618, text='избранное'))

requests.post(r'https://api.telegram.org/bot639244805:AAHKVV29O0ljWwEItHXJvTSijUHMGQn1BSU/sendMessage',
              dict(chat_id='@monitoringchannel432', text='избранное'))

# Extracting parameters from command line
# We are expecting launch from cron by command like: 'python eventer/utility/monitoring.py --log=INFO'
# parser = argparse.ArgumentParser(description='parser of arguments of command line for monitoring launch')
# parser.add_argument('--log', action='store', dest='loglevel', help='level of logging for this launch')
# args = parser.parse_args()

# Check for logging level
# log_level = args.loglevel if args.loglevel else "INFO"
# numeric_level = getattr(logging, log_level.upper(), None)
# if not isinstance(numeric_level, int):
#    raise ValueError("Invalid log level: {}".format(log_level))

# Logging tuning
# logging.basicConfig(format='%(levelname)s - %(asctime)s - %(module)s - %(funcName)s - %(message)s',
#                    level=numeric_level,
#                    filename='/tmp/monitoring.log'
#                    )

# Get telegram_token from environment variable
# telegram_token = os.environ.get("TELEGRAMMONITORINGTOKEN", None)
# if not telegram_token:
#    logging.error("Cannot find environment variable TELEGRAMMONITORINGTOKEN")
#    raise KeyError("Cannot find environment variable TELEGRAMMONITORINGTOKEN")
