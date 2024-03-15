# This file has some advanced examples of how to massage your recording
# Use it as inspiration for the techniques, not as a recommendation for exactly what to do
import ast
import pathlib
import re
import typing

from har2locust.plugin import astprocessor

# useful way to debug: logging.info(ast.unparse(node))


@astprocessor
def inject_authentication(tree: ast.Module, values: dict):
    class T(ast.NodeTransformer):
        def visit_Module(self, node: ast.Module) -> ast.Module:
            things = ast.parse("""
import re
import os

from locust_plugins.listeners import StopUserOnFail
os.environ["LOCUST_TEST_ENV"] = "itp1"
os.environ["LOCUST_TENANT"] = "lb"


@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    import time
    environment.events.request.add_listener(lambda *args, **kw: time.sleep(0.1))
    StopUserOnFail(environment)""")
            node.body[2:2] = things.body  # list slicing is fun
            self.generic_visit(node)
            return node

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
                except Exception:
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


@astprocessor
def do_correlations(tree: ast.Module, values: dict):
    correlation_path = pathlib.Path(".correlations")
    if correlation_path.is_file():
        with open(correlation_path) as f:
            correlations = [
                line.rstrip() for line in f.readlines() if line.strip() and not line.strip().startswith("#")
            ]
    else:
        correlations = []

    class T(ast.NodeTransformer):
        def visit_Dict(self, node: ast.Dict) -> ast.Dict:
            for key in node.keys:
                if typing.cast(ast.Constant, key).s == "bet_number":
                    node.values[node.keys.index(key)] = ast.parse('f"single_{id}"').body[0]  # type: ignore
                for correlation in correlations:
                    _, _, *corr_vars = correlation.split(",")
                    if typing.cast(ast.Constant, key).s in corr_vars:
                        node.values[node.keys.index(key)] = (
                            # the variable will always have the name of the first corr var
                            ast.Name(corr_vars[0].replace("-", "_"))
                        )

            self.generic_visit(node)
            return node

        def visit_With(self, node: ast.With) -> ast.With:
            for correlation in correlations:
                url, corr_expr, *corr_vars = correlation.split(",")
                if url == node.items[0].context_expr.args[1].value:  # type: ignore
                    node.body[0] = ast.parse(  # type: ignore
                        f"""{corr_vars[0].replace('-', '_')} = re.findall('''{corr_expr}''', resp.text)[0] if resp.text else None"""
                    )
            self.generic_visit(node)
            return node

    T().visit(tree)
