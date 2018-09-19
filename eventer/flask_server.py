#  -*- coding: UTF-8 -*-

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/panadmin/", methods=["GET", "POST"])
def panadmin():
    return render_template("panadmin.html")

if __name__ == "__main__":
    app.run()
