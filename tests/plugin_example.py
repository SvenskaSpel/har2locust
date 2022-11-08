from har2locust.plugin import entriesprocessor, valuesprocessor, cstprocessor
import logging
import libcst as cst


@entriesprocessor
def log_something_and_drop_everthing_but_the_first_request(entries):
    logging.info(f"hello")
    entries[:] = [entries[0]]


@valuesprocessor
def rename_and_do_stuff(values):
    values["name"] = "NewName"


@cstprocessor
def add_nice_comment(tree: cst.Module):
    class RenameTaskFunction(cst.CSTTransformer):
        def leave_FunctionDef(self, node: cst.FunctionDef, updated_node: cst.FunctionDef) -> cst.FunctionDef:
            if node.name.value == "t":
                updated_node = updated_node.with_changes(name=cst.Name("renamed_function"))
            return updated_node

    t = RenameTaskFunction()
    return tree.visit(t)
