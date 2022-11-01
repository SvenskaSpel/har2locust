from typing import List, Dict
from typing import Callable

# For an example of how to write a plugin, see rest.py


class ProcessEntries:
    plugins: List[Callable[[List[Dict]], List[Dict]]] = []

    def __init__(self, func: Callable[[List[Dict]], List[Dict]]):
        ProcessEntries.plugins.append(func)

    @classmethod
    def run_plugins(cls, entries: List[Dict]) -> List[Dict]:
        for p in cls.plugins:
            entries = p(entries)
        return entries
