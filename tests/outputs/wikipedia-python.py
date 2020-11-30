import requests


s = requests.Session()
s.headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    ':authority': 'en.wikipedia.org',
    'accept-language': 'en-US,en;q=0.9',
}
s.cookies.set('GeoIP', 'IT:21:Turin:45.07:7.69:v4')
s.cookies.set('enwikimwuser-sessionId', 'd3ddadcb2e4f2882aa39')
s.cookies.set('WMF-Last-Access-Global', '28-Nov-2020')
s.cookies.set('WMF-Last-Access', '28-Nov-2020')

###############################################################################
# request number: 1
# resource type: document

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
headers = {
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    ':path': '/wiki/Python_(programming_language)',
    'sec-fetch-site': 'same-site',
    'upgrade-insecure-requests': '1',
    'referer': 'https://www.wikipedia.org/',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-client-ip: 79.24.172.207
#   - p3p: CP="See https://en.wikipedia.org/wiki/Special:CentralAutoLogin/P3P for more info."
#   - server-timing: cache;desc="hit-front"
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - server: mw1269.eqiad.wmnet
#   - x-content-type-options: nosniff
#   - last-modified: Sat, 28 Nov 2020 07:24:02 GMT
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - content-language: en
#   - age: 15266
#   - date: Sat, 28 Nov 2020 07:34:43 GMT
#   - content-encoding: gzip
#   - x-cache-status: hit-front
#   - cache-control: private, s-maxage=0, max-age=0, must-revalidate
#   - x-request-id: f0bbc176-60b9-47f7-a3f2-5c46077d5168
#   - content-type: text/html; charset=UTF-8
#   - accept-ranges: bytes
#   - x-cache: cp3064 miss, cp3056 hit/76
#   - vary: Accept-Encoding,Cookie,Authorization
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - content-length: 81112
###############################################################################

###############################################################################
# request number: 2
# resource type: document

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
headers = {
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    ':path': '/wiki/Python_(programming_language)',
    'sec-fetch-site': 'same-site',
    'upgrade-insecure-requests': '1',
    'referer': 'https://www.wikipedia.org/',
    'sec-fetch-user': '?1',
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
    'sec-fetch-mode': 'no-cors',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'referer': 'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-dest': 'image',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-client-ip: 79.24.172.207
#   - cache-control: max-age=31536000
#   - date: Thu, 26 Nov 2020 16:45:37 GMT
#   - server-timing: cache;desc="hit-front"
#   - content-length: 1035
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - last-modified: Mon, 14 Mar 2016 18:08:11 GMT
#   - expires: Fri, 26 Nov 2021 16:45:37 GMT
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - x-cache-status: hit-front
#   - content-type: image/vnd.microsoft.icon
#   - age: 155013
#   - x-cache: cp3060 hit, cp3056 hit/4954259
#   - server: mw1332.eqiad.wmnet
#   - etag: W/"aae-52e0629e358c0"
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - access-control-allow-origin: *
###############################################################################

