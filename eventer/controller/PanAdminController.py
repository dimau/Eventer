# -*- coding: utf-8 -*-

from AbstractController import AbstractController
from Event import Event
from flask import render_template, request


class PanAdminController(AbstractController):

    def __init__(self):
        self.session = None

    def index_page(self):
        self.session = self._create_session_with_db()
        answer_string = ""
        if request.method == 'POST':
            source_url = request.form['source_url']  # https://kudago.com/msk/event/fleshmob-fleshmob-ot-platyozhnoj-sistemyi-mir/
            relevant_events = self.session.query(Event).filter(Event._url == source_url).first()
            answer_string = relevant_events.repr()
        return render_template("panadmin.html", answer_string=answer_string)
