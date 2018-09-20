#  -*- coding: UTF-8 -*-

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/panadmin/", methods=["GET", "POST"])
def panadmin():
    answer_string = ""
    if request.method == 'POST':
        source_url = request.form['source_url']
        answer_string = "Вот здесь ответ из базы данных"
    return render_template("panadmin.html", answer_string=answer_string)

if __name__ == "__main__":
    app.run()
