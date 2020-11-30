import requests


s = requests.Session()

###############################################################################
# request number: 1
# resource type: document

url = 'https://www.python.org/'
headers = {
    'sec-fetch-site': 'none',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'navigate',
    'upgrade-insecure-requests': '1',
    'pragma': 'no-cache',
    ':path': '/',
    'sec-fetch-user': '?1',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    ':method': 'GET',
    'sec-fetch-dest': 'document',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.python.org',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - vary: Cookie
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - age: 1477
#   - x-timer: S1606564280.565754,VS0,VE0
#   - x-served-by: cache-bwi5134-BWI, cache-mrs10551-MRS
#   - accept-ranges: bytes
#   - x-cache-hits: 4, 2
#   - content-length: 49772
#   - server: nginx
#   - x-cache: HIT, HIT
#   - x-frame-options: DENY
###############################################################################

###############################################################################
# request number: 2
# resource type: other

url = 'https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-site': 'cross-site',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'purpose': 'prefetch',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'application/signed-exchange;v=b3;q=0.9,*/*;q=0.8',
    ':authority': 'ajax.googleapis.com',
    ':scheme': 'https',
    ':method': 'GET',
    'sec-fetch-mode': 'no-cors',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':path': '/ajax/libs/jquery/1.8.2/jquery.min.js',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - cross-origin-resource-policy: cross-origin
#   - alt-svc: h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
#   - age: 54016
#   - last-modified: Tue, 03 Mar 2020 19:15:00 GMT
#   - x-content-type-options: nosniff
#   - date: Fri, 27 Nov 2020 20:51:03 GMT
#   - accept-ranges: bytes
#   - cache-control: public, max-age=31536000, stale-while-revalidate=2592000
#   - expires: Sat, 27 Nov 2021 20:51:03 GMT
#   - content-type: text/javascript; charset=UTF-8
#   - server: sffe
#   - vary: Accept-Encoding
#   - access-control-allow-origin: *
#   - x-xss-protection: 0
#   - timing-allow-origin: *
#   - content-length: 33621
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 3
# resource type: other

url = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-site': 'cross-site',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'accept-language': 'en-US,en;q=0.9',
    'purpose': 'prefetch',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'application/signed-exchange;v=b3;q=0.9,*/*;q=0.8',
    ':authority': 'ajax.googleapis.com',
    ':scheme': 'https',
    ':method': 'GET',
    'sec-fetch-mode': 'no-cors',
    'cache-control': 'no-cache',
    ':path': '/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-xss-protection: 0
#   - cross-origin-resource-policy: cross-origin
#   - content-length: 67948
#   - age: 241346
#   - alt-svc: h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
#   - last-modified: Tue, 03 Mar 2020 19:15:00 GMT
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - cache-control: public, max-age=31536000, stale-while-revalidate=2592000
#   - content-type: text/javascript; charset=UTF-8
#   - date: Wed, 25 Nov 2020 16:48:53 GMT
#   - vary: Accept-Encoding
#   - access-control-allow-origin: *
#   - expires: Thu, 25 Nov 2021 16:48:53 GMT
#   - server: sffe
#   - timing-allow-origin: *
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 4
# resource type: xhr

url = 'https://www.python.org/authenticated'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'text/html, */*; q=0.01',
    'sec-fetch-site': 'same-origin',
    'pragma': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    ':path': '/authenticated',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    ':method': 'GET',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.python.org',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - age: 1051
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - x-served-by: cache-bwi5142-BWI, cache-mrs10551-MRS
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: MISS, HIT
#   - vary: Cookie
#   - accept-ranges: bytes
#   - content-length: 580
#   - x-timer: S1606564280.170263,VS0,VE0
#   - x-cache-hits: 0, 2
#   - server: nginx
#   - x-frame-options: DENY
###############################################################################

###############################################################################
# request number: 5
# resource type: xhr

url = 'https://console.python.org/python-dot-org-live-consoles-status'
headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-site',
    'Accept-Language': 'en-US,en;q=0.9',
    'Host': 'console.python.org',
    'Pragma': 'no-cache',
    'Sec-Fetch-Mode': 'cors',
    'Origin': 'https://www.python.org',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Cache-Control': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Referer': 'https://www.python.org/',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - Last-Modified: Sat, 21 Nov 2020 02:15:33 GMT
#   - ETag: "5fb87845-11"
#   - Accept-Ranges: bytes
#   - Content-Type: application/json
#   - Content-Length: 17
#   - X-Clacks-Overhead: GNU Terry Pratchett
#   - Date: Sat, 28 Nov 2020 11:51:20 GMT
#   - Access-Control-Allow-Origin: *
#   - Strict-Transport-Security: max-age=315360000; includeSubDomains; preload
#   - Server: PythonAnywhere
###############################################################################

###############################################################################
# request number: 6
# resource type: xhr

url = 'https://2p66nmmycsj3.statuspage.io/api/v2/status.json'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':authority': '2p66nmmycsj3.statuspage.io',
    'sec-fetch-site': 'cross-site',
    'pragma': 'no-cache',
    'referer': 'https://www.python.org/',
    'origin': 'https://www.python.org',
    ':path': '/api/v2/status.json',
    'accept': '*/*',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    ':method': 'GET',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-content-type-options: nosniff
#   - x-xss-protection: 1; mode=block
#   - x-cache: HIT
#   - cache-control: max-age=0, private, must-revalidate
#   - x-statuspage-version: 47018e27126c51e788aa9b18f5b333e9011b979b
#   - age: 697
#   - etag: W/"190e96564a38a17b670f76ea3b77af44"
#   - accept-ranges: bytes
#   - content-type: application/json; charset=utf-8
#   - access-control-allow-origin: *
#   - content-length: 227
#   - x-request-id: efa1dbc3-2d7b-4e02-8fee-6d6f8347e219
#   - x-download-options: noopen
#   - referrer-policy: strict-origin-when-cross-origin
#   - x-runtime: 0.294062
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-permitted-cross-domain-policies: none
#   - vary: Accept,Accept-Encoding,X-Forwarded-Host,X-Forwarded-Scheme,X-Forwarded-Proto,Fastly-SSL
#   - strict-transport-security: max-age=259200
#   - x-statuspage-skip-logging: true
###############################################################################

###############################################################################
# request number: 7
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-about/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'text/html, */*; q=0.01',
    'sec-fetch-site': 'same-origin',
    'pragma': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    ':method': 'GET',
    ':path': '/box/supernav-python-about/',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.python.org',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-timer: S1606564280.297554,VS0,VE0
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - age: 1231
#   - x-cache-hits: 1, 2
#   - accept-ranges: bytes
#   - content-length: 441
#   - x-served-by: cache-bwi5121-BWI, cache-mrs10551-MRS
#   - server: nginx
#   - x-cache: HIT, HIT
#   - x-frame-options: DENY
###############################################################################

###############################################################################
# request number: 8
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-downloads/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'text/html, */*; q=0.01',
    'sec-fetch-site': 'same-origin',
    'pragma': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    ':path': '/box/supernav-python-downloads/',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    ':method': 'GET',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.python.org',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - content-length: 1902
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - age: 1231
#   - x-cache-hits: 1, 2
#   - x-served-by: cache-bwi5130-BWI, cache-mrs10551-MRS
#   - accept-ranges: bytes
#   - x-timer: S1606564280.303022,VS0,VE0
#   - server: nginx
#   - x-cache: HIT, HIT
#   - x-frame-options: DENY
###############################################################################

###############################################################################
# request number: 9
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-documentation/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'text/html, */*; q=0.01',
    ':path': '/box/supernav-python-documentation/',
    'sec-fetch-site': 'same-origin',
    'pragma': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    ':method': 'GET',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.python.org',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - x-cache-hits: 2, 2
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - age: 1231
#   - x-served-by: cache-bwi5129-BWI, cache-mrs10551-MRS
#   - accept-ranges: bytes
#   - x-timer: S1606564280.310042,VS0,VE0
#   - content-length: 576
#   - server: nginx
#   - x-cache: HIT, HIT
#   - x-frame-options: DENY
###############################################################################

###############################################################################
# request number: 10
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-community/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'text/html, */*; q=0.01',
    'sec-fetch-site': 'same-origin',
    'pragma': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':method': 'GET',
    ':path': '/box/supernav-python-community/',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.python.org',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - age: 1231
#   - content-length: 1016
#   - accept-ranges: bytes
#   - x-served-by: cache-bwi5132-BWI, cache-mrs10551-MRS
#   - x-cache-hits: 4, 2
#   - server: nginx
#   - x-cache: HIT, HIT
#   - x-timer: S1606564280.319321,VS0,VE0
#   - x-frame-options: DENY
###############################################################################

###############################################################################
# request number: 11
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-success-stories/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'text/html, */*; q=0.01',
    'sec-fetch-site': 'same-origin',
    'pragma': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    ':path': '/box/supernav-python-success-stories/',
    ':method': 'GET',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.python.org',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - x-cache-hits: 2, 2
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - age: 1231
#   - content-length: 520
#   - accept-ranges: bytes
#   - x-timer: S1606564280.319303,VS0,VE0
#   - x-served-by: cache-bwi5121-BWI, cache-mrs10551-MRS
#   - server: nginx
#   - x-cache: HIT, HIT
#   - x-frame-options: DENY
###############################################################################

###############################################################################
# request number: 12
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-blog/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'text/html, */*; q=0.01',
    'sec-fetch-site': 'same-origin',
    'pragma': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    ':method': 'GET',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':path': '/box/supernav-python-blog/',
    ':authority': 'www.python.org',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - x-cache-hits: 2, 2
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - age: 1231
#   - accept-ranges: bytes
#   - content-length: 704
#   - x-served-by: cache-bwi5136-BWI, cache-mrs10551-MRS
#   - x-timer: S1606564280.325263,VS0,VE0
#   - server: nginx
#   - x-cache: HIT, HIT
#   - x-frame-options: DENY
###############################################################################

###############################################################################
# request number: 13
# resource type: xhr

url = 'https://www.python.org/box/supernav-python-events/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'text/html, */*; q=0.01',
    'sec-fetch-site': 'same-origin',
    'pragma': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    ':method': 'GET',
    ':path': '/box/supernav-python-events/',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.python.org',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/html; charset=utf-8
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - age: 1231
#   - x-timer: S1606564280.331063,VS0,VE0
#   - content-length: 96
#   - accept-ranges: bytes
#   - x-cache-hits: 3, 2
#   - x-served-by: cache-bwi5121-BWI, cache-mrs10551-MRS
#   - server: nginx
#   - x-cache: HIT, HIT
#   - x-frame-options: DENY
###############################################################################

###############################################################################
# request number: 14
# resource type: other

url = 'https://www.python.org/static/favicon.ico'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    ':path': '/static/favicon.ico',
    'pragma': 'no-cache',
    'referer': 'https://www.python.org/',
    'sec-fetch-dest': 'image',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    ':method': 'GET',
    'sec-fetch-mode': 'no-cors',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    ':authority': 'www.python.org',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-cache-hits: 2, 4
#   - content-type: image/x-icon
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - cache-control: max-age=604800, public
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - content-length: 15086
#   - last-modified: Wed, 25 Nov 2020 14:36:14 GMT
#   - accept-ranges: bytes
#   - x-cache: HIT, HIT
#   - x-served-by: cache-bwi5138-BWI, cache-mrs10551-MRS
#   - etag: "5fbe6bde-3aee"
#   - server: nginx
#   - age: 184762
#   - x-timer: S1606564280.391581,VS0,VE0
#   - strict-transport-security: max-age=63072000; includeSubDomains
###############################################################################

