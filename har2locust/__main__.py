import importlib
import json
import logging
import os
import pathlib
import ast
import sys
from typing import List
from urllib.parse import urlsplit
import jinja2
from .argument_parser import get_parser
from .plugin import astprocessor, entriesprocessor, valuesprocessor, outputstringprocessor


def __main__(args=None):
    args = get_parser().parse_args(args)
    logging.basicConfig(level=args.loglevel.upper())
    main(
        args.input,
        plugins=args.plugins.split(",") if args.plugins else [],
        resource_type=args.resource_types.split(","),
        template_name=args.template,
    )


def main(
    har_file: str,
    plugins: List[str] = [],
    resource_type=["xhr", "document", "other"],
    template_name="locust.jinja2",
):
    default_plugins = list(pathlib.Path("har2locust/plugins").glob("*.py"))
    default_and_extra_plugins = default_plugins + plugins
    for plugin in default_and_extra_plugins:
        sys.path.append(os.path.curdir)
        import_path = str(plugin).replace("/", ".").rstrip(".py")
        importlib.import_module(import_path)
    logging.debug(f"loaded plugins {default_and_extra_plugins}")

    har_path = pathlib.Path(har_file)
    name = pathlib.Path(har_file).stem.replace("-", "_").replace(".", "_")  # build class name from filename
    with open(har_path, encoding="utf8", errors="ignore") as f:
        har = json.load(f)
    logging.debug(f"loaded {har_path}")

    pp_dict = process(har, resource_type=resource_type)
    py = rendering(template_name, {"name": name, **pp_dict})
    print(py)


def process(
    har: dict,
    resource_type=["xhr", "document", "other"],
) -> dict:
    """Scan the har dict for common headers

    In doing so request and reponse variables are organized in a useful format:
    from [[{'name': key, 'value': value}, ...], ...] list of list of dict
    to   [{(key, value), ...}, ...] list of set of tuple.
    Moreover requests can be filter by resource type.

    Args:
        har (dict): the dict obtain by parsing har file with json
        resource_type (list): list of resource type to include in the python
            generated code. Supported type are `xhr`, `script`, `stylesheet`,
            `image`, `font`, `document`, `other`.
    """
    supported_resource_type = {
        "xhr",
        "script",
        "stylesheet",
        "image",
        "font",
        "document",
        "other",
    }
    if unsupported := set(resource_type) - supported_resource_type:
        raise NotImplementedError(f"{unsupported} resource types are not supported")

    har_version = har["log"]["version"]
    logging.debug(f'har log version is "{har_version}"')
    if har_version != "1.2":
        logging.warning(f"Untested har version {har_version}")

    entries = har["log"]["entries"]
    logging.debug(f"found {len(entries)} entries")

    # filtering entries
    entries = [e for e in har["log"]["entries"] if e["_resourceType"] in resource_type]

    for e in entries:
        # set defaults
        e["request"]["fname"] = "client.request"
        e["request"]["extraparams"] = [("catch_response", True)]

    for p in entriesprocessor.processors:
        p(entries)

    logging.debug(f"{resource_type=}")
    logging.debug(f"{len(entries)} entries after filtering by resource_type")

    headers_req, headers_res = [], []
    for e in entries:
        headers_req.append({(h["name"], h["value"]) for h in e["request"]["headers"]})
        headers_res.append({(h["name"], h["value"]) for h in e["response"]["headers"]})

    # collect headers common to all requests
    default_headers = set.intersection(*headers_req)

    urlparts = urlsplit(entries[0]["request"]["url"])
    host = f"{urlparts.scheme}://{urlparts.netloc}/"
    for i, e in enumerate(entries):
        r = e["request"]
        r["url"] = r["url"].removeprefix(host)
        r["headers"] = sorted(headers_req[i] - default_headers, key=lambda item: item[0])

    logging.debug("preprocessed har dict")

    # return the "values"-dict for use in rendering
    return dict(host=host, default_headers=sorted(default_headers), entries=entries)


def rendering(template_name: str, values: dict) -> str:
    for p in valuesprocessor.processors:
        p(values)
    logging.debug("valueprocessors applied")

    logging.debug(f'about to load template "{template_name}"')
    if pathlib.Path(template_name).exists():
        template_path = pathlib.Path(template_name)
    else:
        template_path = pathlib.Path(__file__).parents[0].joinpath(pathlib.Path(template_name))
        if not template_path.exists():
            raise Exception(f"Template {template_name} does not exist, neither in current directory nor as built in")

    template_dir = template_path.parents[0]

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
    template = env.get_template(template_path.name)
    logging.debug("template loaded")

    py = template.render(values)
    logging.debug("template rendered")

    try:
        tree = ast.parse(py, type_comments=True)
    except SyntaxError as e:
        logging.debug(py)
        levelmessage = " (set log level DEBUG to see the whole output)" if logging.DEBUG < logging.root.level else ""
        logging.error(f"{e.msg} when parsing rendered template{levelmessage}")
        raise

    for p in astprocessor.processors:
        p(tree, values)
    py = ast.unparse(ast.fix_missing_locations(tree))
    logging.debug("astprocessors applied")

    for p in outputstringprocessor.processors:
        py = p(py)
    logging.debug("outputstringprocessors applied")

    return py


if __name__ == "__main__":
    __main__()
