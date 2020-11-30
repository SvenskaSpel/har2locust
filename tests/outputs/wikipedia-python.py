import requests


s = requests.Session()
s.headers = {
    ':authority': 'en.wikipedia.org',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':method': 'GET',
    'pragma': 'no-cache',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
}
s.cookies.set('GeoIP', 'IT:21:Turin:45.07:7.69:v4')
s.cookies.set('WMF-Last-Access-Global', '28-Nov-2020')
s.cookies.set('WMF-Last-Access', '28-Nov-2020')
s.cookies.set('enwikimwuser-sessionId', 'd3ddadcb2e4f2882aa39')

###############################################################################
# request number: 1
# resource type: document

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-mode': 'navigate',
    'referer': 'https://www.wikipedia.org/',
    ':path': '/wiki/Python_(programming_language)',
    'sec-fetch-site': 'same-site',
    'sec-fetch-dest': 'document',
    'upgrade-insecure-requests': '1',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-content-type-options: nosniff
#   - content-language: en
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - age: 15266
#   - content-length: 81112
#   - server: mw1269.eqiad.wmnet
#   - accept-ranges: bytes
#   - last-modified: Sat, 28 Nov 2020 07:24:02 GMT
#   - cache-control: private, s-maxage=0, max-age=0, must-revalidate
#   - x-cache: cp3064 miss, cp3056 hit/76
#   - vary: Accept-Encoding,Cookie,Authorization
#   - x-request-id: f0bbc176-60b9-47f7-a3f2-5c46077d5168
#   - p3p: CP="See https://en.wikipedia.org/wiki/Special:CentralAutoLogin/P3P for more info."
#   - content-type: text/html; charset=UTF-8
#   - date: Sat, 28 Nov 2020 07:34:43 GMT
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - server-timing: cache;desc="hit-front"
#   - x-cache-status: hit-front
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 2
# resource type: document

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-mode': 'navigate',
    'referer': 'https://www.wikipedia.org/',
    ':path': '/wiki/Python_(programming_language)',
    'sec-fetch-user': '?1',
    'sec-fetch-site': 'same-site',
    'sec-fetch-dest': 'document',
    'upgrade-insecure-requests': '1',
}
rc = s.get(url, headers=headers)


# response status code: 0
###############################################################################

###############################################################################
# request number: 3
# resource type: other

url = 'https://en.wikipedia.org/static/favicon/wikipedia.ico'
headers = {
    ':path': '/static/favicon/wikipedia.ico',
    'sec-fetch-site': 'same-origin',
    'referer': 'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - etag: W/"aae-52e0629e358c0"
#   - date: Thu, 26 Nov 2020 16:45:37 GMT
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - last-modified: Mon, 14 Mar 2016 18:08:11 GMT
#   - server: mw1332.eqiad.wmnet
#   - accept-ranges: bytes
#   - content-length: 1035
#   - vary: Accept-Encoding
#   - access-control-allow-origin: *
#   - age: 155013
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-client-ip: 79.24.172.207
#   - x-cache: cp3060 hit, cp3056 hit/4954259
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - expires: Fri, 26 Nov 2021 16:45:37 GMT
#   - server-timing: cache;desc="hit-front"
#   - x-cache-status: hit-front
#   - cache-control: max-age=31536000
#   - content-type: image/vnd.microsoft.icon
#   - content-encoding: gzip
###############################################################################

