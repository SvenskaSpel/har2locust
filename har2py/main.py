import ast
import json
import logging
import pathlib

import jinja2

# logging.basicConfig(level='DEBUG')


def main(har_file: str, py_file: str, overwrite: bool = False):
    """Load .har file and produce .py

    Args:
        har_file (str): path to the input har file.
        har_py (str): path to the output py file.
        overwrite (bool): overwrite existing .py file. Default to False.
    """

    har_file = pathlib.Path(har_file)
    py_file = pathlib.Path(py_file)

    if not har_file.is_file():
        raise FileNotFoundError

    if har_file.suffix != '.har':
        raise IOError(
            'input file has not ".har" extension. Please use an ".har" file'
        )

    if py_file.suffix != '.py':
        raise IOError(
            'output file has not ".py" extension. Please use an ".py" file'
        )

    if not overwrite and py_file.is_file():
        raise FileExistsError(f'{py_file} already exists.')

    with open(har_file) as f:
        har = json.load(f)
    logging.debug(f'load {har_file}')

    har = preprocessing(har)
    py = rendering(har)

    with open(py_file, 'w') as f:
        f.write(py)
    logging.debug(f'saving {py_file}')


def preprocessing(
    har: dict,
    resource_type=['xhr', 'document', 'other'],
) -> dict:
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
            Default is ['xhr', 'document', 'other'].

    Returns:
        dict: new har dict structured in the following way:
        ```python
        {
            'session': {
                'cookies': [{key, value}, {key, value}, ...],
                'headers': [{key, value}, {key, value}, ...],
            },

            'requests: [
                {
                    # request url without params
                    'url': urls[0],
                    # request method (lowercase): get, post, put, option, ...
                    'method': methods[0],
                    # headers for the specific requests
                    'headers': headers[0] - session['headers'],
                    # cookies for the specific requests
                    'cookies': cookies[0] - session['cookies'],
                    # requests parameters
                    'params': params[0],
                },
                ...
            ],

            response: [
                {
                    #
                    'url': urls[0],
                    # request method (lowercase): get, post, put, option, ...
                    'method': methods[0],
                    # headers for the specific requests
                    'headers': headers[0] - session['headers'],
                    # cookies for the specific requests
                    'cookies': cookies[0] - session['cookies'],
                    # requests parameters
                    'params': params[0],
                },
                ...
            ],

            resources_types: ['document', 'xhr', 'xhr', 'script', ...],
        }

        ```
    """
    supported_resource_type = {
        'xhr',
        'script',
        'stylesheet',
        'image',
        'font',
        'document',
        'other',
    }
    if unsupported := set(resource_type) - supported_resource_type:
        raise NotImplementedError(
            f'{unsupported} resource types are not supported'
        )

    log_version = har['log']['version']
    logging.debug(f'log version is "{log_version}"')
    if log_version != '1.2':
        logging.warning(
            'this script it is only tested on '
            'log version "1.2" and not on "{log_version}"'
        )

    pages = har['log']['pages']
    logging.debug(f'found {len(pages)} pages')

    entries = har['log']['entries']
    logging.debug(f'found {len(entries)} entries')

    # filtering entries by resource type
    entries = [
        e for e in har['log']['entries'] if e['_resourceType'] in resource_type
    ]
    logging.debug(f'resource type allowed {resource_type}')
    logging.debug(f'{len(entries)} entries filter by resource_type')

    # organize request variable in a useful format
    # [[{'name': key, 'value': value}, ...], ...] list of list of dict ->
    # [{(key, value), ...}, ...] list of set of tuple
    urls, methods, headers_req, cookies_req, params = [], [], [], [], []
    headers_res, cookies_res = [], []
    for e in entries:
        req = e['request']
        urls.append(req['url'].split('?')[0])
        methods.append(req['method'].lower())
        headers_req.append({(h['name'], h['value']) for h in req['headers']})
        cookies_req.append({(c['name'], c['value']) for c in req['cookies']})
        params.append({(p['name'], p['value']) for p in req['queryString']})
        res = e['response']
        headers_res.append({(h['name'], h['value']) for h in res['headers']})
        cookies_res.append({(c['name'], c['value']) for c in res['cookies']})

    # inside session dict are collect all varibles common to all requests
    session = {
        'name': 's',  # name of the Session() object
        'headers': set.intersection(*headers_req),
        'cookies': set.intersection(*cookies_req),
    }

    # requests is a list of dictionary with value specific to single requests
    requests = [
        {
            'url': urls[i],
            'method': methods[i],
            'headers': headers_req[i] - session['headers'],
            'cookies': cookies_req[i] - session['cookies'],
            'params': params[i],
        }
        for i, e in enumerate(entries)
    ]

    responses = [
        {
            'status': e['response']['status'],
            'headers': headers_res[i],
            'cookies': cookies_res[i],
            'redirect_url': e['response']['redirectURL'],
            'content': e['response']['content'],
        }
        for i, e in enumerate(entries)
    ]

    resources_types = [e['_resourceType'] for e in entries]

    logging.debug('preprocessed har dict')

    return {
        'session': session,
        'requests': requests,
        'responses': responses,
        'resources_types': resources_types,
    }


def rendering(
    har: dict,
    template_dir: str = pathlib.Path(__file__).parents[0],
    template_name: str = 'template.jinja2',
):
    """Generate valid python code from preprocessed har using jinja2 template.

    Args:
        har (dict): preprocessed har dict
        template_dir (str): path where are store the jinja2 template.
            Defalut to `pathlib.Path(__file__).parents[0]`.
        template_name (str): name of the jinja2 template used by rendering.
            Default to 'template.jinja2'.

    Returns:
        str: generated python code
    """
    # check for the correctness of the har structure
    if set(har) != {'session', 'requests', 'responses', 'resources_types'}:
        raise ValueError(
            'har dict has wrong format. '
            'Must be first preprocessed with preprocessing(har).'
        )

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    logging.debug(f'render har with "{template.name}" template')

    py = template.render(
        session=har['session'],
        requests=har['requests'],
        responses=har['responses'],
        resources_types=har['resources_types'],
    )

    # test if the generated code is python valid code
    try:
        ast.parse(py)
    except SyntaxError:
        raise SyntaxError(
            'cannot parse har into valid python code. '
            'Please check the correctness of the jinja2 template'
        )

    logging.debug('successfully generate valid python code')

    return py
