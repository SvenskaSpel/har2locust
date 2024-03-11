# This file has some advanced examples of how to massage your recording
# Use it as inspiration for the techniques, not as a recommendation for exactly what to do
import ast
import pathlib
import re
import typing

from har2locust.plugin import astprocessor, entriesprocessor

# useful way to debug: print(ast.unparse(node))


@entriesprocessor
def skip_origin_header(entries):
    # this particular site doesnt care about origin header and skipping it makes the locustfile much neater
    for e in entries:
        request = e["request"]
        request["headers"] = [h for h in request["headers"] if h["name"] != "origin"]


@astprocessor
def inject_authentication(tree: ast.Module, values: dict):
    class T(ast.NodeTransformer):
        def visit_ImportFrom(self, node: ast.ImportFrom) -> ast.ImportFrom:
            # our base class is RestUser, not FastHttpUser
            if node.names[0].name == "FastHttpUser":
                node.module = "svs_locust"
                node.names[0].name = "RestUser"
            self.generic_visit(node)
            return node

        def visit_ClassDef(self, node: ast.ClassDef) -> ast.ClassDef:
            typing.cast(ast.Name, node.bases[0]).id = "RestUser"
            node.body.pop(0)  # remove host
            self.generic_visit(node)
            return node

        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
            # replace testlogin request with call to self.auth()
            for i in range(len(node.body)):
                try:
                    url = node.body[i].items[0].context_expr.args[1].value  # type: ignore
                except:  # noqa: E722
                    url = None
                if url == "/player/1/authenticate/testlogin":
                    block = ast.parse(
                        """
self.customer = next(self.customer_iterator)
self.auth()
"""
                    )
                    node.body[i] = block.body[0]
                    # yea, the next line modifies what we're iterating over so we'll miss the last element, which is ugly
                    node.body.insert(i + 1, block.body[1])
            self.generic_visit(node)
            return node

    T().visit(tree)


@astprocessor
def rest_(tree: ast.Module, values: dict):
    class T(ast.NodeTransformer):
        def visit_Call(self, node: ast.Call) -> ast.Call:
            # call rest_ instead of rest for those urls that have &_<timestamp> at the end
            if isinstance(node.func, ast.Attribute):
                try:
                    url = node.args[1]
                except Exception:
                    url = None
                if isinstance(url, ast.Constant):
                    if node.func.attr == "rest":
                        if re.search(r"[&?]_=\d+$", url.value):
                            node.func.attr = "rest_"
                            url.value = re.sub(r"[&?]_=\d+$", "", url.value)
            self.generic_visit(node)
            return node

    T().visit(tree)

            self.generic_visit(node)
            return node

    T().visit(tree)


# More examples

# @entriesprocessor
# def log_something_and_drop_everthing_but_the_first_request(entries):
#     logging.info(f"hello")
#     entries[:] = [entries[0]]  # update list in-place

# @entriesprocessor
# def parametrize_ssn(entries):
#     for e in entries:
#         if "postData" in e["request"]:
#             e["request"]["postData"]["text"] = re.sub(
#                 r'"personalId":"\d*"',
#                 "\"personalId\":self.customer['ssn']",
#                 e["request"]["postData"]["text"],
#             )
