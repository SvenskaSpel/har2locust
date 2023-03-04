from typing import Callable, Optional
from argparse import Namespace
import ast

# For examples of how to write a plugin, see default_plugins/ or tests/plugin_example.py
# The processors allow you to interact with your recording at various stages,


# immediately after reading the HAR JSON
class entriesprocessor:
    processors: list[Callable[[list[dict]], Optional[dict]]] = []

    def __init__(self, func: Callable[[list[dict]], Optional[dict]]):
        self.processors.append(func)


# immediately after reading the HAR JSON, with access to command line arguments
class entriesprocessor_with_args:
    processors: list[Callable[[list[dict], Namespace], Optional[dict]]] = []

    def __init__(self, func: Callable[[list[dict], Namespace], Optional[dict]]):
        self.processors.append(func)


# after rendering template, working with the syntax tree
class astprocessor:
    processors: list[Callable[[ast.Module, dict], None]] = []

    def __init__(self, func: Callable[[ast.Module, dict], None]):
        self.processors.append(func)


# just before printing output, working with the string output
class outputstringprocessor:
    processors: list[Callable[[str], str]] = []

    def __init__(self, func: Callable[[str], str]):
        self.processors.append(func)
