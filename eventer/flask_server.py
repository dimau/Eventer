#  -*- coding: UTF-8 -*-

# Add directories to PYTHONPATH
import sys
sys.path.append('/home/dimau777/projects/eventer/')
sys.path.append('/home/dimau777/projects/eventer/eventer/')
sys.path.append('/home/dimau777/projects/eventer/eventer/answer_maker/')
sys.path.append('/home/dimau777/projects/eventer/eventer/controller/')
sys.path.append('/home/dimau777/projects/eventer/eventer/model/')
sys.path.append('/home/dimau777/projects/eventer/eventer/parser/')
sys.path.append('/home/dimau777/projects/eventer/eventer/utility/')
sys.path.append('/home/dimau777/projects/eventer/eventer/view/')

from PanAdminController import PanAdminController
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/panadmin/", methods=["GET", "POST"])
def panadmin():
    controller = PanAdminController()
    return controller.index_page()


if __name__ == "__main__":
    app.run(debug=True)
