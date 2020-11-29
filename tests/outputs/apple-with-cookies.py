import requests


s = requests.Session()

###############################################################################
# request number: 1
# resource type: document

url = 'https://apple.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Connection': 'keep-alive',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'dslang': 'US-EN',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'site': 'USA',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 301
# response headers:
#   - Cache-Control: no-store
#   - Via: http/1.1 defra1-edge-bx-003.ts.apple.com (ApacheTrafficServer/8.1.1)
#   - CDNUUID: 194cf49c-5bcc-4185-a602-8ab72f3a642b-5663017458
#   - Connection: keep-alive
#   - Content-Length: 304
#   - Server: ATS/8.1.1
#   - Date: Sat, 28 Nov 2020 21:11:54 GMT
#   - Content-Language: en
#   - Location: https://www.apple.com/
#   - X-Cache: none
#   - Content-Type: text/html
###############################################################################

###############################################################################
# request number: 2
# resource type: document

url = 'https://www.apple.com/'
headers = {
    'upgrade-insecure-requests': '1',
    'sec-fetch-mode': 'navigate',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-user': '?1',
    ':path': '/',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cache-control': 'no-cache',
    'sec-fetch-site': 'none',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'document',
    ':scheme': 'https',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    ':method': 'GET',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'dslang': 'US-EN',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'as_xs': 'flc=&idmsl=1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'site': 'USA',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 21:11:54 GMT
#   - content-length: 10565
#   - server: Apache
#   - x-xss-protection: 1; mode=block
#   - content-type: text/html; charset=UTF-8
#   - x-content-type-options: nosniff
#   - cache-control: max-age=0
#   - x-frame-options: SAMEORIGIN
#   - vary: Accept-Encoding
#   - expires: Sat, 28 Nov 2020 21:11:54 GMT
#   - content-encoding: gzip
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 3
# resource type: xhr

url = 'https://securemvt.apple.com/m2/apple/mbox/json'
headers = {
    'Referer': 'https://www.apple.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
params = [
    ('mboxCount', '1'),
    ('devicePixelRatio', '1'),
    ('webGLRenderer', 'Intel%20HD%20Graphics%205000%20OpenGL%20Engine'),
    ('mboxPage', '2146d9fa80fa42c288f19c35d931b005'),
    ('mboxURL', 'https%3A%2F%2Fwww.apple.com%2F'),
    ('browserTimeOffset', '60'),
    ('screenOrientation', 'landscape'),
    ('mboxReferrer', ''),
    ('mboxHost', 'www.apple.com'),
    ('mboxTime', '1606601515689'),
    ('mboxRid', '77bb80a668674b2dab55b60033af89ec'),
    ('screenWidth', '1920'),
    ('browserHeight', '618'),
    ('mboxSession', 'ff127cfbd7014007ac85875fb7ad03d4'),
    ('colorDepth', '24'),
    ('mboxPC', ''),
    ('screenHeight', '1080'),
    ('mboxVersion', '1.5.0'),
    ('mbox', 'target-global-mbox'),
    ('browserWidth', '1597'),
]
rc = s.get(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 4
# resource type: xhr

url = 'https://www.apple.com/us/shop/bag/status'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':path': '/us/shop/bag/status?apikey=SFX9YPYY9PPXCU9KH',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'sec-fetch-mode': 'cors',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'dslang': 'US-EN',
    'check': 'true',
    'geo': 'IT',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'site': 'USA',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('apikey', 'SFX9YPYY9PPXCU9KH'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - expires: Sat, 28 Nov 2020 21:11:56 GMT
#   - x-shred: 28462e6dab51aaac73666900b75a9741
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-length: 137
#   - last-modified: Sat, 28 Nov 2020 21:11:56 GMT
#   - pragma: no-cache
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 21:11:56 GMT; Max-Age=315360000; Secure; HttpOnly
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 21:41:56 GMT; Max-Age=1800; Secure
#   - server: Apple
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - cache-control: private, no-cache, no-store, must-revalidate
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 21:11:56 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - x-request-id: 89719b1c-c3d6-4414-96e0-71e13a564768
#   - content-type: application/json;charset=utf-8
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 5
# resource type: xhr

url = 'https://www.apple.com/ac/localeswitcher/3/it_IT/content/localeswitcher.json'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    ':path': '/ac/localeswitcher/3/it_IT/content/localeswitcher.json',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'dslang': 'US-EN',
    'check': 'true',
    'geo': 'IT',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'site': 'USA',
    'as_dc': 'nc',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - last-modified: Fri, 08 May 2020 00:10:56 GMT
#   - server: Apache
#   - content-length: 390
#   - x-content-type-options: nosniff
#   - cache-control: max-age=508
#   - accept-ranges: bytes
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - expires: Sat, 28 Nov 2020 21:20:24 GMT
#   - vary: Accept-Encoding
#   - content-type: application/json
#   - content-encoding: gzip
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 6
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'sec-fetch-dest': 'empty',
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'dslang': 'US-EN',
    'check': 'true',
    'geo': 'IT',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'site': 'USA',
    'as_dc': 'nc',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('locale', 'en_US'),
    ('src', 'globalnav'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=31536000; includeSubdomains
#   - x-xss-protection: 1; mode=block
#   - expires: Sat, 28 Nov 2020 21:13:03 GMT
#   - x-content-type-options: nosniff
#   - server: Apple
#   - x-frame-options: SAMEORIGIN
#   - x-frame-options: DENY
#   - content-length: 579
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - cache-control: max-age=67
#   - content-type: application/json
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 7
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-dest': 'image',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':path': '/favicon.ico',
    'sec-fetch-mode': 'no-cors',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'dslang': 'US-EN',
    'check': 'true',
    'geo': 'IT',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'site': 'USA',
    'as_dc': 'nc',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - cache-control: max-age=154
#   - content-type: image/x-icon
#   - server: Apache
#   - x-content-type-options: nosniff
#   - content-length: 22382
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 21:14:32 GMT
#   - date: Sat, 28 Nov 2020 21:11:58 GMT
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

