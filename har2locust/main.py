import argparse
import importlib
import json
import logging
import os
import pathlib
import re
import subprocess
import sys
from typing import Dict, List
from urllib.parse import urlsplit

import jinja2

from ._version import version
from .plugin import entriesprocessor


def cli():
    parser = argparse.ArgumentParser(
        epilog="Example usage: har2locust myrecording.har --plugins myplugin1.py > locustfile.py"
    )
    parser.add_argument(
        "input",
        help="har input file",
    )
    parser.add_argument(
        "-t",
        "--template",
        default="locust.jinja2",
        type=str,
        help=(
            "jinja2 template used to generate locustfile. Default to locust.jinja2. Will check current directory/relative paths first and har2locust built-ins second"
        ),
    )
    parser.add_argument(
        "--plugins",
        type=str,
        default="",
        help="Comma separated list of extra python files to source, containing a method decorated with @ProcessEntries for processing har-entries before generating the locustfile.",
    )
    parser.add_argument(
        "-f",
        "--filters",
        default="xhr,document,other",
        type=str,
        help=(
            "Commas separated list of resource types to be included "
            "in the locustfile. Supported type are `xhr`, "
            "`script`, `stylesheet`, `image`, `font`, `document`, `other`. "
            "Default to xhr,document,other."
        ),
    )
    parser.add_argument(
        "--version",
        "-V",
        action="version",
        version=f"%(prog)s {version}",
    )
    parser.add_argument(
        "--loglevel",
        "-L",
        default="INFO",
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel.upper())

    main(
        args.input,
        plugins=args.plugins.split(",") if args.plugins else [],
        resource_type=args.filters.split(","),
        template_name=args.template,
    )


def main(
    har_file: str,
    plugins: List[str] = [],
    resource_type=["xhr", "document", "other"],
    template_name="locust.jinja2",
):
    har_path = pathlib.Path(har_file)
    with open(har_path, encoding="utf8", errors="ignore") as f:
        har = json.load(f)
    logging.debug(f"loaded {har_path}")

    for plugin in ["har2locust/rest.py"] + plugins:
        sys.path.append(os.path.curdir)
        import_path = plugin.replace("/", ".").rstrip(".py")
        importlib.import_module(import_path)

    logging.debug(f"loaded plugins {plugins}")

    urlignore_file = pathlib.Path(".urlignore")
    url_filters = []
    if urlignore_file.is_file():
        with open(urlignore_file) as f:
            url_filters = f.readlines()
            url_filters = [line.rstrip() for line in url_filters]

    headerignore_path = pathlib.Path(".headerignore")
    header_filters = []
    if headerignore_path.is_file():
        with open(headerignore_path) as f:
            header_filters = f.readlines()
            header_filters = [line.rstrip() for line in header_filters]

    # always filter these, because they will be added by locust automatically
    header_filters.extend(["^cookie", "^content-length"])
    # always filter this, because it is not a real header
    header_filters.extend(["^:"])

    host, headers, requests, responses = preprocessing(
        har, resource_type=resource_type, url_filters=url_filters, header_filters=header_filters
    )
    py = rendering(host, headers, requests, responses, template_name=template_name)

    print(py)


def preprocessing(
    har: dict,
    resource_type=["xhr", "document", "other"],
    url_filters: List[str] = [],
    header_filters: List[str] = [],
) -> tuple[str, Dict, List[Dict], List[Dict]]:
    """Scan the har dict for common headers and cookies and group them into
    session headers and session cookies.

    In doing sorequest and reponse variables  are organized in a useful format:
    from [[{'name': key, 'value': value}, ...], ...] list of list of dict
    to   [{(key, value), ...}, ...] list of set of tuple.
    Moreover requests can be filter by resource type.

    Args:
        har (dict): the dict obtain by parsing har file with json
        resource_type (list): list of resource type to include in the python
            generated code. Supported type are `xhr`, `script`, `stylesheet`,
            `image`, `font`, `document`, `other`.
            Default to ['xhr', 'document', 'other'].
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

    pages = har["log"]["pages"]
    logging.debug(f"found {len(pages)} pages")

    entries = har["log"]["entries"]
    logging.debug(f"found {len(entries)} entries")

    # filtering entries
    entries = [
        e
        for e in har["log"]["entries"]
        if e["_resourceType"] in resource_type and not any(re.search(r, e["request"]["url"]) for r in url_filters)
    ]

    for p in entriesprocessor.processors:
        entries = p(entries)

    logging.debug(f"{resource_type=}")
    logging.debug(f"{len(entries)} entries after filtering by resource_type")

    # organize request variable in a useful format
    # [[{'name': key, 'value': value}, ...], ...] list of list of dict ->
    # [{(key, value), ...}, ...] list of set of tuple
    urls, methods, headers_req, cookies_req, post_datas = [], [], [], [], []
    headers_res, cookies_res = [], []
    for e in entries:
        req = e["request"]
        urls.append(req["url"])
        methods.append(req["method"].lower())
        headers_req.append(
            {
                (h["name"], h["value"])
                for h in req["headers"]
                if not any(re.search(r, h["name"]) for r in header_filters)
            }
        )
        cookies_req.append({(c["name"], c["value"]) for c in req["cookies"]})
        post_datas.append(req["postData"]["text"] if "postData" in req else None)
        res = e["response"]
        headers_res.append({(h["name"], h["value"]) for h in res["headers"]})
        cookies_res.append({(c["name"], c["value"]) for c in res["cookies"]})

    # inside session dict are collect all varibles common to all requests
    session = {
        "name": "s",  # name of the Session() object
        "headers": set.intersection(*headers_req),
        "cookies": set.intersection(*cookies_req),
    }
    urlparts = urlsplit(urls[0])
    host = f"{urlparts.scheme}://{urlparts.netloc}/"
    # requests is a list of dictionary with value specific to single requests
    requests = [
        {
            "url": urls[i].removeprefix(host),
            "method": methods[i],
            "headers": headers_req[i] - session["headers"],
            "cookies": cookies_req[i] - session["cookies"],
            # "params": params[i],
            "post_data": post_datas[i],
            "rest": e["rest"] if "rest" in e else False,
        }
        for i, e in enumerate(entries)
    ]

    responses = [
        {
            "status": e["response"]["status"],
            "headers": headers_res[i],
            "cookies": cookies_res[i],
            "redirect_url": e["response"]["redirectURL"],
            "content": e["response"]["content"],
        }
        for i, e in enumerate(entries)
    ]

    logging.debug("preprocessed har dict")

    return host, session, requests, responses


def rendering(host, session, requests, responses, template_name: str = "locust.jinja2") -> str:
    logging.debug(f'about to load template "{template_name}"')
    if pathlib.Path(template_name).exists():
        template_path = pathlib.Path(template_name)
    else:
        template_path = pathlib.Path(__file__).parents[0].joinpath(pathlib.Path(template_name))
        if not template_path.exists():
            raise Exception(f"Template {template_name} does not exist, neither in current directory nor as built in")

    template_dir = template_path.parents[0]
    logging.debug(f"{template_dir=}")

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
    template = env.get_template(template_path.name)

    py = template.render(host=host, session=session, requests=requests, responses=responses)
    p = subprocess.Popen(["black", "-q", "-"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    assert p.stdin  # keep linter happy
    p.stdin.write(py)
    stdout, _stderr = p.communicate()
    assert (
        not p.returncode
    ), f"Black failed to format the output - perhaps your template is broken? unformatted output was: {py}"

    # for some reason the subprocess returns an extra newline, get rid of that
    return stdout[:-1]
