#  -*- coding: UTF-8 -*-

# Add directories to PYTHONPATH
import sys
sys.path.append('/home/dimau777/projects/eventer/')
sys.path.append('/home/dimau777/projects/eventer/eventer/')
sys.path.append('/home/dimau777/projects/eventer/eventer/answer_maker/')
sys.path.append('/home/dimau777/projects/eventer/eventer/controller/')
sys.path.append('/home/dimau777/projects/eventer/eventer/model/')
sys.path.append('/home/dimau777/projects/eventer/eventer/parser/')
sys.path.append('/home/dimau777/projects/eventer/test/')
sys.path.append('/home/dimau777/projects/eventer/test/parser/')
sys.path.append('/home/dimau777/projects/eventer/test/test_web_server/')
sys.path.append('/home/dimau777/projects/eventer/eventer/utility/')
sys.path.append('/home/dimau777/projects/eventer/eventer/view/')

from flask import Flask, Response, request, redirect, url_for
app = Flask(__name__)


@app.route("/", methods=["GET"])
def test_server():
    source = request.args["source"]
    testcase = request.args["testcase"]
    page = request.args["page"]
    filename = "{0}__{1}__{2}".format(source, testcase, page)
    exec("from " + filename + " import status, mimetype, resp", globals())
    return Response(resp, mimetype=mimetype, status=status)


if __name__ == "__main__":
    app.run()
