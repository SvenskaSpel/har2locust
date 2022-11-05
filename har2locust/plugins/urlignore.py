from har2locust.plugin import entriesprocessor
import re
import pathlib


@entriesprocessor
def process(entries):
    urlignore_file = pathlib.Path(".urlignore")
    filters = []
    if urlignore_file.is_file():
        with open(urlignore_file) as f:
            filters = f.readlines()
            filters = [line.rstrip() for line in filters if line.strip() and not line.strip().startswith("#")]

    entries[:] = [e for e in entries if not any(re.search(r, e["request"]["url"]) for r in filters)]
