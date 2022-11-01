from har2locust.plugin import entryprocessor
import logging


@entryprocessor
def log_something_and_drop_everthing_but_the_first_request(entries):
    logging.info(f"hello")
    return [entries[0]]
