from typing import List, Dict
from typing import Callable


class ProcessEntries:
    plugins: List[Callable[[List[Dict]], List[Dict]]] = []

    def __init__(self, func: Callable[[List[Dict]], List[Dict]]):
        ProcessEntries.plugins.append(func)

    @classmethod
    def run_plugins(cls, entries: List[Dict]) -> List[Dict]:
        for p in cls.plugins:
            entries = p(entries)
        return entries


# example:
#
# from har2locust.plugin import ProcessEntries
#
# @ProcessEntries
# def process(entries: List[Dict]) -> List[Dict]:
#     return entries
