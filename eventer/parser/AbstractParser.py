import time
import datetime
import requests
import logging
from Event import Event


class AbstractParser:

    def __init__(self, session):
        self._session = session

    def main(self):
        """
        This method downloads list of events from source (in cycle with parameter page number)
        and save new data to database while we face parsing pointer (it means, that we have reached last successfully
        handled event from this source)
        :return:
        """
        # Define last event from previous parsing session. When we reach it, we stop parsing.
        parsing_pointer = self._create_parsing_pointer()
        self._session.add(parsing_pointer)
        previous_parsing_pointer_value = parsing_pointer.current_pointer

        # Look over all pages while we don't reach a parsing pointer
        page_number = 1
        already_saved_event_in_collection = False
        while True:
            logging.info('New page number = %s', page_number)
            url = self._make_url(page=page_number)
            logging.info('Url for parsing: %s', url)
            url_content = self._get_url_content(url)
            events_collection_source = self._list_parser(url_content)
            logging.info('We have extracted from page in our list %s events', len(events_collection_source))

            # Look over all events from list and create normalize dictionary for every event
            events_collection_normalized = []
            for item in events_collection_source:
                events = self._item_parser(item)
                logging.debug('Event dictionary after item parsing: %s', events)

                # Check parsing pointer for every event to avoid duplicates in database
                if self._check_parsing_pointer(events[0], previous_parsing_pointer_value):
                    logging.info('Checked parsing pointer, we have already handled this event')
                    already_saved_event_in_collection = True
                    continue
                logging.info('Checked parsing pointer, it is a new event')
                events_collection_normalized += events

            # Save new parsing pointer - only in the beginning of this iteration of parsing
            # We will save a new parsing pointer only if we have at least one new event,
            # that doesn't exist already in database
            if page_number == 1 and len(events_collection_normalized) > 0:
                parsing_pointer.current_pointer = self._new_parsing_pointer(events_collection_normalized[0])
                logging.info('Remembered new parsing pointer: %s', parsing_pointer.current_pointer)

            # Remove events which have finished in past
            logging.info('%s events in our list of normalized dictionaries', len(events_collection_normalized))
            events_collection_normalized = self._remove_already_finished_events(events_collection_normalized)
            logging.info('In summary for page number %s. New events: %s, is existing event on the page: %s',
                         page_number, len(events_collection_normalized), already_saved_event_in_collection)

            # Save new set of events to database
            self._write_events_to_db(events_collection_normalized)

            # List of events from source has to be sorted by field where is value for parsing pointer.
            # If we have an event more than parsing pointer, it means that we work with event was
            # parsed last time and we don't have to continue
            if already_saved_event_in_collection or page_number == 10:
                break

            page_number += 1

            # Add sleep to don't ddos attack source server
            time.sleep(1)

    def _create_parsing_pointer(self):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _make_url(self, page):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _get_url_content(self, url):
        """
        Return object Request with full HTML (or JSON dictionary for KudaGo) for url
        :param url:
        :return:
        """
        logging.debug('Enter to the method')
        # TODO: make retries for request
        with requests.get(url) as req:
            logging.info('status code %s, number of symbols in text: %s', req.status_code, len(req.text))
            if req.status_code == 200:
                return req
            logging.error('status code != 200')
            raise RuntimeError("We can't get content from url: " + url + " status code: " + str(req.status_code))

    def _list_parser(self, url_content):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _check_parsing_pointer(self, item, previous_parsing_pointer_value):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _item_parser(self, item):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _new_parsing_pointer(self, event_dictionary):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _remove_already_finished_events(self, events):
        result = []
        # TODO: refactoring 3 - will have be in config file
        current_timestamp = (datetime.datetime.now() + datetime.timedelta(
            hours=3)).timestamp()  # server time is least for 3 hours than real moscow time
        for event in events:
            if event['finish_time'] > current_timestamp:
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

        # Запись всех новых событий в базу данных
        for item in events_collection_normalized:
            event = Event(item)
            self._session.add(event)
        self._session.commit()
        logging.info('Write to database was successful')

        # Assignment real id of last event for duplicates of this event with other dates
        handled_duplicate_source_id = []
        for item in events_collection_normalized:
            if item['duplicate_source_id'] == "" or item['duplicate_source_id'] in handled_duplicate_source_id:
                continue
            all_duplicates = self._session.query(Event).filter(Event._duplicate_source_id == item['duplicate_source_id']).all()
            latest_event_id = sorted(all_duplicates, key=lambda x: x.start_time, reverse=True)[0].event_id
            for event in all_duplicates:
                event.duplicate_id = latest_event_id
                self._session.add(event)
            handled_duplicate_source_id.append(item['duplicate_source_id'])
        self._session.commit()
        logging.info('Number of handled duplicate source id: %s', len(handled_duplicate_source_id))
        return
