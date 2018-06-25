#!/home/host1423612/.virtualenvs/eventer-env/bin/python
#  -*- coding: UTF-8 -*-

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World! Flaaaaaask"


"""
print("Content-Type: text/plain\r\n\r\n")
print("")
print("Hello World! Import")
"""