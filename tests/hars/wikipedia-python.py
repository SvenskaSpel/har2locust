import requests


s = requests.Session()
s.headers = {
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
}

###############################################################################
# request number: 1
# resource type: 

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-site',
    'referer': 'https://www.wikipedia.org/',
    ':authority': 'en.wikipedia.org',
    ':path': '/wiki/Python_(programming_language)',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - server: mw1269.eqiad.wmnet
#   - accept-ranges: bytes
#   - date: Sat, 28 Nov 2020 07:34:43 GMT
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - x-cache: cp3064 miss, cp3056 hit/76
#   - x-request-id: f0bbc176-60b9-47f7-a3f2-5c46077d5168
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: hit-front
#   - content-encoding: gzip
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - age: 15266
#   - p3p: CP="See https://en.wikipedia.org/wiki/Special:CentralAutoLogin/P3P for more info."
#   - x-content-type-options: nosniff
#   - content-length: 81112
#   - content-type: text/html; charset=UTF-8
#   - vary: Accept-Encoding,Cookie,Authorization
#   - cache-control: private, s-maxage=0, max-age=0, must-revalidate
#   - last-modified: Sat, 28 Nov 2020 07:24:02 GMT
#   - content-language: en
#   - server-timing: cache;desc="hit-front"
###############################################################################

###############################################################################
# request number: 2
# resource type: 

url = 'https://en.wikipedia.org/w/api.php'
headers = {
    'accept': '*/*',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'sec-fetch-dest': 'script',
    ':path': '/w/api.php?action=query&format=json&generator=prefixsearch&prop=pageprops%7Cpageimages%7Cdescription&redirects=&ppprop=displaytitle&piprop=thumbnail&pithumbsize=80&pilimit=6&gpssearch=py&gpsnamespace=0&gpslimit=6&callback=callbackStack.queue%5B0%5D',
    'sec-fetch-site': 'same-site',
    'referer': 'https://www.wikipedia.org/',
    ':authority': 'en.wikipedia.org',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
params = [
    ('redirects', ''),
    ('gpslimit', '6'),
    ('ppprop', 'displaytitle'),
    ('prop', 'pageprops%7Cpageimages%7Cdescription'),
    ('pithumbsize', '80'),
    ('callback', 'callbackStack.queue%5B0%5D'),
    ('gpsnamespace', '0'),
    ('format', 'json'),
    ('action', 'query'),
    ('piprop', 'thumbnail'),
    ('gpssearch', 'py'),
    ('pilimit', '6'),
    ('generator', 'prefixsearch'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 11:49:07 GMT
#   - cache-control: private, must-revalidate, max-age=0
#   - accept-ranges: bytes
#   - x-request-id: 3c3fd938-092b-4738-ac54-47110594764b
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - mediawiki-login-suppressed: true
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: pass
#   - x-cache: cp3064 miss, cp3056 pass
#   - age: 0
#   - content-encoding: gzip
#   - x-frame-options: SAMEORIGIN
#   - server-timing: cache;desc="pass"
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - p3p: CP="See https://en.wikipedia.org/wiki/Special:CentralAutoLogin/P3P for more info."
#   - x-search-id: 1bscoiirqfjx3611l5tfw3zsk
#   - x-content-type-options: nosniff
#   - server: mw1398.eqiad.wmnet
#   - content-type: text/javascript; charset=utf-8
#   - content-disposition: inline; filename=api-result.js
#   - vary: Accept-Encoding,Treat-as-Untrusted,X-Forwarded-Proto,Cookie,Authorization
###############################################################################

###############################################################################
# request number: 3
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Pythagorean.svg/80px-Pythagorean.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':path': '/wikipedia/commons/thumb/d/d2/Pythagorean.svg/80px-Pythagorean.svg.png',
    'referer': 'https://www.wikipedia.org/',
    ':authority': 'upload.wikimedia.org',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-timestamp: 1587214815.27967
#   - content-type: image/png
#   - accept-ranges: bytes
#   - etag: a1fc3a59666298d0992be23122748d7f
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - age: 54269
#   - x-cache-status: hit-front
#   - x-cache: cp3063 hit, cp3059 hit/27
#   - date: Fri, 27 Nov 2020 20:44:38 GMT
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - content-length: 1921
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - last-modified: Sat, 18 Apr 2020 13:00:16 GMT
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 4
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Tchaikovsky_by_Reutlinger.jpg/55px-Tchaikovsky_by_Reutlinger.jpg'
headers = {
    'sec-fetch-dest': 'image',
    'referer': 'https://www.wikipedia.org/',
    ':authority': 'upload.wikimedia.org',
    'sec-fetch-site': 'cross-site',
    ':path': '/wikipedia/commons/thumb/4/4d/Tchaikovsky_by_Reutlinger.jpg/55px-Tchaikovsky_by_Reutlinger.jpg',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - last-modified: Sat, 08 Feb 2014 10:19:07 GMT
#   - content-disposition: inline;filename*=UTF-8''Tchaikovsky_by_Reutlinger.jpg
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - age: 50527
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-timestamp: 1391854746.58557
#   - x-cache-status: hit-front
#   - content-length: 1641
#   - content-type: image/jpeg
#   - etag: fa548387884d0cd68b6fbaa7736be4d4
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-cache: cp3063 hit, cp3059 hit/2
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - date: Fri, 27 Nov 2020 21:47:00 GMT
#   - x-object-meta-sha1base36: 1ifsdnd5f51uqqeo7qq2uygh6x1hkdz
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 5
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Kapitolinischer_Pythagoras_adjusted.jpg/60px-Kapitolinischer_Pythagoras_adjusted.jpg'
headers = {
    'sec-fetch-dest': 'image',
    'referer': 'https://www.wikipedia.org/',
    ':path': '/wikipedia/commons/thumb/1/1a/Kapitolinischer_Pythagoras_adjusted.jpg/60px-Kapitolinischer_Pythagoras_adjusted.jpg',
    ':authority': 'upload.wikimedia.org',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - etag: 2f2bca84a937e6146c50da63d1085e48
#   - accept-ranges: bytes
#   - last-modified: Wed, 16 Aug 2017 23:54:00 GMT
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - date: Fri, 27 Nov 2020 21:24:15 GMT
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-timestamp: 1502927639.31295
#   - x-cache: cp3055 hit, cp3059 hit/2
#   - x-cache-status: hit-front
#   - content-type: image/jpeg
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - content-length: 2526
#   - age: 51892
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 6
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Central_pyrenees.jpg/80px-Central_pyrenees.jpg'
headers = {
    'sec-fetch-dest': 'image',
    ':path': '/wikipedia/commons/thumb/0/01/Central_pyrenees.jpg/80px-Central_pyrenees.jpg',
    'referer': 'https://www.wikipedia.org/',
    ':authority': 'upload.wikimedia.org',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - accept-ranges: bytes
#   - content-length: 3582
#   - etag: b3608cc7b4dfaf989f2fe95ba45f018d
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-timestamp: 1502565381.20840
#   - last-modified: Sat, 12 Aug 2017 19:16:22 GMT
#   - x-cache-status: hit-front
#   - content-type: image/jpeg
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - x-cache: cp3059 hit, cp3059 hit/2
#   - date: Fri, 27 Nov 2020 18:41:54 GMT
#   - age: 61633
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 7
# resource type: 

url = 'https://en.wikipedia.org/w/api.php'
headers = {
    'accept': '*/*',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'sec-fetch-dest': 'script',
    'sec-fetch-site': 'same-site',
    'referer': 'https://www.wikipedia.org/',
    ':path': '/w/api.php?action=query&format=json&generator=prefixsearch&prop=pageprops%7Cpageimages%7Cdescription&redirects=&ppprop=displaytitle&piprop=thumbnail&pithumbsize=80&pilimit=6&gpssearch=pytho&gpsnamespace=0&gpslimit=6&callback=callbackStack.queue%5B1%5D',
    ':authority': 'en.wikipedia.org',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
params = [
    ('redirects', ''),
    ('gpslimit', '6'),
    ('ppprop', 'displaytitle'),
    ('prop', 'pageprops%7Cpageimages%7Cdescription'),
    ('gpssearch', 'pytho'),
    ('pithumbsize', '80'),
    ('callback', 'callbackStack.queue%5B1%5D'),
    ('gpsnamespace', '0'),
    ('format', 'json'),
    ('action', 'query'),
    ('piprop', 'thumbnail'),
    ('pilimit', '6'),
    ('generator', 'prefixsearch'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 11:49:07 GMT
#   - x-search-id: 7c3ekqbryinoobjh7yk9q6bu3
#   - cache-control: private, must-revalidate, max-age=0
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - mediawiki-login-suppressed: true
#   - x-client-ip: 79.24.172.207
#   - server: mw1313.eqiad.wmnet
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: pass
#   - content-encoding: gzip
#   - x-frame-options: SAMEORIGIN
#   - server-timing: cache;desc="pass"
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - p3p: CP="See https://en.wikipedia.org/wiki/Special:CentralAutoLogin/P3P for more info."
#   - x-content-type-options: nosniff
#   - x-cache: cp3062 miss, cp3056 pass
#   - content-type: text/javascript; charset=utf-8
#   - content-disposition: inline; filename=api-result.js
#   - x-request-id: d9fd5866-bb27-46a4-8d73-65f715354ffb
#   - age: 2
#   - vary: Accept-Encoding,Treat-as-Untrusted,X-Forwarded-Proto,Cookie,Authorization
###############################################################################

###############################################################################
# request number: 8
# resource type: 

url = 'https://en.wikipedia.org/w/api.php'
headers = {
    'accept': '*/*',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'sec-fetch-dest': 'script',
    'sec-fetch-site': 'same-site',
    'referer': 'https://www.wikipedia.org/',
    ':path': '/w/api.php?action=query&format=json&generator=prefixsearch&prop=pageprops%7Cpageimages%7Cdescription&redirects=&ppprop=displaytitle&piprop=thumbnail&pithumbsize=80&pilimit=6&gpssearch=python&gpsnamespace=0&gpslimit=6&callback=callbackStack.queue%5B2%5D',
    ':authority': 'en.wikipedia.org',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
params = [
    ('redirects', ''),
    ('gpslimit', '6'),
    ('ppprop', 'displaytitle'),
    ('prop', 'pageprops%7Cpageimages%7Cdescription'),
    ('pithumbsize', '80'),
    ('gpssearch', 'python'),
    ('format', 'json'),
    ('action', 'query'),
    ('piprop', 'thumbnail'),
    ('gpsnamespace', '0'),
    ('pilimit', '6'),
    ('callback', 'callbackStack.queue%5B2%5D'),
    ('generator', 'prefixsearch'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - cache-control: private, must-revalidate, max-age=0
#   - accept-ranges: bytes
#   - x-cache: cp3058 miss, cp3056 pass
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - mediawiki-login-suppressed: true
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: pass
#   - age: 0
#   - content-encoding: gzip
#   - x-frame-options: SAMEORIGIN
#   - server-timing: cache;desc="pass"
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - p3p: CP="See https://en.wikipedia.org/wiki/Special:CentralAutoLogin/P3P for more info."
#   - x-content-type-options: nosniff
#   - server: mw1380.eqiad.wmnet
#   - content-type: text/javascript; charset=utf-8
#   - content-disposition: inline; filename=api-result.js
#   - x-search-id: 44kjxuw0qrr2z5ued68howe0b
#   - date: Sat, 28 Nov 2020 11:49:08 GMT
#   - x-request-id: d8d25d2e-cb4a-48eb-8976-da38c86012f6
#   - vary: Accept-Encoding,Treat-as-Untrusted,X-Forwarded-Proto,Cookie,Authorization
###############################################################################

###############################################################################
# request number: 9
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Python_molurus_molurus_2.jpg/80px-Python_molurus_molurus_2.jpg'
headers = {
    'sec-fetch-dest': 'image',
    ':path': '/wikipedia/commons/thumb/3/32/Python_molurus_molurus_2.jpg/80px-Python_molurus_molurus_2.jpg',
    'referer': 'https://www.wikipedia.org/',
    ':authority': 'upload.wikimedia.org',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - accept-ranges: bytes
#   - x-cache: cp3053 hit, cp3059 hit/2
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - content-length: 3852
#   - x-client-ip: 79.24.172.207
#   - etag: 8fff6c5fd4967ef5dc32616f28fd8958
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-timestamp: 1382595764.95444
#   - last-modified: Thu, 24 Oct 2013 06:22:45 GMT
#   - x-cache-status: hit-front
#   - date: Sat, 28 Nov 2020 11:21:37 GMT
#   - content-type: image/jpeg
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - age: 1650
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 10
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Python5-missile001.jpg/80px-Python5-missile001.jpg'
headers = {
    'sec-fetch-dest': 'image',
    ':path': '/wikipedia/commons/thumb/b/bd/Python5-missile001.jpg/80px-Python5-missile001.jpg',
    'referer': 'https://www.wikipedia.org/',
    ':authority': 'upload.wikimedia.org',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - date: Fri, 27 Nov 2020 13:03:55 GMT
#   - accept-ranges: bytes
#   - x-cache: cp3061 hit, cp3059 hit/2
#   - last-modified: Fri, 01 Nov 2013 12:41:45 GMT
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-object-meta-sha1base36: 5kdgg0dtcwjyhb73y1nhn21rsamab54
#   - x-timestamp: 1383309704.49188
#   - x-cache-status: hit-front
#   - content-type: image/jpeg
#   - etag: a2e76b75990d1909e2e11c09afef8724
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - access-control-allow-origin: *
#   - age: 81912
#   - server-timing: cache;desc="hit-front"
#   - content-length: 2573
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 11
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Pratik_jain_dahod_python.JPG/80px-Pratik_jain_dahod_python.JPG'
headers = {
    'sec-fetch-dest': 'image',
    'referer': 'https://www.wikipedia.org/',
    ':path': '/wikipedia/commons/thumb/7/74/Pratik_jain_dahod_python.JPG/80px-Pratik_jain_dahod_python.JPG',
    ':authority': 'upload.wikimedia.org',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-cache: cp3051 hit, cp3059 hit/2
#   - x-client-ip: 79.24.172.207
#   - content-length: 2648
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-object-meta-sha1base36: 4utxwid6p95fj9trk26ocze5drbxyuh
#   - x-cache-status: hit-front
#   - content-type: image/jpeg
#   - etag: 56d50ca376158e598ad042c7e9ff96ee
#   - date: Fri, 27 Nov 2020 15:27:53 GMT
#   - last-modified: Fri, 19 Sep 2014 16:25:42 GMT
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - content-disposition: inline;filename*=UTF-8''Pratik_jain_dahod_python.JPG
#   - age: 73278
#   - x-timestamp: 1411143941.35129
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 12
# resource type: 

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'referer': 'https://www.wikipedia.org/',
    ':authority': 'en.wikipedia.org',
    ':path': '/wiki/Python_(programming_language)',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 0
###############################################################################

###############################################################################
# request number: 13
# resource type: 

url = 'https://en.wikipedia.org/w/load.php'
headers = {
    'accept': 'text/css,*/*;q=0.1',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'sec-fetch-dest': 'style',
    'referer': 'https://en.wikipedia.org/wiki/Python_(programming_language)',
    ':path': '/w/load.php?lang=en&modules=ext.cite.styles%7Cext.pygments%2CwikimediaBadges%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cjquery.makeCollapsible.styles%7Cskins.vector.styles.legacy%7Cwikibase.client.init&only=styles&skin=vector',
    'sec-fetch-site': 'same-origin',
    ':authority': 'en.wikipedia.org',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
params = [
    ('modules', 'ext.cite.styles%7Cext.pygments%2CwikimediaBadges%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cjquery.makeCollapsible.styles%7Cskins.vector.styles.legacy%7Cwikibase.client.init'),
    ('skin', 'vector'),
    ('lang', 'en'),
    ('only', 'styles'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - cache-control: public, max-age=300, s-maxage=300
#   - vary: Accept-Encoding
#   - etag: W/"qf538"
#   - content-length: 10001
#   - accept-ranges: bytes
#   - x-cache: cp3052 hit, cp3056 hit/26
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-request-id: 193be697-baef-4bda-8d60-84700d38ad0d
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - date: Sat, 28 Nov 2020 11:45:03 GMT
#   - x-cache-status: hit-front
#   - expires: Sat, 28 Nov 2020 11:45:41 GMT
#   - age: 0
#   - content-encoding: gzip
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-content-type-options: nosniff
#   - server: ATS/8.0.8
#   - link: </static/images/project-logos/enwiki.png>;rel=preload;as=image;media=not all and (min-resolution: 1.5dppx),</static/images/project-logos/enwiki-1.5x.png>;rel=preload;as=image;media=(min-resolution: 1.5dppx) and (max-resolution: 1.999999dppx),</static/images/project-logos/enwiki-2x.png>;rel=preload;as=image;media=(min-resolution: 2dppx)
#   - access-control-allow-origin: *
#   - content-type: text/css; charset=utf-8
#   - server-timing: cache;desc="hit-front"
###############################################################################

###############################################################################
# request number: 14
# resource type: 

url = 'https://en.wikipedia.org/w/load.php'
headers = {
    'accept': '*/*',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    ':path': '/w/load.php?lang=en&modules=startup&only=scripts&raw=1&skin=vector',
    'referer': 'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'sec-fetch-dest': 'script',
    'sec-fetch-site': 'same-origin',
    ':authority': 'en.wikipedia.org',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
params = [
    ('skin', 'vector'),
    ('modules', 'startup'),
    ('raw', '1'),
    ('lang', 'en'),
    ('only', 'scripts'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - cache-control: public, max-age=300, s-maxage=300
#   - vary: Accept-Encoding
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - etag: W/"169zq"
#   - x-request-id: 77b7d87d-66de-4be7-8a6e-eaf7c2f1c60e
#   - x-cache-status: hit-front
#   - age: 0
#   - content-encoding: gzip
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - content-length: 21673
#   - x-content-type-options: nosniff
#   - server: ATS/8.0.8
#   - date: Sat, 28 Nov 2020 11:48:37 GMT
#   - content-type: text/javascript; charset=utf-8
#   - expires: Sat, 28 Nov 2020 11:48:43 GMT
#   - x-cache: cp3056 hit, cp3056 hit/1196
#   - server-timing: cache;desc="hit-front"
###############################################################################

###############################################################################
# request number: 15
# resource type: 

url = 'https://en.wikipedia.org/w/load.php'
headers = {
    'accept': 'text/css,*/*;q=0.1',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'sec-fetch-dest': 'style',
    'referer': 'https://en.wikipedia.org/wiki/Python_(programming_language)',
    ':path': '/w/load.php?lang=en&modules=site.styles&only=styles&skin=vector',
    'sec-fetch-site': 'same-origin',
    ':authority': 'en.wikipedia.org',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
params = [
    ('skin', 'vector'),
    ('lang', 'en'),
    ('only', 'styles'),
    ('modules', 'site.styles'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - cache-control: public, max-age=300, s-maxage=300
#   - vary: Accept-Encoding
#   - x-cache: cp3056 hit, cp3056 hit/6069
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: hit-front
#   - age: 0
#   - content-encoding: gzip
#   - date: Sat, 28 Nov 2020 11:45:43 GMT
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-content-type-options: nosniff
#   - x-request-id: 603d985c-6869-4d75-a8eb-5f95fef55c8a
#   - server: ATS/8.0.8
#   - content-length: 4754
#   - expires: Sat, 28 Nov 2020 11:46:45 GMT
#   - access-control-allow-origin: *
#   - content-type: text/css; charset=utf-8
#   - server-timing: cache;desc="hit-front"
#   - etag: W/"10au9"
###############################################################################

###############################################################################
# request number: 16
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/19px-Symbol_support_vote.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    ':path': '/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/19px-Symbol_support_vote.svg.png',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/webp
#   - accept-ranges: bytes
#   - etag: 1852eed934502511117688c1d938b2be
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: hit-front
#   - x-timestamp: 1561104676.48059
#   - content-length: 606
#   - last-modified: Fri, 21 Jun 2019 08:11:17 GMT
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - date: Sat, 28 Nov 2020 05:17:03 GMT
#   - age: 23526
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
#   - x-cache: cp3061 hit, cp3059 hit/8173
###############################################################################

###############################################################################
# request number: 17
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/250px-Python_logo_and_wordmark.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    ':path': '/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/250px-Python_logo_and_wordmark.svg.png',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/png
#   - accept-ranges: bytes
#   - date: Sat, 28 Nov 2020 07:11:04 GMT
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-object-meta-sha1base36: q7s36huxo88cvago1b1xjl2pzra3t50
#   - x-cache: cp3061 hit, cp3059 hit/21
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - content-length: 6447
#   - x-cache-status: hit-front
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - last-modified: Tue, 23 Sep 2014 10:14:51 GMT
#   - etag: 81a1d9bee85312ba4f8c7d2757098d8a
#   - x-timestamp: 1411467290.58288
#   - access-control-allow-origin: *
#   - content-disposition: inline;filename*=UTF-8''Python_logo_and_wordmark.svg.png
#   - server-timing: cache;desc="hit-front"
#   - age: 16685
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 18
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Wikibooks-logo-en-noslogan.svg/16px-Wikibooks-logo-en-noslogan.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    ':path': '/wikipedia/commons/thumb/d/df/Wikibooks-logo-en-noslogan.svg/16px-Wikibooks-logo-en-noslogan.svg.png',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/webp
#   - accept-ranges: bytes
#   - x-timestamp: 1561104684.44468
#   - content-length: 616
#   - etag: 7818229ff04d2a207dbfa18f2a5da964
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: hit-front
#   - last-modified: Fri, 21 Jun 2019 08:11:25 GMT
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-cache: cp3061 hit, cp3059 hit/1042
#   - date: Sat, 28 Nov 2020 03:38:37 GMT
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - age: 29432
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 19
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Guido_van_Rossum_OSCON_2006_cropped.png/150px-Guido_van_Rossum_OSCON_2006_cropped.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    ':path': '/wikipedia/commons/thumb/9/94/Guido_van_Rossum_OSCON_2006_cropped.png/150px-Guido_van_Rossum_OSCON_2006_cropped.png',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/png
#   - x-cache: cp3061 hit, cp3059 hit/25
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - last-modified: Mon, 26 Sep 2016 10:14:32 GMT
#   - x-client-ip: 79.24.172.207
#   - content-disposition: inline;filename*=UTF-8''Guido_van_Rossum_OSCON_2006_cropped.png
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: hit-front
#   - content-length: 70109
#   - date: Sat, 28 Nov 2020 04:37:10 GMT
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-timestamp: 1474884871.94609
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - x-object-meta-sha1base36: abr2j5xl15dlzaif75d1y9y7bjay7i4
#   - access-control-allow-origin: *
#   - age: 25919
#   - etag: f011b0c152f44ecbaafeb8c1cd228b6d
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 20
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Python_3._The_standard_type_hierarchy.png/220px-Python_3._The_standard_type_hierarchy.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    ':path': '/wikipedia/commons/thumb/1/10/Python_3._The_standard_type_hierarchy.png/220px-Python_3._The_standard_type_hierarchy.png',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 06:32:46 GMT
#   - last-modified: Fri, 02 Nov 2018 11:27:38 GMT
#   - content-type: image/png
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: hit-front
#   - x-cache: cp3065 hit, cp3059 hit/51
#   - age: 18983
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - etag: f8df116c05a16faa527b1ce705484d9a
#   - x-timestamp: 1541158057.98119
#   - access-control-allow-origin: *
#   - content-length: 29406
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 21
# resource type: 

url = 'https://en.wikipedia.org/static/images/project-logos/enwiki.png'
headers = {
    'sec-fetch-dest': 'image',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'referer': 'https://en.wikipedia.org/wiki/Python_(programming_language)',
    ':path': '/static/images/project-logos/enwiki.png',
    'sec-fetch-site': 'same-origin',
    ':authority': 'en.wikipedia.org',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - x-cache: cp3058 hit, cp3056 hit/556295
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-client-ip: 79.24.172.207
#   - content-type: image/png
#   - age: 78418
#   - access-control-allow-origin: *
#   - server: ATS/8.0.8
#   - accept-ranges: bytes
#   - date: Fri, 27 Nov 2020 14:02:12 GMT
#   - x-cache-status: hit-front
#   - last-modified: Thu, 03 Sep 2020 11:18:43 GMT
#   - cache-control: max-age=31536000
#   - server-timing: cache;desc="hit-front"
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - expires: Sat, 27 Nov 2021 10:03:58 GMT
#   - etag: "2182-5ae66ea426ecb"
#   - content-length: 8578
###############################################################################

###############################################################################
# request number: 22
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Octicons-terminal.svg/24px-Octicons-terminal.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    ':path': '/wikipedia/commons/thumb/6/6f/Octicons-terminal.svg/24px-Octicons-terminal.svg.png',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/webp
#   - accept-ranges: bytes
#   - content-length: 154
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache: cp3055 hit, cp3059 hit/149
#   - x-cache-status: hit-front
#   - age: 5496
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - last-modified: Sun, 22 Mar 2020 15:00:03 GMT
#   - date: Sat, 28 Nov 2020 10:17:34 GMT
#   - x-timestamp: 1584889202.82971
#   - access-control-allow-origin: *
#   - etag: fc96fc5a58fc4ae867307c97322b19af
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 23
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Free_and_open-source_software_logo_%282009%29.svg/28px-Free_and_open-source_software_logo_%282009%29.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    ':path': '/wikipedia/commons/thumb/3/31/Free_and_open-source_software_logo_%282009%29.svg/28px-Free_and_open-source_software_logo_%282009%29.svg.png',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/webp
#   - accept-ranges: bytes
#   - x-timestamp: 1561104766.55744
#   - age: 50265
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - content-length: 1070
#   - x-cache: cp3053 hit, cp3059 hit/1474
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: hit-front
#   - date: Fri, 27 Nov 2020 21:51:25 GMT
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - etag: b262c068bb56bf6cc712b188ea15ae40
#   - last-modified: Fri, 21 Jun 2019 08:12:47 GMT
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 24
# resource type: 

url = 'https://en.wikipedia.org/static/images/mobile/copyright/wikipedia-wordmark-en.svg'
headers = {
    ':path': '/static/images/mobile/copyright/wikipedia-wordmark-en.svg',
    'sec-fetch-dest': 'image',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'referer': 'https://en.wikipedia.org/w/load.php?lang=en&modules=ext.cite.styles%7Cext.pygments%2CwikimediaBadges%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cjquery.makeCollapsible.styles%7Cskins.vector.styles.legacy%7Cwikibase.client.init&only=styles&skin=vector',
    'sec-fetch-site': 'same-origin',
    ':authority': 'en.wikipedia.org',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - accept-ranges: bytes
#   - x-cache: cp3064 hit, cp3056 hit/3343955
#   - cache-control: max-age=31536000
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - content-length: 4298
#   - last-modified: Mon, 20 Apr 2020 23:14:40 GMT
#   - etag: W/"357b-5a3c110489394"
#   - x-cache-status: hit-front
#   - expires: Sat, 27 Nov 2021 10:05:54 GMT
#   - content-encoding: gzip
#   - content-type: image/svg+xml
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - date: Fri, 27 Nov 2020 15:42:17 GMT
#   - server: ATS/8.0.8
#   - age: 72412
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
###############################################################################

###############################################################################
# request number: 25
# resource type: 

url = 'https://en.wikipedia.org/w/skins/Vector/resources/skins.vector.styles/images/external-link-ltr-icon.svg'
headers = {
    ':path': '/w/skins/Vector/resources/skins.vector.styles/images/external-link-ltr-icon.svg?b4b84',
    'sec-fetch-dest': 'image',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'referer': 'https://en.wikipedia.org/w/load.php?lang=en&modules=ext.cite.styles%7Cext.pygments%2CwikimediaBadges%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cjquery.makeCollapsible.styles%7Cskins.vector.styles.legacy%7Cwikibase.client.init&only=styles&skin=vector',
    'sec-fetch-site': 'same-origin',
    ':authority': 'en.wikipedia.org',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
params = [
    ('b4b84', ''),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - accept-ranges: bytes
#   - cache-control: public, s-maxage=31536000, max-age=31536000, immutable
#   - age: 77964
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - date: Fri, 27 Nov 2020 14:09:45 GMT
#   - x-cache-status: hit-front
#   - content-encoding: gzip
#   - content-type: image/svg+xml
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-cache: cp3064 hit, cp3056 hit/2091432
#   - x-content-type-options: nosniff
#   - server: ATS/8.0.8
#   - content-length: 281
#   - last-modified: Tue, 17 Nov 2020 17:51:50 GMT
#   - access-control-allow-origin: *
#   - x-request-id: 886cac5d-8fd8-41b3-9759-d94435e13316
#   - server-timing: cache;desc="hit-front"
###############################################################################

###############################################################################
# request number: 26
# resource type: 

url = 'https://en.wikipedia.org/w/skins/Vector/resources/skins.vector.styles/images/bullet-icon.svg'
headers = {
    'sec-fetch-dest': 'image',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'referer': 'https://en.wikipedia.org/w/load.php?lang=en&modules=ext.cite.styles%7Cext.pygments%2CwikimediaBadges%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cjquery.makeCollapsible.styles%7Cskins.vector.styles.legacy%7Cwikibase.client.init&only=styles&skin=vector',
    'sec-fetch-site': 'same-origin',
    ':path': '/w/skins/Vector/resources/skins.vector.styles/images/bullet-icon.svg?d4515',
    ':authority': 'en.wikipedia.org',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
params = [
    ('d4515', ''),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - accept-ranges: bytes
#   - content-length: 154
#   - cache-control: public, s-maxage=31536000, max-age=31536000, immutable
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-cache: cp3062 hit, cp3056 hit/2402714
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-request-id: e35aa4ad-a65e-4328-9246-43fd45f8cb8a
#   - date: Fri, 27 Nov 2020 13:32:03 GMT
#   - x-cache-status: hit-front
#   - content-encoding: gzip
#   - content-type: image/svg+xml
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-content-type-options: nosniff
#   - server: ATS/8.0.8
#   - last-modified: Tue, 17 Nov 2020 17:51:50 GMT
#   - age: 80226
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
###############################################################################

###############################################################################
# request number: 27
# resource type: 

url = 'https://en.wikipedia.org/w/resources/src/mediawiki.skinning/images/magnify-clip-ltr.svg'
headers = {
    ':path': '/w/resources/src/mediawiki.skinning/images/magnify-clip-ltr.svg?8330e',
    'sec-fetch-dest': 'image',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'referer': 'https://en.wikipedia.org/w/load.php?lang=en&modules=ext.cite.styles%7Cext.pygments%2CwikimediaBadges%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cjquery.makeCollapsible.styles%7Cskins.vector.styles.legacy%7Cwikibase.client.init&only=styles&skin=vector',
    'sec-fetch-site': 'same-origin',
    ':authority': 'en.wikipedia.org',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
params = [
    ('8330e', ''),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - accept-ranges: bytes
#   - last-modified: Tue, 17 Nov 2020 17:50:37 GMT
#   - cache-control: public, s-maxage=31536000, max-age=31536000, immutable
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - age: 62512
#   - date: Fri, 27 Nov 2020 18:27:17 GMT
#   - x-cache-status: hit-front
#   - content-encoding: gzip
#   - content-type: image/svg+xml
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-content-type-options: nosniff
#   - server: ATS/8.0.8
#   - access-control-allow-origin: *
#   - x-cache: cp3060 hit, cp3056 hit/969995
#   - content-length: 247
#   - server-timing: cache;desc="hit-front"
#   - x-request-id: 5d6fd3e9-3f87-4be6-bbb4-c3b8ac525ad8
###############################################################################

###############################################################################
# request number: 28
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/6/65/Lock-green.svg'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    ':path': '/wikipedia/commons/6/65/Lock-green.svg',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - etag: W/f99d5d66e6ef5fb312ed07842356ca2c
#   - accept-ranges: bytes
#   - x-timestamp: 1528236483.69043
#   - x-object-meta-sha1base36: lg26mu0oi9yw04piderazn15lmdu0wm
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - last-modified: Tue, 05 Jun 2018 22:08:04 GMT
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: hit-front
#   - content-encoding: gzip
#   - content-type: image/svg+xml
#   - x-cache: cp3051 hit, cp3059 hit/155122
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - content-length: 272
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - age: 66484
#   - date: Fri, 27 Nov 2020 17:21:05 GMT
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 29
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/d/d6/Lock-gray-alt-2.svg'
headers = {
    'sec-fetch-dest': 'image',
    ':path': '/wikipedia/commons/d/d6/Lock-gray-alt-2.svg',
    ':authority': 'upload.wikimedia.org',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-cache: cp3061 hit, cp3059 hit/284498
#   - vary: Accept-Encoding
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-timestamp: 1480096403.86216
#   - age: 80515
#   - x-client-ip: 79.24.172.207
#   - date: Fri, 27 Nov 2020 13:27:14 GMT
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: hit-front
#   - content-length: 318
#   - content-encoding: gzip
#   - content-type: image/svg+xml
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - x-object-meta-sha1base36: 0h87lgkfxx45g5zv62pzfvffensy2bb
#   - last-modified: Fri, 25 Nov 2016 17:53:24 GMT
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
#   - etag: W/423bb01c87eb6c81999073a8ecd2b383
###############################################################################

###############################################################################
# request number: 30
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/2/23/Icons-mini-file_acrobat.gif'
headers = {
    ':path': '/wikipedia/commons/2/23/Icons-mini-file_acrobat.gif',
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/gif
#   - accept-ranges: bytes
#   - x-object-meta-sha1base36: lwohv5rxnuoyzvtwvg2jugrrqvdefu2
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-cache: cp3065 hit, cp3059 hit/650200
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - last-modified: Tue, 15 Oct 2013 21:03:56 GMT
#   - x-timestamp: 1381871035.57270
#   - etag: 5f29c417cdbae1c11f4451f0428ef444
#   - x-cache-status: hit-front
#   - content-length: 291
#   - date: Fri, 27 Nov 2020 13:03:28 GMT
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - age: 81941
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 31
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/20px-Commons-logo.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    ':path': '/wikipedia/en/thumb/4/4a/Commons-logo.svg/20px-Commons-logo.svg.png',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/webp
#   - accept-ranges: bytes
#   - x-timestamp: 1570587919.50751
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - date: Fri, 27 Nov 2020 19:14:39 GMT
#   - x-cache-status: hit-front
#   - x-cache: cp3059 hit, cp3059 hit/27170
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - last-modified: Wed, 09 Oct 2019 02:25:20 GMT
#   - content-length: 590
#   - etag: 5ebbf2f7c2f303da3e4749e5db11155a
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - age: 59671
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 32
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikiquote-logo.svg/23px-Wikiquote-logo.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    ':path': '/wikipedia/commons/thumb/f/fa/Wikiquote-logo.svg/23px-Wikiquote-logo.svg.png',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/webp
#   - age: 12920
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - etag: 262f5dd505c377156c9a9dd2a42a839f
#   - x-cache-status: hit-front
#   - x-timestamp: 1561104671.64393
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - x-cache: cp3051 hit, cp3059 hit/9045
#   - content-length: 772
#   - date: Sat, 28 Nov 2020 08:13:49 GMT
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - last-modified: Fri, 21 Jun 2019 08:11:12 GMT
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 33
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikibooks-logo.svg/27px-Wikibooks-logo.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    ':path': '/wikipedia/commons/thumb/f/fa/Wikibooks-logo.svg/27px-Wikibooks-logo.svg.png',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/webp
#   - accept-ranges: bytes
#   - x-timestamp: 1561104722.68646
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - etag: ce161da5457042f89851c0177b271759
#   - x-cache-status: hit-front
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - content-length: 1208
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - last-modified: Fri, 21 Jun 2019 08:12:03 GMT
#   - x-cache: cp3063 hit, cp3059 hit/2072
#   - age: 6038
#   - date: Sat, 28 Nov 2020 10:08:31 GMT
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 34
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Wikiversity-logo-en.svg/27px-Wikiversity-logo-en.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    ':path': '/wikipedia/commons/thumb/1/1b/Wikiversity-logo-en.svg/27px-Wikiversity-logo-en.svg.png',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/webp
#   - x-timestamp: 1561104723.26511
#   - accept-ranges: bytes
#   - last-modified: Fri, 21 Jun 2019 08:12:04 GMT
#   - x-cache: cp3063 hit, cp3059 hit/10669
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - etag: c83a3755041803b0e92b7c3b4216f176
#   - x-cache-status: hit-front
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - date: Fri, 27 Nov 2020 19:57:54 GMT
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - age: 57075
#   - content-length: 868
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 35
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wikidata-logo.svg/27px-Wikidata-logo.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':path': '/wikipedia/commons/thumb/f/ff/Wikidata-logo.svg/27px-Wikidata-logo.svg.png',
    ':authority': 'upload.wikimedia.org',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/webp
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: hit-front
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-cache: cp3063 hit, cp3059 hit/12863
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - date: Fri, 27 Nov 2020 21:34:29 GMT
#   - server: ATS/8.0.8
#   - x-timestamp: 1561104697.14317
#   - content-length: 204
#   - age: 51281
#   - etag: c05c16925d1414c3bcb5700098831ffe
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - last-modified: Fri, 21 Jun 2019 08:11:38 GMT
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 36
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/10px-OOjs_UI_icon_edit-ltr-progressive.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    ':path': '/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/10px-OOjs_UI_icon_edit-ltr-progressive.svg.png',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/webp
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - age: 29853
#   - last-modified: Wed, 21 Aug 2019 11:27:38 GMT
#   - x-cache-status: hit-front
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - content-length: 174
#   - x-timestamp: 1566386857.83726
#   - date: Sat, 28 Nov 2020 03:31:36 GMT
#   - etag: abcbb58c0d49c9ff86f13321d906cc27
#   - x-cache: cp3051 hit, cp3059 hit/50359
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 37
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/55px-Python-logo-notext.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':path': '/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/55px-Python-logo-notext.svg.png',
    ':authority': 'upload.wikimedia.org',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/png
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-timestamp: 1502346523.69129
#   - x-cache-status: hit-front
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - content-length: 2007
#   - etag: 388c6400684a795a1bde5a0b1444f2a4
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - last-modified: Thu, 10 Aug 2017 06:28:44 GMT
#   - date: Sat, 28 Nov 2020 04:09:29 GMT
#   - age: 27581
#   - access-control-allow-origin: *
#   - x-cache: cp3063 hit, cp3059 hit/28
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 38
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Folder_Hexagonal_Icon.svg/16px-Folder_Hexagonal_Icon.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    ':path': '/wikipedia/en/thumb/4/48/Folder_Hexagonal_Icon.svg/16px-Folder_Hexagonal_Icon.svg.png',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/webp
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - date: Sat, 28 Nov 2020 03:58:07 GMT
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - etag: d66bb931173eaa89bda9461812d8ac5f
#   - x-cache-status: hit-front
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - age: 28262
#   - x-cache: cp3059 hit, cp3059 hit/33858
#   - access-control-allow-origin: *
#   - content-length: 248
#   - server-timing: cache;desc="hit-front"
#   - x-timestamp: 1561104677.36904
#   - last-modified: Fri, 21 Jun 2019 08:11:18 GMT
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 39
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Symbol_list_class.svg/16px-Symbol_list_class.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    ':path': '/wikipedia/en/thumb/d/db/Symbol_list_class.svg/16px-Symbol_list_class.svg.png',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/webp
#   - accept-ranges: bytes
#   - date: Sat, 28 Nov 2020 00:55:23 GMT
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - age: 39227
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache: cp3059 hit, cp3059 hit/5569
#   - x-cache-status: hit-front
#   - last-modified: Fri, 21 Jun 2019 08:11:25 GMT
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-timestamp: 1561104684.08796
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - etag: 241998bf03a4e504be05e0ac6b5a71d3
#   - content-length: 514
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 40
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/DNC_training_recall_task.gif/200px-DNC_training_recall_task.gif'
headers = {
    ':path': '/wikipedia/commons/thumb/b/b5/DNC_training_recall_task.gif/200px-DNC_training_recall_task.gif',
    'sec-fetch-dest': 'image',
    'referer': 'https://en.wikipedia.org/',
    ':authority': 'upload.wikimedia.org',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - date: Fri, 27 Nov 2020 19:25:59 GMT
#   - content-type: image/gif
#   - accept-ranges: bytes
#   - x-cache-status: hit-local
#   - x-cache: cp3061 hit, cp3059 pass
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - server-timing: cache;desc="hit-local"
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - age: 0
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - x-timestamp: 1501466831.83189
#   - content-length: 766784
#   - access-control-allow-origin: *
#   - last-modified: Mon, 31 Jul 2017 02:07:12 GMT
#   - etag: 29b57b79ec1ed0ef9a99021f711a4c58
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 41
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/en/thumb/f/fd/Portal-puzzle.svg/16px-Portal-puzzle.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    ':path': '/wikipedia/en/thumb/f/fd/Portal-puzzle.svg/16px-Portal-puzzle.svg.png',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/webp
#   - accept-ranges: bytes
#   - age: 22560
#   - x-timestamp: 1561104684.14301
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-cache: cp3055 hit, cp3059 hit/8849
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - content-length: 704
#   - x-cache-status: hit-front
#   - last-modified: Fri, 21 Jun 2019 08:11:25 GMT
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - etag: cb956d8f081d95fa6099dfc28725b94c
#   - date: Sat, 28 Nov 2020 05:33:10 GMT
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 42
# resource type: 

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Symbol_book_class2.svg/16px-Symbol_book_class2.svg.png'
headers = {
    'sec-fetch-dest': 'image',
    ':authority': 'upload.wikimedia.org',
    ':path': '/wikipedia/commons/thumb/8/89/Symbol_book_class2.svg/16px-Symbol_book_class2.svg.png',
    'referer': 'https://en.wikipedia.org/',
    'sec-fetch-site': 'cross-site',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/webp
#   - date: Fri, 27 Nov 2020 22:01:18 GMT
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - etag: 5cb339957252d5262f682467428ee1ee
#   - last-modified: Fri, 21 Jun 2019 08:11:19 GMT
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: hit-front
#   - x-cache: cp3057 hit, cp3059 hit/24454
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - content-length: 538
#   - access-control-expose-headers: Age, Date, Content-Length, Content-Range, X-Content-Duration, X-Cache
#   - server: ATS/8.0.8
#   - x-timestamp: 1561104678.10740
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - age: 49671
#   - timing-allow-origin: *
###############################################################################

###############################################################################
# request number: 43
# resource type: 

url = 'https://en.wikipedia.org/w/load.php'
headers = {
    'accept': '*/*',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    ':path': '/w/load.php?lang=en&modules=jquery%2Coojs-ui-core%2Coojs-ui-widgets&skin=vector&version=1jwo0',
    'referer': 'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'sec-fetch-dest': 'script',
    'sec-fetch-site': 'same-origin',
    ':authority': 'en.wikipedia.org',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
params = [
    ('skin', 'vector'),
    ('lang', 'en'),
    ('version', '1jwo0'),
    ('modules', 'jquery%2Coojs-ui-core%2Coojs-ui-widgets'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-request-id: f85ae9e8-1c21-4aee-a7f4-2f66af98b35e
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: hit-front
#   - expires: Sat, 26 Dec 2020 19:56:55 GMT
#   - date: Fri, 27 Nov 2020 15:21:10 GMT
#   - etag: W/"1jwo0"
#   - age: 0
#   - content-encoding: gzip
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-content-type-options: nosniff
#   - server: ATS/8.0.8
#   - x-cache: cp3058 hit, cp3056 hit/208857
#   - content-type: text/javascript; charset=utf-8
#   - cache-control: public, max-age=2592000, s-maxage=2592000
#   - server-timing: cache;desc="hit-front"
#   - content-length: 97512
###############################################################################

###############################################################################
# request number: 44
# resource type: 

url = 'https://en.wikipedia.org/w/skins/Vector/resources/skins.vector.styles/images/user-avatar.svg'
headers = {
    ':path': '/w/skins/Vector/resources/skins.vector.styles/images/user-avatar.svg?b7f58',
    'sec-fetch-dest': 'image',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'referer': 'https://en.wikipedia.org/w/load.php?lang=en&modules=ext.cite.styles%7Cext.pygments%2CwikimediaBadges%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cjquery.makeCollapsible.styles%7Cskins.vector.styles.legacy%7Cwikibase.client.init&only=styles&skin=vector',
    'sec-fetch-site': 'same-origin',
    ':authority': 'en.wikipedia.org',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
params = [
    ('b7f58', ''),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - x-cache: cp3056 hit, cp3056 hit/2407788
#   - accept-ranges: bytes
#   - cache-control: public, s-maxage=31536000, max-age=31536000, immutable
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - content-length: 221
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - age: 79399
#   - x-cache-status: hit-front
#   - content-encoding: gzip
#   - content-type: image/svg+xml
#   - x-request-id: fc01fa21-abe4-4fa6-ae97-cc7df4be5182
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-content-type-options: nosniff
#   - server: ATS/8.0.8
#   - last-modified: Tue, 17 Nov 2020 17:51:50 GMT
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - date: Fri, 27 Nov 2020 13:45:51 GMT
###############################################################################

###############################################################################
# request number: 45
# resource type: 

url = 'https://en.wikipedia.org/w/skins/Vector/resources/skins.vector.styles/images/search.svg'
headers = {
    'sec-fetch-dest': 'image',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    ':path': '/w/skins/Vector/resources/skins.vector.styles/images/search.svg?4d50a',
    'referer': 'https://en.wikipedia.org/w/load.php?lang=en&modules=ext.cite.styles%7Cext.pygments%2CwikimediaBadges%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cjquery.makeCollapsible.styles%7Cskins.vector.styles.legacy%7Cwikibase.client.init&only=styles&skin=vector',
    'sec-fetch-site': 'same-origin',
    ':authority': 'en.wikipedia.org',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
params = [
    ('4d50a', ''),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - x-request-id: 51e894ab-76d6-4a94-a879-0df74947aa71
#   - accept-ranges: bytes
#   - age: 74657
#   - cache-control: public, s-maxage=31536000, max-age=31536000, immutable
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - date: Fri, 27 Nov 2020 15:04:53 GMT
#   - x-cache-status: hit-front
#   - content-encoding: gzip
#   - content-type: image/svg+xml
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-content-type-options: nosniff
#   - server: ATS/8.0.8
#   - last-modified: Tue, 17 Nov 2020 17:51:50 GMT
#   - content-length: 196
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - x-cache: cp3050 hit, cp3056 hit/2130173
###############################################################################

###############################################################################
# request number: 46
# resource type: 

url = 'https://en.wikipedia.org/w/extensions/WikimediaBadges/resources/images/badge-silver-star.png'
headers = {
    'sec-fetch-dest': 'image',
    ':path': '/w/extensions/WikimediaBadges/resources/images/badge-silver-star.png?70a8c',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'referer': 'https://en.wikipedia.org/w/load.php?lang=en&modules=ext.cite.styles%7Cext.pygments%2CwikimediaBadges%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cjquery.makeCollapsible.styles%7Cskins.vector.styles.legacy%7Cwikibase.client.init&only=styles&skin=vector',
    'sec-fetch-site': 'same-origin',
    ':authority': 'en.wikipedia.org',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
params = [
    ('70a8c', ''),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-cache: cp3060 hit, cp3056 hit/406022
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-client-ip: 79.24.172.207
#   - x-request-id: c819cf4b-a07a-4d54-a5e3-3d3f826c51e8
#   - x-content-type-options: nosniff
#   - content-length: 161
#   - content-type: image/png
#   - access-control-allow-origin: *
#   - server: ATS/8.0.8
#   - accept-ranges: bytes
#   - x-cache-status: hit-front
#   - date: Fri, 27 Nov 2020 16:00:04 GMT
#   - cache-control: public, s-maxage=31536000, max-age=31536000, immutable
#   - server-timing: cache;desc="hit-front"
#   - age: 71346
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - last-modified: Tue, 17 Nov 2020 17:51:48 GMT
###############################################################################

###############################################################################
# request number: 47
# resource type: 

url = 'https://en.wikipedia.org/static/favicon/wikipedia.ico'
headers = {
    'sec-fetch-dest': 'image',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'referer': 'https://en.wikipedia.org/wiki/Python_(programming_language)',
    ':path': '/static/favicon/wikipedia.ico',
    'sec-fetch-site': 'same-origin',
    ':authority': 'en.wikipedia.org',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - accept-ranges: bytes
#   - date: Thu, 26 Nov 2020 16:45:37 GMT
#   - cache-control: max-age=31536000
#   - last-modified: Mon, 14 Mar 2016 18:08:11 GMT
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - content-length: 1035
#   - content-type: image/vnd.microsoft.icon
#   - x-cache-status: hit-front
#   - server: mw1332.eqiad.wmnet
#   - content-encoding: gzip
#   - x-cache: cp3060 hit, cp3056 hit/4954259
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - expires: Fri, 26 Nov 2021 16:45:37 GMT
#   - age: 155013
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
#   - etag: W/"aae-52e0629e358c0"
###############################################################################

###############################################################################
# request number: 48
# resource type: 

url = 'https://en.wikipedia.org/w/extensions/UniversalLanguageSelector/resources/images/cog-sprite.svg'
headers = {
    ':path': '/w/extensions/UniversalLanguageSelector/resources/images/cog-sprite.svg?c3fa1',
    'sec-fetch-dest': 'image',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'referer': 'https://en.wikipedia.org/w/load.php?lang=en&modules=ext.cite.styles%7Cext.pygments%2CwikimediaBadges%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cjquery.makeCollapsible.styles%7Cskins.vector.styles.legacy%7Cwikibase.client.init&only=styles&skin=vector',
    'sec-fetch-site': 'same-origin',
    ':authority': 'en.wikipedia.org',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
params = [
    ('c3fa1', ''),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - accept-ranges: bytes
#   - content-length: 511
#   - cache-control: public, s-maxage=31536000, max-age=31536000, immutable
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-request-id: db094e17-0cb7-4a33-8acb-7caf36734105
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - age: 78646
#   - x-cache-status: hit-front
#   - x-cache: cp3056 hit, cp3056 hit/2250933
#   - content-encoding: gzip
#   - content-type: image/svg+xml
#   - last-modified: Tue, 17 Nov 2020 17:51:37 GMT
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - x-content-type-options: nosniff
#   - server: ATS/8.0.8
#   - date: Fri, 27 Nov 2020 13:58:24 GMT
#   - access-control-allow-origin: *
#   - server-timing: cache;desc="hit-front"
###############################################################################

###############################################################################
# request number: 49
# resource type: 

url = 'https://en.wikipedia.org/w/extensions/UniversalLanguageSelector/resources/images/language-base20.svg'
headers = {
    'sec-fetch-dest': 'image',
    ':path': '/w/extensions/UniversalLanguageSelector/resources/images/language-base20.svg?2004a',
    'cookie': 'WMF-Last-Access-Global=28-Nov-2020; GeoIP=IT:21:Turin:45.07:7.69:v4; WMF-Last-Access=28-Nov-2020; enwikimwuser-sessionId=d3ddadcb2e4f2882aa39',
    'referer': 'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'sec-fetch-site': 'same-origin',
    ':authority': 'en.wikipedia.org',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'enwikimwuser-sessionId': 'd3ddadcb2e4f2882aa39',
    'WMF-Last-Access': '28-Nov-2020',
    'GeoIP': 'IT:21:Turin:45.07:7.69:v4',
    'WMF-Last-Access-Global': '28-Nov-2020',
}
params = [
    ('2004a', ''),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - age: 24124
#   - accept-ranges: bytes
#   - cache-control: public, s-maxage=31536000, max-age=31536000, immutable
#   - strict-transport-security: max-age=106384710; includeSubDomains; preload
#   - x-client-ip: 79.24.172.207
#   - report-to: { "group": "wm_nel", "max_age": 86400, "endpoints": [{ "url": "https://intake-logging.wikimedia.org/v1/events?stream=w3c.reportingapi.network_error&schema_uri=/w3c/reportingapi/network_error/1.0.0" }] }
#   - x-cache-status: hit-front
#   - content-encoding: gzip
#   - content-type: image/svg+xml
#   - x-request-id: 883e0e9d-474c-4b99-9ea3-e823a54d115e
#   - last-modified: Tue, 17 Nov 2020 17:51:37 GMT
#   - nel: { "report_to": "wm_nel", "max_age": 86400, "failure_fraction": 0.05, "success_fraction": 0.0}
#   - content-length: 450
#   - x-content-type-options: nosniff
#   - server: ATS/8.0.8
#   - date: Sat, 28 Nov 2020 05:07:07 GMT
#   - access-control-allow-origin: *
#   - x-cache: cp3064 hit, cp3056 hit/449749
#   - server-timing: cache;desc="hit-front"
###############################################################################

