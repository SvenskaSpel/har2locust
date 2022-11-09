from typing import Callable
import ast

# For examples of how to write a plugin, see plugins/ or tests/plugin_example.py
# The processors allow you to interact with your recording at various stages,

# immediately after reading the HAR JSON
class entriesprocessor:
    processors: list[Callable[[list[dict]], None]] = []

    def __init__(self, func: Callable[[list[dict]], None]):
        self.processors.append(func)


# just before passing values to jinja2 template
class valuesprocessor:
    processors: list[Callable[[dict], None]] = []

    def __init__(self, func: Callable[[dict], None]):
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
