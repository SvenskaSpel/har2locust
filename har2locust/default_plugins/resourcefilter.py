from har2locust.plugin import entriesprocessor_with_args


@entriesprocessor_with_args
def process(entries, args):
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
