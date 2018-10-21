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
        :param mode: 'only_new' = mode of working parser, when parser get only new events until the parsing pointer value
                     'full' = mode of working parser, when parser get all events
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
            events_collection_normalized = []
            for item in events_collection_source:

                # Parsing of one event in the list into list of related Event objects
                events = self._item_parser(item)
                logging.debug('Events after item parsing: %s', events)
                if len(events) == 0:
                    continue

                # Check is this event in database already for every event to avoid duplicates in database
                if self._check_is_this_event_in_db_already(mode, previous_parsing_pointer_value, events[0]):
                    logging.info('We have already handled this event')
                    already_saved_event_in_collection = True
                    continue
                logging.info('It is a new event')
                events_collection_normalized += events

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

    def _check_is_this_event_in_db_already(self, mode, previous_parsing_pointer_value, event):
        """
        Return True if this event is already in the database
        Return False if this event is new
        :param mode:
        :param previous_parsing_pointer_value:
        :param event:
        :return:
        """
        if mode == "only_new" and self._check_parsing_pointer(event, previous_parsing_pointer_value):
            return True
        if mode == "full":
            same_event_in_db = self._session.query(Event).filter(Event._url == event.url).first()
            if same_event_in_db:
                return True
            return False

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
