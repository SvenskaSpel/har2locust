from typing import List, Dict
from typing import Callable

# For an example of how to write a plugin, see rest.py


class entriesprocessor:
    processors: List[Callable[[List[Dict]], None]] = []

    def __init__(self, func: Callable[[List[Dict]], None]):
        self.processors.append(func)


class valuesprocessor:
    processors: List[Callable[[Dict], None]] = []

    def __init__(self, func: Callable[[Dict], None]):
        self.processors.append(func)
