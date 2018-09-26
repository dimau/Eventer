import os
import apiai
import json
import logging


class Router:
    """
    I will use usual class (not static methods) because in future I will want to use some information about User from
    database, and it's more convenient to have session object and user object in instance of this class
    """

    def __init__(self, user_message_text="", session_with_db=None, user=None, type_user_message="_text_message"):
        """
        Constructor for class Router
        :param user_message_text: text from messenger or another source from user
        :param session_with_db: session sqlalchemy to work with database
        :param user: object of class User with information about user
        :param type_user_message: start = new user add our chat bot; _text_message - usual text message from user
        """

        # Initial data - token for working with dialogflow, text message, session with database
        api_ai_token = os.environ.get("APIAITOKEN", None)
        if not api_ai_token:
            logging.error("Cannot find environment variable APIAITOKEN")
            raise KeyError("Cannot find environment variable APIAITOKEN")
        self.api_ai_token = api_ai_token
        self.user_message_text = user_message_text
        self.session = session_with_db
        self.user = user
        self.type_user_message = type_user_message

    def __repr__(self):
        return "<Router user_message_text: {}, type_user_message: {}>".format(self.user_message_text, self.type_user_message)

    def get_answer_maker(self):

        # User add our chat bot to its messenger
        if self.type_user_message == "start":
            from answer_maker.HelpAnswerMaker import HelpAnswerMaker
            return HelpAnswerMaker(self.session, self.user, "Start", result_of_classification={})

        # Get result of NLP from Dialogflow
        result_of_classification = self._get_classification_and_entities()
        intent = result_of_classification['intent_name']

        if intent == "Greeting":
            from answer_maker.GreetingAnswerMaker import GreetingAnswerMaker
            return GreetingAnswerMaker(self.session, self.user, intent, result_of_classification)

        if intent == "Find events":
            from answer_maker.FindEventsAnswerMaker import FindEventsAnswerMaker
            return FindEventsAnswerMaker(self.session, self.user, intent, result_of_classification)

        if intent == "Like" or intent == "Dislike":
            from answer_maker.LikeDislikeAnswerMaker import LikeDislikeAnswerMaker
            return LikeDislikeAnswerMaker(self.session, self.user, intent, result_of_classification)

        if intent == 'Favorites':
            from answer_maker.FavoritesAnswerMaker import FavoritesAnswerMaker
            return FavoritesAnswerMaker(self.session, self.user, intent, result_of_classification)

        if intent == "Help":
            from answer_maker.HelpAnswerMaker import HelpAnswerMaker
            return HelpAnswerMaker(self.session, self.user, intent, result_of_classification)

        # If intent == Fallback or something else
        from answer_maker.FallbackAnswerMaker import FallbackAnswerMaker
        return FallbackAnswerMaker(self.session, self.user, intent, result_of_classification)

    def _get_classification_and_entities(self):
        """
        Function returns results of classification of user message text and entities extracted from this message
        :return: dictionary with intent name and values of entities
        """
        result = {}
        request_to_apiai = apiai.ApiAI(self.api_ai_token).text_request()  # token API for Dialogflow
        request_to_apiai.lang = 'ru'  # language for request message
        request_to_apiai.session_id = "idSessionOfDialog"  # id session of dialog (it's necessary for teaching chat bot in dialogflow in future)
        request_to_apiai.query = self.user_message_text  # prepare text message from user to transmit to dialogflow

        # Execute the query to dialogflow
        try:
            response_json_from_apiai = json.loads(request_to_apiai.getresponse().read().decode('utf-8'))
        except Exception as e:
            logging.error('Text of error: %s', e)
            return {}

        # Extract result of classification - intent name
        result['intent_name'] = response_json_from_apiai['result']['metadata']['intentName']

        # Parameters for intent Find events
        if result['intent_name'] == 'Find events':
            result['date_period'] = response_json_from_apiai['result']['parameters']['date-period']
            result['with_who'] = response_json_from_apiai['result']['parameters']['With-who']
            result['date'] = response_json_from_apiai['result']['parameters']['date']
            result['free_or_not'] = response_json_from_apiai['result']['parameters']['Free-or-not']
            result['time_period'] = response_json_from_apiai['result']['parameters']['time-period']
            result['type-of-action'] = response_json_from_apiai['result']['parameters']['Type-of-action']

        return result
