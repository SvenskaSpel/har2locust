from har2locust.plugin import entriesprocessor


@entriesprocessor
def rest(entries: list[dict]):
    for e in entries:
        for h in e["response"]["headers"]:
            if h["name"].lower() == "content-type":
                if h["value"].startswith("application/json"):
                    r = e["request"]
                    if (
                        "postData" not in r  # not a post, ok for .rest
                        or r["postData"]["mimeType"] == "application/json"  # json payload, also ok
                    ):
                        # logging.debug(f"{r['url']} is a rest request!")
                        r["fname"] = "rest"
                        r["extraparams"] = []  # catch_response=True is already the default for .rest()


# The following is no longer needed, now that rest-method is a part of FastHttpUser, but can still serve as a good example:
# from ast import *
# from har2locust.plugin import astprocessor
#
# @astprocessor
# def process_ast(tree: Module, values: dict):
#     class Transformer(NodeTransformer):
#         def visit_ClassDef(self, node: ClassDef) -> ClassDef:
#             node.bases[0] = Name("RestUser")
#             self.generic_visit(node)
#             return node

#         def visit_ImportFrom(self, node: ImportFrom) -> ImportFrom:
#             if node.names[0].name == "FastHttpUser":
#                 node.module = "locust_plugins.users"
#                 node.names[0].name = "RestUser"
#             self.generic_visit(node)
#             return node

#         def visit_Module(self, node: Module) -> Module:
#             node.body = (
#                 parse(
#                     """
# from locust import events
# from locust_plugins.listeners import RescheduleTaskOnFail
# """
#                 ).body
#                 + node.body
#                 + parse(
#                     f"""
# @events.init.add_listener
# def on_locust_init(environment, **_kwargs):
#     RescheduleTaskOnFail(environment)
# if __name__ == "__main__":
#     run_single_user({values['class_name']})
# """,
#                 ).body
#             )
#             self.generic_visit(node)
#             return node

#     Transformer().visit(tree)
