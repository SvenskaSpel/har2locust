import requests


s = requests.Session()

###############################################################################
# request number: 1
# resource type: document

url = 'https://secure2.store.apple.com/shop/sign_in'
headers = {
    'Host': 'secure2.store.apple.com',
    'Sec-Fetch-Mode': 'navigate',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Site': 'same-site',
    'Connection': 'keep-alive',
    'Referer': 'https://www.apple.com/',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_xs=flc=; as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; s_sq=%5B%5BB%5D%5D',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'as_xsm': '1&TsS1k4znjEvnGjBoAe_vvw',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_xs': 'flc=',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('r', 'SXYD4UDAPXU7P7KXF'),
    ('t', 'SXYD4UDAPXU7P7KXF'),
    ('up', 't'),
    ('o', 'O01HTjYz'),
    ('s', 'aHR0cHM6Ly9zZWN1cmUyLnN0b3JlLmFwcGxlLmNvbS9zaG9wL2NoZWNrb3V0L3N0YXJ0P3BsdG49QTZGNDNFMER8MWFvczg4MjgzMjY3MzJkNWEzNjIxMTQxMDE0ZTU4NmZiNTY5MjEzZGEyY2M'),
    ('c', 'aHR0cHM6Ly93d3cuYXBwbGUuY29tL3Nob3AvYmFnfDFhb3NjY2QxZjg4ZGZjYjY4YWRhNWZmMmY5ZTY5YWMzNjE0OTYyMjZlOWMz'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - Server: Apple
#   - Content-Encoding: gzip
#   - Set-Cookie: as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:38 GMT; Max-Age=15552000; Secure; HttpOnly
#   - x-serverprocessingtime: 16
#   - x-xss-protection: 1; mode=block
#   - Set-Cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:38 GMT; Max-Age=315360000; Secure; HttpOnly
#   - Content-Length: 10158
#   - Strict-Transport-Security: max-age=31536000; includeSubDomains
#   - x-shred: 64eac8aa26c2139b5ad18cbdefd14ff7
#   - Last-Modified: Sat, 28 Nov 2020 11:59:38 GMT
#   - Cache-Control: no-store, private, must-revalidate, proxy-revalidate, max-age=0, pre-check=0, post-check=0, no-cache, no-siteapp
#   - Connection: keep-alive
#   - x-frame-options: SAMEORIGIN
#   - Expires: Thu, 01 Jan 1970 00:00:00 GMT
#   - Vary: *
#   - Set-Cookie: as_dc=nc; version="1"; max-age=1800; expires=Sat, 28-Nov-2020 12:29:38 GMT; path=/; domain=apple.com; secure
#   - Pragma: no-cache
#   - Content-Type: text/html; charset=UTF-8; encoding=UTF8
#   - content-security-policy: frame-ancestors 'self'
#   - Set-Cookie: as_xs=flc=&idmsl=1; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:38 GMT; Max-Age=15552000; Secure; HttpOnly
#   - x-content-type-options: nosniff
#   - Expires: Fri, 27 Nov 2020 11:59:38 GMT
#   - Date: Sat, 28 Nov 2020 11:59:38 GMT
#   - Set-Cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:38 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-request-id: 8a0d60c7-f930-4fee-ab26-2e7bd8fbfdbd
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - dssf: 1
#   - as_xs: flc=&idmsl=1
#   - as_xsm: 1&93mZGW_YVaxBa9JRiFse-Q
#   - as_dc: nc
###############################################################################

###############################################################################
# request number: 2
# resource type: document

url = 'https://www.apple.com/shop/buy-mac/macbook-air'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=applestoreww%252Cappleglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526link%253Dreview%252520bag%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526pidt%253D1%2526oid%253Dproceed%2526oidt%253D3%2526ot%253DSUBMIT; s_aca_ct=%7B%22events%22%3A%22event246%2Cevent210%3D4.47%22%2C%22eVar94%22%3A4.47%2C%22eVar93%22%3A0%7D',
    'upgrade-insecure-requests': '1',
    'sec-fetch-mode': 'navigate',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-user': '?1',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cache-control': 'no-cache',
    ':path': '/shop/buy-mac/macbook-air?proceed=proceed&bfil=2&product=MGN63LL%2FA&step=attach',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'document',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    'check': 'true',
    's_sq': 'applestoreww%252Cappleglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526link%253Dreview%252520bag%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526pidt%253D1%2526oid%253Dproceed%2526oidt%253D3%2526ot%253DSUBMIT',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    's_aca_ct': '%7B%22events%22%3A%22event246%2Cevent210%3D4.47%22%2C%22eVar94%22%3A4.47%2C%22eVar93%22%3A0%7D',
}
params = [
    ('proceed', 'proceed'),
    ('bfil', '2'),
    ('step', 'attach'),
    ('product', 'MGN63LL%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 303
# response headers:
#   - x-xss-protection: 1; mode=block
#   - content-length: 20
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - etag: "d41d8cd98f00b204e9800998ecf8427e"
#   - x-shred: 4f2117550b8e0b2c66ec333589661d50
#   - x-request-id: 2375cd7d-e6c9-4299-bc74-17bfc6f198ff
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:30 GMT; Max-Age=315360000; Secure; HttpOnly
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:30 GMT; Path=/; Secure
#   - expires: Sat, 28 Nov 2020 11:59:30 GMT
#   - pragma: no-cache
#   - server: Apple
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:30 GMT; Max-Age=315360000; Secure; HttpOnly
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - last-modified: Sat, 28 Nov 2020 11:59:30 GMT
#   - location: /shop/bag
#   - date: Sat, 28 Nov 2020 11:59:30 GMT
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 3
# resource type: document

url = 'https://www.apple.com/shop/bag'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=applestoreww%252Cappleglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526link%253Dreview%252520bag%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526pidt%253D1%2526oid%253Dproceed%2526oidt%253D3%2526ot%253DSUBMIT; s_aca_ct=%7B%22events%22%3A%22event246%2Cevent210%3D4.47%22%2C%22eVar94%22%3A4.47%2C%22eVar93%22%3A0%7D',
    'upgrade-insecure-requests': '1',
    'sec-fetch-mode': 'navigate',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    ':path': '/shop/bag',
    'sec-fetch-user': '?1',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'document',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    'check': 'true',
    's_sq': 'applestoreww%252Cappleglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526link%253Dreview%252520bag%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526pidt%253D1%2526oid%253Dproceed%2526oidt%253D3%2526ot%253DSUBMIT',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    's_aca_ct': '%7B%22events%22%3A%22event246%2Cevent210%3D4.47%22%2C%22eVar94%22%3A4.47%2C%22eVar93%22%3A0%7D',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-length: 33186
#   - x-xss-protection: 1; mode=block
#   - set-cookie: as_dc=nc; version="1"; max-age=1800; expires=Sat, 28-Nov-2020 12:29:30 GMT; path=/; domain=apple.com; secure
#   - set-cookie: as_xs=flc=; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:30 GMT; Max-Age=15552000; Secure; HttpOnly
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-frame-options: SAMEORIGIN
#   - x-request-id: 426b5d51-4f9f-447a-90d3-65ea7d1df041
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:30 GMT; Max-Age=315360000; Secure; HttpOnly
#   - expires: Sat, 28 Nov 2020 11:59:30 GMT
#   - x-serverprocessingtime: 161
#   - pragma: no-cache
#   - server: Apple
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:30 GMT; Max-Age=315360000; Secure; HttpOnly
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - content-security-policy: frame-ancestors 'self'
#   - set-cookie: as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:30 GMT; Max-Age=15552000; Secure; HttpOnly
#   - x-content-type-options: nosniff
#   - last-modified: Sat, 28 Nov 2020 11:59:30 GMT
#   - x-shred: 10cc028c060d02de2fe8ae0c55a27a0d
#   - content-type: text/html; charset=UTF-8; encoding=UTF8
#   - date: Sat, 28 Nov 2020 11:59:30 GMT
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_xsm: 1&TsS1k4znjEvnGjBoAe_vvw
#   - dssf: 1
#   - as_dc: nc
#   - as_xs: flc=
###############################################################################

###############################################################################
# request number: 4
# resource type: document

url = 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb'
headers = {
    'upgrade-insecure-requests': '1',
    'sec-fetch-mode': 'navigate',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2; s_sq=%5B%5BB%5D%5D; s_aca_ct=%7B%22events%22%3A%22event246%2Cevent210%3D3.39%22%2C%22eVar94%22%3A3.39%2C%22eVar93%22%3A0%7D',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-user': '?1',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'document',
    ':path': '/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb?option.memory__dummy_z124=065-C99M&option.hard_drivesolid_state_drive__dummy_z124=065-C99Q&option.keyboard_and_documentation_z124=065-C9DG&option.sw_final_cut_pro_x_z124=065-C171&option.sw_logic_pro_x_z124=065-C172&add-to-cart=add-to-cart&product=MGN63LL%2FA&step=config&bfil=2&atbtoken=bd24f42caddadc789d311b27afde1f05fc9262f2',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    ':authority': 'www.apple.com',
}
cookies = {
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_aca_ct': '%7B%22events%22%3A%22event246%2Cevent210%3D3.39%22%2C%22eVar94%22%3A3.39%2C%22eVar93%22%3A0%7D',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('product', 'MGN63LL%2FA'),
    ('bfil', '2'),
    ('option.keyboard_and_documentation_z124', '065-C9DG'),
    ('add-to-cart', 'add-to-cart'),
    ('step', 'config'),
    ('option.memory__dummy_z124', '065-C99M'),
    ('option.sw_final_cut_pro_x_z124', '065-C171'),
    ('option.sw_logic_pro_x_z124', '065-C172'),
    ('atbtoken', 'bd24f42caddadc789d311b27afde1f05fc9262f2'),
    ('option.hard_drivesolid_state_drive__dummy_z124', '065-C99Q'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 303
# response headers:
#   - x-request-id: 8a021fe0-5c84-4a10-aafb-3b5562fb7fdd
#   - x-xss-protection: 1; mode=block
#   - content-length: 20
#   - date: Sat, 28 Nov 2020 11:59:24 GMT
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - location: /shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach
#   - etag: "d41d8cd98f00b204e9800998ecf8427e"
#   - x-shred: ae00b9e41c73ef01677cd4ae55aa5890
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:24 GMT; Max-Age=315360000; Secure; HttpOnly
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:24 GMT; Path=/; Secure
#   - expires: Sat, 28 Nov 2020 11:59:24 GMT
#   - pragma: no-cache
#   - server: Apple
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - last-modified: Sat, 28 Nov 2020 11:59:24 GMT
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:24 GMT; Max-Age=315360000; Secure; HttpOnly
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 5
# resource type: document

url = 'https://www.apple.com/shop/buy-mac/macbook-air'
headers = {
    'upgrade-insecure-requests': '1',
    'sec-fetch-mode': 'navigate',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2; s_sq=%5B%5BB%5D%5D; s_aca_ct=%7B%22events%22%3A%22event246%2Cevent210%3D3.39%22%2C%22eVar94%22%3A3.39%2C%22eVar93%22%3A0%7D',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-user': '?1',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'document',
    ':path': '/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    ':authority': 'www.apple.com',
}
cookies = {
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_aca_ct': '%7B%22events%22%3A%22event246%2Cevent210%3D3.39%22%2C%22eVar94%22%3A3.39%2C%22eVar93%22%3A0%7D',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('bfil', '2'),
    ('step', 'attach'),
    ('product', 'MGN63LL/A'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - date: Sat, 28 Nov 2020 11:59:24 GMT
#   - x-frame-options: DENY
#   - last-modified: Sat, 28 Nov 2020 11:59:11 GMT
#   - content-security-policy: frame-ancestors 'none'
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:24 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-request-id: 631ddafa-a90a-4fd4-a028-a94806d211c1
#   - content-length: 46722
#   - etag: "d0b6b6ce9e4a4648483a76514a76c5c6"
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:24 GMT; Path=/; Secure
#   - content-type: text/html;charset=utf-8
#   - cache-control: private, max-age=98
#   - server: Apple
#   - expires: Sat, 28 Nov 2020 12:01:02 GMT
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - x-shred: 095931eea367ed92b779ec3312a0d95c
#   - x-content-type-options: nosniff
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:24 GMT; Max-Age=315360000; Secure; HttpOnly
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 6
# resource type: document

url = 'https://www.apple.com/shop/buy-mac/macbook-air'
headers = {
    'upgrade-insecure-requests': '1',
    'sec-fetch-mode': 'navigate',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; s_aca_ct=%7B%22events%22%3A%22event246%2Cevent210%3D7.03%22%2C%22eVar94%22%3A7.03%2C%22eVar93%22%3A0%7D',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    ':path': '/shop/buy-mac/macbook-air?proceed=proceed&product=MGN63LL%2FA&step=select',
    'sec-fetch-user': '?1',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'document',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_aca_ct': '%7B%22events%22%3A%22event246%2Cevent210%3D7.03%22%2C%22eVar94%22%3A7.03%2C%22eVar93%22%3A0%7D',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('proceed', 'proceed'),
    ('step', 'select'),
    ('product', 'MGN63LL%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 303
# response headers:
#   - x-request-id: fae35d6b-2735-438c-8bca-5d998de55c55
#   - x-xss-protection: 1; mode=block
#   - content-length: 20
#   - x-frame-options: DENY
#   - x-shred: d2866c9f5cc5e34a8c460445e8753b09
#   - last-modified: Sat, 28 Nov 2020 11:59:19 GMT
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:19 GMT; Max-Age=315360000; Secure; HttpOnly
#   - etag: "d41d8cd98f00b204e9800998ecf8427e"
#   - date: Sat, 28 Nov 2020 11:59:19 GMT
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:19 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - location: /shop/buy-mac/macbook-air?product=MGN63LL/A&step=config
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:19 GMT; Path=/; Secure
#   - server: Apple
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - expires: Sat, 28 Nov 2020 11:59:19 GMT
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 7
# resource type: document

url = 'https://www.apple.com/shop/buy-mac/macbook-air'
headers = {
    'upgrade-insecure-requests': '1',
    'sec-fetch-mode': 'navigate',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; s_aca_ct=%7B%22events%22%3A%22event246%2Cevent210%3D7.03%22%2C%22eVar94%22%3A7.03%2C%22eVar93%22%3A0%7D',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-user': '?1',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cache-control': 'no-cache',
    ':path': '/shop/buy-mac/macbook-air?product=MGN63LL/A&step=config',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'document',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_aca_ct': '%7B%22events%22%3A%22event246%2Cevent210%3D7.03%22%2C%22eVar94%22%3A7.03%2C%22eVar93%22%3A0%7D',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('step', 'config'),
    ('product', 'MGN63LL/A'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 301
# response headers:
#   - x-xss-protection: 1; mode=block
#   - content-length: 20
#   - x-frame-options: DENY
#   - x-request-id: 5c4d604e-4ee9-4304-9385-c125ac0008a3
#   - last-modified: Sat, 28 Nov 2020 11:59:19 GMT
#   - content-security-policy: frame-ancestors 'none'
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:19 GMT; Max-Age=315360000; Secure; HttpOnly
#   - etag: "d41d8cd98f00b204e9800998ecf8427e"
#   - date: Sat, 28 Nov 2020 11:59:19 GMT
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:19 GMT; Max-Age=315360000; Secure; HttpOnly
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:19 GMT; Path=/; Secure
#   - server: Apple
#   - cache-control: private, max-age=120
#   - location: https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - expires: Sat, 28 Nov 2020 12:01:19 GMT
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - x-shred: ab4669324f9b76636d615f6816edc4f5
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 8
# resource type: document

url = 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb'
headers = {
    'upgrade-insecure-requests': '1',
    'sec-fetch-mode': 'navigate',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; s_aca_ct=%7B%22events%22%3A%22event246%2Cevent210%3D7.03%22%2C%22eVar94%22%3A7.03%2C%22eVar93%22%3A0%7D',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-user': '?1',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'document',
    ':path': '/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_aca_ct': '%7B%22events%22%3A%22event246%2Cevent210%3D7.03%22%2C%22eVar94%22%3A7.03%2C%22eVar93%22%3A0%7D',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - cache-control: private, max-age=81
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:19 GMT; Max-Age=315360000; Secure; HttpOnly
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - etag: "dd5e3af3a6bbdb23d85302fc85674e79"
#   - date: Sat, 28 Nov 2020 11:59:19 GMT
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:19 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-type: text/html;charset=utf-8
#   - content-length: 45248
#   - last-modified: Sat, 28 Nov 2020 11:58:45 GMT
#   - server: Apple
#   - expires: Sat, 28 Nov 2020 12:00:40 GMT
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:19 GMT; Path=/; Secure
#   - x-shred: b4e36d2a30b640a6a20f2f4e79260aa2
#   - vary: Accept-Encoding
#   - x-request-id: 1fb4fc2b-2fca-42f2-9c59-6626be52e380
#   - content-encoding: gzip
#   - x-content-type-options: nosniff
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 9
# resource type: document

url = 'https://www.apple.com/us/shop/goto/buy_mac/macbook_air'
headers = {
    'upgrade-insecure-requests': '1',
    'sec-fetch-mode': 'navigate',
    'referer': 'https://www.apple.com/macbook-air/',
    'accept-language': 'en-US,en;q=0.9',
    ':path': '/us/shop/goto/buy_mac/macbook_air',
    'pragma': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; mk_epub=%7B%22btuid%22%3A%22vy62nu%22%2C%22eVar1%22%3A%22macbook%20air%20-%20overview%20(us)%20%7C%20local%20nav%20locked%20%7C%20buy%22%2C%22prop57%22%3A%22www.us.macbookair%22%2C%22prop25%22%3A%22local%20nav%20locked%22%7D; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D7.6%22%5D%2C%22eVar94%22%3A%227.6%22%2C%22eVar93%22%3A%221%22%7D; s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526link%253Dbuy%252520-%252520%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%252520-%252520ac-localnav%2526region%253Dac-localnav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%2526ot%253DA',
    'sec-fetch-user': '?1',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'document',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    's_sq': 'appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526link%253Dbuy%252520-%252520%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%252520-%252520ac-localnav%2526region%253Dac-localnav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%2526ot%253DA',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'mk_epub': '%7B%22btuid%22%3A%22vy62nu%22%2C%22eVar1%22%3A%22macbook%20air%20-%20overview%20(us)%20%7C%20local%20nav%20locked%20%7C%20buy%22%2C%22prop57%22%3A%22www.us.macbookair%22%2C%22prop25%22%3A%22local%20nav%20locked%22%7D',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D7.6%22%5D%2C%22eVar94%22%3A%227.6%22%2C%22eVar93%22%3A%221%22%7D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 303
# response headers:
#   - x-xss-protection: 1; mode=block
#   - content-length: 20
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:09 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - date: Sat, 28 Nov 2020 11:59:10 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - etag: "d41d8cd98f00b204e9800998ecf8427e"
#   - last-modified: Sat, 28 Nov 2020 11:59:09 GMT
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:09 GMT; Path=/; Secure
#   - x-request-id: f12dd9f7-2b23-45d2-aeeb-74bcffe03de7
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:09 GMT; Max-Age=315360000; Secure; HttpOnly
#   - location: https://www.apple.com/us/shop/go/buy_mac/macbook_air
#   - pragma: no-cache
#   - server: Apple
#   - vary: Accept-Encoding
#   - expires: Sat, 28 Nov 2020 11:59:10 GMT
#   - content-encoding: gzip
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - x-shred: 7f69f4c770de84b8b4cea488f6bf678b
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 10
# resource type: document

url = 'https://www.apple.com/us/shop/go/buy_mac/macbook_air'
headers = {
    'upgrade-insecure-requests': '1',
    'sec-fetch-mode': 'navigate',
    'referer': 'https://www.apple.com/macbook-air/',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; mk_epub=%7B%22btuid%22%3A%22vy62nu%22%2C%22eVar1%22%3A%22macbook%20air%20-%20overview%20(us)%20%7C%20local%20nav%20locked%20%7C%20buy%22%2C%22prop57%22%3A%22www.us.macbookair%22%2C%22prop25%22%3A%22local%20nav%20locked%22%7D; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D7.6%22%5D%2C%22eVar94%22%3A%227.6%22%2C%22eVar93%22%3A%221%22%7D; s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526link%253Dbuy%252520-%252520%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%252520-%252520ac-localnav%2526region%253Dac-localnav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%2526ot%253DA',
    'sec-fetch-user': '?1',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    ':path': '/us/shop/go/buy_mac/macbook_air',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'document',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    's_sq': 'appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526link%253Dbuy%252520-%252520%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%252520-%252520ac-localnav%2526region%253Dac-localnav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%2526ot%253DA',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'mk_epub': '%7B%22btuid%22%3A%22vy62nu%22%2C%22eVar1%22%3A%22macbook%20air%20-%20overview%20(us)%20%7C%20local%20nav%20locked%20%7C%20buy%22%2C%22prop57%22%3A%22www.us.macbookair%22%2C%22prop25%22%3A%22local%20nav%20locked%22%7D',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D7.6%22%5D%2C%22eVar94%22%3A%227.6%22%2C%22eVar93%22%3A%221%22%7D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 301
# response headers:
#   - expires: Sat, 28 Nov 2020 12:01:10 GMT
#   - x-xss-protection: 1; mode=block
#   - content-length: 20
#   - last-modified: Sat, 28 Nov 2020 11:59:10 GMT
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - date: Sat, 28 Nov 2020 11:59:10 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - etag: "d41d8cd98f00b204e9800998ecf8427e"
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:10 GMT; Max-Age=315360000; Secure; HttpOnly
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:10 GMT; Max-Age=315360000; Secure; HttpOnly
#   - location: /shop/buy-mac/macbook-air
#   - server: Apple
#   - cache-control: private, max-age=120
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:10 GMT; Path=/; Secure
#   - vary: Accept-Encoding
#   - x-shred: b620b213d82805e82a5b064d4198b8d8
#   - content-encoding: gzip
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - x-request-id: 90c4a4fe-43d5-4fc7-a4c0-6508e17ac964
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 11
# resource type: document

url = 'https://www.apple.com/shop/buy-mac/macbook-air'
headers = {
    'upgrade-insecure-requests': '1',
    'sec-fetch-mode': 'navigate',
    'referer': 'https://www.apple.com/macbook-air/',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; mk_epub=%7B%22btuid%22%3A%22vy62nu%22%2C%22eVar1%22%3A%22macbook%20air%20-%20overview%20(us)%20%7C%20local%20nav%20locked%20%7C%20buy%22%2C%22prop57%22%3A%22www.us.macbookair%22%2C%22prop25%22%3A%22local%20nav%20locked%22%7D; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D7.6%22%5D%2C%22eVar94%22%3A%227.6%22%2C%22eVar93%22%3A%221%22%7D; s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526link%253Dbuy%252520-%252520%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%252520-%252520ac-localnav%2526region%253Dac-localnav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%2526ot%253DA',
    'sec-fetch-user': '?1',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    ':path': '/shop/buy-mac/macbook-air',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'document',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    's_sq': 'appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526link%253Dbuy%252520-%252520%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%252520-%252520ac-localnav%2526region%253Dac-localnav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%2526ot%253DA',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'mk_epub': '%7B%22btuid%22%3A%22vy62nu%22%2C%22eVar1%22%3A%22macbook%20air%20-%20overview%20(us)%20%7C%20local%20nav%20locked%20%7C%20buy%22%2C%22prop57%22%3A%22www.us.macbookair%22%2C%22prop25%22%3A%22local%20nav%20locked%22%7D',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D7.6%22%5D%2C%22eVar94%22%3A%227.6%22%2C%22eVar93%22%3A%221%22%7D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - date: Sat, 28 Nov 2020 11:59:10 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:10 GMT; Max-Age=315360000; Secure; HttpOnly
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:10 GMT; Max-Age=315360000; Secure; HttpOnly
#   - last-modified: Sat, 28 Nov 2020 11:58:36 GMT
#   - x-request-id: 703f2c18-2d95-4643-a1ae-ed8e99c99ee0
#   - cache-control: private, max-age=86
#   - etag: "5dd846c72f93833181e1188c441bfeab"
#   - content-type: text/html;charset=utf-8
#   - server: Apple
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:10 GMT; Path=/; Secure
#   - vary: Accept-Encoding
#   - content-length: 37868
#   - content-encoding: gzip
#   - x-content-type-options: nosniff
#   - expires: Sat, 28 Nov 2020 12:00:36 GMT
#   - x-shred: 55653fe1a0688649fb9962dc48958493
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 12
# resource type: document

url = 'https://www.apple.com/macbook-air/'
headers = {
    'upgrade-insecure-requests': '1',
    'sec-fetch-mode': 'navigate',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-user': '?1',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/mac/',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'document',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; mk_epub=%7B%22btuid%22%3A%22177namr%22%2C%22eVar1%22%3A%22mac%20-%20index%2Ftab%20(us)%20%7C%20family%20browser%20%7C%20MacBook%20Air%5Cn%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5CtNew%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%2C%22prop25%22%3A%22family%20browser%22%7D; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D; s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmac%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmacbook%252520air%252520new%252520-%252520%25252Fmacbook-air%25252F%252520-%252520chapternav%2526region%253Dchapternav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmac%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmacbook-air%25252F%2526ot%253DA',
    ':path': '/macbook-air/',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    's_sq': 'appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmac%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmacbook%252520air%252520new%252520-%252520%25252Fmacbook-air%25252F%252520-%252520chapternav%2526region%253Dchapternav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmac%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmacbook-air%25252F%2526ot%253DA',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'mk_epub': '%7B%22btuid%22%3A%22177namr%22%2C%22eVar1%22%3A%22mac%20-%20index%2Ftab%20(us)%20%7C%20family%20browser%20%7C%20MacBook%20Air%5Cn%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5CtNew%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%2C%22prop25%22%3A%22family%20browser%22%7D',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - server: Apache
#   - x-xss-protection: 1; mode=block
#   - content-type: text/html; charset=UTF-8
#   - x-content-type-options: nosniff
#   - expires: Sat, 28 Nov 2020 11:59:00 GMT
#   - content-length: 30528
#   - cache-control: max-age=0
#   - date: Sat, 28 Nov 2020 11:59:00 GMT
#   - x-frame-options: SAMEORIGIN
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 13
# resource type: document

url = 'https://www.apple.com/mac/'
headers = {
    'upgrade-insecure-requests': '1',
    'sec-fetch-mode': 'navigate',
    ':path': '/mac/',
    'referer': 'https://www.apple.com/',
    'pragma': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-user': '?1',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; mk_epub=%7B%22btuid%22%3A%22126h84u%22%2C%22eVar1%22%3A%22apple%20-%20index%2Ftab%20(us)%20%7C%20global%20nav%20%7C%20mac%22%2C%22prop57%22%3A%22www.us.homepage%22%2C%22prop25%22%3A%22global%20nav%22%7D; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D; s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmac%252520-%252520%25252Fmac%25252F%252520-%252520global%252520nav%2526region%253Dglobal%252520nav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmac%25252F%2526ot%253DA',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'document',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'mk_epub': '%7B%22btuid%22%3A%22126h84u%22%2C%22eVar1%22%3A%22apple%20-%20index%2Ftab%20(us)%20%7C%20global%20nav%20%7C%20mac%22%2C%22prop57%22%3A%22www.us.homepage%22%2C%22prop25%22%3A%22global%20nav%22%7D',
    'check': 'true',
    'geo': 'IT',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_sq': 'appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmac%252520-%252520%25252Fmac%25252F%252520-%252520global%252520nav%2526region%253Dglobal%252520nav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmac%25252F%2526ot%253DA',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D',
    's_cc': 'true',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 12:00:00 GMT
#   - date: Sat, 28 Nov 2020 11:58:54 GMT
#   - server: Apache
#   - x-xss-protection: 1; mode=block
#   - content-type: text/html; charset=UTF-8
#   - x-content-type-options: nosniff
#   - x-frame-options: SAMEORIGIN
#   - content-length: 18977
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - cache-control: max-age=66
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 14
# resource type: document

url = 'https://www.apple.com/'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; mk_epub=%7B%22btuid%22%3A%22twoihc%22%2C%22prop57%22%3A%22www.us.homepage%22%7D; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
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
    ':method': 'GET',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'check': 'true',
    'geo': 'IT',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'mk_epub': '%7B%22btuid%22%3A%22twoihc%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    's_cc': 'true',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-length: 10565
#   - server: Apache
#   - x-xss-protection: 1; mode=block
#   - content-type: text/html; charset=UTF-8
#   - x-content-type-options: nosniff
#   - expires: Sat, 28 Nov 2020 11:58:49 GMT
#   - cache-control: max-age=0
#   - date: Sat, 28 Nov 2020 11:58:49 GMT
#   - x-frame-options: SAMEORIGIN
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 15
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
    ('mboxSession', 'bb7cc510c65f4f4eaba6b8ef81b5547f'),
    ('mboxURL', 'https%3A%2F%2Fwww.apple.com%2F'),
    ('browserTimeOffset', '60'),
    ('screenOrientation', 'landscape'),
    ('mboxRid', 'e1e5810447114e1ea0db6ddfae46a383'),
    ('mboxPage', '28a825d8368e433fb1840aed16581b46'),
    ('mboxReferrer', ''),
    ('mboxHost', 'www.apple.com'),
    ('browserWidth', '1420'),
    ('browserHeight', '630'),
    ('screenWidth', '1920'),
    ('colorDepth', '24'),
    ('mboxPC', ''),
    ('screenHeight', '1080'),
    ('mboxVersion', '1.5.0'),
    ('mbox', 'target-global-mbox'),
    ('mboxTime', '1606568330064'),
]
rc = s.get(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 16
# resource type: xhr

url = 'https://www.apple.com/ac/localeswitcher/3/it_IT/content/localeswitcher.json'
headers = {
    'accept': '*/*',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; mk_epub=%7B%22btuid%22%3A%22twoihc%22%2C%22prop57%22%3A%22www.us.homepage%22%7D; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
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
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'check': 'true',
    'geo': 'IT',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'mk_epub': '%7B%22btuid%22%3A%22twoihc%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    's_cc': 'true',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - last-modified: Fri, 08 May 2020 00:10:56 GMT
#   - cache-control: max-age=556
#   - date: Sat, 28 Nov 2020 11:58:50 GMT
#   - server: Apache
#   - expires: Sat, 28 Nov 2020 12:08:06 GMT
#   - content-length: 390
#   - x-content-type-options: nosniff
#   - accept-ranges: bytes
#   - vary: Accept-Encoding
#   - content-type: application/json
#   - content-encoding: gzip
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 17
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; mk_epub=%7B%22btuid%22%3A%22fae48u%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
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
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'check': 'true',
    'geo': 'IT',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'mk_epub': '%7B%22btuid%22%3A%22fae48u%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
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
#   - date: Sat, 28 Nov 2020 11:58:51 GMT
#   - x-content-type-options: nosniff
#   - server: Apple
#   - x-frame-options: SAMEORIGIN
#   - x-frame-options: DENY
#   - content-length: 579
#   - expires: Sat, 28 Nov 2020 12:00:50 GMT
#   - cache-control: max-age=119
#   - content-type: application/json
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 18
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; mk_epub=%7B%22btuid%22%3A%22fae48u%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
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
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'check': 'true',
    'geo': 'IT',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'mk_epub': '%7B%22btuid%22%3A%22fae48u%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-type: image/x-icon
#   - server: Apache
#   - date: Sat, 28 Nov 2020 11:58:51 GMT
#   - x-content-type-options: nosniff
#   - content-length: 22382
#   - accept-ranges: bytes
#   - cache-control: max-age=219
#   - expires: Sat, 28 Nov 2020 12:02:30 GMT
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 19
# resource type: xhr

url = 'https://www.apple.com/ac/localeswitcher/3/it_IT/content/localeswitcher.json'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/mac/',
    ':path': '/ac/localeswitcher/3/it_IT/content/localeswitcher.json',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D; s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmac%252520-%252520%25252Fmac%25252F%252520-%252520global%252520nav%2526region%253Dglobal%252520nav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmac%25252F%2526ot%253DA; mk_epub=%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'check': 'true',
    'geo': 'IT',
    'mk_epub': '%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_sq': 'appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmac%252520-%252520%25252Fmac%25252F%252520-%252520global%252520nav%2526region%253Dglobal%252520nav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmac%25252F%2526ot%253DA',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D',
    's_cc': 'true',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - last-modified: Fri, 08 May 2020 00:10:56 GMT
#   - server: Apache
#   - expires: Sat, 28 Nov 2020 12:08:06 GMT
#   - content-length: 390
#   - x-content-type-options: nosniff
#   - cache-control: max-age=550
#   - accept-ranges: bytes
#   - date: Sat, 28 Nov 2020 11:58:56 GMT
#   - vary: Accept-Encoding
#   - content-type: application/json
#   - content-encoding: gzip
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 20
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/mac/',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D; s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmac%252520-%252520%25252Fmac%25252F%252520-%252520global%252520nav%2526region%253Dglobal%252520nav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmac%25252F%2526ot%253DA; mk_epub=%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'check': 'true',
    'geo': 'IT',
    'mk_epub': '%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_sq': 'appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmac%252520-%252520%25252Fmac%25252F%252520-%252520global%252520nav%2526region%253Dglobal%252520nav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmac%25252F%2526ot%253DA',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D',
    's_cc': 'true',
}
params = [
    ('locale', 'en_US'),
    ('src', 'globalnav'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - cache-control: max-age=114
#   - strict-transport-security: max-age=31536000; includeSubdomains
#   - x-xss-protection: 1; mode=block
#   - x-content-type-options: nosniff
#   - server: Apple
#   - x-frame-options: SAMEORIGIN
#   - x-frame-options: DENY
#   - content-length: 579
#   - expires: Sat, 28 Nov 2020 12:00:50 GMT
#   - date: Sat, 28 Nov 2020 11:58:56 GMT
#   - content-type: application/json
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 21
# resource type: xhr

url = 'https://www.apple.com/us/shop/mcm/product-price'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':path': '/us/shop/mcm/product-price?parts=MACBOOKAIR_M1,MBP2020_13_M1,MACMINI_M1,MBP2019_16',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D; mk_epub=%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D; s_sq=%5B%5BB%5D%5D',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/mac/',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'mk_epub': '%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D',
    's_cc': 'true',
}
params = [
    ('parts', 'MACBOOKAIR_M1,MBP2020_13_M1,MACMINI_M1,MBP2019_16'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - expires: Sat, 28 Nov 2020 12:00:57 GMT
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - last-modified: Sat, 28 Nov 2020 11:51:56 GMT
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:58:57 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-length: 285
#   - etag: "60ea5ead92cc30e1804649558a97a272"
#   - x-request-id: 0b429fd6-ebf1-4609-960a-1387d30b403d
#   - server: Apple
#   - content-type: application/json; encoding=UTF8;charset=UTF-8
#   - cache-control: private, max-age=120
#   - date: Sat, 28 Nov 2020 11:58:57 GMT
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:28:57 GMT; Path=/; Secure
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:58:57 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-content-type-options: nosniff
#   - set-cookie: as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; Path=/; Domain=apple.com; Secure; HttpOnly
#   - x-shred: dbfbac688d155a494f8955f574b628a5
# response cookies:
#   - as_dc: nc
#   - as_pcts: JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 22
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D; mk_epub=%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D; s_sq=%5B%5BB%5D%5D; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-dest': 'image',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':path': '/favicon.ico',
    'sec-fetch-mode': 'no-cors',
    'referer': 'https://www.apple.com/mac/',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    's_sq': '%5B%5BB%5D%5D',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'mk_epub': '%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-type: image/x-icon
#   - server: Apache
#   - x-content-type-options: nosniff
#   - content-length: 22382
#   - accept-ranges: bytes
#   - cache-control: max-age=213
#   - expires: Sat, 28 Nov 2020 12:02:30 GMT
#   - date: Sat, 28 Nov 2020 11:58:57 GMT
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 23
# resource type: xhr

url = 'https://www.apple.com/ac/localeswitcher/3/it_IT/content/localeswitcher.json'
headers = {
    'accept': '*/*',
    'referer': 'https://www.apple.com/macbook-air/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D; mk_epub=%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D; s_sq=%5B%5BB%5D%5D',
    ':path': '/ac/localeswitcher/3/it_IT/content/localeswitcher.json',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D',
    'mk_epub': '%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - last-modified: Fri, 08 May 2020 00:10:56 GMT
#   - server: Apache
#   - expires: Sat, 28 Nov 2020 12:08:06 GMT
#   - date: Sat, 28 Nov 2020 11:59:02 GMT
#   - x-content-type-options: nosniff
#   - content-length: 390
#   - accept-ranges: bytes
#   - cache-control: max-age=544
#   - vary: Accept-Encoding
#   - content-type: application/json
#   - content-encoding: gzip
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 24
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'accept': '*/*',
    'referer': 'https://www.apple.com/macbook-air/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D; mk_epub=%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D; s_sq=%5B%5BB%5D%5D',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D',
    'mk_epub': '%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
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
#   - date: Sat, 28 Nov 2020 11:59:02 GMT
#   - x-content-type-options: nosniff
#   - server: Apple
#   - x-frame-options: SAMEORIGIN
#   - x-frame-options: DENY
#   - content-length: 579
#   - cache-control: max-age=108
#   - expires: Sat, 28 Nov 2020 12:00:50 GMT
#   - content-type: application/json
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 25
# resource type: xhr

url = 'https://www.apple.com/us/shop/mcm/product-price'
headers = {
    'accept': '*/*',
    'referer': 'https://www.apple.com/macbook-air/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':path': '/us/shop/mcm/product-price?parts=MACBOOKAIR_M1,MBP2020_13_M1,MBP2019_16',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D; mk_epub=%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D; s_sq=%5B%5BB%5D%5D',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D',
    'mk_epub': '%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts', 'MACBOOKAIR_M1,MBP2020_13_M1,MBP2019_16'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - date: Sat, 28 Nov 2020 11:59:02 GMT
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:02 GMT; Path=/; Secure
#   - x-frame-options: DENY
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:02 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-length: 246
#   - x-request-id: 29565b7b-cb4b-42ee-a488-7623debcbdf7
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:02 GMT; Max-Age=315360000; Secure; HttpOnly
#   - server: Apple
#   - last-modified: Sat, 28 Nov 2020 11:28:55 GMT
#   - content-type: application/json; encoding=UTF8;charset=UTF-8
#   - cache-control: private, max-age=120
#   - expires: Sat, 28 Nov 2020 12:01:02 GMT
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - x-shred: 59f5e5b31f6a82123e700bf0969372e6
#   - x-content-type-options: nosniff
#   - etag: "024e35d489441dd22e1f37c0c8eacaaa"
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 26
# resource type: xhr

url = 'https://www.apple.com/us/shop/mcm/tradein-credit'
headers = {
    'accept': '*/*',
    'referer': 'https://www.apple.com/macbook-air/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D; mk_epub=%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D; s_sq=%5B%5BB%5D%5D',
    ':path': '/us/shop/mcm/tradein-credit?ids=6822',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D',
    'mk_epub': '%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('ids', '6822'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - date: Sat, 28 Nov 2020 11:59:02 GMT
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:02 GMT; Path=/; Secure
#   - x-frame-options: DENY
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:02 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-length: 167
#   - x-request-id: cb6a65c9-4319-41a9-9acb-9ed3ae446c97
#   - etag: "be841b98bcc65c680726447afde658d2"
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:02 GMT; Max-Age=315360000; Secure; HttpOnly
#   - server: Apple
#   - content-type: application/json; encoding=UTF8;charset=UTF-8
#   - cache-control: private, max-age=120
#   - expires: Sat, 28 Nov 2020 12:01:02 GMT
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - x-content-type-options: nosniff
#   - last-modified: Sat, 28 Nov 2020 11:34:26 GMT
#   - x-shred: 0ceb720d986857001b5a958353c1321d
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 27
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    'referer': 'https://www.apple.com/macbook-air/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-dest': 'image',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':path': '/favicon.ico',
    'sec-fetch-mode': 'no-cors',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D; mk_epub=%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D; s_sq=%5B%5BB%5D%5D',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D',
    'mk_epub': '%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-type: image/x-icon
#   - server: Apache
#   - date: Sat, 28 Nov 2020 11:59:03 GMT
#   - x-content-type-options: nosniff
#   - content-length: 22382
#   - accept-ranges: bytes
#   - cache-control: max-age=207
#   - expires: Sat, 28 Nov 2020 12:02:30 GMT
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 28
# resource type: xhr

url = 'https://www.apple.com/shop/bag/status'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/shop/bag/status?apikey=SJHJUH4YFCTTPD4F4',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('apikey', 'SJHJUH4YFCTTPD4F4'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - date: Sat, 28 Nov 2020 11:59:12 GMT
#   - x-frame-options: DENY
#   - content-type: application/json;charset=utf-8
#   - content-security-policy: frame-ancestors 'none'
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:12 GMT; Max-Age=315360000; Secure; HttpOnly
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-shred: 8a89837e83a5f9f46e92058a02259a36
#   - x-request-id: b48e9f3e-7a41-4fd1-8b13-a58c0b577e76
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:12 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-length: 137
#   - expires: Sat, 28 Nov 2020 11:59:12 GMT
#   - pragma: no-cache
#   - server: Apple
#   - cache-control: private, no-cache, no-store, must-revalidate
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - last-modified: Sat, 28 Nov 2020 11:59:12 GMT
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:12 GMT; Max-Age=1800; Secure
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 29
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':path': '/shop/delivery-message?parts.0=MGN63LL%2FA&parts.1=MGND3LL%2FA&parts.2=MGN93LL%2FA&mt=regular&_=1606564751169',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    'cache-control': 'no-cache',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts.1', 'MGND3LL%2FA'),
    ('_', '1606564751169'),
    ('mt', 'regular'),
    ('parts.0', 'MGN63LL%2FA'),
    ('parts.2', 'MGN93LL%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - etag: "29ec11b4361e2bd43431fc80abaded48"
#   - x-request-id: 03dc1d7d-38a6-4a78-af4f-3a3384966408
#   - x-xss-protection: 1; mode=block
#   - date: Sat, 28 Nov 2020 11:59:12 GMT
#   - x-frame-options: DENY
#   - x-shred: fe11c8e5bc714a00fe8f24e101f1fc9c
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:12 GMT; Max-Age=315360000; Secure; HttpOnly
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-length: 2619
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:12 GMT; Max-Age=315360000; Secure; HttpOnly
#   - expires: Sat, 28 Nov 2020 11:59:12 GMT
#   - pragma: no-cache
#   - server: Apple
#   - x-content-type-options: nosniff
#   - last-modified: Sat, 28 Nov 2020 11:59:12 GMT
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:12 GMT; Max-Age=1800; Secure
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 30
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    'cache-control': 'no-cache',
    ':path': '/shop/delivery-message?parts.0=MGN73LL%2FA&parts.1=MGNE3LL%2FA&parts.2=MGNA3LL%2FA&mt=regular&_=1606564751170',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('_', '1606564751170'),
    ('parts.0', 'MGN73LL%2FA'),
    ('mt', 'regular'),
    ('parts.2', 'MGNA3LL%2FA'),
    ('parts.1', 'MGNE3LL%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - date: Sat, 28 Nov 2020 11:59:12 GMT
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:12 GMT; Max-Age=315360000; Secure; HttpOnly
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-length: 2619
#   - etag: "f1dc33a1bc6f26266fa75dd39892cf7f"
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:12 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-shred: ca3cb5c31fa3b6c39550dfd82fe8fd52
#   - expires: Sat, 28 Nov 2020 11:59:12 GMT
#   - pragma: no-cache
#   - server: Apple
#   - x-content-type-options: nosniff
#   - x-request-id: ae22c422-f75b-4ea8-b928-2c1c9b160603
#   - last-modified: Sat, 28 Nov 2020 11:59:12 GMT
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:12 GMT; Max-Age=1800; Secure
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 31
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    'cache-control': 'no-cache',
    ':path': '/shop/retail/pickup-message?parts.0=MGN63LL%2FA&parts.1=MGND3LL%2FA&parts.2=MGN93LL%2FA',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts.1', 'MGND3LL%2FA'),
    ('parts.2', 'MGN93LL%2FA'),
    ('parts.0', 'MGN63LL%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 11:59:13 GMT
#   - x-xss-protection: 1; mode=block
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:13 GMT; Max-Age=1800; Secure
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - etag: "85b8326af30304fc90fdc4226363d716"
#   - expires: Sat, 28 Nov 2020 11:59:13 GMT
#   - pragma: no-cache
#   - x-request-id: 528d7d97-2da7-4774-bd0e-fbe6dbe95770
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:13 GMT; Max-Age=315360000; Secure; HttpOnly
#   - server: Apple
#   - x-shred: 35b6794469e915901a08352fe9580c48
#   - x-content-type-options: nosniff
#   - last-modified: Sat, 28 Nov 2020 11:59:13 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:13 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - content-length: 678
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 32
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    ':path': '/shop/retail/pickup-message?parts.0=MGN73LL%2FA&parts.1=MGNE3LL%2FA&parts.2=MGNA3LL%2FA',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts.2', 'MGNA3LL%2FA'),
    ('parts.1', 'MGNE3LL%2FA'),
    ('parts.0', 'MGN73LL%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 11:59:13 GMT
#   - x-xss-protection: 1; mode=block
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:13 GMT; Max-Age=1800; Secure
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - etag: "160c59faae07886437ad8f608e70d68a"
#   - expires: Sat, 28 Nov 2020 11:59:13 GMT
#   - pragma: no-cache
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:13 GMT; Max-Age=315360000; Secure; HttpOnly
#   - server: Apple
#   - x-request-id: 05e26a26-6a43-4f82-926f-9c601481e23d
#   - x-content-type-options: nosniff
#   - x-shred: eb19244e18d35204ecc9bb94b193aea3
#   - last-modified: Sat, 28 Nov 2020 11:59:13 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:13 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - content-length: 678
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 33
# resource type: xhr

url = 'https://www.apple.com/shop/updateFinanceSummary'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    'cache-control': 'no-cache',
    'accept': '*/*',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D; pxro=1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':path': '/shop/updateFinanceSummary?node=home/shop_mac/family/macbook_air&parts.0=MGN63LL%2FA&parts.1=MGND3LL%2FA&parts.2=MGN93LL%2FA&parts.3=MGN73LL%2FA&parts.4=MGNE3LL%2FA&parts.5=MGNA3LL%2FA&tia=&bfil=2',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_sq': '%5B%5BB%5D%5D',
    'pxro': '1',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts.4', 'MGNE3LL%2FA'),
    ('bfil', '2'),
    ('parts.1', 'MGND3LL%2FA'),
    ('parts.3', 'MGN73LL%2FA'),
    ('parts.0', 'MGN63LL%2FA'),
    ('tia', ''),
    ('parts.5', 'MGNA3LL%2FA'),
    ('parts.2', 'MGN93LL%2FA'),
    ('node', 'home/shop_mac/family/macbook_air'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:13 GMT; Path=/; Secure
#   - date: Sat, 28 Nov 2020 11:59:13 GMT
#   - expires: Sat, 28 Nov 2020 12:01:13 GMT
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - last-modified: Sat, 28 Nov 2020 11:28:57 GMT
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:13 GMT; Max-Age=315360000; Secure; HttpOnly
#   - server: Apple
#   - x-request-id: 4fc2504a-35ec-4da6-8d1d-7ba5fe79924e
#   - content-length: 579
#   - cache-control: private, max-age=120
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - x-content-type-options: nosniff
#   - etag: "5bcb2ab803df32a2a73aeffdbade92ab"
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:13 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-shred: 0dd9a43f1b36cf58415b8c91e1d52ee1
#   - content-type: application/json;charset=utf-8
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 34
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s55089049129067'
headers = {
    'Referer': 'https://www.apple.com/',
    'Content-Type': 'text/plain;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
params = [
    ('v94', '1.07'),
    ('bh', '630'),
    ('k', 'Y'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fmacbook-air%2F'),
    ('AQB', '1'),
    ('server', 'as-13.5.0'),
    ('c14', 'macbook%20air%20-%20overview%20%28us%29'),
    ('pageName', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('events', 'event210%3D1.07%2Cevent246'),
    ('c40', '10078'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air'),
    ('pf', '1'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('c', '24'),
    ('ndh', '1'),
    ('c8', 'AOS%3A%20Mac'),
    ('cc', 'USD'),
    ('pev2', 'Step%201'),
    ('ce', 'UTF-8'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('bw', '1420'),
    ('v', 'N'),
    ('v4', 'D%3DpageName'),
    ('t', '28%2F10%2F2020%2012%3A59%3A13%206%20-60'),
    ('c4', 'D%3Dg'),
    ('v97', 's.tl-o'),
    ('lrt', '724'),
    ('v19', 'D%3Dc19'),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('AQE', '1'),
    ('c5', 'macintel'),
    ('s', '1920x1080'),
    ('j', '1.6'),
    ('v49', 'D%3Dr'),
    ('v14', 'en-us'),
    ('v35', 'web%20apply%7Cdenied%7Cpre%3Anot%20safari'),
    ('pe', 'lnk_o'),
    ('v54', 'D%3Dg'),
]
rc = s.post(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 35
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'accept': '*/*',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D; pxro=1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_sq': '%5B%5BB%5D%5D',
    'pxro': '1',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
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
#   - date: Sat, 28 Nov 2020 11:59:13 GMT
#   - strict-transport-security: max-age=31536000; includeSubdomains
#   - x-xss-protection: 1; mode=block
#   - x-content-type-options: nosniff
#   - cache-control: max-age=97
#   - server: Apple
#   - x-frame-options: SAMEORIGIN
#   - x-frame-options: DENY
#   - content-length: 579
#   - expires: Sat, 28 Nov 2020 12:00:50 GMT
#   - content-type: application/json
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 36
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s57395114027206'
headers = {
    'Referer': 'https://www.apple.com/',
    'Content-Type': 'text/plain;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
params = [
    ('bh', '630'),
    ('k', 'Y'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fmacbook-air%2F'),
    ('AQB', '1'),
    ('server', 'as-13.5.0'),
    ('c14', 'macbook%20air%20-%20overview%20%28us%29'),
    ('events', 'event33%2Cevent210%3D1.39%2Cevent246'),
    ('pageName', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('c40', '10078'),
    ('v94', '1.39'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air'),
    ('pf', '1'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('lrt', '1'),
    ('c', '24'),
    ('ndh', '1'),
    ('c8', 'AOS%3A%20Mac'),
    ('cc', 'USD'),
    ('ce', 'UTF-8'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('c37', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect%7Ccold%20start'),
    ('bw', '1420'),
    ('v', 'N'),
    ('v4', 'D%3DpageName'),
    ('pev2', 'Cold'),
    ('t', '28%2F10%2F2020%2012%3A59%3A13%206%20-60'),
    ('c4', 'D%3Dg'),
    ('v97', 's.tl-o'),
    ('v19', 'D%3Dc19'),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('AQE', '1'),
    ('c5', 'macintel'),
    ('s', '1920x1080'),
    ('j', '1.6'),
    ('v49', 'D%3Dr'),
    ('v14', 'en-us'),
    ('pe', 'lnk_o'),
    ('v54', 'D%3Dg'),
]
rc = s.post(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 37
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D; pxro=1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-dest': 'image',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':path': '/favicon.ico',
    'sec-fetch-mode': 'no-cors',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    ':method': 'GET',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_sq': '%5B%5BB%5D%5D',
    'pxro': '1',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-type: image/x-icon
#   - server: Apache
#   - x-content-type-options: nosniff
#   - cache-control: max-age=196
#   - content-length: 22382
#   - accept-ranges: bytes
#   - date: Sat, 28 Nov 2020 11:59:14 GMT
#   - expires: Sat, 28 Nov 2020 12:02:30 GMT
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 38
# resource type: xhr

url = 'https://store.storeimages.cdn-apple.com/4982/store.apple.com/shop/rs-external/rel/external.js'
headers = {
    'Host': 'store.storeimages.cdn-apple.com',
    'Sec-Fetch-Dest': 'empty',
    'Connection': 'keep-alive',
    'Sec-Fetch-Site': 'cross-site',
    'Referer': 'https://www.apple.com/',
    'Accept': '*/*',
    'Sec-Fetch-Mode': 'cors',
    'Accept-Language': 'en-US,en;q=0.9',
    'Origin': 'https://www.apple.com',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - Server: Apple
#   - Content-Encoding: gzip
#   - X-Frame-Options: DENY
#   - Date: Sat, 28 Nov 2020 11:59:14 GMT
#   - Cache-Control: max-age=85
#   - Accept-Ranges: bytes
#   - X-XSS-Protection: 1; mode=block
#   - Connection: keep-alive
#   - Content-Security-Policy: frame-ancestors 'none'
#   - x-shred: 73dc9cc218b4d274a506b1659d8cc044
#   - X-Cache: TCP_HIT from a92-122-95-84.deploy.akamaitechnologies.com (AkamaiGHost/10.2.2.1-31386017) (-)
#   - Expires: Sat, 28 Nov 2020 12:00:39 GMT
#   - X-Content-Type-Options: nosniff
#   - Vary: Accept-Encoding
#   - Last-Modified: Sat, 31 Oct 2020 06:14:18 GMT
#   - X-CDN: Akam
#   - Access-Control-Allow-Origin: *
#   - Content-Type: application/javascript
#   - Content-Length: 141036
#   - ETag: "7dfa5-5b2f16c562280-gzip"
#   - Strict-Transport-Security: max-age=31536000
#   - Access-Control-Expose-Headers: X-CDN
###############################################################################

###############################################################################
# request number: 39
# resource type: other

url = 'https://xp.apple.com/report/2/xp_aos_clientperf'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Dest': 'empty',
    'Connection': 'keep-alive',
    'Access-Control-Request-Method': 'POST',
    'Referer': 'https://www.apple.com/',
    'Accept': '*/*',
    'Host': 'xp.apple.com',
    'Sec-Fetch-Mode': 'cors',
    'Origin': 'https://www.apple.com',
    'Cache-Control': 'no-cache',
    'Accept-Language': 'en-US,en;q=0.9',
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'Access-Control-Request-Headers': 'content-type',
}
rc = s.options(url, headers=headers)


# response status code: 200
# response headers:
#   - Access-Control-Allow-Headers: content-type
#   - X-Apple-Application-Instance: 233
#   - Access-Control-Allow-Origin: https://www.apple.com
#   - Strict-Transport-Security: max-age=31536000
#   - X-Apple-Jingle-Correlation-Key: 2X6YU2T3HN72ZRDQTFTUHWKPTA
#   - Access-Control-Allow-Methods: POST
#   - X-Apple-Application-Site: ST
#   - Date: Sat, 28 Nov 2020 11:59:14 GMT
#   - Connection: keep-alive
#   - Access-Control-Max-Age: 86400
#   - Access-Control-Allow-Credentials: true
#   - Content-Length: 0
###############################################################################

###############################################################################
# request number: 40
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s56893829888064'
headers = {
    'Referer': 'https://www.apple.com/',
    'Content-Type': 'text/plain;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
params = [
    ('v6', 'D%3DpageName%2B%22%7C%7C%7CStep%201%20-%20Select%20Button%7Cselected%22'),
    ('bh', '630'),
    ('oidt', '3'),
    ('k', 'Y'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fmacbook-air%2F'),
    ('AQB', '1'),
    ('activitymap.', ''),
    ('server', 'as-13.5.0'),
    ('lrt', '91'),
    ('c14', 'macbook%20air%20-%20overview%20%28us%29'),
    ('pidt', '1'),
    ('region', 'body'),
    ('pageName', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('c40', '10078'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air'),
    ('pf', '1'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('c.', ''),
    ('events', 'event210%3D7.01%2Cevent246%2Cevent500'),
    ('.c', ''),
    ('c', '24'),
    ('ndh', '1'),
    ('c8', 'AOS%3A%20Mac'),
    ('cc', 'USD'),
    ('ce', 'UTF-8'),
    ('t', '28%2F10%2F2020%2012%3A59%3A19%206%20-60'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('page', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('bw', '1420'),
    ('.a', ''),
    ('.activitymap', ''),
    ('v94', '7.01'),
    ('v', 'N'),
    ('v4', 'D%3DpageName'),
    ('ot', 'SUBMIT'),
    ('c4', 'D%3Dg'),
    ('v97', 's.tl-o'),
    ('pid', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('pageIDType', '1'),
    ('v19', 'D%3Dc19'),
    ('a.', ''),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('oid', 'proceed'),
    ('AQE', '1'),
    ('c5', 'macintel'),
    ('s', '1920x1080'),
    ('j', '1.6'),
    ('v49', 'D%3Dr'),
    ('v14', 'en-us'),
    ('pe', 'lnk_o'),
    ('pev2', 'undefined%7CStep%201%20-%20Select%20Button%7Cselected'),
    ('v54', 'D%3Dg'),
    ('link', 'select%20apple%20m1%20chip%20with%208core%20cpu%20and%207core%20gpu%20%7C%20no%20href%20%7C%20body'),
]
rc = s.post(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 41
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':path': '/shop/delivery-message?parts.0=MGN63LL%2FA&option.0=065-C99M%2C065-C99Q%2C065-C9DG%2C065-C171%2C065-C172&mt=regular&_=1606564760188',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('mt', 'regular'),
    ('_', '1606564760188'),
    ('option.0', '065-C99M%2C065-C99Q%2C065-C9DG%2C065-C171%2C065-C172'),
    ('parts.0', 'MGN63LL%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - expires: Sat, 28 Nov 2020 11:59:21 GMT
#   - x-shred: 149ff2d0d584f4bc505369f987b35dc5
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:21 GMT; Max-Age=1800; Secure
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:21 GMT; Max-Age=315360000; Secure; HttpOnly
#   - last-modified: Sat, 28 Nov 2020 11:59:21 GMT
#   - content-length: 1081
#   - x-request-id: b5308b25-7b34-4be5-b7b9-07d9e520deb8
#   - pragma: no-cache
#   - date: Sat, 28 Nov 2020 11:59:21 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:21 GMT; Max-Age=315360000; Secure; HttpOnly
#   - server: Apple
#   - etag: "78649f7e4831b77dc7e079f490707d00"
#   - x-content-type-options: nosniff
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 42
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s54378695892321'
headers = {
    'Referer': 'https://www.apple.com/',
    'Content-Type': 'text/plain;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
params = [
    ('bh', '630'),
    ('k', 'Y'),
    ('AQB', '1'),
    ('server', 'as-13.5.0'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air%2Fspace-gray-apple-m1-chip-with-8%25E2%2580%2591core-cpu-and-7%25E2%2580%2591core-gpu-256gb%23'),
    ('c40', '10078'),
    ('pf', '1'),
    ('events', 'event210%3D0.96%2Cevent246'),
    ('c', '24'),
    ('ndh', '1'),
    ('c8', 'AOS%3A%20Mac'),
    ('cc', 'USD'),
    ('pev2', 'Step%201'),
    ('ce', 'UTF-8'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air'),
    ('bw', '1420'),
    ('t', '28%2F10%2F2020%2012%3A59%3A21%206%20-60'),
    ('v', 'N'),
    ('v4', 'D%3DpageName'),
    ('c4', 'D%3Dg'),
    ('v97', 's.tl-o'),
    ('pageName', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('c14', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('v19', 'D%3Dc19'),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('AQE', '1'),
    ('v94', '0.96'),
    ('c5', 'macintel'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('s', '1920x1080'),
    ('j', '1.6'),
    ('v49', 'D%3Dr'),
    ('lrt', '598'),
    ('v14', 'en-us'),
    ('v35', 'web%20apply%7Cdenied%7Cpre%3Anot%20safari'),
    ('pe', 'lnk_o'),
    ('v54', 'D%3Dg'),
]
rc = s.post(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 43
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'accept': '*/*',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
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
#   - cache-control: max-age=88
#   - strict-transport-security: max-age=31536000; includeSubdomains
#   - x-xss-protection: 1; mode=block
#   - x-content-type-options: nosniff
#   - server: Apple
#   - x-frame-options: SAMEORIGIN
#   - x-frame-options: DENY
#   - content-length: 579
#   - expires: Sat, 28 Nov 2020 12:00:50 GMT
#   - date: Sat, 28 Nov 2020 11:59:22 GMT
#   - content-type: application/json
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 44
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    ':path': '/shop/retail/pickup-message?parts.0=MGN63LL%2FA&option.0=065-C99M%2C065-C99Q%2C065-C9DG%2C065-C171%2C065-C172',
    'sec-fetch-dest': 'empty',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('option.0', '065-C99M%2C065-C99Q%2C065-C9DG%2C065-C171%2C065-C172'),
    ('parts.0', 'MGN63LL%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - expires: Sat, 28 Nov 2020 11:59:22 GMT
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - content-length: 292
#   - server: Apple
#   - etag: "775cdf1983cc35d0363d91d0132a6700"
#   - last-modified: Sat, 28 Nov 2020 11:59:22 GMT
#   - x-content-type-options: nosniff
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:22 GMT; Max-Age=1800; Secure
#   - x-shred: 38f3b09344ed283b0fe7a29c188c5bd5
#   - date: Sat, 28 Nov 2020 11:59:22 GMT
#   - x-request-id: ceaba216-9341-4e35-ba5a-ff1cb9336699
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 45
# resource type: xhr

url = 'https://www.apple.com/shop/configUpdate/MGN63LL/A'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    ':path': '/shop/configUpdate/MGN63LL/A?node=home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig&option.memory__dummy_z124=065-C99M&option.hard_drivesolid_state_drive__dummy_z124=065-C99Q&option.keyboard_and_documentation_z124=065-C9DG&option.sw_final_cut_pro_x_z124=065-C171&option.sw_logic_pro_x_z124=065-C172&product=MGN63LL%2FA&step=config&bfil=2',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('product', 'MGN63LL%2FA'),
    ('bfil', '2'),
    ('option.keyboard_and_documentation_z124', '065-C9DG'),
    ('step', 'config'),
    ('option.memory__dummy_z124', '065-C99M'),
    ('node', 'home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('option.sw_final_cut_pro_x_z124', '065-C171'),
    ('option.sw_logic_pro_x_z124', '065-C172'),
    ('option.hard_drivesolid_state_drive__dummy_z124', '065-C99Q'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - cache-control: private, max-age=59
#   - x-xss-protection: 1; mode=block
#   - expires: Sat, 28 Nov 2020 12:00:21 GMT
#   - x-frame-options: DENY
#   - last-modified: Sat, 28 Nov 2020 11:58:22 GMT
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:22 GMT; Path=/; Secure
#   - content-security-policy: frame-ancestors 'none'
#   - content-length: 1970
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-request-id: 4910bd54-cca2-4f95-9e07-045127c24e79
#   - x-shred: 80020217b73f20b8728c4453e23d4864
#   - server: Apple
#   - content-type: application/json; encoding=UTF8;charset=UTF-8
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - x-content-type-options: nosniff
#   - date: Sat, 28 Nov 2020 11:59:22 GMT
#   - etag: "23991255b5e8a8029161ec433ec0ca9f"
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 46
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s5719408662668'
headers = {
    'Referer': 'https://www.apple.com/',
    'Content-Type': 'text/plain;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
params = [
    ('bh', '630'),
    ('k', 'Y'),
    ('AQB', '1'),
    ('server', 'as-13.5.0'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air%2Fspace-gray-apple-m1-chip-with-8%25E2%2580%2591core-cpu-and-7%25E2%2580%2591core-gpu-256gb%23'),
    ('c40', '10078'),
    ('t', '28%2F10%2F2020%2012%3A59%3A22%206%20-60'),
    ('pf', '1'),
    ('lrt', '1'),
    ('c', '24'),
    ('ndh', '1'),
    ('c8', 'AOS%3A%20Mac'),
    ('cc', 'USD'),
    ('ce', 'UTF-8'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air'),
    ('bw', '1420'),
    ('v', 'N'),
    ('v4', 'D%3DpageName'),
    ('pev2', 'Cold'),
    ('c4', 'D%3Dg'),
    ('v97', 's.tl-o'),
    ('pageName', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('c14', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('v19', 'D%3Dc19'),
    ('events', 'event33%2Cevent210%3D1.33%2Cevent246'),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('AQE', '1'),
    ('c5', 'macintel'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('v94', '1.33'),
    ('s', '1920x1080'),
    ('v49', 'D%3Dr'),
    ('j', '1.6'),
    ('v14', 'en-us'),
    ('pe', 'lnk_o'),
    ('v54', 'D%3Dg'),
    ('c37', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig%7Ccold%20start'),
]
rc = s.post(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 47
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    ':path': '/shop/delivery-message?parts.0=MGN63LL%2FA&option.0=065-C99J%2C065-C99M%2C065-C99Q%2C065-C9CL%2C065-C9DG%2C065-C9CK%2C065-C9CH%2C065-C9CJ%2C065-C171%2C065-C172&mt=regular&_=1606564760189',
    'cache-control': 'no-cache',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('option.0', '065-C99J%2C065-C99M%2C065-C99Q%2C065-C9CL%2C065-C9DG%2C065-C9CK%2C065-C9CH%2C065-C9CJ%2C065-C171%2C065-C172'),
    ('mt', 'regular'),
    ('parts.0', 'MGN63LL%2FA'),
    ('_', '1606564760189'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-cache: TCP_MISS from a92-122-95-54.deploy.akamaitechnologies.com (AkamaiGHost/10.2.2.1-31386017) (-)
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - expires: Sat, 28 Nov 2020 11:59:22 GMT
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-length: 1081
#   - pragma: no-cache
#   - server: Apple
#   - etag: "78649f7e4831b77dc7e079f490707d00"
#   - last-modified: Sat, 28 Nov 2020 11:59:22 GMT
#   - x-request-id: ab4e08a8-7bea-468a-be73-7d4c6a0bf9d2
#   - x-shred: b65116103131a52806499f238a7dbd8a
#   - x-content-type-options: nosniff
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:22 GMT; Max-Age=1800; Secure
#   - date: Sat, 28 Nov 2020 11:59:22 GMT
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 48
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    ':path': '/shop/retail/pickup-message?parts.0=MGN63LL%2FA&option.0=065-C99J%2C065-C99M%2C065-C99Q%2C065-C9CL%2C065-C9DG%2C065-C9CK%2C065-C9CH%2C065-C9CJ%2C065-C171%2C065-C172',
    'sec-fetch-dest': 'empty',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('option.0', '065-C99J%2C065-C99M%2C065-C99Q%2C065-C9CL%2C065-C9DG%2C065-C9CK%2C065-C9CH%2C065-C9CJ%2C065-C171%2C065-C172'),
    ('parts.0', 'MGN63LL%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-shred: 96084d670cdc4332526624b546ad82a8
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: DENY
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - expires: Sat, 28 Nov 2020 11:59:22 GMT
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - content-length: 292
#   - server: Apple
#   - etag: "775cdf1983cc35d0363d91d0132a6700"
#   - last-modified: Sat, 28 Nov 2020 11:59:22 GMT
#   - x-request-id: 19ebd534-a76e-4c5f-896b-b22c19e016bf
#   - x-content-type-options: nosniff
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:22 GMT; Max-Age=1800; Secure
#   - date: Sat, 28 Nov 2020 11:59:22 GMT
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 49
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-dest': 'image',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':path': '/favicon.ico',
    'sec-fetch-mode': 'no-cors',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
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
#   - content-type: image/x-icon
#   - cache-control: max-age=188
#   - server: Apache
#   - x-content-type-options: nosniff
#   - content-length: 22382
#   - accept-ranges: bytes
#   - date: Sat, 28 Nov 2020 11:59:22 GMT
#   - expires: Sat, 28 Nov 2020 12:02:30 GMT
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 50
# resource type: xhr

url = 'https://store.storeimages.cdn-apple.com/4982/store.apple.com/shop/rs-external/rel/external.js'
headers = {
    'Host': 'store.storeimages.cdn-apple.com',
    'Sec-Fetch-Dest': 'empty',
    'Connection': 'keep-alive',
    'Sec-Fetch-Site': 'cross-site',
    'Referer': 'https://www.apple.com/',
    'Accept': '*/*',
    'Sec-Fetch-Mode': 'cors',
    'Accept-Language': 'en-US,en;q=0.9',
    'Origin': 'https://www.apple.com',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - Server: Apple
#   - Content-Encoding: gzip
#   - X-Frame-Options: DENY
#   - Accept-Ranges: bytes
#   - X-XSS-Protection: 1; mode=block
#   - Connection: keep-alive
#   - Content-Security-Policy: frame-ancestors 'none'
#   - x-shred: 73dc9cc218b4d274a506b1659d8cc044
#   - X-Cache: TCP_HIT from a92-122-95-84.deploy.akamaitechnologies.com (AkamaiGHost/10.2.2.1-31386017) (-)
#   - Expires: Sat, 28 Nov 2020 12:00:39 GMT
#   - Cache-Control: max-age=76
#   - X-Content-Type-Options: nosniff
#   - Vary: Accept-Encoding
#   - Last-Modified: Sat, 31 Oct 2020 06:14:18 GMT
#   - X-CDN: Akam
#   - Access-Control-Allow-Origin: *
#   - Content-Type: application/javascript
#   - Content-Length: 141036
#   - ETag: "7dfa5-5b2f16c562280-gzip"
#   - Date: Sat, 28 Nov 2020 11:59:23 GMT
#   - Strict-Transport-Security: max-age=31536000
#   - Access-Control-Expose-Headers: X-CDN
###############################################################################

###############################################################################
# request number: 51
# resource type: other

url = 'https://xp.apple.com/report/2/xp_aos_clientperf'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Dest': 'empty',
    'Connection': 'keep-alive',
    'Access-Control-Request-Method': 'POST',
    'Referer': 'https://www.apple.com/',
    'Accept': '*/*',
    'Host': 'xp.apple.com',
    'Sec-Fetch-Mode': 'cors',
    'Origin': 'https://www.apple.com',
    'Cache-Control': 'no-cache',
    'Accept-Language': 'en-US,en;q=0.9',
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'Access-Control-Request-Headers': 'content-type',
}
rc = s.options(url, headers=headers)


# response status code: 200
# response headers:
#   - Access-Control-Allow-Headers: content-type
#   - Access-Control-Allow-Origin: https://www.apple.com
#   - Strict-Transport-Security: max-age=31536000
#   - Date: Sat, 28 Nov 2020 11:59:23 GMT
#   - Access-Control-Allow-Methods: POST
#   - X-Apple-Application-Site: ST
#   - Connection: keep-alive
#   - X-Apple-Application-Instance: 245
#   - Access-Control-Max-Age: 86400
#   - Access-Control-Allow-Credentials: true
#   - X-Apple-Jingle-Correlation-Key: FONLIHFLXSISLWNNV27DGHXK64
#   - Content-Length: 0
###############################################################################

###############################################################################
# request number: 52
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s5737338969557'
headers = {
    'Referer': 'https://www.apple.com/',
    'Content-Type': 'text/plain;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
params = [
    ('events', 'scAdd%2Cevent210%3D3.37%2Cevent246%2Cevent500'),
    ('bh', '630'),
    ('oidt', '3'),
    ('v94', '3.37'),
    ('k', 'Y'),
    ('AQB', '1'),
    ('page', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('activitymap.', ''),
    ('server', 'as-13.5.0'),
    ('link', 'add%20to%20bag%20%28inner%20text%29%20%7C%20no%20href%20%7C%20body'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air%2Fspace-gray-apple-m1-chip-with-8%25E2%2580%2591core-cpu-and-7%25E2%2580%2591core-gpu-256gb%23'),
    ('pidt', '1'),
    ('v5', 'D%3DpageName%2B%22%7C%7CCTO%7CAdd%20to%20Bag%22'),
    ('region', 'body'),
    ('oid', 'add-to-cart'),
    ('products', 'macbook_air%3BMGN63%3B1%3B999.00%3B%3B'),
    ('c40', '10078'),
    ('pf', '1'),
    ('t', '28%2F10%2F2020%2012%3A59%3A24%206%20-60'),
    ('pid', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('c.', ''),
    ('.c', ''),
    ('c', '24'),
    ('ndh', '1'),
    ('c8', 'AOS%3A%20Mac'),
    ('cc', 'USD'),
    ('pev2', 'CTO'),
    ('ce', 'UTF-8'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air'),
    ('bw', '1420'),
    ('.a', ''),
    ('.activitymap', ''),
    ('v', 'N'),
    ('v4', 'D%3DpageName'),
    ('ot', 'SUBMIT'),
    ('c4', 'D%3Dg'),
    ('v97', 's.tl-o'),
    ('pageName', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('c14', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('pageIDType', '1'),
    ('v19', 'D%3Dc19'),
    ('a.', ''),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('AQE', '1'),
    ('c5', 'macintel'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('s', '1920x1080'),
    ('j', '1.6'),
    ('v49', 'D%3Dr'),
    ('lrt', '62'),
    ('v14', 'en-us'),
    ('pe', 'lnk_o'),
    ('v54', 'D%3Dg'),
]
rc = s.post(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 53
# resource type: xhr

url = 'https://www.apple.com/shop/bag/status'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/shop/bag/status?apikey=SJHJUH4YFCTTPD4F4',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('apikey', 'SJHJUH4YFCTTPD4F4'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 11:59:26 GMT
#   - x-xss-protection: 1; mode=block
#   - x-request-id: 8951d6e0-5f95-4e54-bce1-0a92dddc9d6c
#   - x-frame-options: DENY
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:26 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - expires: Sat, 28 Nov 2020 11:59:26 GMT
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:26 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-length: 137
#   - pragma: no-cache
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:26 GMT; Max-Age=1800; Secure
#   - server: Apple
#   - cache-control: private, no-cache, no-store, must-revalidate
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - last-modified: Sat, 28 Nov 2020 11:59:26 GMT
#   - x-shred: 4757fcd44d5092fa330c8c24b9a3d3a8
#   - content-type: application/json;charset=utf-8
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 54
# resource type: xhr

url = 'https://www.apple.com/shop/buyFlowAttachConfigProductSummary/MGN63LL/A'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    ':path': '/shop/buyFlowAttachConfigProductSummary/MGN63LL/A?node=home/shop_mac/family/macbook_air&step=attach&bfil=2&product=MGN63LL%2FA&step=attach&option.sw_logic_pro_x_z124=065-C172&option.keyboard_and_documentation_z124=065-C9DG&option.memory__dummy_z124=065-C99M&complete=true&option.hard_drivesolid_state_drive__dummy_z124=065-C99Q&option.sw_final_cut_pro_x_z124=065-C171&proceed=proceed',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('product', 'MGN63LL%2FA'),
    ('bfil', '2'),
    ('option.keyboard_and_documentation_z124', '065-C9DG'),
    ('step', 'attach'),
    ('option.memory__dummy_z124', '065-C99M'),
    ('complete', 'true'),
    ('option.sw_final_cut_pro_x_z124', '065-C171'),
    ('option.hard_drivesolid_state_drive__dummy_z124', '065-C99Q'),
    ('proceed', 'proceed'),
    ('option.sw_logic_pro_x_z124', '065-C172'),
    ('node', 'home/shop_mac/family/macbook_air'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 11:59:26 GMT
#   - content-length: 804
#   - x-shred: 55c0b6ad27ff3f8361949ab2cc096398
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: DENY
#   - x-request-id: 42e3edab-922f-467f-aaf9-f3234fe64051
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:26 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:26 GMT; Max-Age=315360000; Secure; HttpOnly
#   - expires: Sat, 28 Nov 2020 12:01:09 GMT
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:26 GMT; Path=/; Secure
#   - cache-control: private, max-age=103
#   - server: Apple
#   - content-type: application/json; encoding=UTF8;charset=UTF-8
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - etag: "514f19dee4342585b61cc2d5593eed3d"
#   - x-content-type-options: nosniff
#   - last-modified: Sat, 28 Nov 2020 11:59:13 GMT
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 55
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/shop/delivery-message?parts.0=S6124LL%2FA&parts.1=MJ1M2AM%2FA&parts.2=MX0K2AM%2FA&mt=compact&_=1606564765355',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts.0', 'S6124LL%2FA'),
    ('parts.1', 'MJ1M2AM%2FA'),
    ('_', '1606564765355'),
    ('mt', 'compact'),
    ('parts.2', 'MX0K2AM%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - x-shred: d5695525be89f566d66f0bf9367b04c1
#   - pragma: no-cache
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - server: Apple
#   - x-request-id: 9ecaa922-0b00-459b-b585-bf80822d353c
#   - etag: "9869b80006656e76fd565f180c59cf7e"
#   - x-content-type-options: nosniff
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
#   - content-length: 1112
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 56
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'x-requested-with': 'XMLHttpRequest',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    ':path': '/shop/delivery-message?parts.0=MLA02LL%2FA&parts.1=MUF82AM%2FA&parts.2=MRQM2ZM%2FA&mt=compact&_=1606564765356',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts.0', 'MLA02LL%2FA'),
    ('_', '1606564765356'),
    ('parts.2', 'MRQM2ZM%2FA'),
    ('mt', 'compact'),
    ('parts.1', 'MUF82AM%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-shred: b58d219ecf4ac5aa8bcf5107d7aed020
#   - content-length: 1117
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - etag: "db4d166b1b34516deb40fe2d756af67d"
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - x-request-id: ebe0f017-1e99-4609-8e3a-b8a5b61685bc
#   - pragma: no-cache
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - server: Apple
#   - x-content-type-options: nosniff
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 57
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/shop/delivery-message?parts.0=MUFG2AM%2FA&parts.1=MQ4H2AM%2FA&parts.2=MWP22AM%2FA&mt=compact&_=1606564765357',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'sec-fetch-mode': 'cors',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('_', '1606564765357'),
    ('parts.0', 'MUFG2AM%2FA'),
    ('parts.2', 'MWP22AM%2FA'),
    ('mt', 'compact'),
    ('parts.1', 'MQ4H2AM%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-request-id: 14383983-3353-4512-9619-9c24c11763ff
#   - x-xss-protection: 1; mode=block
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - content-length: 1119
#   - pragma: no-cache
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - server: Apple
#   - etag: "7bb2939718ef8efa7be606d9e24d8ee8"
#   - x-shred: 76fa3376927b710e8fba7d20f586cef3
#   - x-content-type-options: nosniff
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 58
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    ':path': '/shop/delivery-message?parts.0=MV7N2AM%2FA&parts.1=MRXJ2AM%2FA&parts.2=MMEL2AM%2FA&mt=compact&_=1606564765358',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('_', '1606564765358'),
    ('parts.0', 'MV7N2AM%2FA'),
    ('mt', 'compact'),
    ('parts.1', 'MRXJ2AM%2FA'),
    ('parts.2', 'MMEL2AM%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - etag: "295c45334086e5878080e8c4be15e2d7"
#   - content-length: 1119
#   - pragma: no-cache
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - server: Apple
#   - x-shred: 59cac7873ddac86c5ce0e54b36cdf169
#   - x-content-type-options: nosniff
#   - x-request-id: 28ef2c16-5533-4835-8de6-4af1a01735b2
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 59
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/shop/delivery-message?parts.0=HMUA2VC%2FA&parts.1=HMUB2LL%2FA&parts.2=MK122LL%2FA&mt=compact&_=1606564765359',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts.2', 'MK122LL%2FA'),
    ('parts.1', 'HMUB2LL%2FA'),
    ('parts.0', 'HMUA2VC%2FA'),
    ('mt', 'compact'),
    ('_', '1606564765359'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-request-id: 50c022da-3af2-4d45-9972-9c47fe20b9b8
#   - x-xss-protection: 1; mode=block
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-length: 1127
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - pragma: no-cache
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - server: Apple
#   - etag: "172c9c75800a5b0a2fe480f7103f933b"
#   - x-shred: fabff9c77206f5d10bb52b9b3c5cc8dd
#   - x-content-type-options: nosniff
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 60
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/shop/delivery-message?parts.0=HMU22ZM%2FA&parts.1=HPA02ZM%2FA&mt=compact&_=1606564765360',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('_', '1606564765360'),
    ('parts.0', 'HMU22ZM%2FA'),
    ('mt', 'compact'),
    ('parts.1', 'HPA02ZM%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-shred: d6fa087576d99bc3fdb2337ccd5b937b
#   - x-xss-protection: 1; mode=block
#   - content-length: 873
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - etag: "a8496c7f3f1fb0a543a1148cb00009e9"
#   - x-request-id: 34dd6b13-21bc-4643-a3be-85fe069ee775
#   - pragma: no-cache
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - server: Apple
#   - x-content-type-options: nosniff
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 61
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':path': '/shop/retail/pickup-message?parts.0=S6124LL%2FA&parts.1=MJ1M2AM%2FA&parts.2=MX0K2AM%2FA&little=true',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts.2', 'MX0K2AM%2FA'),
    ('parts.1', 'MJ1M2AM%2FA'),
    ('little', 'true'),
    ('parts.0', 'S6124LL%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-request-id: cecdb21c-0e80-4bb8-801c-529cbb4b0c04
#   - x-xss-protection: 1; mode=block
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - content-length: 475
#   - pragma: no-cache
#   - etag: "b9e91d6c67a36c5d5d86e2200e136c79"
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - server: Apple
#   - x-shred: 02b2ca61d50382d030ab9047d0938ab7
#   - x-content-type-options: nosniff
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 62
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    ':path': '/shop/retail/pickup-message?parts.0=MLA02LL%2FA&parts.1=MUF82AM%2FA&parts.2=MRQM2ZM%2FA&little=true',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts.0', 'MLA02LL%2FA'),
    ('little', 'true'),
    ('parts.1', 'MUF82AM%2FA'),
    ('parts.2', 'MRQM2ZM%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - expires: Sat, 28 Nov 2020 11:59:28 GMT
#   - pragma: no-cache
#   - server: Apple
#   - x-request-id: 44cb7e08-cac9-4a4f-b28a-f3a756a52d6a
#   - x-shred: fa795f1fdb35467d1ee9d56246bd0d93
#   - last-modified: Sat, 28 Nov 2020 11:59:28 GMT
#   - x-content-type-options: nosniff
#   - date: Sat, 28 Nov 2020 11:59:28 GMT
#   - content-length: 715
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - etag: "69a6bdeb11f22a603cb18448e69980ea"
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 63
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'accept-encoding': 'gzip, deflate, br',
    ':path': '/shop/retail/pickup-message?parts.0=MUFG2AM%2FA&parts.1=MQ4H2AM%2FA&parts.2=MWP22AM%2FA&little=true',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts.0', 'MUFG2AM%2FA'),
    ('little', 'true'),
    ('parts.1', 'MQ4H2AM%2FA'),
    ('parts.2', 'MWP22AM%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: DENY
#   - etag: "f0fd7822f3da9297934ca54ed51bd8a1"
#   - x-request-id: 5c0986a4-f3b8-4969-94dc-74c845c75826
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - expires: Sat, 28 Nov 2020 11:59:28 GMT
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:28 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - server: Apple
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:28 GMT; Max-Age=315360000; Secure; HttpOnly
#   - last-modified: Sat, 28 Nov 2020 11:59:28 GMT
#   - content-length: 661
#   - x-content-type-options: nosniff
#   - x-shred: 34e378b8a5eb20677ffd5a8cea3c785f
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:28 GMT; Max-Age=1800; Secure
#   - date: Sat, 28 Nov 2020 11:59:28 GMT
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 64
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/shop/retail/pickup-message?parts.0=MV7N2AM%2FA&parts.1=MRXJ2AM%2FA&parts.2=MMEL2AM%2FA&little=true',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('little', 'true'),
    ('parts.0', 'MV7N2AM%2FA'),
    ('parts.1', 'MRXJ2AM%2FA'),
    ('parts.2', 'MMEL2AM%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - expires: Sat, 28 Nov 2020 11:59:28 GMT
#   - x-shred: 643ee9168a2909d998e0ed4b328ee159
#   - pragma: no-cache
#   - x-request-id: e85f738a-d42f-4cab-be7c-0662b0bd6554
#   - server: Apple
#   - content-length: 697
#   - last-modified: Sat, 28 Nov 2020 11:59:28 GMT
#   - x-content-type-options: nosniff
#   - etag: "30f5777bcf377a3e177d1c9923bd1b23"
#   - date: Sat, 28 Nov 2020 11:59:28 GMT
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 65
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':path': '/shop/retail/pickup-message?parts.0=HMUA2VC%2FA&parts.1=HMUB2LL%2FA&parts.2=MK122LL%2FA&little=true',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts.0', 'HMUA2VC%2FA'),
    ('little', 'true'),
    ('parts.1', 'HMUB2LL%2FA'),
    ('parts.2', 'MK122LL%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - x-shred: a98c8e51d835d9bc14c21c64ef4fe6aa
#   - pragma: no-cache
#   - x-request-id: 89807fde-3ee0-4947-bfdc-1d839c86f113
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - etag: "a07d206f3ec3c8e28e298fcac08537b3"
#   - server: Apple
#   - content-length: 665
#   - x-content-type-options: nosniff
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 66
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    ':path': '/shop/retail/pickup-message?parts.0=HMU22ZM%2FA&parts.1=HPA02ZM%2FA&little=true',
    'accept-encoding': 'gzip, deflate, br',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':method': 'GET',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts.0', 'HMU22ZM%2FA'),
    ('little', 'true'),
    ('parts.1', 'HPA02ZM%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - x-shred: 36a8946356b07871d144bff4a7bf39f2
#   - etag: "25d909e1f4f92ef25e1622ccd030755d"
#   - pragma: no-cache
#   - content-length: 540
#   - x-request-id: 83de65dd-fbe3-4160-9c52-1fb08ce2145f
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - server: Apple
#   - x-content-type-options: nosniff
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 67
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
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
#   - x-content-type-options: nosniff
#   - cache-control: max-age=82
#   - server: Apple
#   - x-frame-options: SAMEORIGIN
#   - x-frame-options: DENY
#   - content-length: 579
#   - expires: Sat, 28 Nov 2020 12:00:50 GMT
#   - date: Sat, 28 Nov 2020 11:59:28 GMT
#   - content-type: application/json
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 68
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s52456596436101'
headers = {
    'Referer': 'https://www.apple.com/',
    'Content-Type': 'text/plain;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
params = [
    ('bh', '630'),
    ('k', 'Y'),
    ('AQB', '1'),
    ('server', 'as-13.5.0'),
    ('t', '28%2F10%2F2020%2012%3A59%3A28%206%20-60'),
    ('v94', '2.88'),
    ('c14', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('c40', '10078'),
    ('events', 'event33%2Cevent210%3D2.88%2Cevent246'),
    ('pf', '1'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air%3Fbfil%3D2%26product%3DMGN63LL%2FA%26step%3Dattach'),
    ('c', '24'),
    ('ndh', '1'),
    ('c8', 'AOS%3A%20Mac'),
    ('cc', 'USD'),
    ('ce', 'UTF-8'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fattach'),
    ('bw', '1420'),
    ('v', 'N'),
    ('v4', 'D%3DpageName'),
    ('pev2', 'Cold'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air%2Fspace-gray-apple-m1-chip-with-8%25E2%2580%2591core-cpu-and-7%25E2%2580%2591core-gpu-256gb'),
    ('pageName', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fattach'),
    ('lrt', '2503'),
    ('c4', 'D%3Dg'),
    ('c37', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fattach%7Ccold%20start'),
    ('v97', 's.tl-o'),
    ('v19', 'D%3Dc19'),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('AQE', '1'),
    ('c5', 'macintel'),
    ('s', '1920x1080'),
    ('j', '1.6'),
    ('v49', 'D%3Dr'),
    ('v14', 'en-us'),
    ('pe', 'lnk_o'),
    ('v54', 'D%3Dg'),
]
rc = s.post(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 69
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-dest': 'image',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':path': '/favicon.ico',
    'sec-fetch-mode': 'no-cors',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
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
#   - content-type: image/x-icon
#   - server: Apache
#   - x-content-type-options: nosniff
#   - cache-control: max-age=181
#   - date: Sat, 28 Nov 2020 11:59:29 GMT
#   - content-length: 22382
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 12:02:30 GMT
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 70
# resource type: xhr

url = 'https://store.storeimages.cdn-apple.com/4982/store.apple.com/shop/rs-external/rel/external.js'
headers = {
    'Host': 'store.storeimages.cdn-apple.com',
    'Sec-Fetch-Dest': 'empty',
    'Connection': 'keep-alive',
    'Sec-Fetch-Site': 'cross-site',
    'Referer': 'https://www.apple.com/',
    'Accept': '*/*',
    'Sec-Fetch-Mode': 'cors',
    'Accept-Language': 'en-US,en;q=0.9',
    'Origin': 'https://www.apple.com',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - Server: Apple
#   - Content-Encoding: gzip
#   - X-Frame-Options: DENY
#   - Accept-Ranges: bytes
#   - X-XSS-Protection: 1; mode=block
#   - Connection: keep-alive
#   - Content-Security-Policy: frame-ancestors 'none'
#   - x-shred: 73dc9cc218b4d274a506b1659d8cc044
#   - X-Cache: TCP_HIT from a92-122-95-84.deploy.akamaitechnologies.com (AkamaiGHost/10.2.2.1-31386017) (-)
#   - Expires: Sat, 28 Nov 2020 12:00:39 GMT
#   - X-Content-Type-Options: nosniff
#   - Vary: Accept-Encoding
#   - Date: Sat, 28 Nov 2020 11:59:30 GMT
#   - Last-Modified: Sat, 31 Oct 2020 06:14:18 GMT
#   - X-CDN: Akam
#   - Access-Control-Allow-Origin: *
#   - Content-Type: application/javascript
#   - Content-Length: 141036
#   - ETag: "7dfa5-5b2f16c562280-gzip"
#   - Strict-Transport-Security: max-age=31536000
#   - Access-Control-Expose-Headers: X-CDN
#   - Cache-Control: max-age=69
###############################################################################

###############################################################################
# request number: 71
# resource type: other

url = 'https://xp.apple.com/report/2/xp_aos_clientperf'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Dest': 'empty',
    'Connection': 'keep-alive',
    'Access-Control-Request-Method': 'POST',
    'Referer': 'https://www.apple.com/',
    'Accept': '*/*',
    'Host': 'xp.apple.com',
    'Sec-Fetch-Mode': 'cors',
    'Origin': 'https://www.apple.com',
    'Cache-Control': 'no-cache',
    'Accept-Language': 'en-US,en;q=0.9',
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'Access-Control-Request-Headers': 'content-type',
}
rc = s.options(url, headers=headers)


# response status code: 200
# response headers:
#   - Access-Control-Allow-Headers: content-type
#   - Access-Control-Allow-Origin: https://www.apple.com
#   - Strict-Transport-Security: max-age=31536000
#   - Access-Control-Allow-Methods: POST
#   - X-Apple-Application-Site: ST
#   - X-Apple-Jingle-Correlation-Key: ULPZODFXG2RFWYZZ5FVCBTIXGY
#   - Connection: keep-alive
#   - Access-Control-Max-Age: 86400
#   - Access-Control-Allow-Credentials: true
#   - Date: Sat, 28 Nov 2020 11:59:30 GMT
#   - X-Apple-Application-Instance: 246
#   - Content-Length: 0
###############################################################################

###############################################################################
# request number: 72
# resource type: xhr

url = 'https://www.apple.com/shop/bag/status'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/shop/bag/status?apikey=SJHJUH4YFCTTPD4F4',
    'referer': 'https://www.apple.com/shop/bag',
    'pragma': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; as_xs=flc=; as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; s_sq=%5B%5BB%5D%5D',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'as_xsm': '1&TsS1k4znjEvnGjBoAe_vvw',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_xs': 'flc=',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('apikey', 'SJHJUH4YFCTTPD4F4'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-request-id: 0f191352-02fb-4708-9389-131847f017fa
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 11:59:32 GMT
#   - content-security-policy: frame-ancestors 'none'
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:32 GMT; Max-Age=1800; Secure
#   - content-length: 137
#   - last-modified: Sat, 28 Nov 2020 11:59:32 GMT
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:32 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - x-shred: 076f68c1c717e2a5694dc93e60255ed1
#   - server: Apple
#   - date: Sat, 28 Nov 2020 11:59:32 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:32 GMT; Max-Age=315360000; Secure; HttpOnly
#   - cache-control: private, no-cache, no-store, must-revalidate
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - content-type: application/json;charset=utf-8
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 73
# resource type: xhr

url = 'https://www.apple.com/shop/recommendedForYou-full'
headers = {
    'x-aos-model-page': 'cart',
    'referer': 'https://www.apple.com/shop/bag',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':path': '/shop/recommendedForYou-full?partsInCart.0=MGN63LL/A&inline=true&recentAddedPart=MGN63LL/A',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; as_xs=flc=; as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; s_sq=%5B%5BB%5D%5D',
    'accept-encoding': 'gzip, deflate, br',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.apple.com',
    'cache-control': 'no-cache',
    ':method': 'POST',
    'accept': '*/*',
    'content-length': '0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'modelversion': 'v2',
    'syntax': 'graviton',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'x-requested-with': 'XMLHttpRequest',
    'x-aos-stk': '9b49e9bc',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'as_xsm': '1&TsS1k4znjEvnGjBoAe_vvw',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_xs': 'flc=',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('inline', 'true'),
    ('recentAddedPart', 'MGN63LL/A'),
    ('partsInCart.0', 'MGN63LL/A'),
]
rc = s.post(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-xss-protection: 1; mode=block
#   - x-request-id: f3c431bd-e6b5-4411-bdfd-f884c43b93b0
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 11:59:32 GMT
#   - set-cookie: as_xs=flc=; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:32 GMT; Max-Age=15552000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:32 GMT; Max-Age=1800; Secure
#   - access-control-allow-origin: https://www.apple.com
#   - last-modified: Sat, 28 Nov 2020 11:59:32 GMT
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:32 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-shred: 5cc55ea61f50b8ff9215e484c70a0e3d
#   - pragma: no-cache
#   - server: Apple
#   - set-cookie: as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:32 GMT; Max-Age=15552000; Secure; HttpOnly
#   - date: Sat, 28 Nov 2020 11:59:32 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:32 GMT; Max-Age=315360000; Secure; HttpOnly
#   - etag: "88836b1c32feac9edc46b3e946530b53"
#   - x-content-type-options: nosniff
#   - content-length: 12731
#   - access-control-allow-credentials: true
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_xsm: 1&TsS1k4znjEvnGjBoAe_vvw
#   - dssf: 1
#   - as_dc: nc
#   - as_xs: flc=
###############################################################################

###############################################################################
# request number: 74
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/shop/bag',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; as_xs=flc=; as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; s_sq=%5B%5BB%5D%5D',
    ':method': 'GET',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'as_xsm': '1&TsS1k4znjEvnGjBoAe_vvw',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_xs': 'flc=',
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
#   - x-content-type-options: nosniff
#   - cache-control: max-age=78
#   - server: Apple
#   - x-frame-options: SAMEORIGIN
#   - x-frame-options: DENY
#   - content-length: 579
#   - expires: Sat, 28 Nov 2020 12:00:50 GMT
#   - date: Sat, 28 Nov 2020 11:59:32 GMT
#   - content-type: application/json
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 75
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'referer': 'https://www.apple.com/shop/bag',
    'accept-language': 'en-US,en;q=0.9',
    'pragma': 'no-cache',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-dest': 'image',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    ':path': '/favicon.ico',
    'sec-fetch-mode': 'no-cors',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; as_xs=flc=; as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; s_sq=%5B%5BB%5D%5D',
    'cache-control': 'no-cache',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'as_xsm': '1&TsS1k4znjEvnGjBoAe_vvw',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_xs': 'flc=',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - date: Sat, 28 Nov 2020 11:59:33 GMT
#   - content-type: image/x-icon
#   - server: Apache
#   - x-content-type-options: nosniff
#   - x-cache: TCP_MEM_HIT from a92-122-95-54.deploy.akamaitechnologies.com (AkamaiGHost/10.2.2.1-31386017) (-)
#   - content-length: 22382
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 12:02:30 GMT
#   - cache-control: max-age=177
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 76
# resource type: xhr

url = 'https://store.storeimages.cdn-apple.com/4982/store.apple.com/shop/rs-external/rel/external.js'
headers = {
    'Host': 'store.storeimages.cdn-apple.com',
    'Sec-Fetch-Dest': 'empty',
    'Connection': 'keep-alive',
    'Sec-Fetch-Site': 'cross-site',
    'Referer': 'https://www.apple.com/',
    'Accept': '*/*',
    'Sec-Fetch-Mode': 'cors',
    'Accept-Language': 'en-US,en;q=0.9',
    'Origin': 'https://www.apple.com',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - Server: Apple
#   - Content-Encoding: gzip
#   - X-Frame-Options: DENY
#   - Cache-Control: max-age=66
#   - Accept-Ranges: bytes
#   - X-XSS-Protection: 1; mode=block
#   - Connection: keep-alive
#   - Content-Security-Policy: frame-ancestors 'none'
#   - x-shred: 73dc9cc218b4d274a506b1659d8cc044
#   - X-Cache: TCP_HIT from a92-122-95-84.deploy.akamaitechnologies.com (AkamaiGHost/10.2.2.1-31386017) (-)
#   - Expires: Sat, 28 Nov 2020 12:00:39 GMT
#   - X-Content-Type-Options: nosniff
#   - Vary: Accept-Encoding
#   - Last-Modified: Sat, 31 Oct 2020 06:14:18 GMT
#   - X-CDN: Akam
#   - Date: Sat, 28 Nov 2020 11:59:33 GMT
#   - Access-Control-Allow-Origin: *
#   - Content-Type: application/javascript
#   - Content-Length: 141036
#   - ETag: "7dfa5-5b2f16c562280-gzip"
#   - Strict-Transport-Security: max-age=31536000
#   - Access-Control-Expose-Headers: X-CDN
###############################################################################

###############################################################################
# request number: 77
# resource type: other

url = 'https://xp.apple.com/report/2/xp_aos_clientperf'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Dest': 'empty',
    'Connection': 'keep-alive',
    'Access-Control-Request-Method': 'POST',
    'Referer': 'https://www.apple.com/',
    'Accept': '*/*',
    'Host': 'xp.apple.com',
    'Sec-Fetch-Mode': 'cors',
    'Origin': 'https://www.apple.com',
    'Cache-Control': 'no-cache',
    'Accept-Language': 'en-US,en;q=0.9',
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'Access-Control-Request-Headers': 'content-type',
}
rc = s.options(url, headers=headers)


# response status code: 200
# response headers:
#   - Access-Control-Allow-Headers: content-type
#   - Access-Control-Allow-Origin: https://www.apple.com
#   - Strict-Transport-Security: max-age=31536000
#   - Access-Control-Allow-Methods: POST
#   - X-Apple-Application-Site: ST
#   - Connection: keep-alive
#   - Access-Control-Max-Age: 86400
#   - Access-Control-Allow-Credentials: true
#   - X-Apple-Application-Instance: 251
#   - X-Apple-Jingle-Correlation-Key: 7T6U7HPVMXMQL3V57DTOS33MAM
#   - Content-Length: 0
#   - Date: Sat, 28 Nov 2020 11:59:33 GMT
###############################################################################

###############################################################################
# request number: 78
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s52405784184661'
headers = {
    'Referer': 'https://www.apple.com/',
    'Content-Type': 'text/plain;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
params = [
    ('bh', '630'),
    ('oidt', '3'),
    ('k', 'Y'),
    ('AQB', '1'),
    ('activitymap.', ''),
    ('server', 'as-13.5.0'),
    ('pidt', '1'),
    ('page', 'AOS%3A%20bag'),
    ('lrt', '61'),
    ('region', 'body'),
    ('c40', '10078'),
    ('c14', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fattach'),
    ('pf', '1'),
    ('v94', '6.08'),
    ('t', '28%2F10%2F2020%2012%3A59%3A37%206%20-60'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20bag'),
    ('c.', ''),
    ('v39', 'D%3DpageName%2B%22%7C%7CBag%7CStandardCheckout%22'),
    ('pid', 'AOS%3A%20bag'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbag'),
    ('oid', 'Check%20Out'),
    ('.c', ''),
    ('link', 'check%20out%20%28inner%20text%29%20%7C%20no%20href%20%7C%20body'),
    ('ndh', '1'),
    ('c', '24'),
    ('cc', 'USD'),
    ('ce', 'UTF-8'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('pev2', 'shoppingCart.actions.t.checkout'),
    ('bw', '1420'),
    ('.a', ''),
    ('.activitymap', ''),
    ('v', 'N'),
    ('v4', 'D%3DpageName'),
    ('ot', 'SUBMIT'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air%3Fbfil%3D2%26product%3DMGN63LL%2FA%26step%3Dattach'),
    ('c4', 'D%3Dg'),
    ('v97', 's.tl-o'),
    ('pageIDType', '1'),
    ('v19', 'D%3Dc19'),
    ('a.', ''),
    ('events', 'event210%3D6.08%2Cevent246%2Cevent500'),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('AQE', '1'),
    ('pageName', 'AOS%3A%20bag'),
    ('c5', 'macintel'),
    ('s', '1920x1080'),
    ('j', '1.6'),
    ('v49', 'D%3Dr'),
    ('v14', 'en-us'),
    ('c8', 'AOS%3A%20Bag'),
    ('pe', 'lnk_o'),
    ('v54', 'D%3Dg'),
]
rc = s.post(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 79
# resource type: xhr

url = 'https://www.apple.com/shop/bagx/checkout_now'
headers = {
    'x-aos-model-page': 'cart',
    'referer': 'https://www.apple.com/shop/bag',
    'accept-language': 'en-US,en;q=0.9',
    ':path': '/shop/bagx/checkout_now?_a=checkout&_m=shoppingCart.actions',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'empty',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; as_xs=flc=; as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; s_sq=%5B%5BB%5D%5D',
    'content-length': '322',
    'accept-encoding': 'gzip, deflate, br',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.apple.com',
    'cache-control': 'no-cache',
    ':method': 'POST',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'modelversion': 'v2',
    'syntax': 'graviton',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    ':scheme': 'https',
    'x-requested-with': 'XMLHttpRequest',
    'x-aos-stk': '9b49e9bc',
    ':authority': 'www.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'as_xsm': '1&TsS1k4znjEvnGjBoAe_vvw',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_xs': 'flc=',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('_m', 'shoppingCart.actions'),
    ('_a', 'checkout'),
]
rc = s.post(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:38 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-xss-protection: 1; mode=block
#   - last-modified: Sat, 28 Nov 2020 11:59:38 GMT
#   - content-type: application/json; charset=UTF-8; encoding=UTF8
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:38 GMT; Max-Age=315360000; Secure; HttpOnly
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - date: Sat, 28 Nov 2020 11:59:38 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-shred: 41d5c228bf6f7c4837131d5832491a41
#   - x-frame-options: SAMEORIGIN
#   - content-length: 345
#   - pragma: no-cache
#   - x-serverprocessingtime: 72
#   - server: Apple
#   - expires: Sat, 28 Nov 2020 11:59:38 GMT
#   - vary: Accept-Encoding
#   - set-cookie: as_dc=nc; version="1"; max-age=1800; expires=Sat, 28-Nov-2020 12:29:38 GMT; path=/; domain=apple.com; secure
#   - content-encoding: gzip
#   - content-security-policy: frame-ancestors 'self'
#   - x-request-id: 6ba1df9e-ab94-4b93-a68a-1e67a87686fb
#   - x-content-type-options: nosniff
#   - set-cookie: as_xs=flc=; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:38 GMT; Max-Age=15552000; Secure; HttpOnly
#   - set-cookie: as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:38 GMT; Max-Age=15552000; Secure; HttpOnly
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_xsm: 1&TsS1k4znjEvnGjBoAe_vvw
#   - dssf: 1
#   - as_dc: nc
#   - as_xs: flc=
###############################################################################

###############################################################################
# request number: 80
# resource type: xhr

url = 'https://secure2.store.apple.com/shop/bag/status'
headers = {
    'Host': 'secure2.store.apple.com',
    'Sec-Fetch-Dest': 'empty',
    'Connection': 'keep-alive',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q',
    'Accept': '*/*',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': 'https://secure2.store.apple.com/shop/sign_in?c=aHR0cHM6Ly93d3cuYXBwbGUuY29tL3Nob3AvYmFnfDFhb3NjY2QxZjg4ZGZjYjY4YWRhNWZmMmY5ZTY5YWMzNjE0OTYyMjZlOWMz&o=O01HTjYz&r=SXYD4UDAPXU7P7KXF&s=aHR0cHM6Ly9zZWN1cmUyLnN0b3JlLmFwcGxlLmNvbS9zaG9wL2NoZWNrb3V0L3N0YXJ0P3BsdG49QTZGNDNFMER8MWFvczg4MjgzMjY3MzJkNWEzNjIxMTQxMDE0ZTU4NmZiNTY5MjEzZGEyY2M&t=SXYD4UDAPXU7P7KXF&up=t',
    'Cache-Control': 'no-cache',
    'Accept-Language': 'en-US,en;q=0.9',
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('apikey', 'SKCXTKATUYT9JK4HD'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - Server: Apple
#   - X-Frame-Options: DENY
#   - Set-Cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:39 GMT; Max-Age=1800; Secure
#   - Expires: Fri, 27 Nov 2020 11:59:39 GMT
#   - Strict-Transport-Security: max-age=31536000; includeSubDomains
#   - X-XSS-Protection: 1; mode=block
#   - Last-Modified: Sat, 28 Nov 2020 11:59:39 GMT
#   - Connection: keep-alive
#   - Content-Security-Policy: frame-ancestors 'none'
#   - Set-Cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:39 GMT; Max-Age=315360000; Secure; HttpOnly
#   - Vary: accept-encoding
#   - Expires: Thu, 01 Jan 1970 00:00:00 GMT
#   - Content-Length: 17
#   - X-Content-Type-Options: nosniff
#   - x-request-id: e61cbda2-c288-4106-bf0b-19c7fa14ea48
#   - x-shred: 0d13b5754739951f74c61bb7f47ef962
#   - Set-Cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:39 GMT; Max-Age=315360000; Secure; HttpOnly
#   - Pragma: no-cache
#   - Content-Type: application/json;charset=utf-8
#   - Cache-Control: private, no-store, no-cache, must-revalidate, no-siteapp
#   - Content-Language: en-US
#   - Date: Sat, 28 Nov 2020 11:59:39 GMT
# response cookies:
#   - as_dc: nc
#   - dssf: 1
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
###############################################################################

###############################################################################
# request number: 81
# resource type: xhr

url = 'https://secure2.store.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'Host': 'secure2.store.apple.com',
    'Sec-Fetch-Dest': 'empty',
    'Connection': 'keep-alive',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q',
    'Accept': '*/*',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': 'https://secure2.store.apple.com/shop/sign_in?c=aHR0cHM6Ly93d3cuYXBwbGUuY29tL3Nob3AvYmFnfDFhb3NjY2QxZjg4ZGZjYjY4YWRhNWZmMmY5ZTY5YWMzNjE0OTYyMjZlOWMz&o=O01HTjYz&r=SXYD4UDAPXU7P7KXF&s=aHR0cHM6Ly9zZWN1cmUyLnN0b3JlLmFwcGxlLmNvbS9zaG9wL2NoZWNrb3V0L3N0YXJ0P3BsdG49QTZGNDNFMER8MWFvczg4MjgzMjY3MzJkNWEzNjIxMTQxMDE0ZTU4NmZiNTY5MjEzZGEyY2M&t=SXYD4UDAPXU7P7KXF&up=t',
    'Cache-Control': 'no-cache',
    'Accept-Language': 'en-US,en;q=0.9',
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
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
#   - Server: Apple
#   - Content-Encoding: gzip
#   - Set-Cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:39 GMT; Path=/; Secure
#   - X-Frame-Options: DENY
#   - Cache-Control: private, max-age=120
#   - Edge-Control: !no-store, cache-maxage=120
#   - Strict-Transport-Security: max-age=31536000; includeSubDomains
#   - x-shred: b0abdff3ab738ad2a74bf72156baf7e1
#   - X-XSS-Protection: 1; mode=block
#   - Content-Type: text/html;charset=utf-8
#   - Connection: keep-alive
#   - Content-Security-Policy: frame-ancestors 'none'
#   - Last-Modified: Sat, 28 Nov 2020 11:53:16 GMT
#   - Vary: accept-encoding
#   - X-Content-Type-Options: nosniff
#   - ETag: "b81a098cfd586c44ab4211da0183e7c1"
#   - Expires: Sat, 28 Nov 2020 12:01:39 GMT
#   - x-request-id: 1d2be014-eeb4-43b8-b909-5a91a3ecff31
#   - Content-Length: 8204
#   - Date: Sat, 28 Nov 2020 11:59:39 GMT
# response cookies:
#   - as_dc: nc
###############################################################################

###############################################################################
# request number: 82
# resource type: document

url = 'https://idmsa.apple.com/appleauth/auth/authorize/signin'
headers = {
    'Sec-Fetch-Mode': 'navigate',
    'Referer': 'https://secure2.store.apple.com/',
    'Host': 'idmsa.apple.com',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Connection': 'keep-alive',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Sec-Fetch-Dest': 'iframe',
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('language', 'en_US'),
    ('frame_id', 'auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj'),
    ('response_mode', 'web_message'),
    ('redirect_uri', 'https://secure2.store.apple.com'),
    ('client_id', 'a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b'),
    ('state', 'auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj'),
    ('response_type', 'code'),
    ('iframeId', 'auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - Transfer-Encoding: chunked
#   - Server: Apple
#   - Content-Encoding: gzip
#   - X-Apple-I-Request-ID: 8f1b031d-51f5-4d12-b2af-4b89ec8cce52
#   - X-BuildVersion: R2
#   - Cache-Control: no-cache
#   - Content-Language: en-US-x-lvariant-USA
#   - X-XSS-Protection: 1; mode=block
#   - Cache-Control: no-store
#   - Connection: keep-alive
#   - Content-Security-Policy: default-src 'self'; script-src 'self' https://*.apple.com https://*.cdn-apple.com ; object-src 'self' https://*.apple-mapkit.com; style-src 'unsafe-inline' https://*.apple.com https://*.cdn-apple.com https://*.apple-mapkit.com ; img-src 'self' data: https://*.apple.com https://*.cdn-apple.com https://*.icloud.com https://*.mzstatic.com https://*.apple-mapkit.com ; media-src * data:; connect-src 'self' https://*.apple-mapkit.com; font-src 'self' https://*.apple.com https://*.cdn-apple.com; frame-src https://appleid.apple.com;  frame-ancestors https://secure2.store.apple.com;
#   - Date: Sat, 28 Nov 2020 11:59:40 GMT
#   - X-Apple-Auth-Attributes: dic0tBi4vhC93orxwirSFqhMve5dYbsQPWFmvVU/gdFdeqbKLQpUuUOsUCxX8FHl/ZGJjs4OnbXsmni0Xl/Yyutsbp8ogC3bXvj0tHXlrafJstxkI8ghdxz9G9oopF/AbMjQ5snnEE18nVXm4yvlfF2esocAC4tujG28cg==
#   - Expires: Thu, 01 Jan 1970 00:00:00 GMT
#   - vary: accept-encoding
#   - X-Content-Type-Options: nosniff
#   - Pragma: no-cache
#   - scnt: 8093ff807ba9fcfb78f018de1f0a2305
#   - Set-Cookie: dslang=US-EN; Domain=apple.com; Path=/; Secure; HttpOnly
#   - Set-Cookie: aa=991DE1862A229067497F55E997BAE2F5; Domain=idmsa.apple.com; Path=/; Secure; HttpOnly
#   - X-FRAME-OPTIONS: ALLOW-FROM https://secure2.store.apple.com
#   - Set-Cookie: site=USA; Domain=apple.com; Path=/; Secure; HttpOnly
#   - Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
#   - Content-Type: text/html;charset=UTF-8
# response cookies:
#   - aa: 991DE1862A229067497F55E997BAE2F5
#   - dslang: US-EN
#   - site: USA
###############################################################################

###############################################################################
# request number: 83
# resource type: xhr

url = 'https://store.storeimages.cdn-apple.com/4982/store.apple.com/shop/rs-external/rel/external.js'
headers = {
    'Host': 'store.storeimages.cdn-apple.com',
    'Referer': 'https://secure2.store.apple.com/',
    'Sec-Fetch-Dest': 'empty',
    'Connection': 'keep-alive',
    'Sec-Fetch-Site': 'cross-site',
    'Accept': '*/*',
    'Sec-Fetch-Mode': 'cors',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Origin': 'https://secure2.store.apple.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - Server: Apple
#   - Content-Encoding: gzip
#   - X-Frame-Options: DENY
#   - Accept-Ranges: bytes
#   - X-XSS-Protection: 1; mode=block
#   - Connection: keep-alive
#   - Content-Security-Policy: frame-ancestors 'none'
#   - x-shred: 73dc9cc218b4d274a506b1659d8cc044
#   - X-Cache: TCP_HIT from a92-122-95-84.deploy.akamaitechnologies.com (AkamaiGHost/10.2.2.1-31386017) (A)
#   - Date: Sat, 28 Nov 2020 11:59:40 GMT
#   - Expires: Sat, 28 Nov 2020 12:00:39 GMT
#   - X-Content-Type-Options: nosniff
#   - Vary: Accept-Encoding
#   - Last-Modified: Sat, 31 Oct 2020 06:14:18 GMT
#   - X-CDN: Akam
#   - Access-Control-Allow-Origin: *
#   - Content-Type: application/javascript
#   - Content-Length: 141036
#   - ETag: "7dfa5-5b2f16c562280-gzip"
#   - Strict-Transport-Security: max-age=31536000
#   - Access-Control-Expose-Headers: X-CDN
#   - Cache-Control: max-age=59
###############################################################################

###############################################################################
# request number: 84
# resource type: other

url = 'https://xp.apple.com/report/2/xp_aos_clientperf'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Referer': 'https://secure2.store.apple.com/',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Dest': 'empty',
    'Connection': 'keep-alive',
    'Access-Control-Request-Method': 'POST',
    'Accept': '*/*',
    'Host': 'xp.apple.com',
    'Sec-Fetch-Mode': 'cors',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Origin': 'https://secure2.store.apple.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Access-Control-Request-Headers': 'content-type',
}
rc = s.options(url, headers=headers)


# response status code: 200
# response headers:
#   - Access-Control-Allow-Headers: content-type
#   - Strict-Transport-Security: max-age=31536000
#   - Access-Control-Allow-Methods: POST
#   - X-Apple-Application-Site: ST
#   - X-Apple-Application-Instance: 248
#   - Access-Control-Allow-Origin: https://secure2.store.apple.com
#   - Connection: keep-alive
#   - Access-Control-Max-Age: 86400
#   - Access-Control-Allow-Credentials: true
#   - Date: Sat, 28 Nov 2020 11:59:40 GMT
#   - Content-Length: 0
#   - X-Apple-Jingle-Correlation-Key: RBYLFZFQYQLAQWWURGWXTWP4WA
###############################################################################

###############################################################################
# request number: 85
# resource type: xhr

url = 'https://idmsa.apple.com/appleauth/jslog'
headers = {
    'Content-type': 'application/json',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://idmsa.apple.com/appleauth/auth/authorize/signin?frame_id=auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj&language=en_US&iframeId=auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj&client_id=a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b&redirect_uri=https://secure2.store.apple.com&response_type=code&response_mode=web_message&state=auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj',
    'Cache-Control': 'no-cache',
    'Content-Length': '280',
    'Accept': 'application/json',
    'Pragma': 'no-cache',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; aa=991DE1862A229067497F55E997BAE2F5; dslang=US-EN; site=USA',
    'scnt': '',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Host': 'idmsa.apple.com',
    'x-csrf-token': '',
    'Connection': 'keep-alive',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://idmsa.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'dslang': 'US-EN',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'as_xs': 'flc=&idmsl=1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'site': 'USA',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'aa': '991DE1862A229067497F55E997BAE2F5',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.post(url, headers=headers, cookies=cookies)


# response status code: 204
# response headers:
#   - Server: Apple
#   - X-XSS-Protection: 1; mode=block
#   - Cache-Control: no-store
#   - Set-Cookie: site=USA; Domain=apple.com; Path=/; Secure; HttpOnly
#   - Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
#   - Content-Security-Policy: default-src 'self'; script-src 'self' https://*.apple.com https://*.cdn-apple.com ; object-src 'self' https://*.apple-mapkit.com; style-src 'unsafe-inline' https://*.apple.com https://*.cdn-apple.com https://*.apple-mapkit.com ; img-src 'self' data: https://*.apple.com https://*.cdn-apple.com https://*.icloud.com https://*.mzstatic.com https://*.apple-mapkit.com ; media-src * data:; connect-src 'self' https://*.apple-mapkit.com; font-src 'self' https://*.apple.com https://*.cdn-apple.com; frame-src https://appleid.apple.com;
#   - Date: Sat, 28 Nov 2020 11:59:41 GMT
#   - X-Content-Type-Options: nosniff
#   - Expires: Thu, 01 Jan 1970 00:00:00 GMT
#   - Connection: keep-alive
#   - X-FRAME-OPTIONS: DENY
#   - X-BuildVersion: R2
#   - scnt: b44963741cc0a2b8ff76999a2a4d3369
#   - Cache-Control: no-cache
#   - X-Apple-I-Request-ID: cd293672-d66b-45c1-884f-eed28001cdbb
#   - Set-Cookie: dslang=US-EN; Domain=apple.com; Path=/; Secure; HttpOnly
#   - Pragma: no-cache
# response cookies:
#   - dslang: US-EN
#   - site: USA
###############################################################################

###############################################################################
# request number: 86
# resource type: other

url = 'https://secure2.store.apple.com/favicon.ico'
headers = {
    'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'Host': 'secure2.store.apple.com',
    'Connection': 'keep-alive',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
    'Referer': 'https://secure2.store.apple.com/shop/sign_in?c=aHR0cHM6Ly93d3cuYXBwbGUuY29tL3Nob3AvYmFnfDFhb3NjY2QxZjg4ZGZjYjY4YWRhNWZmMmY5ZTY5YWMzNjE0OTYyMjZlOWMz&o=O01HTjYz&r=SXYD4UDAPXU7P7KXF&s=aHR0cHM6Ly9zZWN1cmUyLnN0b3JlLmFwcGxlLmNvbS9zaG9wL2NoZWNrb3V0L3N0YXJ0P3BsdG49QTZGNDNFMER8MWFvczg4MjgzMjY3MzJkNWEzNjIxMTQxMDE0ZTU4NmZiNTY5MjEzZGEyY2M&t=SXYD4UDAPXU7P7KXF&up=t',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'no-cors',
    'Cache-Control': 'no-cache',
    'Sec-Fetch-Dest': 'image',
    'Pragma': 'no-cache',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'dslang': 'US-EN',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'as_xs': 'flc=&idmsl=1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'site': 'USA',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
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
#   - Server: Apple
#   - Accept-Ranges: bytes
#   - X-XSS-Protection: 1; mode=block
#   - Edge-Control: !no-store, cache-maxage=1440m
#   - X-Frame-Options: DENY
#   - Date: Sat, 28 Nov 2020 11:59:41 GMT
#   - Content-Type: image/x-icon
#   - X-Content-Type-Options: nosniff
#   - ETag: "2366-4fd2591660cbc"
#   - Connection: keep-alive
#   - Content-Length: 9062
#   - Content-Security-Policy: frame-ancestors 'none'
#   - Cache-Control: max-age=86400
#   - Last-Modified: Tue, 01 Jul 2014 18:01:41 GMT
#   - x-shred: f7bb3b171d6b570205a5f584a50ba929
#   - Expires: Sun, 29 Nov 2020 11:59:41 GMT
#   - Strict-Transport-Security: max-age=31536000; includeSubDomains
###############################################################################

###############################################################################
# request number: 87
# resource type: xhr

url = 'https://idmsa.apple.com/appleauth/jslog'
headers = {
    'Content-type': 'application/json',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://idmsa.apple.com/appleauth/auth/authorize/signin?frame_id=auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj&language=en_US&iframeId=auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj&client_id=a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b&redirect_uri=https://secure2.store.apple.com&response_type=code&response_mode=web_message&state=auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json',
    'Pragma': 'no-cache',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; aa=991DE1862A229067497F55E997BAE2F5; dslang=US-EN; site=USA',
    'scnt': '',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Host': 'idmsa.apple.com',
    'x-csrf-token': '',
    'Connection': 'keep-alive',
    'Content-Length': '399',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://idmsa.apple.com',
}
cookies = {
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    'dslang': 'US-EN',
    'check': 'true',
    'geo': 'IT',
    'dssf': '1',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'as_xs': 'flc=&idmsl=1',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    'site': 'USA',
    'as_dc': 'nc',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'aa': '991DE1862A229067497F55E997BAE2F5',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.post(url, headers=headers, cookies=cookies)


# response status code: 204
# response headers:
#   - scnt: b558191cfd30dcaf5ca07a6a03a3042c
#   - Server: Apple
#   - X-XSS-Protection: 1; mode=block
#   - Cache-Control: no-store
#   - Set-Cookie: site=USA; Domain=apple.com; Path=/; Secure; HttpOnly
#   - Expires: Thu, 01 Jan 1970 00:00:00 GMT
#   - Content-Security-Policy: default-src 'self'; script-src 'self' https://*.apple.com https://*.cdn-apple.com ; object-src 'self' https://*.apple-mapkit.com; style-src 'unsafe-inline' https://*.apple.com https://*.cdn-apple.com https://*.apple-mapkit.com ; img-src 'self' data: https://*.apple.com https://*.cdn-apple.com https://*.icloud.com https://*.mzstatic.com https://*.apple-mapkit.com ; media-src * data:; connect-src 'self' https://*.apple-mapkit.com; font-src 'self' https://*.apple.com https://*.cdn-apple.com; frame-src https://appleid.apple.com;
#   - Date: Sat, 28 Nov 2020 11:59:41 GMT
#   - X-Content-Type-Options: nosniff
#   - X-Apple-I-Request-ID: 4f86ec7e-c89c-41f4-bdf0-a60cdb207c01
#   - Connection: keep-alive
#   - X-FRAME-OPTIONS: DENY
#   - X-BuildVersion: R2
#   - Cache-Control: no-cache
#   - Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
#   - Set-Cookie: dslang=US-EN; Domain=apple.com; Path=/; Secure; HttpOnly
#   - Pragma: no-cache
# response cookies:
#   - dslang: US-EN
#   - site: USA
###############################################################################

