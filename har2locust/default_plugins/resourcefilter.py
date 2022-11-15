from har2locust.plugin import entriesprocessor
import re
import pathlib

# accessing args here is somewhat of a hack, but plugins dont usually need access to command line params,
# and I didnt want them *all* to have to take it as a method argument
from ..__main__ import args


@entriesprocessor
def process(entries):
    # accessing args here is somewhat of a hack, but plugins dont usually need access to command line params,
    # and I didnt want them *all* to have to take it as a method argument
    resource_types = args.resource_types.split(",")
    supported_resource_type = {
        "xhr",
        "script",
        "stylesheet",
        "image",
        "font",
        "document",
        "other",
    }
    if unsupported := set(resource_types) - supported_resource_type:
        raise NotImplementedError(f"{unsupported} resource types are not supported")

    entries[:] = [e for e in entries if e["_resourceType"] in resource_types]
