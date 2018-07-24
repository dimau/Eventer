#  -*- coding: UTF-8 -*-


from flask import Flask
from flask import Response
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    json_response = """
    {
    "fulfillmentText": "Вот такой ответ тебе!",
    "fulfillmentMessages": [
        {
            "text": {
                "text": [
                    "[{'type':0,'speech':'Вот такой ответ для Телеграма'}]"
                ]
            }
        }
    ],
    "payload": {
      "telegram": {
          "text": "This is a text response for Telegram."
      }
    },
    "source": "dimauservices.ru"
    }"""
    return Response(json_response, mimetype='application/json; charset=utf-8')


@app.route("/test/")
def hello():
    return "Hello World! It works!"


if __name__ == "__main__":
    app.run()
