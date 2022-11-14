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


def __main__():
    global args  # allow plugins to access command line arguments
    args = get_parser().parse_args()
    logging.basicConfig(level=args.loglevel.upper())
    load_plugins(args.plugins.split(",") if args.plugins else [])
    main(args.input, template_name=args.template)


def main(har_file: str, template_name="locust.jinja2"):
    har_path = pathlib.Path(har_file)
    name = pathlib.Path(har_file).stem.replace("-", "_").replace(".", "_")  # build class name from filename
    with open(har_path, encoding="utf8", errors="ignore") as f:
        har = json.load(f)
    logging.debug(f"loaded {har_path}")

    pp_dict = process(har)
    py = rendering(template_name, {"name": name, **pp_dict})
    print(py)


def process(har: dict) -> dict:
    """Scan the har dict for common headers

    In doing so request and reponse variables are organized in a useful format:
    from [[{'name': key, 'value': value}, ...], ...] list of list of dict
    to   [{(key, value), ...}, ...] list of set of tuple.
    Moreover requests can be filter by resource type.

    Args:
        har (dict): the dict obtain by parsing har file with json
    """
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

    logging.debug(f"{len(entries)} entries after applying entriesprocessors")

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


def load_plugins(plugins: List[str] = []):
    package_root_dir = pathlib.Path(__file__).parents[1]
    plugin_dir = package_root_dir / "har2locust/plugins"
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
