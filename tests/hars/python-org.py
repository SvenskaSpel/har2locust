import requests


s = requests.Session()
s.headers = {
}

###############################################################################
# request number: 1
# resource type: 

url = 'https://www.python.org/'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'upgrade-insecure-requests': '1',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    ':path': '/',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'sec-fetch-user': '?1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'none',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-length: 49772
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - content-type: text/html; charset=utf-8
#   - x-cache: HIT, HIT
#   - vary: Cookie
#   - age: 1477
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - x-cache-hits: 4, 2
#   - server: nginx
#   - x-timer: S1606564280.565754,VS0,VE0
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-served-by: cache-bwi5134-BWI, cache-mrs10551-MRS
###############################################################################

###############################################################################
# request number: 2
# resource type: 

url = 'https://www.python.org/static/js/libs/modernizr.js'
headers = {
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'sec-fetch-dest': 'script',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    ':path': '/static/js/libs/modernizr.js',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - cache-control: max-age=604800, public
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - age: 363283
#   - x-cache: HIT, HIT
#   - last-modified: Mon, 23 Nov 2020 16:47:16 GMT
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - accept-ranges: bytes
#   - content-length: 5053
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-cache-hits: 1, 6
#   - x-served-by: cache-bwi5148-BWI, cache-mrs10551-MRS
#   - etag: "5fbbe794-2de9"
#   - content-type: application/javascript
#   - x-timer: S1606564280.681044,VS0,VE0
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 3
# resource type: 

url = 'https://www.python.org/static/stylesheets/style.b50cef9e3bb9.css'
headers = {
    ':path': '/static/stylesheets/style.b50cef9e3bb9.css',
    'accept': 'text/css,*/*;q=0.1',
    ':method': 'GET',
    'sec-fetch-dest': 'style',
    'accept-encoding': 'gzip, deflate, br',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - last-modified: Wed, 25 Nov 2020 13:46:49 GMT
#   - vary: Accept-Encoding
#   - cache-control: max-age=604800, public
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - content-length: 113718
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - accept-ranges: bytes
#   - x-timer: S1606564280.680332,VS0,VE0
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-cache-hits: 1, 6
#   - content-type: text/css
#   - x-served-by: cache-bwi5139-BWI, cache-mrs10551-MRS
#   - age: 252046
#   - etag: "5fbe6049-4b4b6"
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 4
# resource type: 

url = 'https://www.python.org/static/stylesheets/mq.eef77a5d2257.css'
headers = {
    'accept': 'text/css,*/*;q=0.1',
    ':method': 'GET',
    'sec-fetch-dest': 'style',
    'accept-encoding': 'gzip, deflate, br',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    ':path': '/static/stylesheets/mq.eef77a5d2257.css',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - cache-control: max-age=604800, public
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - last-modified: Wed, 25 Nov 2020 14:36:19 GMT
#   - age: 184973
#   - x-cache: HIT, HIT
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - accept-ranges: bytes
#   - x-timer: S1606564280.681022,VS0,VE0
#   - x-served-by: cache-bwi5124-BWI, cache-mrs10551-MRS
#   - server: nginx
#   - x-cache-hits: 3, 63
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: text/css
#   - etag: "5fbe6be3-12118"
#   - content-encoding: gzip
#   - content-length: 10372
###############################################################################

###############################################################################
# request number: 5
# resource type: 

url = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css'
headers = {
    'accept': 'text/css,*/*;q=0.1',
    ':path': '/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css',
    ':method': 'GET',
    'sec-fetch-dest': 'style',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    ':authority': 'ajax.googleapis.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - expires: Wed, 24 Nov 2021 12:25:54 GMT
#   - vary: Accept-Encoding
#   - content-type: text/css; charset=UTF-8
#   - server: sffe
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - access-control-allow-origin: *
#   - cross-origin-resource-policy: cross-origin
#   - cache-control: public, max-age=31536000, stale-while-revalidate=2592000
#   - alt-svc: h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
#   - age: 343525
#   - x-xss-protection: 0
#   - last-modified: Tue, 03 Mar 2020 19:15:00 GMT
#   - content-encoding: gzip
#   - timing-allow-origin: *
#   - date: Tue, 24 Nov 2020 12:25:54 GMT
#   - content-length: 8422
###############################################################################

###############################################################################
# request number: 6
# resource type: 

url = 'https://www.python.org/static/img/python-logo.png'
headers = {
    'sec-fetch-dest': 'image',
    ':path': '/static/img/python-logo.png',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - etag: "5fbe6bde-2776"
#   - cache-control: max-age=604800, public
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - content-type: image/png
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - accept-ranges: bytes
#   - x-timer: S1606564280.833001,VS0,VE0
#   - content-length: 10102
#   - age: 176937
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - last-modified: Wed, 25 Nov 2020 14:36:14 GMT
#   - x-cache-hits: 1, 5
#   - x-served-by: cache-bwi5149-BWI, cache-mrs10551-MRS
###############################################################################

###############################################################################
# request number: 7
# resource type: 

url = 'https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js'
headers = {
    ':path': '/ajax/libs/jquery/1.8.2/jquery.min.js',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-dest': 'script',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    ':authority': 'ajax.googleapis.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - age: 54016
#   - vary: Accept-Encoding
#   - expires: Sat, 27 Nov 2021 20:51:03 GMT
#   - server: sffe
#   - x-content-type-options: nosniff
#   - date: Fri, 27 Nov 2020 20:51:03 GMT
#   - accept-ranges: bytes
#   - access-control-allow-origin: *
#   - cross-origin-resource-policy: cross-origin
#   - cache-control: public, max-age=31536000, stale-while-revalidate=2592000
#   - alt-svc: h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
#   - timing-allow-origin: *
#   - content-length: 33621
#   - x-xss-protection: 0
#   - last-modified: Tue, 03 Mar 2020 19:15:00 GMT
#   - content-encoding: gzip
#   - content-type: text/javascript; charset=UTF-8
###############################################################################

###############################################################################
# request number: 8
# resource type: 

url = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js'
headers = {
    ':path': '/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-dest': 'script',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    ':authority': 'ajax.googleapis.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - date: Wed, 25 Nov 2020 16:48:53 GMT
#   - content-length: 67948
#   - server: sffe
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - access-control-allow-origin: *
#   - cross-origin-resource-policy: cross-origin
#   - cache-control: public, max-age=31536000, stale-while-revalidate=2592000
#   - alt-svc: h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
#   - timing-allow-origin: *
#   - age: 241346
#   - last-modified: Tue, 03 Mar 2020 19:15:00 GMT
#   - x-xss-protection: 0
#   - expires: Thu, 25 Nov 2021 16:48:53 GMT
#   - content-encoding: gzip
#   - content-type: text/javascript; charset=UTF-8
###############################################################################

###############################################################################
# request number: 9
# resource type: 

url = 'https://www.python.org/static/js/libs/masonry.pkgd.min.js'
headers = {
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'sec-fetch-dest': 'script',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    ':path': '/static/js/libs/masonry.pkgd.min.js',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - x-timer: S1606564280.793033,VS0,VE0
#   - cache-control: max-age=604800, public
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - content-length: 7869
#   - last-modified: Mon, 23 Nov 2020 16:47:16 GMT
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - accept-ranges: bytes
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - age: 358661
#   - content-type: application/javascript
#   - x-cache-hits: 1, 5
#   - etag: "5fbbe794-6643"
#   - content-encoding: gzip
#   - x-served-by: cache-bwi5149-BWI, cache-mrs10551-MRS
###############################################################################

###############################################################################
# request number: 10
# resource type: 

url = 'https://www.python.org/static/js/libs/html-includes.js'
headers = {
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'sec-fetch-dest': 'script',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    ':path': '/static/js/libs/html-includes.js',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - cache-control: max-age=604800, public
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - last-modified: Mon, 23 Nov 2020 16:47:16 GMT
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - accept-ranges: bytes
#   - etag: "5fbbe794-b2"
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: application/javascript
#   - age: 365590
#   - x-served-by: cache-bwi5134-BWI, cache-mrs10551-MRS
#   - x-cache-hits: 1, 5
#   - content-encoding: gzip
#   - content-length: 143
#   - x-timer: S1606564280.825064,VS0,VE0
###############################################################################

###############################################################################
# request number: 11
# resource type: 

url = 'https://www.python.org/static/js/main-min.d5f95c9c5614.js'
headers = {
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'sec-fetch-dest': 'script',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    ':path': '/static/js/main-min.d5f95c9c5614.js',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-cache-hits: 3, 5
#   - vary: Accept-Encoding
#   - cache-control: max-age=604800, public
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - accept-ranges: bytes
#   - x-served-by: cache-bwi5127-BWI, cache-mrs10551-MRS
#   - server: nginx
#   - last-modified: Mon, 23 Nov 2020 16:47:21 GMT
#   - age: 401692
#   - x-timer: S1606564280.832049,VS0,VE0
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-type: application/javascript
#   - etag: "5fbbe799-65aa"
#   - content-encoding: gzip
#   - content-length: 8113
###############################################################################

###############################################################################
# request number: 12
# resource type: 

url = 'https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js'
headers = {
    ':path': '/ajax/libs/jquery/1.8.2/jquery.min.js',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'accept': 'application/signed-exchange;v=b3;q=0.9,*/*;q=0.8',
    'purpose': 'prefetch',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':authority': 'ajax.googleapis.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - age: 54016
#   - vary: Accept-Encoding
#   - expires: Sat, 27 Nov 2021 20:51:03 GMT
#   - server: sffe
#   - x-content-type-options: nosniff
#   - date: Fri, 27 Nov 2020 20:51:03 GMT
#   - accept-ranges: bytes
#   - access-control-allow-origin: *
#   - cross-origin-resource-policy: cross-origin
#   - cache-control: public, max-age=31536000, stale-while-revalidate=2592000
#   - alt-svc: h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
#   - timing-allow-origin: *
#   - content-length: 33621
#   - x-xss-protection: 0
#   - last-modified: Tue, 03 Mar 2020 19:15:00 GMT
#   - content-encoding: gzip
#   - content-type: text/javascript; charset=UTF-8
###############################################################################

###############################################################################
# request number: 13
# resource type: 

url = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js'
headers = {
    ':path': '/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'accept': 'application/signed-exchange;v=b3;q=0.9,*/*;q=0.8',
    'purpose': 'prefetch',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':authority': 'ajax.googleapis.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - date: Wed, 25 Nov 2020 16:48:53 GMT
#   - content-length: 67948
#   - server: sffe
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - access-control-allow-origin: *
#   - cross-origin-resource-policy: cross-origin
#   - cache-control: public, max-age=31536000, stale-while-revalidate=2592000
#   - alt-svc: h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
#   - timing-allow-origin: *
#   - age: 241346
#   - last-modified: Tue, 03 Mar 2020 19:15:00 GMT
#   - x-xss-protection: 0
#   - expires: Thu, 25 Nov 2021 16:48:53 GMT
#   - content-encoding: gzip
#   - content-type: text/javascript; charset=UTF-8
###############################################################################

###############################################################################
# request number: 14
# resource type: 

url = 'https://ssl.google-analytics.com/ga.js'
headers = {
    'Referer': 'https://www.python.org/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - Access-Control-Allow-Origin: *
#   - Content-Type: application/javascript
###############################################################################

###############################################################################
# request number: 15
# resource type: 

url = 'https://www.python.org/static/img/python-logo-large.c36dccadd999.png'
headers = {
    'sec-fetch-site': 'same-origin',
    'sec-fetch-dest': 'image',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.python.org/static/stylesheets/mq.eef77a5d2257.css',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    ':path': '/static/img/python-logo-large.c36dccadd999.png?1576869008',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
params = [
    ('1576869008', ''),
]
rc = s.get(url, headers=headers, params=params)


# response status code: 200
# response headers:
#   - cache-control: max-age=604800, public
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - last-modified: Wed, 25 Nov 2020 14:36:19 GMT
#   - x-served-by: cache-bwi5150-BWI, cache-mrs10551-MRS
#   - content-type: image/png
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - accept-ranges: bytes
#   - x-cache: HIT, HIT
#   - x-timer: S1606564280.892588,VS0,VE0
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - age: 185078
#   - content-length: 13093
#   - etag: "5fbe6be3-3325"
#   - x-cache-hits: 1, 2
###############################################################################

###############################################################################
# request number: 16
# resource type: 

url = 'https://www.python.org/static/fonts/SourceSansPro-Regular-webfont.fd0d51605201.woff'
headers = {
    ':path': '/static/fonts/SourceSansPro-Regular-webfont.fd0d51605201.woff',
    'origin': 'https://www.python.org',
    'sec-fetch-dest': 'font',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.python.org/static/stylesheets/style.b50cef9e3bb9.css',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-timer: S1606564280.905585,VS0,VE0
#   - cache-control: max-age=604800, public
#   - content-type: font/woff
#   - last-modified: Wed, 25 Nov 2020 14:36:19 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - accept-ranges: bytes
#   - x-cache-hits: 2, 4
#   - content-length: 26392
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - age: 194373
#   - x-served-by: cache-bwi5121-BWI, cache-mrs10551-MRS
#   - etag: "5fbe6be3-6718"
###############################################################################

###############################################################################
# request number: 17
# resource type: 

url = 'https://www.python.org/static/fonts/FluxRegular.f5549a4fe75f.woff'
headers = {
    'origin': 'https://www.python.org',
    'sec-fetch-dest': 'font',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.python.org/static/stylesheets/style.b50cef9e3bb9.css',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    ':path': '/static/fonts/FluxRegular.f5549a4fe75f.woff',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-cache-hits: 1, 4
#   - cache-control: max-age=604800, public
#   - content-type: font/woff
#   - last-modified: Wed, 25 Nov 2020 14:36:19 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - accept-ranges: bytes
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-timer: S1606564280.907535,VS0,VE0
#   - etag: "5fbe6be3-7528"
#   - x-served-by: cache-bwi5132-BWI, cache-mrs10551-MRS
#   - content-length: 29992
#   - age: 101362
###############################################################################

###############################################################################
# request number: 18
# resource type: 

url = 'https://www.python.org/static/fonts/SourceSansPro-Bold-webfont.be855452e565.woff'
headers = {
    'origin': 'https://www.python.org',
    'sec-fetch-dest': 'font',
    'accept': '*/*',
    ':method': 'GET',
    ':path': '/static/fonts/SourceSansPro-Bold-webfont.be855452e565.woff',
    'accept-encoding': 'gzip, deflate, br',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.python.org/static/stylesheets/style.b50cef9e3bb9.css',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - age: 363410
#   - x-cache-hits: 1, 4
#   - cache-control: max-age=604800, public
#   - content-type: font/woff
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - accept-ranges: bytes
#   - x-served-by: cache-bwi5122-BWI, cache-mrs10551-MRS
#   - last-modified: Mon, 23 Nov 2020 16:47:20 GMT
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-timer: S1606564280.907765,VS0,VE0
#   - etag: "5fbbe798-6690"
#   - content-length: 26256
###############################################################################

###############################################################################
# request number: 19
# resource type: 

url = 'https://www.python.org/static/fonts/SourceSansPro-It-webfont.1aa29ac0f190.woff'
headers = {
    'origin': 'https://www.python.org',
    'sec-fetch-dest': 'font',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.python.org/static/stylesheets/style.b50cef9e3bb9.css',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    ':path': '/static/fonts/SourceSansPro-It-webfont.1aa29ac0f190.woff',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-cache-hits: 1, 4
#   - cache-control: max-age=604800, public
#   - content-type: font/woff
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-cache: HIT, HIT
#   - age: 356684
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - accept-ranges: bytes
#   - etag: "5fbbe798-6d3c"
#   - x-timer: S1606564280.907989,VS0,VE0
#   - last-modified: Mon, 23 Nov 2020 16:47:20 GMT
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-length: 27964
#   - x-served-by: cache-bwi5139-BWI, cache-mrs10551-MRS
###############################################################################

###############################################################################
# request number: 20
# resource type: 

url = 'https://www.python.org/static/fonts/FluxBold.3fd71a747d5c.woff'
headers = {
    'origin': 'https://www.python.org',
    'sec-fetch-dest': 'font',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.python.org/static/stylesheets/style.b50cef9e3bb9.css',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    ':path': '/static/fonts/FluxBold.3fd71a747d5c.woff',
    'sec-fetch-mode': 'cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - age: 53961
#   - cache-control: max-age=604800, public
#   - content-type: font/woff
#   - last-modified: Wed, 25 Nov 2020 14:36:19 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-served-by: cache-bwi5138-BWI, cache-mrs10551-MRS
#   - date: Sat, 28 Nov 2020 11:51:19 GMT
#   - accept-ranges: bytes
#   - x-cache: HIT, HIT
#   - x-timer: S1606564280.911318,VS0,VE0
#   - content-length: 29105
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - etag: "5fbe6be3-71b1"
#   - x-cache-hits: 1, 5
###############################################################################

###############################################################################
# request number: 21
# resource type: 

url = 'https://www.python.org/authenticated'
headers = {
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html, */*; q=0.01',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    ':path': '/authenticated',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-served-by: cache-bwi5142-BWI, cache-mrs10551-MRS
#   - x-cache: MISS, HIT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - content-type: text/html; charset=utf-8
#   - age: 1051
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - x-cache-hits: 0, 2
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-length: 580
#   - vary: Cookie
#   - x-timer: S1606564280.170263,VS0,VE0
###############################################################################

###############################################################################
# request number: 22
# resource type: 

url = 'https://console.python.org/python-dot-org-live-consoles-status'
headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'Origin': 'https://www.python.org',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.python.org/',
    'Accept': '*/*',
    'Cache-Control': 'no-cache',
    'Host': 'console.python.org',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - Accept-Ranges: bytes
#   - Content-Length: 17
#   - Access-Control-Allow-Origin: *
#   - Server: PythonAnywhere
#   - Last-Modified: Sat, 21 Nov 2020 02:15:33 GMT
#   - Strict-Transport-Security: max-age=315360000; includeSubDomains; preload
#   - Date: Sat, 28 Nov 2020 11:51:20 GMT
#   - X-Clacks-Overhead: GNU Terry Pratchett
#   - Content-Type: application/json
#   - ETag: "5fb87845-11"
###############################################################################

###############################################################################
# request number: 23
# resource type: 

url = 'https://2p66nmmycsj3.statuspage.io/api/v2/status.json'
headers = {
    'origin': 'https://www.python.org',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': '2p66nmmycsj3.statuspage.io',
    'referer': 'https://www.python.org/',
    ':path': '/api/v2/status.json',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - x-permitted-cross-domain-policies: none
#   - accept-ranges: bytes
#   - referrer-policy: strict-origin-when-cross-origin
#   - strict-transport-security: max-age=259200
#   - x-statuspage-skip-logging: true
#   - x-cache: HIT
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - age: 697
#   - x-statuspage-version: 47018e27126c51e788aa9b18f5b333e9011b979b
#   - etag: W/"190e96564a38a17b670f76ea3b77af44"
#   - x-runtime: 0.294062
#   - content-length: 227
#   - x-xss-protection: 1; mode=block
#   - x-content-type-options: nosniff
#   - x-request-id: efa1dbc3-2d7b-4e02-8fee-6d6f8347e219
#   - vary: Accept,Accept-Encoding,X-Forwarded-Host,X-Forwarded-Scheme,X-Forwarded-Proto,Fastly-SSL
#   - content-type: application/json; charset=utf-8
#   - cache-control: max-age=0, private, must-revalidate
#   - x-download-options: noopen
#   - access-control-allow-origin: *
###############################################################################

###############################################################################
# request number: 24
# resource type: 

url = 'https://www.python.org/box/supernav-python-about/'
headers = {
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html, */*; q=0.01',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':path': '/box/supernav-python-about/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-mode': 'cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - content-length: 441
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-timer: S1606564280.297554,VS0,VE0
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - content-type: text/html; charset=utf-8
#   - x-cache: HIT, HIT
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-served-by: cache-bwi5121-BWI, cache-mrs10551-MRS
#   - age: 1231
#   - x-cache-hits: 1, 2
###############################################################################

###############################################################################
# request number: 25
# resource type: 

url = 'https://www.python.org/box/supernav-python-downloads/'
headers = {
    ':path': '/box/supernav-python-downloads/',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html, */*; q=0.01',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - content-type: text/html; charset=utf-8
#   - x-served-by: cache-bwi5130-BWI, cache-mrs10551-MRS
#   - x-cache: HIT, HIT
#   - content-length: 1902
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - x-timer: S1606564280.303022,VS0,VE0
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - age: 1231
#   - x-cache-hits: 1, 2
###############################################################################

###############################################################################
# request number: 26
# resource type: 

url = 'https://www.python.org/box/supernav-python-documentation/'
headers = {
    ':path': '/box/supernav-python-documentation/',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html, */*; q=0.01',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-timer: S1606564280.310042,VS0,VE0
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - content-type: text/html; charset=utf-8
#   - x-cache: HIT, HIT
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - x-served-by: cache-bwi5129-BWI, cache-mrs10551-MRS
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - content-length: 576
#   - x-cache-hits: 2, 2
#   - age: 1231
###############################################################################

###############################################################################
# request number: 27
# resource type: 

url = 'https://www.python.org/box/supernav-python-community/'
headers = {
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':path': '/box/supernav-python-community/',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'accept': 'text/html, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - content-type: text/html; charset=utf-8
#   - x-cache: HIT, HIT
#   - content-length: 1016
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - x-cache-hits: 4, 2
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-timer: S1606564280.319321,VS0,VE0
#   - x-served-by: cache-bwi5132-BWI, cache-mrs10551-MRS
#   - age: 1231
###############################################################################

###############################################################################
# request number: 28
# resource type: 

url = 'https://www.python.org/box/supernav-python-success-stories/'
headers = {
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html, */*; q=0.01',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    ':path': '/box/supernav-python-success-stories/',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - content-type: text/html; charset=utf-8
#   - x-cache: HIT, HIT
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-timer: S1606564280.319303,VS0,VE0
#   - x-cache-hits: 2, 2
#   - content-length: 520
#   - x-served-by: cache-bwi5121-BWI, cache-mrs10551-MRS
#   - age: 1231
###############################################################################

###############################################################################
# request number: 29
# resource type: 

url = 'https://www.python.org/box/supernav-python-blog/'
headers = {
    ':path': '/box/supernav-python-blog/',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html, */*; q=0.01',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - content-type: text/html; charset=utf-8
#   - x-cache: HIT, HIT
#   - content-length: 704
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - server: nginx
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-served-by: cache-bwi5136-BWI, cache-mrs10551-MRS
#   - x-timer: S1606564280.325263,VS0,VE0
#   - x-cache-hits: 2, 2
#   - age: 1231
###############################################################################

###############################################################################
# request number: 30
# resource type: 

url = 'https://www.python.org/box/supernav-python-events/'
headers = {
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html, */*; q=0.01',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    ':path': '/box/supernav-python-events/',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - content-type: text/html; charset=utf-8
#   - x-cache: HIT, HIT
#   - accept-ranges: bytes
#   - x-frame-options: DENY
#   - content-length: 96
#   - server: nginx
#   - x-cache-hits: 3, 2
#   - x-timer: S1606564280.331063,VS0,VE0
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - x-served-by: cache-bwi5121-BWI, cache-mrs10551-MRS
#   - age: 1231
###############################################################################

###############################################################################
# request number: 31
# resource type: 

url = 'https://www.python.org/static/favicon.ico'
headers = {
    'sec-fetch-dest': 'image',
    ':path': '/static/favicon.ico',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':authority': 'www.python.org',
    ':scheme': 'https',
    'cache-control': 'no-cache',
    'referer': 'https://www.python.org/',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 11:51:20 GMT
#   - x-timer: S1606564280.391581,VS0,VE0
#   - cache-control: max-age=604800, public
#   - via: 1.1 vegur, 1.1 varnish, 1.1 varnish
#   - x-served-by: cache-bwi5138-BWI, cache-mrs10551-MRS
#   - x-cache: HIT, HIT
#   - x-cache-hits: 2, 4
#   - accept-ranges: bytes
#   - server: nginx
#   - age: 184762
#   - strict-transport-security: max-age=63072000; includeSubDomains
#   - etag: "5fbe6bde-3aee"
#   - last-modified: Wed, 25 Nov 2020 14:36:14 GMT
#   - content-type: image/x-icon
#   - content-length: 15086
###############################################################################

