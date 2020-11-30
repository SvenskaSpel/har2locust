import requests


s = requests.Session()

###############################################################################
# request number: 1
# resource type: document

url = 'https://apple.com/'
headers = {
    'Upgrade-Insecure-Requests': '1',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Host': 'apple.com',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Pragma': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'Cache-Control': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
}
cookies = {
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'geo': 'IT',
    'dssf': '1',
    'dslang': 'US-EN',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'check': 'true',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'pxro': '1',
    'as_xs': 'flc=&idmsl=1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'site': 'USA',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 301
# response headers:
#   - CDNUUID: 194cf49c-5bcc-4185-a602-8ab72f3a642b-5663017458
#   - Content-Language: en
#   - Location: https://www.apple.com/
#   - Cache-Control: no-store
#   - Via: http/1.1 defra1-edge-bx-003.ts.apple.com (ApacheTrafficServer/8.1.1)
#   - Content-Length: 304
#   - Server: ATS/8.1.1
#   - Connection: keep-alive
#   - Date: Sat, 28 Nov 2020 21:11:54 GMT
#   - Content-Type: text/html
#   - X-Cache: none
###############################################################################

###############################################################################
# request number: 2
# resource type: document

url = 'https://www.apple.com/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'navigate',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    ':authority': 'www.apple.com',
    ':method': 'GET',
    'sec-fetch-dest': 'document',
    'upgrade-insecure-requests': '1',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'none',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    ':path': '/',
    'sec-fetch-user': '?1',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    'pragma': 'no-cache',
}
cookies = {
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'geo': 'IT',
    'dssf': '1',
    'dslang': 'US-EN',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'check': 'true',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'pxro': '1',
    'as_xs': 'flc=&idmsl=1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'site': 'USA',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - x-frame-options: SAMEORIGIN
#   - x-content-type-options: nosniff
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - date: Sat, 28 Nov 2020 21:11:54 GMT
#   - content-length: 10565
#   - x-xss-protection: 1; mode=block
#   - vary: Accept-Encoding
#   - expires: Sat, 28 Nov 2020 21:11:54 GMT
#   - cache-control: max-age=0
#   - content-type: text/html; charset=UTF-8
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 3
# resource type: xhr

url = 'https://securemvt.apple.com/m2/apple/mbox/json'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Referer': 'https://www.apple.com/',
}
params = [
    ('mbox', 'target-global-mbox'),
    ('browserHeight', '618'),
    ('mboxTime', '1606601515689'),
    ('devicePixelRatio', '1'),
    ('browserWidth', '1597'),
    ('mboxVersion', '1.5.0'),
    ('mboxPC', ''),
    ('colorDepth', '24'),
    ('mboxPage', '2146d9fa80fa42c288f19c35d931b005'),
    ('screenWidth', '1920'),
    ('mboxHost', 'www.apple.com'),
    ('mboxSession', 'ff127cfbd7014007ac85875fb7ad03d4'),
    ('screenOrientation', 'landscape'),
    ('mboxURL', 'https%3A%2F%2Fwww.apple.com%2F'),
    ('mboxReferrer', ''),
    ('webGLRenderer', 'Intel%20HD%20Graphics%205000%20OpenGL%20Engine'),
    ('screenHeight', '1080'),
    ('mboxRid', '77bb80a668674b2dab55b60033af89ec'),
    ('browserTimeOffset', '60'),
    ('mboxCount', '1'),
]
rc = s.get(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 4
# resource type: xhr

url = 'https://www.apple.com/us/shop/bag/status'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    ':path': '/us/shop/bag/status?apikey=SFX9YPYY9PPXCU9KH',
    'pragma': 'no-cache',
    'accept': '*/*',
    ':authority': 'www.apple.com',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    ':method': 'GET',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.apple.com/',
}
cookies = {
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'geo': 'IT',
    'dssf': '1',
    'dslang': 'US-EN',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'check': 'true',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'pxro': '1',
    'as_xs': 'flc=&idmsl=1',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'site': 'USA',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
}
params = [
    ('apikey', 'SFX9YPYY9PPXCU9KH'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-request-id: 89719b1c-c3d6-4414-96e0-71e13a564768
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - x-xss-protection: 1; mode=block
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - last-modified: Sat, 28 Nov 2020 21:11:56 GMT
#   - content-security-policy: frame-ancestors 'none'
#   - content-length: 137
#   - x-shred: 28462e6dab51aaac73666900b75a9741
#   - content-type: application/json;charset=utf-8
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 21:41:56 GMT; Max-Age=1800; Secure
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 21:11:56 GMT; Max-Age=315360000; Secure; HttpOnly
#   - cache-control: private, no-cache, no-store, must-revalidate
#   - server: Apple
#   - expires: Sat, 28 Nov 2020 21:11:56 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - pragma: no-cache
#   - x-frame-options: DENY
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 21:11:56 GMT; Max-Age=315360000; Secure; HttpOnly
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
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'pragma': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc',
    ':path': '/ac/localeswitcher/3/it_IT/content/localeswitcher.json',
    'accept': '*/*',
    ':authority': 'www.apple.com',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    ':method': 'GET',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.apple.com/',
}
cookies = {
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'geo': 'IT',
    'dssf': '1',
    'dslang': 'US-EN',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'check': 'true',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'pxro': '1',
    'as_xs': 'flc=&idmsl=1',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'site': 'USA',
    'as_dc': 'nc',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 21:20:24 GMT
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - last-modified: Fri, 08 May 2020 00:10:56 GMT
#   - content-length: 390
#   - x-content-type-options: nosniff
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: application/json
#   - accept-ranges: bytes
#   - vary: Accept-Encoding
#   - cache-control: max-age=508
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 6
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'pragma': 'no-cache',
    'accept': '*/*',
    ':authority': 'www.apple.com',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    ':scheme': 'https',
    ':method': 'GET',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.apple.com/',
}
cookies = {
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'geo': 'IT',
    'dssf': '1',
    'dslang': 'US-EN',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'check': 'true',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'pxro': '1',
    'as_xs': 'flc=&idmsl=1',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'site': 'USA',
    'as_dc': 'nc',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
}
params = [
    ('src', 'globalnav'),
    ('locale', 'en_US'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubdomains
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - cache-control: max-age=67
#   - x-frame-options: SAMEORIGIN
#   - expires: Sat, 28 Nov 2020 21:13:03 GMT
#   - x-content-type-options: nosniff
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-type: application/json
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: DENY
#   - content-length: 579
###############################################################################

###############################################################################
# request number: 7
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    ':path': '/favicon.ico',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'image',
    ':authority': 'www.apple.com',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    ':scheme': 'https',
    ':method': 'GET',
    'sec-fetch-mode': 'no-cors',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.apple.com/',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
}
cookies = {
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'geo': 'IT',
    'dssf': '1',
    'dslang': 'US-EN',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'check': 'true',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'pxro': '1',
    'as_xs': 'flc=&idmsl=1',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'site': 'USA',
    'as_dc': 'nc',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-type: image/x-icon
#   - date: Sat, 28 Nov 2020 21:11:58 GMT
#   - x-content-type-options: nosniff
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - cache-control: max-age=154
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 21:14:32 GMT
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - content-length: 22382
###############################################################################

