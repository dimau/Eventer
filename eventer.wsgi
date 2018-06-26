#!/home/host1423612/eventer-env/bin/python
#  -*- coding: UTF-8 -*-

import sys

activate_this = '/home/host1423612/eventer-env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

sys.path.append('/home/host1423612/dimau.ru/htdocs/www/')

from flask_server import app as application