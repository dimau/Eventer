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


requests.post(r'https://api.telegram.org/bot639244805:AAHKVV29O0ljWwEItHXJvTSijUHMGQn1BSU/sendMessage',
              dict(chat_id='@monitoringchannel432', text='избранное'))
