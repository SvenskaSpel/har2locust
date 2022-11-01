from har2locust.plugin import entriesprocessor, valuesprocessor
import logging


@entriesprocessor
def log_something_and_drop_everthing_but_the_first_request(entries):
    logging.info(f"hello")
    entries[:] = [entries[0]]


@valuesprocessor
def rename_and_do_stuff(values):
    values["name"] = "NewName"
