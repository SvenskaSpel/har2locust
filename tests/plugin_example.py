from har2locust.plugin import entriesprocessor, valuesprocessor, astprocessor
import logging
import ast
from ast import *
import re


@entriesprocessor
def parametrize_ssn(entries):
    # this assumes you have a dict on your user called self.customer
    for e in entries:
        if "postData" in e["request"]:
            e["request"]["postData"]["text"] = re.sub(
                r'"personalId":"\d*"',
                "\"personalId\":self.customer['ssn']",
                e["request"]["postData"]["text"],
            )


# @astprocessor allows you to do all kinds of advanced stuff, like this function that wraps the entire task function body in a with-block.
@astprocessor
def get_customer_from_reader(tree: Module, values: dict):
    class T(NodeTransformer):
        def visit_FunctionDef(self, node: FunctionDef) -> FunctionDef:
            if node.name == "t":
                with_block = parse(
                    f"""
with self.reader.user() as self.customer:
    pass
                    """
                ).body[0]
                assert isinstance(with_block, With), with_block
                with_block.body = node.body
                node.body = [with_block]
            self.generic_visit(node)
            return node

    T().visit(tree)


# More examples

# @entriesprocessor
# def log_something_and_drop_everthing_but_the_first_request(entries):
#     logging.info(f"hello")
#     entries[:] = [entries[0]]  # update list in-place


# @valuesprocessor
# def custom_user_classname(values):
#     values["name"] = "NewName"
