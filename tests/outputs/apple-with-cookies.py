import requests


s = requests.Session()

###############################################################################
# request number: 1
# resource type: document

url = 'https://apple.com/'
headers = {
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
    'Host': 'apple.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Mode': 'navigate',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Cache-Control': 'no-cache',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'dslang': 'US-EN',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'geo': 'IT',
    'pxro': '1',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 301
# response headers:
#   - Content-Language: en
#   - Via: http/1.1 defra1-edge-bx-003.ts.apple.com (ApacheTrafficServer/8.1.1)
#   - Server: ATS/8.1.1
#   - Location: https://www.apple.com/
#   - CDNUUID: 194cf49c-5bcc-4185-a602-8ab72f3a642b-5663017458
#   - Content-Type: text/html
#   - Content-Length: 304
#   - Connection: keep-alive
#   - Date: Sat, 28 Nov 2020 21:11:54 GMT
#   - Cache-Control: no-store
#   - X-Cache: none
###############################################################################

###############################################################################
# request number: 2
# resource type: document

url = 'https://www.apple.com/'
headers = {
    'sec-fetch-mode': 'navigate',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'document',
    'pragma': 'no-cache',
    'sec-fetch-site': 'none',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    ':path': '/',
    'upgrade-insecure-requests': '1',
    ':method': 'GET',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'dslang': 'US-EN',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'geo': 'IT',
    'pxro': '1',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-length: 10565
#   - expires: Sat, 28 Nov 2020 21:11:54 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - cache-control: max-age=0
#   - server: Apache
#   - x-content-type-options: nosniff
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: SAMEORIGIN
#   - date: Sat, 28 Nov 2020 21:11:54 GMT
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - content-type: text/html; charset=UTF-8
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
    ('mboxRid', '77bb80a668674b2dab55b60033af89ec'),
    ('mboxURL', 'https%3A%2F%2Fwww.apple.com%2F'),
    ('mboxSession', 'ff127cfbd7014007ac85875fb7ad03d4'),
    ('devicePixelRatio', '1'),
    ('mboxTime', '1606601515689'),
    ('browserHeight', '618'),
    ('mboxHost', 'www.apple.com'),
    ('screenWidth', '1920'),
    ('mboxCount', '1'),
    ('mboxReferrer', ''),
    ('browserTimeOffset', '60'),
    ('colorDepth', '24'),
    ('mboxPC', ''),
    ('mboxVersion', '1.5.0'),
    ('screenHeight', '1080'),
    ('mbox', 'target-global-mbox'),
    ('screenOrientation', 'landscape'),
    ('browserWidth', '1597'),
    ('webGLRenderer', 'Intel%20HD%20Graphics%205000%20OpenGL%20Engine'),
    ('mboxPage', '2146d9fa80fa42c288f19c35d931b005'),
]
rc = s.get(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 4
# resource type: xhr

url = 'https://www.apple.com/us/shop/bag/status'
headers = {
    ':path': '/us/shop/bag/status?apikey=SFX9YPYY9PPXCU9KH',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'referer': 'https://www.apple.com/',
    'sec-fetch-mode': 'cors',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'dslang': 'US-EN',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'geo': 'IT',
    'pxro': '1',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
}
params = [
    ('apikey', 'SFX9YPYY9PPXCU9KH'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - expires: Sat, 28 Nov 2020 21:11:56 GMT
#   - last-modified: Sat, 28 Nov 2020 21:11:56 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 21:11:56 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 21:11:56 GMT; Max-Age=315360000; Secure; HttpOnly
#   - cache-control: private, no-cache, no-store, must-revalidate
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - x-frame-options: DENY
#   - content-type: application/json;charset=utf-8
#   - x-shred: 28462e6dab51aaac73666900b75a9741
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 21:41:56 GMT; Max-Age=1800; Secure
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-request-id: 89719b1c-c3d6-4414-96e0-71e13a564768
#   - pragma: no-cache
#   - content-length: 137
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 5
# resource type: xhr

url = 'https://www.apple.com/ac/localeswitcher/3/it_IT/content/localeswitcher.json'
headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'referer': 'https://www.apple.com/',
    'sec-fetch-mode': 'cors',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    ':path': '/ac/localeswitcher/3/it_IT/content/localeswitcher.json',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'dslang': 'US-EN',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'geo': 'IT',
    'pxro': '1',
    'as_dc': 'nc',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - accept-ranges: bytes
#   - last-modified: Fri, 08 May 2020 00:10:56 GMT
#   - content-type: application/json
#   - server: Apache
#   - x-content-type-options: nosniff
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - content-length: 390
#   - expires: Sat, 28 Nov 2020 21:20:24 GMT
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - cache-control: max-age=508
###############################################################################

###############################################################################
# request number: 6
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'referer': 'https://www.apple.com/',
    'sec-fetch-mode': 'cors',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'check': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'dslang': 'US-EN',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'geo': 'IT',
    'pxro': '1',
    'as_dc': 'nc',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
}
params = [
    ('locale', 'en_US'),
    ('src', 'globalnav'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - cache-control: max-age=67
#   - content-type: application/json
#   - content-length: 579
#   - x-content-type-options: nosniff
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 21:13:03 GMT
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: SAMEORIGIN
#   - strict-transport-security: max-age=31536000; includeSubdomains
###############################################################################

###############################################################################
# request number: 7
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    ':path': '/favicon.ico',
    'sec-fetch-mode': 'no-cors',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-site': 'same-origin',
    'referer': 'https://www.apple.com/',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'sec-fetch-dest': 'image',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'check': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'dslang': 'US-EN',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'geo': 'IT',
    'pxro': '1',
    'as_dc': 'nc',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 21:14:32 GMT
#   - content-type: image/x-icon
#   - date: Sat, 28 Nov 2020 21:11:58 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - accept-ranges: bytes
#   - server: Apache
#   - x-content-type-options: nosniff
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - cache-control: max-age=154
#   - content-length: 22382
###############################################################################

