[![PyPI](https://img.shields.io/pypi/v/har2locust.svg)](https://pypi.org/project/har2locust/)
[![PyPI](https://img.shields.io/pypi/pyversions/har2locust.svg)](https://pypi.org/project/har2locust/)
[![Build Status](https://github.com/SvenskaSpel/har2locust/workflows/Tests/badge.svg)](https://github.com/SvenskaSpel/har2locust/actions?query=workflow%3ATests)

# har2locust

Creating a [locust file](https://docs.locust.io/en/stable/writing-a-locustfile.html) from scratch is sometimes hard. Don't you wish you could just generate it automatically from a browser session?

Well, now you can! har2locust converts your browser recordings ([HAR](https://en.wikipedia.org/wiki/HAR_(file_format)) files) into locust files.

[Here's an example of a generated file](https://github.com/SvenskaSpel/har2locust/tree/main/tests/outputs/reqres.in.py).

At its core har2locust uses a [jinja2 template](https://github.com/SvenskaSpel/har2locust/tree/main/har2locust/locust.jinja2) to define the output. You can easily change that to customize your output, or you can go even further and use the [plugin system](https://github.com/SvenskaSpel/har2locust/tree/main/har2locust/plugin.py) to make any kind of changes to the processing/output.

## Installation

`pip install har2locust`

## Usage

1. Navigate the web with your browser while recording your activity. Then export the recording into a HAR file. Here is an example using Chrome Devs Tools
![har.gif](https://github.com/SvenskaSpel/har2locust/blob/main/har.gif?raw=true)

2. Run `har2locust myrecording.har > locustfile.py`

```
> har2locust --help
usage: har2locust [-h] [-t TEMPLATE] [--plugins PLUGINS] [--disable-plugins DISABLE_PLUGINS]
                  [--resource-types RESOURCE_TYPES] [--version] [--loglevel LOGLEVEL]
                  input

positional arguments:
  input                 har input file

options:
  -h, --help            show this help message and exit
  -t TEMPLATE, --template TEMPLATE
                        jinja2 template used to generate locustfile. Defaults to locust.jinja2. Will check current
                        directory/relative paths first and har2locust built-ins second
  --plugins PLUGINS     Comma separated list of extra python files to source OR packages to import, containing
                        decorated methods for processing the har file.
  --disable-plugins DISABLE_PLUGINS
                        Temporarily disable default plugins. Specified by comma separated list of default plugin
                        python files to source.
  --resource-types RESOURCE_TYPES
                        Commas separated list of resource types to be included in the locustfile. Supported type are
                        `xhr`, `script`, `stylesheet`, `image`, `font`, `document`, `other`. Defaults to
                        xhr,document,other.
  --version, -V         show program's version number and exit
  --loglevel LOGLEVEL, -L LOGLEVEL

Simplest usage:
har2locust myrecording.har > locustfile.py

Load extra plugins by import path and/or filename:
har2locust --plugins har2locust.extra_plugins.plugin_example,myplugin.py myrecording.har

Disable one of the default plugins:
har2locust --disable-plugins=rest.py myrecording.har

Parameters can also be set using environment variables or config files (har2locust.conf or ~/.har2locust.conf) For details about how to set parameters see https://goo.gl/R74nmi
```

3. Run locust!

## Advanced usage

* Filter your recording using the files `.urlignore` and `.headerignore` (read from your current directory).
Populate them with regexes to filter any unwanted requests or headers from your recordings. 
Some headers are always ignored (cookie, content-length and chrome's "fake" headers)
Here are some examples: [.urlignore](https://github.com/SvenskaSpel/har2locust/tree/main/.urlignore), 
[.headerignore](https://github.com/SvenskaSpel/har2locust/tree/main/.headerignore)

* Use the [plugin system](https://github.com/SvenskaSpel/har2locust/tree/main/har2locust/plugin.py) 
for more advanced processing.

## Notes

har2locust builds upon [har2py](https://github.com/S1M0N38/har2py), modified to generate a locustfile 
instead of a basic Python file and extended to support plugins.

har2locust is very new, and before 1.0 there may be changes to interfaces without notice. If you encounter an issue, PRs are very welcome.

Also, dont expect that the generated file will always be very useful out of the box. You'll want to add [response validations](https://docs.locust.io/en/stable/writing-a-locustfile.html#validating-responses) to ensure the quality of your test, and perhaps parametrize dynamic data like usernames.
