import requests


s = requests.Session()

###############################################################################
# request number: 1
# resource type: document

url = 'https://www.python.org/'
headers = {
    'sec-fetch-site': 'none',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'pragma': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.python.org',
    'sec-fetch-user': '?1',
    ':path': '/',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cache-control': 'no-cache',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-length: 49772
#   - age: 1477
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - x-cache-hits: 4, 2
#   - vary: Cookie
#   - x-timer: S1606564280.565754,VS0,VE0
#   - x-served-by: cache-bwi5134-BWI, cache-mrs10551-MRS
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
###############################################################################

###############################################################################
# request number: 2
# resource type: other

url = 'https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'purpose': 'prefetch',
    'sec-fetch-site': 'cross-site',
    ':authority': 'ajax.googleapis.com',
    ':path': '/ajax/libs/jquery/1.8.2/jquery.min.js',
    ':scheme': 'https',
    'sec-fetch-mode': 'no-cors',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'accept': 'application/signed-exchange;v=b3;q=0.9,*/*;q=0.8',
    'cache-control': 'no-cache',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-length: 33621
#   - last-modified: Tue, 03 Mar 2020 19:15:00 GMT
#   - content-type: text/javascript; charset=UTF-8
#   - alt-svc: h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
#   - timing-allow-origin: *
#   - x-content-type-options: nosniff
#   - cache-control: public, max-age=31536000, stale-while-revalidate=2592000
#   - expires: Sat, 27 Nov 2021 20:51:03 GMT
#   - accept-ranges: bytes
#   - server: sffe
#   - date: Fri, 27 Nov 2020 20:51:03 GMT
#   - x-xss-protection: 0
#   - cross-origin-resource-policy: cross-origin
#   - vary: Accept-Encoding
#   - age: 54016
#   - access-control-allow-origin: *
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 3
# resource type: other

url = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'purpose': 'prefetch',
    'sec-fetch-site': 'cross-site',
    ':authority': 'ajax.googleapis.com',
    ':scheme': 'https',
    'sec-fetch-mode': 'no-cors',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'accept': 'application/signed-exchange;v=b3;q=0.9,*/*;q=0.8',
    'cache-control': 'no-cache',
    ':path': '/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - last-modified: Tue, 03 Mar 2020 19:15:00 GMT
#   - content-type: text/javascript; charset=UTF-8
#   - alt-svc: h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
#   - timing-allow-origin: *
#   - x-content-type-options: nosniff
#   - cache-control: public, max-age=31536000, stale-while-revalidate=2592000
#   - age: 241346
#   - date: Wed, 25 Nov 2020 16:48:53 GMT
#   - accept-ranges: bytes
#   - content-length: 67948
#   - server: sffe
#   - x-xss-protection: 0
#   - cross-origin-resource-policy: cross-origin
#   - vary: Accept-Encoding
#   - expires: Thu, 25 Nov 2021 16:48:53 GMT
#   - access-control-allow-origin: *
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 4
# resource type: xhr

url = 'https://www.python.org/authenticated'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    ':path': '/authenticated',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.python.org',
    'accept': 'text/html, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'referer': 'https://www.python.org/',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - server: nginx
#   - x-cache: MISS, HIT
#   - x-served-by: cache-bwi5142-BWI, cache-mrs10551-MRS
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - x-cache-hits: 0, 2
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - vary: Cookie
#   - age: 1051
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-timer: S1606564280.170263,VS0,VE0
#   - content-length: 580
###############################################################################

###############################################################################
# request number: 5
# resource type: xhr

url = 'https://console.python.org/python-dot-org-live-consoles-status'
headers = {
    'Referer': 'https://www.python.org/',
    'Origin': 'https://www.python.org',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Dest': 'empty',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Sec-Fetch-Mode': 'cors',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Host': 'console.python.org',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - Access-Control-Allow-Origin: *
#   - ETag: "5fb87845-11"
#   - Accept-Ranges: bytes
#   - Server: PythonAnywhere
#   - Content-Length: 17
#   - Strict-Transport-Security: max-age=315360000; includeSubDomains; preload
#   - Date: Sat, 28 Nov 2020 11:51:20 GMT
#   - X-Clacks-Overhead: GNU Terry Pratchett
#   - Content-Type: application/json
#   - Last-Modified: Sat, 21 Nov 2020 02:15:33 GMT
###############################################################################

###############################################################################
# request number: 6
# resource type: xhr

url = 'https://2p66nmmycsj3.statuspage.io/api/v2/status.json'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'origin': 'https://www.python.org',
    'sec-fetch-site': 'cross-site',
    ':path': '/api/v2/status.json',
    ':authority': '2p66nmmycsj3.statuspage.io',
    'sec-fetch-mode': 'cors',
    ':scheme': 'https',
    'referer': 'https://www.python.org/',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'cache-control': 'no-cache',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-request-id: efa1dbc3-2d7b-4e02-8fee-6d6f8347e219
#   - x-xss-protection: 1; mode=block
#   - cache-control: max-age=0, private, must-revalidate
#   - x-statuspage-version: 47018e27126c51e788aa9b18f5b333e9011b979b
#   - access-control-allow-origin: *
#   - x-download-options: noopen
#   - content-length: 227
#   - x-statuspage-skip-logging: true
#   - x-permitted-cross-domain-policies: none
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-cache: HIT
#   - referrer-policy: strict-origin-when-cross-origin
#   - strict-transport-security: max-age=259200
#   - accept-ranges: bytes
#   - etag: W/"190e96564a38a17b670f76ea3b77af44"
#   - x-runtime: 0.294062
#   - age: 697
#   - vary: Accept,Accept-Encoding,X-Forwarded-Host,X-Forwarded-Scheme,X-Forwarded-Proto,Fastly-SSL
#   - x-content-type-options: nosniff
#   - content-type: application/json; charset=utf-8
###############################################################################

###############################################################################
# request number: 7
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-about/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.python.org',
    'accept': 'text/html, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'referer': 'https://www.python.org/',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    ':path': '/box/supernav-python-about/',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-served-by: cache-bwi5121-BWI, cache-mrs10551-MRS
#   - age: 1231
#   - server: nginx
#   - content-length: 441
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - x-cache-hits: 1, 2
#   - x-timer: S1606564280.297554,VS0,VE0
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
###############################################################################

###############################################################################
# request number: 8
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-downloads/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.python.org',
    'accept': 'text/html, */*; q=0.01',
    ':path': '/box/supernav-python-downloads/',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'referer': 'https://www.python.org/',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-timer: S1606564280.303022,VS0,VE0
#   - age: 1231
#   - server: nginx
#   - content-length: 1902
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - x-cache-hits: 1, 2
#   - x-served-by: cache-bwi5130-BWI, cache-mrs10551-MRS
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
###############################################################################

###############################################################################
# request number: 9
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-documentation/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.python.org',
    'accept': 'text/html, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'referer': 'https://www.python.org/',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    ':path': '/box/supernav-python-documentation/',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - age: 1231
#   - server: nginx
#   - content-length: 576
#   - x-timer: S1606564280.310042,VS0,VE0
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - x-served-by: cache-bwi5129-BWI, cache-mrs10551-MRS
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-cache-hits: 2, 2
###############################################################################

###############################################################################
# request number: 10
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-community/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.python.org',
    'accept': 'text/html, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'referer': 'https://www.python.org/',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    ':path': '/box/supernav-python-community/',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - age: 1231
#   - x-served-by: cache-bwi5132-BWI, cache-mrs10551-MRS
#   - content-length: 1016
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - x-cache-hits: 4, 2
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-timer: S1606564280.319321,VS0,VE0
###############################################################################

###############################################################################
# request number: 11
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-success-stories/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.python.org',
    ':path': '/box/supernav-python-success-stories/',
    'accept': 'text/html, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'referer': 'https://www.python.org/',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-served-by: cache-bwi5121-BWI, cache-mrs10551-MRS
#   - age: 1231
#   - server: nginx
#   - content-length: 520
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - accept-ranges: bytes
#   - x-timer: S1606564280.319303,VS0,VE0
#   - x-frame-options: DENY
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-cache-hits: 2, 2
###############################################################################

###############################################################################
# request number: 12
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-blog/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/box/supernav-python-blog/',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.python.org',
    'accept': 'text/html, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'referer': 'https://www.python.org/',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - age: 1231
#   - server: nginx
#   - x-served-by: cache-bwi5136-BWI, cache-mrs10551-MRS
#   - x-timer: S1606564280.325263,VS0,VE0
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - content-length: 704
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-cache-hits: 2, 2
###############################################################################

###############################################################################
# request number: 13
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-events/'
headers = {
    ':path': '/box/supernav-python-events/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.python.org',
    'accept': 'text/html, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'referer': 'https://www.python.org/',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-cache-hits: 3, 2
#   - x-served-by: cache-bwi5121-BWI, cache-mrs10551-MRS
#   - age: 1231
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - accept-ranges: bytes
#   - x-timer: S1606564280.331063,VS0,VE0
#   - x-frame-options: DENY
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - content-length: 96
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
###############################################################################

###############################################################################
# request number: 14
# resource type: other

url = 'https://www.python.org/static/favicon.ico'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    ':authority': 'www.python.org',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-dest': 'image',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'sec-fetch-mode': 'no-cors',
    'referer': 'https://www.python.org/',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    ':path': '/static/favicon.ico',
    'cache-control': 'no-cache',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-timer: S1606564280.391581,VS0,VE0
#   - content-type: image/x-icon
#   - server: nginx
#   - etag: "5fbe6bde-3aee"
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-length: 15086
#   - cache-control: max-age=604800, public
#   - accept-ranges: bytes
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-served-by: cache-bwi5138-BWI, cache-mrs10551-MRS
#   - x-cache: HIT, HIT
#   - last-modified: Wed, 25 Nov 2020 14:36:14 GMT
#   - x-cache-hits: 2, 4
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - age: 184762
###############################################################################

