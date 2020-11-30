import requests


s = requests.Session()

###############################################################################
# request number: 1
# resource type: document

url = 'https://www.python.org/'
headers = {
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-fetch-site': 'none',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    ':path': '/',
    'upgrade-insecure-requests': '1',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    ':authority': 'www.python.org',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-cache-hits: 4, 2
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-cache: HIT, HIT
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - content-length: 49772
#   - accept-ranges: bytes
#   - content-type: text/html; charset=utf-8
#   - vary: Cookie
#   - x-frame-options: DENY
#   - server: nginx
#   - age: 1477
#   - x-timer: S1606564280.565754,VS0,VE0
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-served-by: cache-bwi5134-BWI, cache-mrs10551-MRS
###############################################################################

###############################################################################
# request number: 2
# resource type: other

url = 'https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js'
headers = {
    ':path': '/ajax/libs/jquery/1.8.2/jquery.min.js',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'no-cors',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/signed-exchange;v=b3;q=0.9,*/*;q=0.8',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'purpose': 'prefetch',
    'sec-fetch-dest': 'empty',
    ':authority': 'ajax.googleapis.com',
    'accept-language': 'en-US,en;q=0.9',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - alt-svc: h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
#   - server: sffe
#   - x-xss-protection: 0
#   - date: Fri, 27 Nov 2020 20:51:03 GMT
#   - age: 54016
#   - content-length: 33621
#   - content-type: text/javascript; charset=UTF-8
#   - timing-allow-origin: *
#   - cache-control: public, max-age=31536000, stale-while-revalidate=2592000
#   - accept-ranges: bytes
#   - last-modified: Tue, 03 Mar 2020 19:15:00 GMT
#   - expires: Sat, 27 Nov 2021 20:51:03 GMT
#   - x-content-type-options: nosniff
#   - vary: Accept-Encoding
#   - access-control-allow-origin: *
#   - content-encoding: gzip
#   - cross-origin-resource-policy: cross-origin
###############################################################################

###############################################################################
# request number: 3
# resource type: other

url = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js'
headers = {
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'no-cors',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/signed-exchange;v=b3;q=0.9,*/*;q=0.8',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'purpose': 'prefetch',
    ':path': '/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js',
    ':authority': 'ajax.googleapis.com',
    'accept-language': 'en-US,en;q=0.9',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - alt-svc: h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
#   - server: sffe
#   - date: Wed, 25 Nov 2020 16:48:53 GMT
#   - x-xss-protection: 0
#   - content-type: text/javascript; charset=UTF-8
#   - timing-allow-origin: *
#   - expires: Thu, 25 Nov 2021 16:48:53 GMT
#   - cache-control: public, max-age=31536000, stale-while-revalidate=2592000
#   - accept-ranges: bytes
#   - last-modified: Tue, 03 Mar 2020 19:15:00 GMT
#   - age: 241346
#   - content-length: 67948
#   - x-content-type-options: nosniff
#   - vary: Accept-Encoding
#   - access-control-allow-origin: *
#   - content-encoding: gzip
#   - cross-origin-resource-policy: cross-origin
###############################################################################

###############################################################################
# request number: 4
# resource type: xhr

url = 'https://www.python.org/authenticated'
headers = {
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    'accept': 'text/html, */*; q=0.01',
    ':authority': 'www.python.org',
    ':path': '/authenticated',
    'accept-language': 'en-US,en;q=0.9',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-cache-hits: 0, 2
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - accept-ranges: bytes
#   - content-type: text/html; charset=utf-8
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - vary: Cookie
#   - x-frame-options: DENY
#   - server: nginx
#   - content-length: 580
#   - x-timer: S1606564280.170263,VS0,VE0
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: MISS, HIT
#   - age: 1051
#   - x-served-by: cache-bwi5142-BWI, cache-mrs10551-MRS
###############################################################################

###############################################################################
# request number: 5
# resource type: xhr

url = 'https://console.python.org/python-dot-org-live-consoles-status'
headers = {
    'Referer': 'https://www.python.org/',
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Host': 'console.python.org',
    'Sec-Fetch-Mode': 'cors',
    'Origin': 'https://www.python.org',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - ETag: "5fb87845-11"
#   - Server: PythonAnywhere
#   - X-Clacks-Overhead: GNU Terry Pratchett
#   - Access-Control-Allow-Origin: *
#   - Content-Length: 17
#   - Date: Sat, 28 Nov 2020 11:51:20 GMT
#   - Accept-Ranges: bytes
#   - Last-Modified: Sat, 21 Nov 2020 02:15:33 GMT
#   - Strict-Transport-Security: max-age=315360000; includeSubDomains; preload
#   - Content-Type: application/json
###############################################################################

###############################################################################
# request number: 6
# resource type: xhr

url = 'https://2p66nmmycsj3.statuspage.io/api/v2/status.json'
headers = {
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    ':authority': '2p66nmmycsj3.statuspage.io',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'origin': 'https://www.python.org',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    'sec-fetch-site': 'cross-site',
    ':path': '/api/v2/status.json',
    'accept-language': 'en-US,en;q=0.9',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - cache-control: max-age=0, private, must-revalidate
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-content-type-options: nosniff
#   - x-statuspage-skip-logging: true
#   - x-cache: HIT
#   - vary: Accept,Accept-Encoding,X-Forwarded-Host,X-Forwarded-Scheme,X-Forwarded-Proto,Fastly-SSL
#   - x-statuspage-version: 47018e27126c51e788aa9b18f5b333e9011b979b
#   - x-runtime: 0.294062
#   - x-permitted-cross-domain-policies: none
#   - x-request-id: efa1dbc3-2d7b-4e02-8fee-6d6f8347e219
#   - strict-transport-security: max-age=259200
#   - x-download-options: noopen
#   - age: 697
#   - content-type: application/json; charset=utf-8
#   - referrer-policy: strict-origin-when-cross-origin
#   - accept-ranges: bytes
#   - content-length: 227
#   - x-xss-protection: 1; mode=block
#   - etag: W/"190e96564a38a17b670f76ea3b77af44"
#   - access-control-allow-origin: *
###############################################################################

###############################################################################
# request number: 7
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-about/'
headers = {
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'text/html, */*; q=0.01',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    ':path': '/box/supernav-python-about/',
    ':authority': 'www.python.org',
    'accept-language': 'en-US,en;q=0.9',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-cache: HIT, HIT
#   - x-served-by: cache-bwi5121-BWI, cache-mrs10551-MRS
#   - x-cache-hits: 1, 2
#   - age: 1231
#   - accept-ranges: bytes
#   - content-type: text/html; charset=utf-8
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-frame-options: DENY
#   - server: nginx
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-timer: S1606564280.297554,VS0,VE0
#   - content-length: 441
###############################################################################

###############################################################################
# request number: 8
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-downloads/'
headers = {
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':path': '/box/supernav-python-downloads/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    'accept': 'text/html, */*; q=0.01',
    ':authority': 'www.python.org',
    'accept-language': 'en-US,en;q=0.9',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-cache: HIT, HIT
#   - content-length: 1902
#   - x-served-by: cache-bwi5130-BWI, cache-mrs10551-MRS
#   - x-cache-hits: 1, 2
#   - age: 1231
#   - accept-ranges: bytes
#   - content-type: text/html; charset=utf-8
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-frame-options: DENY
#   - server: nginx
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-timer: S1606564280.303022,VS0,VE0
###############################################################################

###############################################################################
# request number: 9
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-documentation/'
headers = {
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/box/supernav-python-documentation/',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    'accept': 'text/html, */*; q=0.01',
    ':authority': 'www.python.org',
    'accept-language': 'en-US,en;q=0.9',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-cache: HIT, HIT
#   - x-cache-hits: 2, 2
#   - age: 1231
#   - accept-ranges: bytes
#   - content-type: text/html; charset=utf-8
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-frame-options: DENY
#   - server: nginx
#   - x-timer: S1606564280.310042,VS0,VE0
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - content-length: 576
#   - x-served-by: cache-bwi5129-BWI, cache-mrs10551-MRS
###############################################################################

###############################################################################
# request number: 10
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-community/'
headers = {
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    'accept': 'text/html, */*; q=0.01',
    ':authority': 'www.python.org',
    ':path': '/box/supernav-python-community/',
    'accept-language': 'en-US,en;q=0.9',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-cache-hits: 4, 2
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-cache: HIT, HIT
#   - age: 1231
#   - accept-ranges: bytes
#   - content-type: text/html; charset=utf-8
#   - x-served-by: cache-bwi5132-BWI, cache-mrs10551-MRS
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - content-length: 1016
#   - x-frame-options: DENY
#   - server: nginx
#   - x-timer: S1606564280.319321,VS0,VE0
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
###############################################################################

###############################################################################
# request number: 11
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-success-stories/'
headers = {
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    'accept': 'text/html, */*; q=0.01',
    ':authority': 'www.python.org',
    ':path': '/box/supernav-python-success-stories/',
    'accept-language': 'en-US,en;q=0.9',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-cache: HIT, HIT
#   - x-cache-hits: 2, 2
#   - x-served-by: cache-bwi5121-BWI, cache-mrs10551-MRS
#   - x-timer: S1606564280.319303,VS0,VE0
#   - age: 1231
#   - accept-ranges: bytes
#   - content-type: text/html; charset=utf-8
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-frame-options: DENY
#   - server: nginx
#   - content-length: 520
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
###############################################################################

###############################################################################
# request number: 12
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-blog/'
headers = {
    ':path': '/box/supernav-python-blog/',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    'accept': 'text/html, */*; q=0.01',
    ':authority': 'www.python.org',
    'accept-language': 'en-US,en;q=0.9',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-timer: S1606564280.325263,VS0,VE0
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-length: 704
#   - x-cache: HIT, HIT
#   - x-cache-hits: 2, 2
#   - age: 1231
#   - accept-ranges: bytes
#   - content-type: text/html; charset=utf-8
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-frame-options: DENY
#   - server: nginx
#   - x-served-by: cache-bwi5136-BWI, cache-mrs10551-MRS
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
###############################################################################

###############################################################################
# request number: 13
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-events/'
headers = {
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    ':path': '/box/supernav-python-events/',
    'sec-fetch-mode': 'cors',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    'accept': 'text/html, */*; q=0.01',
    ':authority': 'www.python.org',
    'accept-language': 'en-US,en;q=0.9',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-length: 96
#   - x-cache: HIT, HIT
#   - x-cache-hits: 3, 2
#   - x-timer: S1606564280.331063,VS0,VE0
#   - x-served-by: cache-bwi5121-BWI, cache-mrs10551-MRS
#   - age: 1231
#   - accept-ranges: bytes
#   - content-type: text/html; charset=utf-8
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-frame-options: DENY
#   - server: nginx
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
###############################################################################

###############################################################################
# request number: 14
# resource type: other

url = 'https://www.python.org/static/favicon.ico'
headers = {
    'sec-fetch-mode': 'no-cors',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    ':path': '/static/favicon.ico',
    ':method': 'GET',
    'sec-fetch-dest': 'image',
    ':authority': 'www.python.org',
    'accept-language': 'en-US,en;q=0.9',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-type: image/x-icon
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-cache: HIT, HIT
#   - age: 184762
#   - content-length: 15086
#   - accept-ranges: bytes
#   - last-modified: Wed, 25 Nov 2020 14:36:14 GMT
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-cache-hits: 2, 4
#   - x-served-by: cache-bwi5138-BWI, cache-mrs10551-MRS
#   - x-timer: S1606564280.391581,VS0,VE0
#   - server: nginx
#   - cache-control: max-age=604800, public
#   - etag: "5fbe6bde-3aee"
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
###############################################################################

