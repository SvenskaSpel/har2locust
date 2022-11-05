from har2locust.plugin import entriesprocessor
import re
import pathlib


@entriesprocessor
def process(entries):
    headerignore_path = pathlib.Path(".headerignore")
    header_filters = []
    if headerignore_path.is_file():
        with open(headerignore_path) as f:
            header_filters = f.readlines()
            header_filters = [line.rstrip() for line in header_filters if not line.strip().startswith("#")]

    # always filter these, because they will be added by locust automatically
    header_filters.extend(["^cookie", "^content-length"])
    # always filter this, because it is not a real header
    header_filters.extend(["^:"])

    for e in entries:
        request = e["request"]
        request["headers"] = [h for h in request["headers"] if not any(re.search(r, h["name"]) for r in header_filters)]
