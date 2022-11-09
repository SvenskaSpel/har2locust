from har2locust.plugin import entriesprocessor, astprocessor
import logging
from ast import *


@entriesprocessor
def process(entries):
    output = []
    for e in entries:
        headers = e["response"]["headers"]
        for h in headers:
            if h["name"].lower() == "content-type":
                if h["value"] == "application/javascript":
                    logging.debug(f"ignoring request {e['request']['url']}")
                    break
                if h["value"].startswith("application/json"):
                    if (
                        "postData" not in e["request"]  # not a post, ok for .rest
                        or e["request"]["postData"]["mimeType"] == "application/json"  # json payload, also ok
                    ):
                        logging.debug(f"{e['request']['url']} is a rest request!")
                        e["rest"] = True
        else:
            logging.debug(f"appending request {e['request']['url']}")
            output.append(e)
    entries[:] = output  # overwrite entries, in place


@astprocessor
def process_ast(tree: Module, values: dict):
    class Transformer(NodeTransformer):
        def visit_ClassDef(self, node: ClassDef) -> ClassDef:
            node.bases[0] = Name("RestUser")
            self.generic_visit(node)
            return node

        def visit_Import(self, node: Import) -> Import:
            self.generic_visit(node)
            return node

        def visit_ImportFrom(self, node: ImportFrom) -> ImportFrom:
            if node.names[0].name == "FastHttpUser":
                node.module = "locust_plugins.users"
                node.names[0].name = "RestUser"
            self.generic_visit(node)
            return node

        def visit_Module(self, node: Module) -> Module:
            node.body = (
                parse(
                    """
from locust import events
from locust_plugins.listeners import RescheduleTaskOnFail
"""
                ).body
                + node.body
                + parse(
                    f"""
@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    RescheduleTaskOnFail(environment)
if __name__ == "__main__":
    run_single_user({values['name']})
""",
                ).body
            )
            self.generic_visit(node)
            return node

    Transformer().visit(tree)
