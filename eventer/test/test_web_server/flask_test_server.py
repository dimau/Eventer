#  -*- coding: UTF-8 -*-

# Add directories to PYTHONPATH
import sys
sys.path.append('/home/dimau777/projects/eventer/')
sys.path.append('/home/dimau777/projects/eventer/eventer/')
sys.path.append('/home/dimau777/projects/eventer/eventer/answer_maker/')
sys.path.append('/home/dimau777/projects/eventer/eventer/controller/')
sys.path.append('/home/dimau777/projects/eventer/eventer/model/')
sys.path.append('/home/dimau777/projects/eventer/eventer/parser/')
sys.path.append('/home/dimau777/projects/eventer/eventer/test/')
sys.path.append('/home/dimau777/projects/eventer/eventer/utility/')
sys.path.append('/home/dimau777/projects/eventer/eventer/view/')

from flask import Flask, Response
app = Flask(__name__)


@app.route("/kudago_one_event/", methods=["GET"])
def kudago_one_event():
    from test_web_server.kudago_one_event_server_answer import json_response
    return Response(json_response, mimetype='application/json; charset=utf-8')


if __name__ == "__main__":
    app.run()
