import json
import logging
import pathlib

import jinja2

logging.basicConfig(level='DEBUG')


def main(har_file: str, overwrite: bool = False):
    """Load .har file and produce .py

    Args:
        har_file : absoulte path of the har file
        overwrite (bool): overwrite existing .py file. Default to False.
    """

    har_file = pathlib.Path(har_file)
    py_file = har_file.with_suffix('.py')

    if not har_file.is_file():
        raise FileNotFoundError

    if har_file.suffix != '.har':
        raise IOError(
            'selected file has not ".har" extension. Please use an ".har" file'
        )

    if not overwrite and py_file.is_file():
        raise FileExistsError(f'{py_file} already exists.')

    with open(har_file) as f:
        har = json.load(f)
    logging.debug(f'load {har_file}')

    py = har2py(har)
    logging.debug('successfully generate .py file')

    with open(py_file, 'w') as f:
        f.write(py)
    logging.debug(f'saving {py_file}')


def har2py(har: dict):
    """Parse .har file and produce .py

    Args:
        har_file : absoulte path of the har file
        overwrite (bool):
    """
    log_version = har['log']['version']
    logging.debug(f'log version is "{log_version}"')
    assert log_version == '1.2'  # test only on this version

    pages = har['log']['pages']
    logging.debug(f'found {len(pages)} pages')

    entries = har['log']['entries']
    logging.debug(f'found {len(entries)} entries')

    # organize request variable in a useful format
    # [[{'name': key, 'value': value}, ...], ...] list of list of dict ->
    # [{(key, value), ...}, ...] list of set of tuple
    urls, methods, headers, cookies, params = [], [], [], [], []
    for e in entries:
        r = e['request']
        urls.append(r['url'])
        methods.append(r['method'].lower())
        headers.append({(h['name'], h['value']) for h in r['headers']})
        cookies.append({(c['name'], c['value']) for c in r['cookies']})
        params.append({(p['name'], p['value']) for p in r['queryString']})

    # inside session dict are collect all varibles common to all requests
    session = {
        'name': 's',  # name of the Session() object
        'headers': set.intersection(*headers),
        'cookies': set.intersection(*cookies),
    }

    # requests is a list of dictionary with value specific to single requests
    requests = [
        {
            'url': urls[i],
            'method': methods[i],
            'headers': headers[i] - session['headers'],
            'cookies': cookies[i] - session['cookies'],
            'params': params[i],
        }
        for i, e in enumerate(entries)
    ]

    responses = [
        {
            'status': e['response']['status'],
            'headers': {
                (h['name'], h['value']) for h in e['response']['headers']
            },
            'cookies': {
                (c['name'], c['value']) for c in e['response']['cookies']
            },
            'redirect_url': e['response']['redirectURL'],
            'content': e['response']['content'],
        }
        for i, e in enumerate(entries)
    ]

    template_dir = pathlib.Path(__file__).parents[0]
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
    template = env.get_template('template.jinja2')
    logging.debug(f'render har with "{template.name}" template')

    return template.render(
        session=session, requests=requests, responses=responses
    )
