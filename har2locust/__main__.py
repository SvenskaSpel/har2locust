from argparse import Namespace
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
from .plugin import entriesprocessor, entriesprocessor_with_args, valuesprocessor, astprocessor, outputstringprocessor


def __main__(arguments=None):
    args = get_parser().parse_args(arguments)
    logging.basicConfig(level=args.loglevel.upper())
    load_plugins(args.plugins.split(",") if args.plugins else [])
    har_path = pathlib.Path(args.input)
    name = har_path.stem.replace("-", "_").replace(".", "_")  # build class name from filename
    with open(har_path, encoding="utf8", errors="ignore") as f:
        har = json.load(f)
    logging.debug(f"loaded {har_path}")

    pp_dict = process(har, args)
    py = rendering(args.template, {"name": name, **pp_dict})
    print(py)


def process(har: dict, args: Namespace) -> dict:
    if har["log"]["version"] != "1.2":
        logging.warning(f"Untested har version {har['log']['version']}")

    entries = har["log"]["entries"]

    logging.debug(f"found {len(entries)} entries")

    for e in entries:
        # set defaults
        e["request"]["fname"] = "client.request"
        e["request"]["extraparams"] = [("catch_response", True)]

    for p in entriesprocessor.processors:
        p(entries)

    for p in entriesprocessor_with_args.processors:
        p(entries, args)

    logging.debug(f"{len(entries)} entries after applying entriesprocessors")

    headers_req = []

    # calculate headers shared by all requests (same name and value)
    default_headers = None
    for e in entries:
        headers = e["request"]["headers"]
        if default_headers is None:
            default_headers = headers[:]
        else:
            for dh in default_headers[:]:
                for h in headers:
                    if dh["name"] == h["name"]:
                        if dh["value"] != h["value"]:
                            default_headers.remove(dh)  # header has different value
                            break
                        break
                else:
                    default_headers.remove(dh)  # header not present
    if default_headers is None:
        default_headers = []

    default_headers.sort(key=lambda item: item["name"])

    urlparts = urlsplit(entries[0]["request"]["url"])
    host = f"{urlparts.scheme}://{urlparts.netloc}/"
    for e in entries:
        e["request"]["url"] = e["request"]["url"].removeprefix(host)
        headers = e["request"]["headers"]
        for h in headers[:]:
            for dh in default_headers:
                if h["name"] == dh["name"]:
                    headers.remove(dh)
        headers[:] = sorted(headers, key=lambda item: item["name"])
    logging.debug("preprocessed har dict")

    # return the "values"-dict for use in rendering
    return dict(host=host, default_headers=default_headers, entries=entries)


def rendering(template_name: str, values: dict) -> str:
    for p in valuesprocessor.processors:
        p(values)
    logging.debug("valueprocessors applied")

    logging.debug(f'about to load template "{template_name}"')
    if pathlib.Path(template_name).exists():
        template_path = pathlib.Path(template_name)
    else:
        template_path = pathlib.Path(__file__).parents[0] / template_name
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


def load_plugins(plugins: List[str] = []):
    package_root_dir = pathlib.Path(__file__).parents[1]
    plugin_dir = package_root_dir / "har2locust/default_plugins"
    logging.debug(f"loading default plugins from {plugin_dir}")
    default_plugins = [str(d.relative_to(package_root_dir)) for d in plugin_dir.glob("*.py")]
    default_and_extra_plugins = default_plugins + plugins
    sys.path.append(os.path.curdir)  # accept plugins by relative path
    for plugin in default_and_extra_plugins:
        import_path = plugin.replace("/", ".").rstrip(".py")
        importlib.import_module(import_path)
    logging.debug(f"loaded plugins {default_and_extra_plugins}")


if __name__ == "__main__":
    __main__()
