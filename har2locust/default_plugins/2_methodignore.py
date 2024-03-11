import pathlib

from har2locust.plugin import entriesprocessor


@entriesprocessor
def methodignore(entries: list[dict]):
    methodignore_path = pathlib.Path(".methodignore")
    filters = []
    if methodignore_path.is_file():
        with open(methodignore_path) as f:
            filters = f.readlines()
            filters = [line.rstrip() for line in filters if line.strip() and not line.strip().startswith("#")]
    else:
        filters = ["OPTIONS"]  # nobody likes you, OPTIONS

    entries[:] = [e for e in entries if e["request"]["method"] not in filters]
