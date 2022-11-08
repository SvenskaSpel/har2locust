from har2locust.plugin import entriesprocessor, valuesprocessor, astprocessor
import logging
import ast
import re


@entriesprocessor
def log_something_and_drop_everthing_but_the_first_request(entries):
    logging.info(f"hello")
    entries[:] = [entries[0]]  # update list in-place


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


@valuesprocessor
def rename_and_do_stuff(values):
    values["name"] = "NewName"


@astprocessor
def rename_task_function(tree: ast.Module):
    class RenameTaskFunction(ast.NodeTransformer):
        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
            if node.name == "t":
                node.name = "renamed_function"
            return node

    RenameTaskFunction().visit(tree)
