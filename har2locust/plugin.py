from typing import List, Dict
from typing import Callable
import libcst as cst

# For examples of how to write a plugin, see plugins/
# The processors allow you to interact with your recording at various stages,

# immediately after reading the HAR
class entriesprocessor:
    processors: List[Callable[[List[Dict]], None]] = []

    def __init__(self, func: Callable[[List[Dict]], None]):
        self.processors.append(func)


# just before passing values to template
class valuesprocessor:
    processors: List[Callable[[Dict], None]] = []

    def __init__(self, func: Callable[[Dict], None]):
        self.processors.append(func)


# after rendering template, working with the syntax tree
class cstprocessor:
    processors: List[Callable[[cst.Module], cst.Module]] = []

    def __init__(self, func: Callable[[cst.Module], cst.Module]):
        self.processors.append(func)


# just before printing outputm working with the string output
class outputstringprocessor:
    processors: List[Callable[[str], str]] = []

    def __init__(self, func: Callable[[str], str]):
        self.processors.append(func)
