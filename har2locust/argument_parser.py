import configargparse
from argparse import RawDescriptionHelpFormatter
from ._version import version


DEFAULT_CONFIG_FILES = ["~/.har2locust.conf", "har2locust.conf"]


def get_parser() -> configargparse.ArgumentParser:
    parser = configargparse.ArgumentParser(
        epilog="""Simplest usage:
har2locust myrecording.har > locustfile.py

Load one extra plugins by import path and another one by filename: 
har2locust --plugins har2locust.extra_plugins.plugin_example,myplugin.py myrecording.har

Disable one of the default plugins:
har2locust --disable-plugins=rest.py myrecording.har

Parameters can also be set using environment variables or config files (har2locust.conf or ~/.har2locust.conf) For details about how to set parameters see https://goo.gl/R74nmi""",
        auto_env_var_prefix="HAR2LOCUST_",
        add_env_var_help=False,
        add_config_file_help=False,
        formatter_class=RawDescriptionHelpFormatter,
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
            "jinja2 template used to generate locustfile. Defaults to locust.jinja2. Will check current directory/relative paths first and har2locust built-ins second"
        ),
    )
    parser.add_argument(
        "--plugins",
        type=str,
        default="",
        help="Comma separated list of extra python files to source OR packages to import, containing decorated methods for processing the har file.",
    )
    parser.add_argument(
        "--disable-plugins",
        type=str,
        default="",
        help="Temporarily disable default plugins. Specified by comma separated list of default plugin python files to source.",
    )
    parser.add_argument(
        "--resource-types",
        default="xhr,document,other",
        type=str,
        help=(
            "Commas separated list of resource types to be included "
            "in the locustfile. Supported type are `xhr`, "
            "`script`, `stylesheet`, `image`, `font`, `document`, `other`. "
            "Defaults to xhr,document,other."
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
