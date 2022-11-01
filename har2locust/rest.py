from .plugin import ProcessEntries
import logging


@ProcessEntries
def process(entries):
    output = []
    for e in entries:
        headers = e["response"]["headers"]
        for h in headers:
            if h["name"].lower() == "content-type":
                logging.debug(h)
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
            output.append(e)
    return output
