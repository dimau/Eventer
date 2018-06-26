#!/home/host1423612/eventer-env/bin/python
#  -*- coding: UTF-8 -*-


from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World! Flaaaaaask"


@app.route("/test")
def hello():
    return "233333 hi"

"""
print("Content-Type: text/plain\r\n\r\n")
print("")
print("Hello World! Import")
if __name__ == "__main__":
    app.run()
"""