from har2locust.plugin import entriesprocessor, valuesprocessor
import logging


@entriesprocessor
def process(entries):
    output = []
    for e in entries:
        headers = e["response"]["headers"]
        for h in headers:
            if h["name"].lower() == "content-type":
                if h["value"] == "application/javascript":
                    logging.debug(f"ignoring request {e['request']['url']}")
                    break
                if h["value"].startswith("application/json"):
                    if (
                        "postData" not in e["request"]  # not a post, ok for .rest
                        or e["request"]["postData"]["mimeType"] == "application/json"  # json payload, also ok
                    ):
                        logging.debug(f"{e['request']['url']} is a rest request!")
                        e["rest"] = True
        else:
            logging.debug(f"appending request {e['request']['url']}")
            output.append(e)
    entries[:] = output  # overwrite entries, in place


@valuesprocessor
def process_values(values):
    values["baseuser_module"] = "locust_plugins.users"
    values["baseuser_class"] = "RestUser"
    # Black formatting fail on these...
    values[
        "prefix"
    ] = """
from locust import task, run_single_user, events
from locust_plugins.listeners import RescheduleTaskOnFail"""
    values[
        "postfix"
    ] = f"""@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    RescheduleTaskOnFail(environment)
    
if __name__ == "__main__":
    run_single_user({values['name']})
    """
