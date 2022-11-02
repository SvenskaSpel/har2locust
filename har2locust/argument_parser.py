import configargparse
from ._version import version

DEFAULT_CONFIG_FILES = ["~/.har2locust.conf", "har2locust.conf"]


def get_parser() -> configargparse.ArgumentParser:
    parser = configargparse.ArgumentParser(
        epilog="Example usage: har2locust myrecording.har --plugins myplugin1.py > locustfile.py",
        auto_env_var_prefix="HAR2LOCUST_",
        default_config_files=DEFAULT_CONFIG_FILES,
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
    return parser
