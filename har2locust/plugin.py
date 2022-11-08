from typing import List, Dict
from typing import Callable
import ast

# For examples of how to write a plugin, see plugins/ or tests/plugin_example.py
# The processors allow you to interact with your recording at various stages,

# immediately after reading the HAR JSON
class entriesprocessor:
    processors: List[Callable[[List[Dict]], None]] = []

    def __init__(self, func: Callable[[List[Dict]], None]):
        self.processors.append(func)


# just before passing values to jinja2 template
class valuesprocessor:
    processors: List[Callable[[Dict], None]] = []

    def __init__(self, func: Callable[[Dict], None]):
        self.processors.append(func)


# after rendering template, working with the syntax tree
class astprocessor:
    processors: List[Callable[[ast.Module], None]] = []

    def __init__(self, func: Callable[[ast.Module], None]):
        self.processors.append(func)


# just before printing output, working with the string output
class outputstringprocessor:
    processors: List[Callable[[str], str]] = []

    def __init__(self, func: Callable[[str], str]):
        self.processors.append(func)
