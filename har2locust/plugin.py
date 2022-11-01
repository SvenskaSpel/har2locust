from typing import List, Dict
from typing import Callable

# For an example of how to write a plugin, see rest.py


class entriesprocessor:
    processors: List[Callable[[List[Dict]], List[Dict]]] = []

    def __init__(self, func: Callable[[List[Dict]], List[Dict]]):
        self.processors.append(func)
