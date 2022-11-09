from har2locust.plugin import astprocessor
from ast import *


@astprocessor
def process_ast(tree: Module, values: dict):
    class Transformer(NodeTransformer):
        def visit_ClassDef(self, node: ClassDef) -> ClassDef:
            node.name = values["name"]

            host_statement = node.body[0]
            assert isinstance(host_statement, Assign)
            host_statement.value = Constant(value=values["host"])

            if values["default_headers"]:
                d = dict(values["default_headers"])
                default_headers_statement = Assign(
                    targets=[Name(id="default_headers", ctx=Store())],
                    value=Dict(
                        keys=[Constant(k) for k in d.keys()],
                        values=[Constant(v) for v in d.values()],
                    ),
                )
                node.body.insert(1, default_headers_statement)

            self.generic_visit(node)
            return node

    Transformer().visit(tree)
