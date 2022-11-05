from har2locust.plugin import entriesprocessor
import re
import pathlib


@entriesprocessor
def process(entries):
    headerignore_path = pathlib.Path(".headerignore")
    filters = []
    if headerignore_path.is_file():
        with open(headerignore_path) as f:
            filters = f.readlines()
            filters = [line.rstrip() for line in filters if line.strip() and not line.strip().startswith("#")]

    # always filter these, because they will be added by locust automatically
    filters.extend(["^cookie", "^content-length"])
    # always filter this, because it is not a real header
    filters.extend(["^:"])

    for e in entries:
        request = e["request"]
        request["headers"] = [h for h in request["headers"] if not any(re.search(r, h["name"]) for r in filters)]
