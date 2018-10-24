import time
import datetime
import requests
import logging
from Event import Event


class AbstractParser:

    def __init__(self, session):
        self._session = session

    def main(self, mode='only_new', test_url=None):
        """
        This method downloads list of events from source (in cycle with parameter page number)
        and save new data to database while we face parsing pointer (it means, that we have reached last successfully
        handled event from this source)
        :param mode: 'only_new' = parser get only new events from the top of the list until it reach the parsing pointer value
                     'full' = parser get all events and save to the database only new of them without changing already existing in our database
                     'full_with_updating' = parser get all events, updating already saved events and deleting not existing on the source events
        :param test_url: you can transmit test url for testing purpose, in this case _make_url() will use this url (usually localhost url)
        :return:
        """
        # Define last event from previous parsing session.
        # If we use 'only_new' mode, when we reach it, we will stop parsing.
        # If we use 'full' mode, we have update it's value
        parsing_pointer = self._create_parsing_pointer()
        self._session.add(parsing_pointer)
        previous_parsing_pointer_value = parsing_pointer.current_pointer

        # Look over all pages (in the case of 'only_new' mode we do it only while we don't reach a parsing pointer)
        page_number = 1
        already_saved_event_in_collection = False
        # All_events_ids will contains ids (urls) for all Events after whole parsing cycle
        # It can be used for inactivation or deleting removed from source events from our database too
        all_events_ids = []
        while True:
            logging.info('New page number = %s', page_number)

            # Make an url for parsing
            url = self._make_url(page=page_number, test_url=test_url)
            logging.info('Url for parsing: %s', url)

            # Get url content and stop parsing if we have got not 200 code or empty page or something like this
            url_content = self._get_url_content(url)
            if self._is_bad_page(url_content):
                break

            # Get list of events (every event in the list is in source format)
            events_collection_source = self._list_parser(url_content)
            if not events_collection_source:
                break
            logging.info('We have extracted from page in our list %s events', len(events_collection_source))

            # Look over all events from the list and create Event object for every event
            # Events_collection_normalized will contains all NEW Events after whole parsing cycle
            events_collection_normalized = []
            for item in events_collection_source:

                # Parsing of one event in the list into list of related Event objects
                events = self._item_parser(item)
                logging.debug('Events after item parsing: %s', events)
                if len(events) == 0:
                    continue
                # We are gathering the list of all actual events for now from the source
                if mode == "full_with_updating":
                    all_events_ids.append(events[0].url)

                # We are trying to find the same event in the database. For every event.
                # For 'only_new' and 'full' mode it helps to avoid duplicates in database
                # For 'full_with_updating' mode it helps change existing in the database events
                # Result depends on mode of parsing, but in any case we get list of events for adding to the session with database
                events_for_db, already_saved_event_in_collection = self._checking_events_in_database(mode, previous_parsing_pointer_value, events)
                events_collection_normalized += events_for_db

            # Save new parsing pointer - only in the beginning of this iteration of parsing
            # We will save a new parsing pointer only if we have at least one new event,
            # that doesn't exist already in database
            if page_number == 1 and len(events_collection_normalized) > 0:
                parsing_pointer.current_pointer = self._new_parsing_pointer(events_collection_normalized[0])
                logging.info('Remembered new parsing pointer: %s', parsing_pointer.current_pointer)

            # Remove events which have finished in past
            logging.info('%s events in our list of normalized collection of events', len(events_collection_normalized))
            events_collection_normalized = self._remove_already_finished_events(events_collection_normalized)
            logging.info('In summary for page number %s. New events: %s, is existing event on the page: %s',
                         page_number, len(events_collection_normalized), already_saved_event_in_collection)

            # Save new set of events to database
            self._write_events_to_db(events_collection_normalized)

            # For mode = "only_new"
            # List of events from source has to be sorted by field where is value for parsing pointer.
            # If we have an event more than parsing pointer, it means that we work with event was
            # parsed last time and we don't have to continue
            if mode == "only_new" and already_saved_event_in_collection:
                break
            # It can prevent DDOS attack for the source file
            if page_number == 1000:
                break

            page_number += 1

            # Add sleep to don't ddos attack source server
            time.sleep(1)

        # Inactivate events in the database which are not represented in the source for now
        if mode == "full_with_updating":
            self._inactivate_not_represented_on_source_events(all_events_ids)

        # For test purpose - we can check how many pages we have handled
        return page_number

    def _create_parsing_pointer(self):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _make_url(self, page, test_url):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    @staticmethod
    def _get_url_content(url):
        """
        Return object Request with full HTML (or JSON dictionary for KudaGo) for url
        :param url:
        :return:
        """
        logging.debug('Enter to the method')
        with requests.get(url) as req:
            logging.info('status code %s, number of symbols in text: %s', req.status_code, len(req.text))
            return req

    @staticmethod
    def _is_bad_page(url_content):
        logging.debug('Enter to the method')
        if url_content.status_code != 200:
            logging.error('Stop parsing. Status code == %s', url_content.status_code)
            return True
        return False

    def _list_parser(self, url_content):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _check_parsing_pointer(self, item, previous_parsing_pointer_value):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _item_parser(self, item):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _checking_events_in_database(self, mode, previous_parsing_pointer_value, events):

        # Initialisation of vars
        events_for_db = events
        already_saved_event_in_collection = False

        if mode == "only_new":
            if self._check_parsing_pointer(events[0], previous_parsing_pointer_value):
                logging.info('We have already handled this event')
                already_saved_event_in_collection = True
                events_for_db = []
            else:
                logging.info('It is a new event')

        if mode == "full":
            if self._check_is_this_event_in_db_already(events[0]):
                logging.info('We have already handled this event')
                already_saved_event_in_collection = True
                events_for_db = []
            else:
                logging.info('It is a new event')

        if mode == "full_with_updating":
            same_events_in_db = self._get_same_events_from_db(events[0])
            logging.info('This event is already in our database: %s', len(same_events_in_db))
            events_for_db = self._update_events_from_db(same_events_in_db, events)

        return events_for_db, already_saved_event_in_collection

    def _check_is_this_event_in_db_already(self, event):
        """
        Return True if this event is already in the database
        Return False if this event is new
        :param event:
        :return:
        """
        same_event_in_db = self._session.query(Event).filter(Event._url == event.url).first()
        if same_event_in_db:
            return True
        return False

    def _get_same_events_from_db(self, event):
        """
        Return list of Events from the database with the same url which has event from parameter
        :param event:
        :return:
        """
        same_events_in_db = self._session.query(Event).filter(Event._url == event.url).all()
        return same_events_in_db

    @staticmethod
    def _update_events_from_db(same_events_in_db, events):
        result_list_of_events = []

        # Preparing list of Event ids which are represented in the source for now
        ids_actual_events = []

        # Gathering updated events from the database and new events from the source
        for event in events:
            i_find_event = False
            for event_from_db in same_events_in_db:
                if event.start_time == event_from_db.start_time and event.finish_time == event_from_db.finish_time:
                    event_from_db.update_event(event)
                    result_list_of_events.append(event_from_db)
                    i_find_event = True
                    ids_actual_events.append(event_from_db.event_id)
                    break
            if not i_find_event:
                result_list_of_events.append(event)

        # Inactivating of not represented in source events
        for event_from_db in same_events_in_db:
            if event_from_db.event_id in ids_actual_events:
                continue
            event_from_db.status = "hidden"
            result_list_of_events.append(event_from_db)

        return result_list_of_events

    def _inactivate_not_represented_on_source_events(self, all_events_ids):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _new_parsing_pointer(self, event):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    @staticmethod
    def _remove_already_finished_events(events):
        result = []
        # TODO: refactoring 3 - will have be in config file
        # Server time is least for 3 hours than real moscow time
        current_timestamp = (datetime.datetime.now() + datetime.timedelta(hours=3)).timestamp()
        for event in events:
            if event.finish_time > current_timestamp:
                result.append(event)
        return result

    def _write_events_to_db(self, events_collection_normalized):
        """
        Writes list with events to database
        :param events_collection_normalized:
        :return:
        """
        logging.debug('Enter to the method')
        logging.info('We will write to database %s events', len(events_collection_normalized))

        # Save all new events to the database
        for event in events_collection_normalized:
            self._session.add(event)
        self._session.commit()
        logging.info('Write to database was successful')

        # Assignment real id of last event for duplicates of this event with other dates
        handled_duplicate_source_id = []
        for event in events_collection_normalized:
            if (not event.duplicate_source_id) or (event.duplicate_source_id in handled_duplicate_source_id):
                continue
            all_duplicates = self._session.query(Event).filter(Event._duplicate_source_id == event.duplicate_source_id).all()
            latest_event_id = sorted(all_duplicates, key=lambda x: x.start_time, reverse=True)[0].event_id
            for duplicate_event in all_duplicates:
                duplicate_event.duplicate_id = latest_event_id
                self._session.add(duplicate_event)
            handled_duplicate_source_id.append(event.duplicate_source_id)
        self._session.commit()
        logging.info('Number of handled duplicate source id: %s', len(handled_duplicate_source_id))
        return
