#!/home/host1423612/eventer-env/bin/python
#  -*- coding: UTF-8 -*-

import sys
print("It works", file=sys.stderr)

try:
    from flask import Flask

    app = Flask(__name__)


    @app.route("/cgi-bin/eventer.wsgi")
    @app.route("cgi-bin/eventer.wsgi")
    @app.route("/")
    @app.route("/test")
    def hello():
        return "Hello World! Flaaaaaask"

except:
    #import sys

    from traceback import format_list, extract_tb

    (extype, value, trace) = sys.exc_info()
    print("%s:%s\n%s" % (extype, value, ''.join(format_list(extract_tb(trace)))), file=sys.stderr)


"""
print("Content-Type: text/plain\r\n\r\n")
print("")
print("Hello World! Import")
if __name__ == "__main__":
    app.run()
"""