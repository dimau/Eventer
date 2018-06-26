#!/home/host1423612/eventer-env/bin/python
#  -*- coding: UTF-8 -*-


from flask import Flask
from flask import Response
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    json_response = """{
  "fulfillmentText": "This is a text response",
  "source": "dimau.ru/eventer.wsgi/"
}"""
    return Response(json_response, mimetype='application/json')


@app.route("/test/")
def hello():
    return "Hello World! It works!"


if __name__ == "__main__":
    app.run()
