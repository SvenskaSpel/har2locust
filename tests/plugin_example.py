from har2locust.plugin import entriesprocessor
import logging


@entriesprocessor
def log_something_and_drop_everthing_but_the_first_request(entries):
    logging.info(f"hello")
    return [entries[0]]
