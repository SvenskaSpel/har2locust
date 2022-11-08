from har2locust.plugin import entriesprocessor, valuesprocessor, cstprocessor
import logging
import libcst as cst
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


@cstprocessor
def rename_task_function(tree: cst.Module) -> cst.Module:
    class RenameTaskFunction(cst.CSTTransformer):
        def leave_FunctionDef(self, node: cst.FunctionDef, updated_node: cst.FunctionDef) -> cst.FunctionDef:
            if node.name.value == "t":
                updated_node = updated_node.with_changes(name=cst.Name("renamed_function"))
            return updated_node

    return tree.visit(RenameTaskFunction())
