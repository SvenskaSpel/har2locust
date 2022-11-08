import importlib
import json
import logging
import os
import pathlib
import libcst as cst
import sys
from typing import List
from urllib.parse import urlsplit
import jinja2
from .argument_parser import get_parser
from .plugin import cstprocessor, entriesprocessor, valuesprocessor, outputstringprocessor


def cli():
    args = get_parser().parse_args()
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
    har_path = pathlib.Path(har_file)

    # build safe class name from filename
    name = pathlib.Path(har_file).stem.replace("-", "_").replace(".", "_")

    with open(har_path, encoding="utf8", errors="ignore") as f:
        har = json.load(f)
    logging.debug(f"loaded {har_path}")

    default_plugins = [
        "har2locust/plugins/rest.py",
        "har2locust/plugins/urlignore.py",
        "har2locust/plugins/headerignore.py",
        "har2locust/plugins/black.py",
    ]
    default_and_extra_plugins = default_plugins + plugins
    for plugin in default_and_extra_plugins:
        sys.path.append(os.path.curdir)
        import_path = plugin.replace("/", ".").rstrip(".py")
        importlib.import_module(import_path)
    logging.debug(f"loaded plugins {default_and_extra_plugins}")

    pp_dict = process(har, resource_type=resource_type)

    py = rendering(
        template_name,
        {
            "name": name,
            "prefix": "from locust import task, run_single_user",
            "baseuser_module": "locust",
            "baseuser_class": "FastHttpUser",
            "extra_class_text": "",
            **pp_dict,
        },
    )

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

    for p in entriesprocessor.processors:
        p(entries)

    logging.debug(f"{resource_type=}")
    logging.debug(f"{len(entries)} entries after filtering by resource_type")

    # organize request variable in a useful format
    # [[{'name': key, 'value': value}, ...], ...] list of list of dict ->
    # [{(key, value), ...}, ...] list of set of tuple
    headers_req, headers_res = [], []
    for e in entries:
        headers_req.append({(h["name"], h["value"]) for h in e["request"]["headers"]})
        headers_res.append({(h["name"], h["value"]) for h in e["response"]["headers"]})

    # collect headers common to all requests
    default_headers = set.intersection(*headers_req)

    urlparts = urlsplit(entries[0]["request"]["url"])
    host = f"{urlparts.scheme}://{urlparts.netloc}/"
    # requests is a list of dictionary with value specific to single requests
    requests = [
        {
            "url": e["request"]["url"].removeprefix(host),
            "method": e["request"]["method"].lower(),
            "headers": headers_req[i] - default_headers,
            "post_data": e["request"]["postData"]["text"] if "postData" in e["request"] else None,
            "rest": e["rest"] if "rest" in e else False,
        }
        for i, e in enumerate(entries)
    ]

    responses = [
        {
            "status": e["response"]["status"],
            "headers": headers_res[i],
            "redirect_url": e["response"]["redirectURL"],
            "content": e["response"]["content"],
        }
        for i, e in enumerate(entries)
    ]

    logging.debug("preprocessed har dict")

    return dict(host=host, default_headers=default_headers, requests=requests, responses=responses)


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
        tree = cst.parse_module(py)
    except cst.ParserSyntaxError as e:
        levelmessage = " Set log level DEBUG to see the whole output." if logging.DEBUG < logging.root.level else ""
        logging.error(
            f"Generated python code was invalid. Check your template.{levelmessage}\n{e.message} at:\n{e.context} ({e.raw_line}:{e.raw_column})"
        )
        logging.debug(py)
        sys.exit(1)
    for p in cstprocessor.processors:
        tree = p(tree)
    py = tree.code
    logging.debug("cstprocessors applied")

    for p in outputstringprocessor.processors:
        py = p(py)
    logging.debug("outputstringprocessors applied")

    return py
