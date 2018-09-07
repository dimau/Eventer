from Rating import Rating
from Event import Event
import sqlalchemy
import logging
from collections import Counter
import numpy as np


class Sorter:
    """
    Class for sorting events
    """

    def __init__(self, session, user, events, categories, free_of_charge, with_who):
        self._session = session
        self._user = user
        self._events = events
        self._events_ids = self._extract_events_ids()
        self._categories = categories
        self._free_of_charge = free_of_charge
        self._with_who = with_who

    def get_sorted_events(self):
        """
        Return sorted list of relevant events that is fitting for user request
        MAXIMUM 100 events per time
        :param start_timestamp:
        :param finish_timestamp:
        :param categories:
        :return: sorted list of Events
        """
        matrix_events_features = []
        matrix_events_features.append(self._events)
        matrix_events_features.append(self._get_scores_all_users_favorites_events())
        matrix_events_features.append(self._get_scores_children_events())
        matrix_events_features.append(self._get_scores_free_events())
        matrix_events_features.append(self._get_scores_user_favorite_categories())
        matrix_events_features = self._pivot_matrix(matrix_events_features)
        matrix_events_relevance = self._calculate_relevance(matrix_events_features)
        matrix_events_relevance = self._sort_by_relevance(matrix_events_relevance)
        matrix_events_relevance = self._sort_by_datetime(matrix_events_relevance)
        sorted_events = self._sort_for_diversity(matrix_events_relevance)
        return sorted_events[0:100]  # we will return for one time only 100 most relevant events

    def _get_scores_all_users_favorites_events(self):
        """
        Return list of feature values: amount of all additions to favorites minus amount of all actions of skipping
        normalized to the total amount of assesses
        :return: list of feature values for every event in the source list (self._events)
        """
        event_ids = self._get_all_event_ids_in_list()

        positive_ratings_amount = self._session.query(Rating._event_id, sqlalchemy.func.count(Rating._event_id)).\
            filter(Rating._event_id.in_(event_ids)).filter(Rating._like == 1).filter(Rating._user_id != self._user.user_id).\
            group_by(Rating._event_id).all()
        logging.debug("Positive_ratings_amount: %s", positive_ratings_amount)
        # positive_ratings_amount = [(28, 3), (58, 1), (2815, 1)]
        # first number = event_id, second number = amount of likes

        negative_ratings_amount = self._session.query(Rating._event_id, sqlalchemy.func.count(Rating._event_id)). \
            filter(Rating._event_id.in_(event_ids)).filter(Rating._like == 0).filter(Rating._user_id != self._user.user_id). \
            group_by(Rating._event_id).all()
        logging.debug("Negative_ratings_amount: %s", negative_ratings_amount)
        # negative_ratings_amount = [(28, 3), (2815, 1)]
        # first number = event_id, second number = amount of dislikes

        feature_values = []
        for event in self._events:

            positive_rating = 0
            for item in positive_ratings_amount:
                if item[0] == event.event_id:
                    positive_rating = item[1]
                    break

            negative_rating = 0
            for item in negative_ratings_amount:
                if item[0] == event.event_id:
                    negative_rating = item[1]
                    break

            if positive_rating != 0 or negative_rating != 0:
                result = (positive_rating - negative_rating) / (positive_rating + negative_rating)
            else:
                result = 0

            feature_values.append(result)

        logging.debug("Scores_all_users_favorites_events: %s", list(zip(self._events_ids, feature_values)))
        return feature_values

    def _get_scores_children_events(self):

        # If user wants children events, we have extracted from base only children events,
        # we won't doing anything for sorting
        if self._with_who == 'children':
            return [0] * len(self._events)

        feature_values = []
        for event in self._events:
            for_kids = 0
            if "kids" in event.categories.split("|"):
                for_kids = 1
            feature_values.append(for_kids)

        logging.debug("Scores_children_events: %s", list(zip(self._events_ids, feature_values)))
        return feature_values

    def _get_scores_free_events(self):

        # If user wants free events, we have extracted from base only free events, we won't doing anything for sorting
        if self._free_of_charge:
            return [0] * len(self._events)

        feature_values = []
        for event in self._events:
            free = 0
            if event.price_min == 0 and event.price_max == 0:
                free = 1
            feature_values.append(free)

        logging.debug("Scores_free_events: %s", list(zip(self._events_ids, feature_values)))
        return feature_values

    def _get_scores_user_favorite_categories(self):
        """
        1. Extract all favorite events
        2. Extract all categories from favorite events
        3. Count amount of all categories = all_amount_of_categories
        4. Count amount of each distinct category in all categories from favorite events = liked_categories_and_weight
        5. Feature for every event = sum of weights of all categories of the event / amount of all categories
        :return:
        """
        liked_events_categories = self._session.query(Rating._event_id, Event._categories).\
            filter(Rating._like == 1).filter(Rating._user_id == self._user.user_id).join(Event).all()
        logging.debug("Liked_events_categories: %s", liked_events_categories)
        # We will receive like this: [(28, 'cinema'), (2815, 'festival|cinema'), (2815, 'festival|cinema')]

        all_liked_events_categories = []
        for item in liked_events_categories:
            all_liked_events_categories += item[1].split("|")
        all_amount_of_categories = len(all_liked_events_categories)
        logging.debug("All_amount_of_categories: %s", all_amount_of_categories)

        liked_categories_and_weight = Counter(all_liked_events_categories)
        # We will receive like this: Counter({'cinema': 2, 'festival': 1})

        feature_values = []
        for event in self._events:
            value = 0
            event_categories = event.categories.split('|')
            for category in event_categories:
                if category in liked_categories_and_weight:
                    value += liked_categories_and_weight[category]
                    continue
            feature_values.append(value/all_amount_of_categories)

        logging.debug("Scores_user_favorite_categories: %s", list(zip(self._events_ids, feature_values)))
        return feature_values

    def _pivot_matrix(self, matrix_events_features):
        """
        Transpose matrix of events and features so every list consists of 1 event and all its features
        :param matrix_events_features:
        :return: a list of lists where each list consists of 1 Event and all its features
        """
        a = np.array(matrix_events_features)
        a = a.transpose()
        return a

    def _calculate_relevance(self, matrix_events_features):
        matrix_events_relevance = []
        matrix_for_logging = []
        for item in matrix_events_features:
            event = item[0]
            scores_all_users_favorites_events = item[1]
            scores_children_events = item[2]
            scores_free_events = item[3]
            scores_user_favorite_categories = item[4]
            relevance = 30 * scores_all_users_favorites_events - 3 * scores_children_events + 3 * scores_free_events + 50 * scores_user_favorite_categories
            matrix_events_relevance.append((event, relevance))
            matrix_for_logging.append((event.event_id, relevance))
        logging.debug("Matrix events - relevance: %s", matrix_for_logging)
        return matrix_events_relevance

    def _sort_by_relevance(self, matrix_events_relevance):
        pass

    def _sort_by_datetime(self, sorted_events_plus_relevance):
        pass

    def _sort_for_diversity(self, sorted_events_plus_relevance):
        pass

    def _get_all_event_ids_in_list(self):
        event_ids = []
        for event in self._events:
            event_ids.append(event.event_id)
        return event_ids

    def _extract_events_ids(self):
        """
        Return list of events ids - we will use it for logging in several methods
        :return: list of integers
        """
        events_ids = []
        for event in self._events:
            events_ids.append(event.event_id)
        return events_ids
