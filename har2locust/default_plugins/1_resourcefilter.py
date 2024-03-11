import logging

from har2locust.plugin import entriesprocessor_with_args


@entriesprocessor_with_args
def resourcefilter(entries, args):
    resource_types = args.resource_types.split(",")
    known_resource_type = {
        "xhr",
        "script",
        "stylesheet",
        "image",
        "media",
        "font",
        "document",
        "other",
        "fetch",
        "texttrack",
        "eventsource",
        "manifest",
        # websocket
    }
    if unknown := set(resource_types) - known_resource_type:
        logging.warning(f"You asked for an unknown/unsupported resource type!? ({unknown})")

    entries[:] = [e for e in entries if e.get("_resourceType", "other") in resource_types]
