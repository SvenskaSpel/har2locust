[![PyPI](https://img.shields.io/pypi/v/har2locust.svg)](https://pypi.org/project/har2locust/)
[![PyPI](https://img.shields.io/pypi/pyversions/har2locust.svg)](https://pypi.org/project/har2locust/)
[![Build Status](https://github.com/SvenskaSpel/har2locust/workflows/Tests/badge.svg)](https://github.com/SvenskaSpel/har2locustlocust/actions?query=workflow%3ATests)

# har2locust

Creating a [locust file](https://docs.locust.io/en/stable/writing-a-locustfile.html) from scratch is sometimes hard. Don't you wish you could just generate it automatically from a browser session?

Well, now you can!

When browsing the web with the Developer Tools open you can record the Network
Activities (requests perform by your browser & responses you get from servers).
Then you can export all these data into an [HAR](https://en.wikipedia.org/wiki/HAR_(file_format))
file (Http ARchive).

[Here's an example of har2locust's output](https://github.com/SvenskaSpel/har2locust/tree/master/tests/outputs/reqres.in.py)

har2locust builds upon [har2py](https://github.com/S1M0N38/har2py), modified to generate a locustfile 
instead of a basic Python file and extended to support plugins.

Note: It is currently in early beta. It mostly works, but there may be changes to behaviour 
and interface without notice. If you encounter an issue, PRs are very welcome.

Also, dont expect that the generated file will always work out of the box. You'll need to add [response validations](https://docs.locust.io/en/stable/writing-a-locustfile.html#validating-responses) to ensure the quality of your test, and perhaps parametrize dynamic data like usernames. 

## Installation

`pip install har2locust`

This will also install locust and [locust-plugins](https://github.com/SvenskaSpel/locust-plugins/), because they are needed to run the generated locustfiles.

## Usage

1. Navigate the web with your browser while recording your activity. Then save the
data in HAR file. Here is an example with Chrome Devs Tools
![har.gif](https://github.com/SvenskaSpel/har2locust/blob/main/har.gif?raw=true)

2. Run `har2locust myharfile.har > locustfile.py`

```
> har2locust --help
usage: har2locust [-h] [-t TEMPLATE] [--plugins PLUGINS] [--resource-types RESOURCE_TYPES]
                  [--version] [--loglevel LOGLEVEL]
                  input

positional arguments:
  input                 har input file

options:
  -h, --help            show this help message and exit
  -t TEMPLATE, --template TEMPLATE
                        jinja2 template used to generate locustfile. Defaults to locust.jinja2. Will
                        check current directory/relative paths first and har2locust built-ins second
  --plugins PLUGINS     Comma separated list of extra python files to source, containing decorated
                        methods for processing the har file.
  --resource-types RESOURCE_TYPES
                        Commas separated list of resource types to be included in the locustfile.
                        Supported type are `xhr`, `script`, `stylesheet`, `image`, `font`,
                        `document`, `other`. Defaults to xhr,document,other.
  --version, -V         show program's version number and exit
  --loglevel LOGLEVEL, -L LOGLEVEL

Example usage: har2locust myrecording.har myplugin1.py > locustfile

Parameters can also be set using environment variables or config files (har2locust.conf
or ~/.har2locust.conf) For details, see https://goo.gl/R74nmi
```

3. You can define "plugins" to process your input and add custom output. The built in plugins (e.g. [rest.py](https://github.com/SvenskaSpel/har2locust/tree/master/har2locust/plugins/rest.py)) are used by default, and also serve as examples for how to make your own.

4. Those built in plugins also read two files: .urlignore and .headerignore (from your current directory).
Populate them with regexes to filter any unwanted requests or headers from your recordings. 
Some headers are always ignored (cookie, content-length and chrome's "fake" headers)
Here are some examples: [.urlignore](https://github.com/SvenskaSpel/har2locust/tree/master/.urlignore), 
[.headerignore](https://github.com/SvenskaSpel/har2locust/tree/master/.headerignore)