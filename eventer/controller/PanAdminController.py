# -*- coding: utf-8 -*-

import sqlalchemy
from AbstractController import AbstractController
from Event import Event
from flask import render_template, request
# it's needed for operation relationship between User, Event and Rating
from User import User
from Rating import Rating


class PanAdminController(AbstractController):

    def __init__(self):
        self.session = None

    def index_page(self):
        self.session = self._create_session_with_db()
        answer_string = ""

        if request.method == 'POST':

            # We have check both urls: with "/" at the end and without "/" at the end
            source_url = request.form['source_url']  # https://kudago.com/msk/event/fleshmob-fleshmob-ot-platyozhnoj-sistemyi-mir/
            if source_url and source_url[-1] == "/":
                source_url2 = source_url[0:-1]
            else:
                source_url2 = source_url + "/"

            # Trying to get an event from the database by url
            relevant_event = self.session.query(Event).filter(sqlalchemy.or_(Event._url == source_url, Event._url == source_url2)).first()

            # Making an answer
            if relevant_event:
                answer_string = repr(relevant_event)
            else:
                answer_string = "There is not information about event with url: " + source_url

        return render_template("panadmin.html", answer_string=answer_string)
