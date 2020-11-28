import requests


s = requests.Session()
s.headers = {
}

###############################################################################
# request number: 1
# resource type: 

url = 'https://apple.com/'
headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-User': '?1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Mode': 'navigate',
    'Host': 'apple.com',
    'Cache-Control': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'Connection': 'keep-alive',
    'Sec-Fetch-Site': 'none',
    'Pragma': 'no-cache',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 301
# response headers:
#   - Content-Language: en
#   - X-Cache: none
#   - Cache-Control: no-store
#   - Date: Sat, 28 Nov 2020 21:11:54 GMT
#   - Via: http/1.1 defra1-edge-bx-003.ts.apple.com (ApacheTrafficServer/8.1.1)
#   - Content-Type: text/html
#   - Content-Length: 304
#   - Connection: keep-alive
#   - CDNUUID: 194cf49c-5bcc-4185-a602-8ab72f3a642b-5663017458
#   - Location: https://www.apple.com/
#   - Server: ATS/8.1.1
###############################################################################

###############################################################################
# request number: 2
# resource type: 

url = 'https://www.apple.com/'
headers = {
    'sec-fetch-mode': 'navigate',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'none',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-dest': 'document',
    'upgrade-insecure-requests': '1',
    ':path': '/',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - x-xss-protection: 1; mode=block
#   - x-content-type-options: nosniff
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - date: Sat, 28 Nov 2020 21:11:54 GMT
#   - expires: Sat, 28 Nov 2020 21:11:54 GMT
#   - cache-control: max-age=0
#   - content-encoding: gzip
#   - x-frame-options: SAMEORIGIN
#   - content-type: text/html; charset=UTF-8
#   - content-length: 10565
###############################################################################

###############################################################################
# request number: 3
# resource type: 

url = 'https://www.apple.com/metrics/target/scripts/1.0/at.js'
headers = {
    ':path': '/metrics/target/scripts/1.0/at.js',
    'referer': 'https://www.apple.com/',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'script',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - nncoection: close
#   - vary: Accept-Encoding
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - x-content-type-options: nosniff
#   - expires: Sat, 28 Nov 2020 21:11:55 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-length: 27731
#   - server: Apache
#   - content-type: application/x-javascript
#   - cache-control: max-age=0
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 4
# resource type: 

url = 'https://www.apple.com/ac/globalnav/6/en_US/styles/ac-globalnav.built.css'
headers = {
    'accept': 'text/css,*/*;q=0.1',
    'referer': 'https://www.apple.com/',
    ':method': 'GET',
    'sec-fetch-dest': 'style',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    ':path': '/ac/globalnav/6/en_US/styles/ac-globalnav.built.css',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - x-content-type-options: nosniff
#   - expires: Sat, 28 Nov 2020 21:11:55 GMT
#   - ntcoent-length: 104975
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: text/css
#   - content-length: 11656
#   - cache-control: max-age=0
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 5
# resource type: 

url = 'https://www.apple.com/ac/localnav/5/styles/ac-localnav.built.css'
headers = {
    'accept': 'text/css,*/*;q=0.1',
    'referer': 'https://www.apple.com/',
    ':method': 'GET',
    'sec-fetch-dest': 'style',
    'accept-encoding': 'gzip, deflate, br',
    ':path': '/ac/localnav/5/styles/ac-localnav.built.css',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - x-content-type-options: nosniff
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: text/css
#   - expires: Sat, 28 Nov 2020 21:12:09 GMT
#   - content-encoding: gzip
#   - cache-control: max-age=14
#   - content-length: 7611
###############################################################################

###############################################################################
# request number: 6
# resource type: 

url = 'https://www.apple.com/ac/globalfooter/6/en_US/styles/ac-globalfooter.built.css'
headers = {
    'accept': 'text/css,*/*;q=0.1',
    'referer': 'https://www.apple.com/',
    ':path': '/ac/globalfooter/6/en_US/styles/ac-globalfooter.built.css',
    ':method': 'GET',
    'sec-fetch-dest': 'style',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - x-content-type-options: nosniff
#   - content-length: 5275
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: text/css
#   - cache-control: max-age=26
#   - content-encoding: gzip
#   - expires: Sat, 28 Nov 2020 21:12:21 GMT
###############################################################################

###############################################################################
# request number: 7
# resource type: 

url = 'https://www.apple.com/wss/fonts'
headers = {
    'accept': 'text/css,*/*;q=0.1',
    'sec-fetch-site': 'same-origin',
    'referer': 'https://www.apple.com/',
    ':method': 'GET',
    'sec-fetch-dest': 'style',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    ':path': '/wss/fonts?families=SF+Pro,v3|SF+Pro+Icons,v3',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
params = [
    ('families', 'SF+Pro,v3|SF+Pro+Icons,v3'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - x-content-type-options: nosniff
#   - expires: Sat, 28 Nov 2020 21:11:55 GMT
#   - content-length: 1179
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-powered-by: PHP/5.3.3
#   - server: Apache
#   - cache-control: max-age=0, no-cache
#   - content-type: text/css
#   - pragma: no-cache
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 8
# resource type: 

url = 'https://www.apple.com/v/home/q/built/styles/main.built.css'
headers = {
    'accept': 'text/css,*/*;q=0.1',
    'referer': 'https://www.apple.com/',
    ':method': 'GET',
    'sec-fetch-dest': 'style',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':path': '/v/home/q/built/styles/main.built.css',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - x-content-type-options: nosniff
#   - expires: Sat, 28 Nov 2020 21:11:55 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: text/css
#   - cneonction: close
#   - cache-control: max-age=0
#   - content-length: 43867
#   - content-encoding: gzip
#   - ntcoent-length: 803878
###############################################################################

###############################################################################
# request number: 9
# resource type: 

url = 'https://www.apple.com/v/home/q/built/scripts/head.built.js'
headers = {
    'referer': 'https://www.apple.com/',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'script',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    ':path': '/v/home/q/built/scripts/head.built.js',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - x-content-type-options: nosniff
#   - expires: Sat, 28 Nov 2020 21:11:55 GMT
#   - content-length: 15546
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: application/x-javascript
#   - cache-control: max-age=0
#   - ntcoent-length: 55001
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 10
# resource type: 

url = 'https://www.apple.com/ac/globalnav/6/en_US/scripts/ac-globalnav.built.js'
headers = {
    'referer': 'https://www.apple.com/',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':path': '/ac/globalnav/6/en_US/scripts/ac-globalnav.built.js',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'script',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - x-content-type-options: nosniff
#   - expires: Sat, 28 Nov 2020 21:11:55 GMT
#   - content-length: 37494
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: application/x-javascript
#   - cache-control: max-age=0
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 11
# resource type: 

url = 'https://www.apple.com/metrics/ac-analytics/2.11.0/scripts/ac-analytics.js'
headers = {
    'referer': 'https://www.apple.com/',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'script',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/metrics/ac-analytics/2.11.0/scripts/ac-analytics.js',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - cache-control: max-age=19
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - x-content-type-options: nosniff
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: application/x-javascript
#   - cneonction: close
#   - content-encoding: gzip
#   - expires: Sat, 28 Nov 2020 21:12:14 GMT
###############################################################################

###############################################################################
# request number: 12
# resource type: 

url = 'https://www.apple.com/ac/globalfooter/6/en_US/scripts/ac-globalfooter.built.js'
headers = {
    ':path': '/ac/globalfooter/6/en_US/scripts/ac-globalfooter.built.js',
    'accept': '*/*',
    'referer': 'https://www.apple.com/',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'script',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - nncoection: close
#   - vary: Accept-Encoding
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - expires: Sat, 28 Nov 2020 21:14:31 GMT
#   - x-content-type-options: nosniff
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - cache-control: max-age=156
#   - server: Apache
#   - content-type: application/x-javascript
#   - content-encoding: gzip
#   - content-length: 3086
###############################################################################

###############################################################################
# request number: 13
# resource type: 

url = 'https://www.apple.com/ac/localeswitcher/3/en_US/scripts/localeswitcher.built.js'
headers = {
    'referer': 'https://www.apple.com/',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'script',
    ':path': '/ac/localeswitcher/3/en_US/scripts/localeswitcher.built.js',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - x-content-type-options: nosniff
#   - expires: Sat, 28 Nov 2020 21:14:37 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: application/x-javascript
#   - cache-control: max-age=162
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 14
# resource type: 

url = 'https://www.apple.com/v/home/q/built/scripts/main.built.js'
headers = {
    ':path': '/v/home/q/built/scripts/main.built.js',
    'referer': 'https://www.apple.com/',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'script',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - x-content-type-options: nosniff
#   - cache-control: max-age=94
#   - expires: Sat, 28 Nov 2020 21:13:29 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: application/x-javascript
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 15
# resource type: 

url = 'https://www.apple.com/ac/ac-films/6.5.0/styles/modal.css'
headers = {
    'accept': 'text/css,*/*;q=0.1',
    'referer': 'https://www.apple.com/',
    ':method': 'GET',
    'sec-fetch-dest': 'style',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    ':path': '/ac/ac-films/6.5.0/styles/modal.css',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - content-encoding: gzip
#   - x-content-type-options: nosniff
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - expires: Sat, 28 Nov 2020 21:14:40 GMT
#   - content-type: text/css
#   - cache-control: max-age=165
#   - content-length: 16169
#   - ntcoent-length: 105272
###############################################################################

###############################################################################
# request number: 16
# resource type: 

url = 'https://www.apple.com/ac/ac-films/6.5.0/scripts/autofilms.built.js'
headers = {
    'referer': 'https://www.apple.com/',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    ':path': '/ac/ac-films/6.5.0/scripts/autofilms.built.js',
    'sec-fetch-dest': 'script',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - nncoection: close
#   - vary: Accept-Encoding
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - x-content-type-options: nosniff
#   - expires: Sat, 28 Nov 2020 21:14:33 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - cache-control: max-age=158
#   - content-type: application/x-javascript
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 17
# resource type: 

url = 'https://www.apple.com/metrics/data-relay/1.1.4/scripts/data-relay.js'
headers = {
    'referer': 'https://www.apple.com/',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'script',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    ':path': '/metrics/data-relay/1.1.4/scripts/data-relay.js',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - nncoection: close
#   - vary: Accept-Encoding
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - content-length: 4955
#   - expires: Sat, 28 Nov 2020 21:14:04 GMT
#   - x-content-type-options: nosniff
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: application/x-javascript
#   - cache-control: max-age=129
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 18
# resource type: 

url = 'https://www.apple.com/metrics/data-relay/1.1.4/scripts/auto-relay.js'
headers = {
    'referer': 'https://www.apple.com/',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'script',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'pragma': 'no-cache',
    'sec-fetch-mode': 'no-cors',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    ':path': '/metrics/data-relay/1.1.4/scripts/auto-relay.js',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'geo': 'IT',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-length: 197
#   - nncoection: close
#   - date: Sat, 28 Nov 2020 21:11:55 GMT
#   - x-content-type-options: nosniff
#   - expires: Sat, 28 Nov 2020 21:11:55 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: application/x-javascript
#   - cache-control: max-age=0
###############################################################################

###############################################################################
# request number: 19
# resource type: 

url = 'https://securemvt.apple.com/m2/apple/mbox/json'
headers = {
    'Referer': 'https://www.apple.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
params = [
    ('colorDepth', '24'),
    ('browserHeight', '618'),
    ('mbox', 'target-global-mbox'),
    ('mboxHost', 'www.apple.com'),
    ('devicePixelRatio', '1'),
    ('mboxTime', '1606601515689'),
    ('mboxReferrer', ''),
    ('mboxCount', '1'),
    ('mboxSession', 'ff127cfbd7014007ac85875fb7ad03d4'),
    ('mboxPC', ''),
    ('mboxVersion', '1.5.0'),
    ('browserTimeOffset', '60'),
    ('mboxRid', '77bb80a668674b2dab55b60033af89ec'),
    ('webGLRenderer', 'Intel%20HD%20Graphics%205000%20OpenGL%20Engine'),
    ('screenOrientation', 'landscape'),
    ('screenHeight', '1080'),
    ('browserWidth', '1597'),
    ('mboxPage', '2146d9fa80fa42c288f19c35d931b005'),
    ('mboxURL', 'https%3A%2F%2Fwww.apple.com%2F'),
    ('screenWidth', '1920'),
]
rc = s.get(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 20
# resource type: 

url = 'https://www.apple.com/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_apple_image__cxwwnrj0urau_large.svg'
headers = {
    'sec-fetch-dest': 'image',
    'referer': 'https://www.apple.com/ac/globalnav/6/en_US/styles/ac-globalnav.built.css',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    'sec-fetch-mode': 'no-cors',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    ':path': '/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_apple_image__cxwwnrj0urau_large.svg',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - cache-control: max-age=299
#   - last-modified: Fri, 08 May 2020 00:14:29 GMT
#   - content-length: 554
#   - accept-ranges: bytes
#   - x-content-type-options: nosniff
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: image/svg+xml
#   - expires: Sat, 28 Nov 2020 21:16:55 GMT
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 21
# resource type: 

url = 'https://www.apple.com/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_links_mac_image__fv4ktb435mum_large.svg'
headers = {
    'sec-fetch-dest': 'image',
    'referer': 'https://www.apple.com/ac/globalnav/6/en_US/styles/ac-globalnav.built.css',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':path': '/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_links_mac_image__fv4ktb435mum_large.svg',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cache-control': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - nncoection: close
#   - last-modified: Fri, 08 May 2020 00:14:29 GMT
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 21:16:29 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - cache-control: max-age=273
#   - content-type: image/svg+xml
#   - content-length: 802
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 22
# resource type: 

url = 'https://www.apple.com/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_links_ipad_image__fefum478f4uq_large.svg'
headers = {
    'sec-fetch-dest': 'image',
    'referer': 'https://www.apple.com/ac/globalnav/6/en_US/styles/ac-globalnav.built.css',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    ':path': '/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_links_ipad_image__fefum478f4uq_large.svg',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - nncoection: close
#   - vary: Accept-Encoding
#   - content-length: 547
#   - content-encoding: gzip
#   - expires: Sat, 28 Nov 2020 21:17:02 GMT
#   - last-modified: Fri, 08 May 2020 00:14:29 GMT
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - content-type: image/svg+xml
#   - cache-control: max-age=306
###############################################################################

###############################################################################
# request number: 23
# resource type: 

url = 'https://www.apple.com/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_links_iphone_image__dhepc4hn14cy_large.svg'
headers = {
    'sec-fetch-dest': 'image',
    'referer': 'https://www.apple.com/ac/globalnav/6/en_US/styles/ac-globalnav.built.css',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    ':path': '/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_links_iphone_image__dhepc4hn14cy_large.svg',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - nncoection: close
#   - vary: Accept-Encoding
#   - content-length: 593
#   - content-encoding: gzip
#   - last-modified: Fri, 08 May 2020 00:14:29 GMT
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 21:18:15 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - cache-control: max-age=379
#   - server: Apache
#   - content-type: image/svg+xml
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 24
# resource type: 

url = 'https://www.apple.com/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_links_watch_image__dfo5u4bhooqe_large.svg'
headers = {
    'sec-fetch-dest': 'image',
    'referer': 'https://www.apple.com/ac/globalnav/6/en_US/styles/ac-globalnav.built.css',
    ':method': 'GET',
    ':path': '/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_links_watch_image__dfo5u4bhooqe_large.svg',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - nncoection: close
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - expires: Sat, 28 Nov 2020 21:17:00 GMT
#   - last-modified: Fri, 08 May 2020 00:14:29 GMT
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - cache-control: max-age=304
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-length: 910
#   - content-type: image/svg+xml
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 25
# resource type: 

url = 'https://www.apple.com/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_links_tv_image__dtzdy60o3imq_large.svg'
headers = {
    ':path': '/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_links_tv_image__dtzdy60o3imq_large.svg',
    'sec-fetch-dest': 'image',
    'referer': 'https://www.apple.com/ac/globalnav/6/en_US/styles/ac-globalnav.built.css',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - nncoection: close
#   - last-modified: Fri, 08 May 2020 00:14:29 GMT
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - content-length: 264
#   - expires: Sat, 28 Nov 2020 21:17:29 GMT
#   - content-type: image/svg+xml
#   - cache-control: max-age=333
###############################################################################

###############################################################################
# request number: 26
# resource type: 

url = 'https://www.apple.com/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_links_music_image__bewxrazzig02_large.svg'
headers = {
    'sec-fetch-dest': 'image',
    'referer': 'https://www.apple.com/ac/globalnav/6/en_US/styles/ac-globalnav.built.css',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_links_music_image__bewxrazzig02_large.svg',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - nncoection: close
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - cache-control: max-age=61
#   - last-modified: Fri, 08 May 2020 00:14:29 GMT
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - content-length: 594
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: image/svg+xml
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - expires: Sat, 28 Nov 2020 21:12:57 GMT
###############################################################################

###############################################################################
# request number: 27
# resource type: 

url = 'https://www.apple.com/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_links_support_image__b24reo1n4fbm_large.svg'
headers = {
    'sec-fetch-dest': 'image',
    'referer': 'https://www.apple.com/ac/globalnav/6/en_US/styles/ac-globalnav.built.css',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    ':path': '/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_links_support_image__b24reo1n4fbm_large.svg',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - nncoection: close
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - last-modified: Fri, 08 May 2020 00:14:29 GMT
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 21:15:37 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-length: 739
#   - cache-control: max-age=221
#   - content-type: image/svg+xml
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 28
# resource type: 

url = 'https://www.apple.com/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_search_image__fca9mfoh8a2q_large.svg'
headers = {
    'sec-fetch-dest': 'image',
    'referer': 'https://www.apple.com/ac/globalnav/6/en_US/styles/ac-globalnav.built.css',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    ':path': '/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_search_image__fca9mfoh8a2q_large.svg',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - last-modified: Fri, 08 May 2020 00:14:29 GMT
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - cache-control: max-age=207
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-length: 707
#   - content-type: image/svg+xml
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - expires: Sat, 28 Nov 2020 21:15:23 GMT
###############################################################################

###############################################################################
# request number: 29
# resource type: 

url = 'https://www.apple.com/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_bag_image__bmix8075eg4i_large.svg'
headers = {
    'sec-fetch-dest': 'image',
    'referer': 'https://www.apple.com/ac/globalnav/6/en_US/styles/ac-globalnav.built.css',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/ac/globalnav/6/en_US/images/be15095f-5a20-57d0-ad14-cf4c638e223a/globalnav_bag_image__bmix8075eg4i_large.svg',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - nncoection: close
#   - expires: Sat, 28 Nov 2020 21:13:26 GMT
#   - last-modified: Fri, 08 May 2020 00:14:29 GMT
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - content-length: 718
#   - cache-control: max-age=90
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: image/svg+xml
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 30
# resource type: 

url = 'https://www.apple.com/wss/fonts/SF-Pro-Text/v3/sf-pro-text_semibold.woff2'
headers = {
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'origin': 'https://www.apple.com',
    'sec-fetch-dest': 'font',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
    'referer': 'https://www.apple.com/wss/fonts?families=SF+Pro,v3|SF+Pro+Icons,v3',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    ':path': '/wss/fonts/SF-Pro-Text/v3/sf-pro-text_semibold.woff2',
    'sec-fetch-mode': 'cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 22:05:34 GMT
#   - cache-control: max-age=3218
#   - x-content-type-options: nosniff
#   - access-control-allow-origin: *
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-powered-by: PHP/5.3.3
#   - server: Apache
#   - content-length: 114264
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - content-type: font/woff2
###############################################################################

###############################################################################
# request number: 31
# resource type: 

url = 'https://www.apple.com/wss/fonts/SF-Pro-Text/v3/sf-pro-text_regular.woff2'
headers = {
    ':path': '/wss/fonts/SF-Pro-Text/v3/sf-pro-text_regular.woff2',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'origin': 'https://www.apple.com',
    'sec-fetch-dest': 'font',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
    'referer': 'https://www.apple.com/wss/fonts?families=SF+Pro,v3|SF+Pro+Icons,v3',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'sec-fetch-mode': 'cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - cache-control: max-age=2327
#   - x-content-type-options: nosniff
#   - access-control-allow-origin: *
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-powered-by: PHP/5.3.3
#   - server: Apache
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - content-length: 99020
#   - expires: Sat, 28 Nov 2020 21:50:43 GMT
#   - content-type: font/woff2
###############################################################################

###############################################################################
# request number: 32
# resource type: 

url = 'https://www.apple.com/us/shop/bag/status'
headers = {
    ':path': '/us/shop/bag/status?apikey=SFX9YPYY9PPXCU9KH',
    'accept': '*/*',
    'referer': 'https://www.apple.com/',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
params = [
    ('apikey', 'SFX9YPYY9PPXCU9KH'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 21:11:56 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-type: application/json;charset=utf-8
#   - cache-control: private, no-cache, no-store, must-revalidate
#   - x-request-id: 89719b1c-c3d6-4414-96e0-71e13a564768
#   - content-language: en-US
#   - x-shred: 28462e6dab51aaac73666900b75a9741
#   - expires: Sat, 28 Nov 2020 21:11:56 GMT
#   - x-frame-options: DENY
#   - server: Apple
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - x-xss-protection: 1; mode=block
#   - x-content-type-options: nosniff
#   - content-length: 137
#   - content-security-policy: frame-ancestors 'none'
#   - last-modified: Sat, 28 Nov 2020 21:11:56 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - pragma: no-cache
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 21:11:56 GMT; Max-Age=315360000; Secure; HttpOnly
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 21:41:56 GMT; Max-Age=1800; Secure
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - dssf: 1
#   - as_dc: nc
###############################################################################

###############################################################################
# request number: 33
# resource type: 

url = 'https://www.apple.com/v/home/q/images/heroes/black-friday-offer/set-a/phone__ulbbo0vgyf6y_large.png'
headers = {
    'sec-fetch-dest': 'image',
    ':path': '/v/home/q/images/heroes/black-friday-offer/set-a/phone__ulbbo0vgyf6y_large.png',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/v/home/q/built/styles/main.built.css',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - x-content-type-options: nosniff
#   - content-type: image/png
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-length: 30019
#   - last-modified: Wed, 25 Nov 2020 21:46:33 GMT
#   - expires: Sat, 28 Nov 2020 21:40:26 GMT
#   - cache-control: max-age=1710
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 34
# resource type: 

url = 'https://www.apple.com/v/home/q/images/heroes/black-friday-offer/set-a/airpods__b0941p5gmwj6_large.png'
headers = {
    'sec-fetch-dest': 'image',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/v/home/q/built/styles/main.built.css',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    ':path': '/v/home/q/images/heroes/black-friday-offer/set-a/airpods__b0941p5gmwj6_large.png',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-length: 51304
#   - x-content-type-options: nosniff
#   - content-type: image/png
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - cache-control: max-age=2499
#   - server: Apache
#   - last-modified: Wed, 25 Nov 2020 21:46:33 GMT
#   - expires: Sat, 28 Nov 2020 21:53:35 GMT
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 35
# resource type: 

url = 'https://www.apple.com/v/home/q/images/heroes/black-friday-offer/set-a/watch__csqqcayzqueu_large.png'
headers = {
    'sec-fetch-dest': 'image',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/v/home/q/built/styles/main.built.css',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    ':path': '/v/home/q/images/heroes/black-friday-offer/set-a/watch__csqqcayzqueu_large.png',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 21:40:10 GMT
#   - cache-control: max-age=1694
#   - x-content-type-options: nosniff
#   - content-type: image/png
#   - content-length: 50860
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - last-modified: Wed, 25 Nov 2020 21:46:33 GMT
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 36
# resource type: 

url = 'https://www.apple.com/v/home/q/images/logos/holiday-2020/logo__dcojfwkzna2q_large.png'
headers = {
    'sec-fetch-dest': 'image',
    ':path': '/v/home/q/images/logos/holiday-2020/logo__dcojfwkzna2q_large.png',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/v/home/q/built/styles/main.built.css',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - last-modified: Wed, 11 Nov 2020 20:35:08 GMT
#   - x-content-type-options: nosniff
#   - content-type: image/png
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-length: 2397
#   - cache-control: max-age=355
#   - expires: Sat, 28 Nov 2020 21:17:51 GMT
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 37
# resource type: 

url = 'https://www.apple.com/v/home/q/images/logos/apple-one/logo__dcojfwkzna2q_large.png'
headers = {
    ':path': '/v/home/q/images/logos/apple-one/logo__dcojfwkzna2q_large.png',
    'sec-fetch-dest': 'image',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/v/home/q/built/styles/main.built.css',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - cache-control: max-age=1506
#   - expires: Sat, 28 Nov 2020 21:37:02 GMT
#   - x-content-type-options: nosniff
#   - content-type: image/png
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-length: 1623
#   - last-modified: Wed, 11 Nov 2020 20:35:07 GMT
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 38
# resource type: 

url = 'https://www.apple.com/v/home/q/images/logos/apple-news-plus/logo_light__cfvl40z2nzau_large.png'
headers = {
    'sec-fetch-dest': 'image',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':path': '/v/home/q/images/logos/apple-news-plus/logo_light__cfvl40z2nzau_large.png',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/v/home/q/built/styles/main.built.css',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - x-content-type-options: nosniff
#   - content-type: image/png
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 21:28:53 GMT
#   - content-length: 2187
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - last-modified: Mon, 23 Nov 2020 04:40:05 GMT
#   - cache-control: max-age=1017
###############################################################################

###############################################################################
# request number: 39
# resource type: 

url = 'https://www.apple.com/v/home/q/images/promos/apple-news-plus/tile__cauwwcyyn9hy_large.png'
headers = {
    'sec-fetch-dest': 'image',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/v/home/q/built/styles/main.built.css',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    ':path': '/v/home/q/images/promos/apple-news-plus/tile__cauwwcyyn9hy_large.png',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - x-content-type-options: nosniff
#   - content-type: image/png
#   - accept-ranges: bytes
#   - content-length: 621455
#   - cache-control: max-age=1087
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - last-modified: Mon, 23 Nov 2020 04:40:05 GMT
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - expires: Sat, 28 Nov 2020 21:30:03 GMT
###############################################################################

###############################################################################
# request number: 40
# resource type: 

url = 'https://www.apple.com/v/home/q/images/logos/apple-card/logo__dcojfwkzna2q_large.png'
headers = {
    ':path': '/v/home/q/images/logos/apple-card/logo__dcojfwkzna2q_large.png',
    'sec-fetch-dest': 'image',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/v/home/q/built/styles/main.built.css',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - x-content-type-options: nosniff
#   - content-type: image/png
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 21:52:50 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-length: 1855
#   - server: Apache
#   - cache-control: max-age=2454
#   - last-modified: Wed, 11 Nov 2020 20:35:07 GMT
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 41
# resource type: 

url = 'https://www.apple.com/v/home/q/images/logos/tv-plus/logo_light__cfvl40z2nzau_large.png'
headers = {
    'sec-fetch-dest': 'image',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    ':path': '/v/home/q/images/logos/tv-plus/logo_light__cfvl40z2nzau_large.png',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/v/home/q/built/styles/main.built.css',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - last-modified: Wed, 11 Nov 2020 20:35:08 GMT
#   - x-content-type-options: nosniff
#   - content-type: image/png
#   - accept-ranges: bytes
#   - cache-control: max-age=528
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - expires: Sat, 28 Nov 2020 21:20:44 GMT
#   - content-length: 1154
###############################################################################

###############################################################################
# request number: 42
# resource type: 

url = 'https://www.apple.com/v/home/q/images/logos/tv-plus-doug-unplugs/logo__dcojfwkzna2q_large.png'
headers = {
    'sec-fetch-dest': 'image',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'pragma': 'no-cache',
    ':path': '/v/home/q/images/logos/tv-plus-doug-unplugs/logo__dcojfwkzna2q_large.png',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/v/home/q/built/styles/main.built.css',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - x-content-type-options: nosniff
#   - content-type: image/png
#   - accept-ranges: bytes
#   - content-length: 7418
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - last-modified: Wed, 25 Nov 2020 21:46:33 GMT
#   - expires: Sat, 28 Nov 2020 21:40:37 GMT
#   - cache-control: max-age=1721
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 43
# resource type: 

url = 'https://www.apple.com/wss/fonts/SF-Pro-Icons/v3/sf-pro-icons_regular.woff2'
headers = {
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'origin': 'https://www.apple.com',
    'sec-fetch-dest': 'font',
    ':path': '/wss/fonts/SF-Pro-Icons/v3/sf-pro-icons_regular.woff2',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
    'referer': 'https://www.apple.com/wss/fonts?families=SF+Pro,v3|SF+Pro+Icons,v3',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'sec-fetch-mode': 'cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-length: 11208
#   - cache-control: max-age=1442
#   - x-content-type-options: nosniff
#   - access-control-allow-origin: *
#   - expires: Sat, 28 Nov 2020 21:35:58 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - content-type: font/woff2
###############################################################################

###############################################################################
# request number: 44
# resource type: 

url = 'https://www.apple.com/wss/fonts/SF-Pro-Display/v3/sf-pro-display_semibold.woff2'
headers = {
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'origin': 'https://www.apple.com',
    'sec-fetch-dest': 'font',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
    'referer': 'https://www.apple.com/wss/fonts?families=SF+Pro,v3|SF+Pro+Icons,v3',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'sec-fetch-mode': 'cors',
    ':path': '/wss/fonts/SF-Pro-Display/v3/sf-pro-display_semibold.woff2',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - x-content-type-options: nosniff
#   - access-control-allow-origin: *
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-powered-by: PHP/5.3.3
#   - server: Apache
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - cache-control: max-age=1956
#   - content-length: 116700
#   - expires: Sat, 28 Nov 2020 21:44:32 GMT
#   - content-type: font/woff2
###############################################################################

###############################################################################
# request number: 45
# resource type: 

url = 'https://www.apple.com/wss/fonts/SF-Pro-Display/v3/sf-pro-display_regular.woff2'
headers = {
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    ':path': '/wss/fonts/SF-Pro-Display/v3/sf-pro-display_regular.woff2',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'origin': 'https://www.apple.com',
    'sec-fetch-dest': 'font',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
    'referer': 'https://www.apple.com/wss/fonts?families=SF+Pro,v3|SF+Pro+Icons,v3',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'sec-fetch-mode': 'cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - cache-control: max-age=2229
#   - x-content-type-options: nosniff
#   - expires: Sat, 28 Nov 2020 21:49:05 GMT
#   - access-control-allow-origin: *
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-powered-by: PHP/5.3.3
#   - server: Apache
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - content-length: 98616
#   - content-type: font/woff2
###############################################################################

###############################################################################
# request number: 46
# resource type: 

url = 'https://www.apple.com/ac/localeswitcher/3/it_IT/content/localeswitcher.json'
headers = {
    'referer': 'https://www.apple.com/',
    'accept': '*/*',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    ':path': '/ac/localeswitcher/3/it_IT/content/localeswitcher.json',
    'sec-fetch-mode': 'cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_dc': 'nc',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - last-modified: Fri, 08 May 2020 00:10:56 GMT
#   - vary: Accept-Encoding
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-length: 390
#   - server: Apache
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - expires: Sat, 28 Nov 2020 21:20:24 GMT
#   - content-encoding: gzip
#   - cache-control: max-age=508
#   - content-type: application/json
###############################################################################

###############################################################################
# request number: 47
# resource type: 

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'referer': 'https://www.apple.com/',
    'accept': '*/*',
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_dc': 'nc',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
params = [
    ('src', 'globalnav'),
    ('locale', 'en_US'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=31536000; includeSubdomains
#   - x-xss-protection: 1; mode=block
#   - cache-control: max-age=67
#   - content-length: 579
#   - x-content-type-options: nosniff
#   - expires: Sat, 28 Nov 2020 21:13:03 GMT
#   - x-frame-options: DENY
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - server: Apple
#   - x-frame-options: SAMEORIGIN
#   - content-type: application/json
###############################################################################

###############################################################################
# request number: 48
# resource type: 

url = 'https://www.apple.com/v/home/q/images/heroes/holiday-2020/set-a/phone__ulbbo0vgyf6y_large.png'
headers = {
    'sec-fetch-dest': 'image',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':path': '/v/home/q/images/heroes/holiday-2020/set-a/phone__ulbbo0vgyf6y_large.png',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/v/home/q/built/styles/main.built.css',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_dc': 'nc',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-length: 136391
#   - x-content-type-options: nosniff
#   - content-type: image/png
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - expires: Sat, 28 Nov 2020 22:01:44 GMT
#   - last-modified: Wed, 11 Nov 2020 20:35:06 GMT
#   - cache-control: max-age=2988
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 49
# resource type: 

url = 'https://www.apple.com/v/home/q/images/heroes/holiday-2020/set-a/watch__csqqcayzqueu_large.png'
headers = {
    'sec-fetch-dest': 'image',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    ':path': '/v/home/q/images/heroes/holiday-2020/set-a/watch__csqqcayzqueu_large.png',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/v/home/q/built/styles/main.built.css',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_dc': 'nc',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 21:17:20 GMT
#   - x-content-type-options: nosniff
#   - content-type: image/png
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - cache-control: max-age=324
#   - server: Apache
#   - content-length: 125317
#   - last-modified: Wed, 11 Nov 2020 20:35:06 GMT
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 50
# resource type: 

url = 'https://www.apple.com/v/home/q/images/heroes/holiday-2020/set-a/ipad__bq6djchifrbm_large.png'
headers = {
    ':path': '/v/home/q/images/heroes/holiday-2020/set-a/ipad__bq6djchifrbm_large.png',
    'sec-fetch-dest': 'image',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/v/home/q/built/styles/main.built.css',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_dc': 'nc',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-length: 99000
#   - x-content-type-options: nosniff
#   - content-type: image/png
#   - accept-ranges: bytes
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
#   - expires: Sat, 28 Nov 2020 21:32:34 GMT
#   - last-modified: Wed, 11 Nov 2020 20:35:06 GMT
#   - cache-control: max-age=1238
###############################################################################

###############################################################################
# request number: 51
# resource type: 

url = 'https://www.apple.com/v/home/q/images/heroes/iphone-12-pro/iphone_12_pro_us__e5oyysg4k0ya_large.jpg'
headers = {
    'sec-fetch-dest': 'image',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    ':method': 'GET',
    ':path': '/v/home/q/images/heroes/iphone-12-pro/iphone_12_pro_us__e5oyysg4k0ya_large.jpg',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/v/home/q/built/styles/main.built.css',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_dc': 'nc',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-length: 96542
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - cache-control: max-age=2972
#   - last-modified: Fri, 13 Nov 2020 20:38:21 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - expires: Sat, 28 Nov 2020 22:01:28 GMT
#   - content-type: image/jpeg
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
###############################################################################

###############################################################################
# request number: 52
# resource type: 

url = 'https://securemetrics.apple.com/b/ss/appleglobal,applestoreww/1/JS-2.17.0/s93104056458127'
headers = {
    ':path': '/b/ss/appleglobal,applestoreww/1/JS-2.17.0/s93104056458127?AQB=1&ndh=1&pf=1&t=28%2F10%2F2020%2022%3A11%3A56%206%20-60&fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A&ce=UTF-8&pageName=apple%20-%20index%2Ftab%20%28us%29&g=https%3A%2F%2Fwww.apple.com%2F&cc=USD&ch=www.us.homepage&server=ac-2.11.0&h1=www.us.homepage&v3=aos%3A%20us&c4=D%3Dg&v4=D%3DpageName&c5=macintel&v14=en-us&c19=aos%3A%20us%3A%20apple%20-%20index%2Ftab%20%28us%29&c20=aos%3A%20us&c25=direct%20entry&v54=D%3Dg&v57=network%20request%20failed&v97=s.t-p&s=1920x1080&c=24&j=1.6&v=N&k=Y&bw=1597&bh=618&AQE=1',
    'sec-fetch-dest': 'image',
    'referer': 'https://www.apple.com/',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    ':authority': 'securemetrics.apple.com',
    'pragma': 'no-cache',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_dc': 'nc',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
params = [
    ('t', '28%2F10%2F2020%2022%3A11%3A56%206%20-60'),
    ('ndh', '1'),
    ('k', 'Y'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('j', '1.6'),
    ('c', '24'),
    ('bh', '618'),
    ('v', 'N'),
    ('pf', '1'),
    ('pageName', 'apple%20-%20index%2Ftab%20%28us%29'),
    ('c20', 'aos%3A%20us'),
    ('v97', 's.t-p'),
    ('bw', '1597'),
    ('c5', 'macintel'),
    ('c4', 'D%3Dg'),
    ('v4', 'D%3DpageName'),
    ('AQE', '1'),
    ('c25', 'direct%20entry'),
    ('v14', 'en-us'),
    ('v57', 'network%20request%20failed'),
    ('AQB', '1'),
    ('v54', 'D%3Dg'),
    ('h1', 'www.us.homepage'),
    ('v3', 'aos%3A%20us'),
    ('cc', 'USD'),
    ('s', '1920x1080'),
    ('ce', 'UTF-8'),
    ('server', 'ac-2.11.0'),
    ('c19', 'aos%3A%20us%3A%20apple%20-%20index%2Ftab%20%28us%29'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2F'),
    ('ch', 'www.us.homepage'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - set-cookie: s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; Path=/; Domain=apple.com; Max-Age=63072000; Expires=Mon, 28 Nov 2022 21:11:11 GMT; SameSite=None; Secure
#   - content-length: 43
#   - xserver: anedge-6f88bf85bc-kxbn7
#   - server: jag
#   - vary: *
#   - x-xss-protection: 1; mode=block
#   - x-content-type-options: nosniff
#   - etag: 3450142755753656320-4621650426975194593
#   - access-control-allow-origin: *
#   - p3p: CP="This is not a P3P policy"
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - cache-control: no-cache, no-store, max-age=0, no-transform, private
#   - x-c: master-1404.I1e61f9.M0-468
#   - pragma: no-cache
#   - last-modified: Sun, 29 Nov 2020 21:11:57 GMT
#   - expires: Fri, 27 Nov 2020 21:11:57 GMT
#   - content-type: image/gif;charset=utf-8
#   - date: Sat, 28 Nov 2020 21:11:56 GMT
# response cookies:
#   - s_vi: [CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]
###############################################################################

###############################################################################
# request number: 53
# resource type: 

url = 'https://www.apple.com/ac/localeswitcher/3/it_IT/styles/localeswitcher.built.css'
headers = {
    'accept': 'text/css,*/*;q=0.1',
    'referer': 'https://www.apple.com/',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    ':method': 'GET',
    'sec-fetch-dest': 'style',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    ':path': '/ac/localeswitcher/3/it_IT/styles/localeswitcher.built.css',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_dc': 'nc',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - vary: Accept-Encoding
#   - expires: Sat, 28 Nov 2020 21:12:01 GMT
#   - date: Sat, 28 Nov 2020 21:11:57 GMT
#   - ntcoent-length: 37718
#   - x-content-type-options: nosniff
#   - cache-control: max-age=4
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - content-type: text/css
#   - content-length: 3969
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 54
# resource type: 

url = 'https://www.apple.com/wss/fonts/SF-Pro-Icons/v3/sf-pro-icons_light.woff2'
headers = {
    'accept': '*/*',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    ':path': '/wss/fonts/SF-Pro-Icons/v3/sf-pro-icons_light.woff2',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'origin': 'https://www.apple.com',
    'sec-fetch-dest': 'font',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
    'referer': 'https://www.apple.com/wss/fonts?families=SF+Pro,v3|SF+Pro+Icons,v3',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_dc': 'nc',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - cache-control: max-age=2624
#   - x-content-type-options: nosniff
#   - content-length: 11388
#   - expires: Sat, 28 Nov 2020 21:55:42 GMT
#   - access-control-allow-origin: *
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - date: Sat, 28 Nov 2020 21:11:58 GMT
#   - content-type: font/woff2
###############################################################################

###############################################################################
# request number: 55
# resource type: 

url = 'https://www.apple.com/wss/fonts/SF-Pro-Text/v3/sf-pro-text_light.woff2'
headers = {
    'accept': '*/*',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    ':scheme': 'https',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'origin': 'https://www.apple.com',
    'sec-fetch-dest': 'font',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
    'referer': 'https://www.apple.com/wss/fonts?families=SF+Pro,v3|SF+Pro+Icons,v3',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    ':path': '/wss/fonts/SF-Pro-Text/v3/sf-pro-text_light.woff2',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_dc': 'nc',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 22:00:36 GMT
#   - content-length: 115268
#   - x-content-type-options: nosniff
#   - access-control-allow-origin: *
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - server: Apache
#   - date: Sat, 28 Nov 2020 21:11:58 GMT
#   - cache-control: max-age=2918
#   - content-type: font/woff2
###############################################################################

###############################################################################
# request number: 56
# resource type: 

url = 'https://www.apple.com/favicon.ico'
headers = {
    ':path': '/favicon.ico',
    'sec-fetch-dest': 'image',
    'referer': 'https://www.apple.com/',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA; mbox=session#ff127cfbd7014007ac85875fb7ad03d4#1606599776; as_dc=nc; mk_epub=%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':scheme': 'https',
    ':authority': 'www.apple.com',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-mode': 'no-cors',
}
cookies = {
    'dslang': 'US-EN',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_sq': '%5B%5BB%5D%5D',
    's_cc': 'true',
    'mbox': 'session#ff127cfbd7014007ac85875fb7ad03d4#1606599776',
    'dssf': '1',
    'geo': 'IT',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'mk_epub': '%7B%22btuid%22%3A%221tfpbf5%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_dc': 'nc',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'pxro': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - content-type: image/x-icon
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - cache-control: max-age=154
#   - server: Apache
#   - date: Sat, 28 Nov 2020 21:11:58 GMT
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - expires: Sat, 28 Nov 2020 21:14:32 GMT
#   - content-length: 22382
###############################################################################

