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
    source = request.args.get("source", "")
    testcase = request.args.get("testcase", "")
    page = request.args.get("page", "")
    event_source_id = request.args.get('event_source_id', '')
    # Structure of the filename from directory "test_web_server" for page with information about list of events
    if page:
        filename = "{0}__{1}__{2}".format(source, testcase, page)
    # Structure of the filename from directory "test_web_server" for page with information about 1 concrete event
    elif event_source_id:
        filename = "{0}__{1}__{2}".format(source, testcase, event_source_id)
    else:
        raise ValueError("Cannot make a right file name because there is not page or event_source_id in url")
    exec("from " + filename + " import status, mimetype, resp", globals())
    return Response(resp, mimetype=mimetype, status=status)


if __name__ == "__main__":
    app.run()
