#!/home/host1423612/.virtualenvs/eventer-env/bin/python
from wsgiref.handlers import CGIHandler
from index3 import app

CGIHandler().run(app)