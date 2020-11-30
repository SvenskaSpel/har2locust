import requests


s = requests.Session()

###############################################################################
# request number: 1
# resource type: document

url = 'https://secure2.store.apple.com/shop/sign_in'
headers = {
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_xs=flc=; as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; s_sq=%5B%5BB%5D%5D',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.apple.com/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Mode': 'navigate',
    'Connection': 'keep-alive',
    'Host': 'secure2.store.apple.com',
    'Cache-Control': 'no-cache',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xs': 'flc=',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    'as_xsm': '1&TsS1k4znjEvnGjBoAe_vvw',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('o', 'O01HTjYz'),
    ('up', 't'),
    ('s', 'aHR0cHM6Ly9zZWN1cmUyLnN0b3JlLmFwcGxlLmNvbS9zaG9wL2NoZWNrb3V0L3N0YXJ0P3BsdG49QTZGNDNFMER8MWFvczg4MjgzMjY3MzJkNWEzNjIxMTQxMDE0ZTU4NmZiNTY5MjEzZGEyY2M'),
    ('t', 'SXYD4UDAPXU7P7KXF'),
    ('r', 'SXYD4UDAPXU7P7KXF'),
    ('c', 'aHR0cHM6Ly93d3cuYXBwbGUuY29tL3Nob3AvYmFnfDFhb3NjY2QxZjg4ZGZjYjY4YWRhNWZmMmY5ZTY5YWMzNjE0OTYyMjZlOWMz'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - Content-Encoding: gzip
#   - Set-Cookie: as_xs=flc=&idmsl=1; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:38 GMT; Max-Age=15552000; Secure; HttpOnly
#   - x-content-type-options: nosniff
#   - Set-Cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:38 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: SAMEORIGIN
#   - Content-Type: text/html; charset=UTF-8; encoding=UTF8
#   - Server: Apple
#   - Set-Cookie: as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:38 GMT; Max-Age=15552000; Secure; HttpOnly
#   - Content-Length: 10158
#   - x-request-id: 8a0d60c7-f930-4fee-ab26-2e7bd8fbfdbd
#   - content-security-policy: frame-ancestors 'self'
#   - Strict-Transport-Security: max-age=31536000; includeSubDomains
#   - Expires: Thu, 01 Jan 1970 00:00:00 GMT
#   - Pragma: no-cache
#   - x-serverprocessingtime: 16
#   - Vary: *
#   - Date: Sat, 28 Nov 2020 11:59:38 GMT
#   - Set-Cookie: as_dc=nc; version="1"; max-age=1800; expires=Sat, 28-Nov-2020 12:29:38 GMT; path=/; domain=apple.com; secure
#   - Last-Modified: Sat, 28 Nov 2020 11:59:38 GMT
#   - Connection: keep-alive
#   - Cache-Control: no-store, private, must-revalidate, proxy-revalidate, max-age=0, pre-check=0, post-check=0, no-cache, no-siteapp
#   - Expires: Fri, 27 Nov 2020 11:59:38 GMT
#   - Set-Cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:38 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-shred: 64eac8aa26c2139b5ad18cbdefd14ff7
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_xsm: 1&93mZGW_YVaxBa9JRiFse-Q
#   - as_dc: nc
#   - dssf: 1
#   - as_xs: flc=&idmsl=1
###############################################################################

###############################################################################
# request number: 2
# resource type: document

url = 'https://www.apple.com/shop/buy-mac/macbook-air'
headers = {
    ':path': '/shop/buy-mac/macbook-air?proceed=proceed&bfil=2&product=MGN63LL%2FA&step=attach',
    'sec-fetch-mode': 'navigate',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=applestoreww%252Cappleglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526link%253Dreview%252520bag%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526pidt%253D1%2526oid%253Dproceed%2526oidt%253D3%2526ot%253DSUBMIT; s_aca_ct=%7B%22events%22%3A%22event246%2Cevent210%3D4.47%22%2C%22eVar94%22%3A4.47%2C%22eVar93%22%3A0%7D',
    ':method': 'GET',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    's_sq': 'applestoreww%252Cappleglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526link%253Dreview%252520bag%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526pidt%253D1%2526oid%253Dproceed%2526oidt%253D3%2526ot%253DSUBMIT',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_aca_ct': '%7B%22events%22%3A%22event246%2Cevent210%3D4.47%22%2C%22eVar94%22%3A4.47%2C%22eVar93%22%3A0%7D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('bfil', '2'),
    ('step', 'attach'),
    ('product', 'MGN63LL%2FA'),
    ('proceed', 'proceed'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 303
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - content-length: 20
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - x-shred: 4f2117550b8e0b2c66ec333589661d50
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 11:59:30 GMT
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - last-modified: Sat, 28 Nov 2020 11:59:30 GMT
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:30 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-request-id: 2375cd7d-e6c9-4299-bc74-17bfc6f198ff
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:30 GMT; Path=/; Secure
#   - etag: "d41d8cd98f00b204e9800998ecf8427e"
#   - date: Sat, 28 Nov 2020 11:59:30 GMT
#   - pragma: no-cache
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:30 GMT; Max-Age=315360000; Secure; HttpOnly
#   - location: /shop/bag
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 3
# resource type: document

url = 'https://www.apple.com/shop/bag'
headers = {
    'sec-fetch-mode': 'navigate',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/shop/bag',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; s_sq=applestoreww%252Cappleglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526link%253Dreview%252520bag%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526pidt%253D1%2526oid%253Dproceed%2526oidt%253D3%2526ot%253DSUBMIT; s_aca_ct=%7B%22events%22%3A%22event246%2Cevent210%3D4.47%22%2C%22eVar94%22%3A4.47%2C%22eVar93%22%3A0%7D',
    ':method': 'GET',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    's_sq': 'applestoreww%252Cappleglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526link%253Dreview%252520bag%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520home%25252Fshop_mac%25252Ffamily%25252Fmacbook_air%25252Fattach%2526pidt%253D1%2526oid%253Dproceed%2526oidt%253D3%2526ot%253DSUBMIT',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_aca_ct': '%7B%22events%22%3A%22event246%2Cevent210%3D4.47%22%2C%22eVar94%22%3A4.47%2C%22eVar93%22%3A0%7D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-length: 33186
#   - x-content-type-options: nosniff
#   - x-frame-options: SAMEORIGIN
#   - set-cookie: as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:30 GMT; Max-Age=15552000; Secure; HttpOnly
#   - x-shred: 10cc028c060d02de2fe8ae0c55a27a0d
#   - x-serverprocessingtime: 161
#   - x-request-id: 426b5d51-4f9f-447a-90d3-65ea7d1df041
#   - content-type: text/html; charset=UTF-8; encoding=UTF8
#   - expires: Sat, 28 Nov 2020 11:59:30 GMT
#   - vary: Accept-Encoding
#   - content-security-policy: frame-ancestors 'self'
#   - content-encoding: gzip
#   - last-modified: Sat, 28 Nov 2020 11:59:30 GMT
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:30 GMT; Max-Age=315360000; Secure; HttpOnly
#   - set-cookie: as_xs=flc=; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:30 GMT; Max-Age=15552000; Secure; HttpOnly
#   - date: Sat, 28 Nov 2020 11:59:30 GMT
#   - pragma: no-cache
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:30 GMT; Max-Age=315360000; Secure; HttpOnly
#   - set-cookie: as_dc=nc; version="1"; max-age=1800; expires=Sat, 28-Nov-2020 12:29:30 GMT; path=/; domain=apple.com; secure
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - as_xs: flc=
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - as_xsm: 1&TsS1k4znjEvnGjBoAe_vvw
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 4
# resource type: document

url = 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb'
headers = {
    'sec-fetch-mode': 'navigate',
    ':path': '/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb?option.memory__dummy_z124=065-C99M&option.hard_drivesolid_state_drive__dummy_z124=065-C99Q&option.keyboard_and_documentation_z124=065-C9DG&option.sw_final_cut_pro_x_z124=065-C171&option.sw_logic_pro_x_z124=065-C172&add-to-cart=add-to-cart&product=MGN63LL%2FA&step=config&bfil=2&atbtoken=bd24f42caddadc789d311b27afde1f05fc9262f2',
    'cache-control': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2; s_sq=%5B%5BB%5D%5D; s_aca_ct=%7B%22events%22%3A%22event246%2Cevent210%3D3.39%22%2C%22eVar94%22%3A3.39%2C%22eVar93%22%3A0%7D',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'document',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    ':method': 'GET',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_aca_ct': '%7B%22events%22%3A%22event246%2Cevent210%3D3.39%22%2C%22eVar94%22%3A3.39%2C%22eVar93%22%3A0%7D',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('add-to-cart', 'add-to-cart'),
    ('option.sw_final_cut_pro_x_z124', '065-C171'),
    ('option.sw_logic_pro_x_z124', '065-C172'),
    ('option.keyboard_and_documentation_z124', '065-C9DG'),
    ('atbtoken', 'bd24f42caddadc789d311b27afde1f05fc9262f2'),
    ('product', 'MGN63LL%2FA'),
    ('option.hard_drivesolid_state_drive__dummy_z124', '065-C99Q'),
    ('option.memory__dummy_z124', '065-C99M'),
    ('step', 'config'),
    ('bfil', '2'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 303
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:24 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-length: 20
#   - x-content-type-options: nosniff
#   - date: Sat, 28 Nov 2020 11:59:24 GMT
#   - content-language: en-US
#   - x-shred: ae00b9e41c73ef01677cd4ae55aa5890
#   - x-frame-options: DENY
#   - vary: Accept-Encoding
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:24 GMT; Path=/; Secure
#   - x-request-id: 8a021fe0-5c84-4a10-aafb-3b5562fb7fdd
#   - content-encoding: gzip
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - location: /shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach
#   - etag: "d41d8cd98f00b204e9800998ecf8427e"
#   - expires: Sat, 28 Nov 2020 11:59:24 GMT
#   - pragma: no-cache
#   - last-modified: Sat, 28 Nov 2020 11:59:24 GMT
#   - x-xss-protection: 1; mode=block
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:24 GMT; Max-Age=315360000; Secure; HttpOnly
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 5
# resource type: document

url = 'https://www.apple.com/shop/buy-mac/macbook-air'
headers = {
    'sec-fetch-mode': 'navigate',
    'cache-control': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2; s_sq=%5B%5BB%5D%5D; s_aca_ct=%7B%22events%22%3A%22event246%2Cevent210%3D3.39%22%2C%22eVar94%22%3A3.39%2C%22eVar93%22%3A0%7D',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'document',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    ':path': '/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    ':method': 'GET',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_aca_ct': '%7B%22events%22%3A%22event246%2Cevent210%3D3.39%22%2C%22eVar94%22%3A3.39%2C%22eVar93%22%3A0%7D',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('product', 'MGN63LL/A'),
    ('step', 'attach'),
    ('bfil', '2'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:24 GMT; Max-Age=315360000; Secure; HttpOnly
#   - date: Sat, 28 Nov 2020 11:59:24 GMT
#   - x-content-type-options: nosniff
#   - cache-control: private, max-age=98
#   - last-modified: Sat, 28 Nov 2020 11:59:11 GMT
#   - content-type: text/html;charset=utf-8
#   - x-request-id: 631ddafa-a90a-4fd4-a028-a94806d211c1
#   - x-frame-options: DENY
#   - vary: Accept-Encoding
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:24 GMT; Path=/; Secure
#   - content-encoding: gzip
#   - etag: "d0b6b6ce9e4a4648483a76514a76c5c6"
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-length: 46722
#   - x-shred: 095931eea367ed92b779ec3312a0d95c
#   - x-xss-protection: 1; mode=block
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:24 GMT; Max-Age=315360000; Secure; HttpOnly
#   - expires: Sat, 28 Nov 2020 12:01:02 GMT
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 6
# resource type: document

url = 'https://www.apple.com/shop/buy-mac/macbook-air'
headers = {
    'sec-fetch-mode': 'navigate',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    ':path': '/shop/buy-mac/macbook-air?proceed=proceed&product=MGN63LL%2FA&step=select',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'document',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; s_aca_ct=%7B%22events%22%3A%22event246%2Cevent210%3D7.03%22%2C%22eVar94%22%3A7.03%2C%22eVar93%22%3A0%7D',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    ':method': 'GET',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    's_aca_ct': '%7B%22events%22%3A%22event246%2Cevent210%3D7.03%22%2C%22eVar94%22%3A7.03%2C%22eVar93%22%3A0%7D',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('step', 'select'),
    ('product', 'MGN63LL%2FA'),
    ('proceed', 'proceed'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 303
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:19 GMT; Path=/; Secure
#   - content-length: 20
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - date: Sat, 28 Nov 2020 11:59:19 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:19 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - x-request-id: fae35d6b-2735-438c-8bca-5d998de55c55
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:19 GMT; Max-Age=315360000; Secure; HttpOnly
#   - etag: "d41d8cd98f00b204e9800998ecf8427e"
#   - pragma: no-cache
#   - expires: Sat, 28 Nov 2020 11:59:19 GMT
#   - location: /shop/buy-mac/macbook-air?product=MGN63LL/A&step=config
#   - x-shred: d2866c9f5cc5e34a8c460445e8753b09
#   - x-xss-protection: 1; mode=block
#   - last-modified: Sat, 28 Nov 2020 11:59:19 GMT
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 7
# resource type: document

url = 'https://www.apple.com/shop/buy-mac/macbook-air'
headers = {
    'sec-fetch-mode': 'navigate',
    'cache-control': 'no-cache',
    ':path': '/shop/buy-mac/macbook-air?product=MGN63LL/A&step=config',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'document',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; s_aca_ct=%7B%22events%22%3A%22event246%2Cevent210%3D7.03%22%2C%22eVar94%22%3A7.03%2C%22eVar93%22%3A0%7D',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    ':method': 'GET',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    's_aca_ct': '%7B%22events%22%3A%22event246%2Cevent210%3D7.03%22%2C%22eVar94%22%3A7.03%2C%22eVar93%22%3A0%7D',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('step', 'config'),
    ('product', 'MGN63LL/A'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 301
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:19 GMT; Path=/; Secure
#   - content-length: 20
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - x-request-id: 5c4d604e-4ee9-4304-9385-c125ac0008a3
#   - date: Sat, 28 Nov 2020 11:59:19 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:19 GMT; Max-Age=315360000; Secure; HttpOnly
#   - cache-control: private, max-age=120
#   - x-frame-options: DENY
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - x-shred: ab4669324f9b76636d615f6816edc4f5
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - expires: Sat, 28 Nov 2020 12:01:19 GMT
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:19 GMT; Max-Age=315360000; Secure; HttpOnly
#   - etag: "d41d8cd98f00b204e9800998ecf8427e"
#   - x-xss-protection: 1; mode=block
#   - last-modified: Sat, 28 Nov 2020 11:59:19 GMT
#   - location: https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 8
# resource type: document

url = 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb'
headers = {
    'sec-fetch-mode': 'navigate',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'document',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; s_aca_ct=%7B%22events%22%3A%22event246%2Cevent210%3D7.03%22%2C%22eVar94%22%3A7.03%2C%22eVar93%22%3A0%7D',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    ':method': 'GET',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    's_aca_ct': '%7B%22events%22%3A%22event246%2Cevent210%3D7.03%22%2C%22eVar94%22%3A7.03%2C%22eVar93%22%3A0%7D',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - cache-control: private, max-age=81
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:19 GMT; Path=/; Secure
#   - x-request-id: 1fb4fc2b-2fca-42f2-9c59-6626be52e380
#   - x-content-type-options: nosniff
#   - last-modified: Sat, 28 Nov 2020 11:58:45 GMT
#   - date: Sat, 28 Nov 2020 11:59:19 GMT
#   - expires: Sat, 28 Nov 2020 12:00:40 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:19 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-type: text/html;charset=utf-8
#   - x-frame-options: DENY
#   - vary: Accept-Encoding
#   - x-shred: b4e36d2a30b640a6a20f2f4e79260aa2
#   - content-encoding: gzip
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - etag: "dd5e3af3a6bbdb23d85302fc85674e79"
#   - content-length: 45248
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:19 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 9
# resource type: document

url = 'https://www.apple.com/us/shop/goto/buy_mac/macbook_air'
headers = {
    'sec-fetch-mode': 'navigate',
    ':path': '/us/shop/goto/buy_mac/macbook_air',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'referer': 'https://www.apple.com/macbook-air/',
    'sec-fetch-dest': 'document',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    ':method': 'GET',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; mk_epub=%7B%22btuid%22%3A%22vy62nu%22%2C%22eVar1%22%3A%22macbook%20air%20-%20overview%20(us)%20%7C%20local%20nav%20locked%20%7C%20buy%22%2C%22prop57%22%3A%22www.us.macbookair%22%2C%22prop25%22%3A%22local%20nav%20locked%22%7D; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D7.6%22%5D%2C%22eVar94%22%3A%227.6%22%2C%22eVar93%22%3A%221%22%7D; s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526link%253Dbuy%252520-%252520%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%252520-%252520ac-localnav%2526region%253Dac-localnav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%2526ot%253DA',
}
cookies = {
    's_sq': 'appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526link%253Dbuy%252520-%252520%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%252520-%252520ac-localnav%2526region%253Dac-localnav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%2526ot%253DA',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mk_epub': '%7B%22btuid%22%3A%22vy62nu%22%2C%22eVar1%22%3A%22macbook%20air%20-%20overview%20(us)%20%7C%20local%20nav%20locked%20%7C%20buy%22%2C%22prop57%22%3A%22www.us.macbookair%22%2C%22prop25%22%3A%22local%20nav%20locked%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D7.6%22%5D%2C%22eVar94%22%3A%227.6%22%2C%22eVar93%22%3A%221%22%7D',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 303
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-shred: 7f69f4c770de84b8b4cea488f6bf678b
#   - content-length: 20
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - last-modified: Sat, 28 Nov 2020 11:59:09 GMT
#   - expires: Sat, 28 Nov 2020 11:59:10 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:09 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-request-id: f12dd9f7-2b23-45d2-aeeb-74bcffe03de7
#   - x-frame-options: DENY
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - date: Sat, 28 Nov 2020 11:59:10 GMT
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:09 GMT; Path=/; Secure
#   - etag: "d41d8cd98f00b204e9800998ecf8427e"
#   - pragma: no-cache
#   - location: https://www.apple.com/us/shop/go/buy_mac/macbook_air
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:09 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 10
# resource type: document

url = 'https://www.apple.com/us/shop/go/buy_mac/macbook_air'
headers = {
    'sec-fetch-mode': 'navigate',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-user': '?1',
    ':authority': 'www.apple.com',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.apple.com/macbook-air/',
    ':path': '/us/shop/go/buy_mac/macbook_air',
    'sec-fetch-dest': 'document',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    ':method': 'GET',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; mk_epub=%7B%22btuid%22%3A%22vy62nu%22%2C%22eVar1%22%3A%22macbook%20air%20-%20overview%20(us)%20%7C%20local%20nav%20locked%20%7C%20buy%22%2C%22prop57%22%3A%22www.us.macbookair%22%2C%22prop25%22%3A%22local%20nav%20locked%22%7D; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D7.6%22%5D%2C%22eVar94%22%3A%227.6%22%2C%22eVar93%22%3A%221%22%7D; s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526link%253Dbuy%252520-%252520%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%252520-%252520ac-localnav%2526region%253Dac-localnav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%2526ot%253DA',
}
cookies = {
    's_sq': 'appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526link%253Dbuy%252520-%252520%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%252520-%252520ac-localnav%2526region%253Dac-localnav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%2526ot%253DA',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mk_epub': '%7B%22btuid%22%3A%22vy62nu%22%2C%22eVar1%22%3A%22macbook%20air%20-%20overview%20(us)%20%7C%20local%20nav%20locked%20%7C%20buy%22%2C%22prop57%22%3A%22www.us.macbookair%22%2C%22prop25%22%3A%22local%20nav%20locked%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D7.6%22%5D%2C%22eVar94%22%3A%227.6%22%2C%22eVar93%22%3A%221%22%7D',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 301
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:10 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-length: 20
#   - x-content-type-options: nosniff
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:10 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-request-id: 90c4a4fe-43d5-4fc7-a4c0-6508e17ac964
#   - content-language: en-US
#   - last-modified: Sat, 28 Nov 2020 11:59:10 GMT
#   - cache-control: private, max-age=120
#   - x-frame-options: DENY
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - x-shred: b620b213d82805e82a5b064d4198b8d8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - date: Sat, 28 Nov 2020 11:59:10 GMT
#   - location: /shop/buy-mac/macbook-air
#   - expires: Sat, 28 Nov 2020 12:01:10 GMT
#   - etag: "d41d8cd98f00b204e9800998ecf8427e"
#   - x-xss-protection: 1; mode=block
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:10 GMT; Path=/; Secure
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 11
# resource type: document

url = 'https://www.apple.com/shop/buy-mac/macbook-air'
headers = {
    'sec-fetch-mode': 'navigate',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'referer': 'https://www.apple.com/macbook-air/',
    'sec-fetch-dest': 'document',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    ':method': 'GET',
    ':path': '/shop/buy-mac/macbook-air',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; mk_epub=%7B%22btuid%22%3A%22vy62nu%22%2C%22eVar1%22%3A%22macbook%20air%20-%20overview%20(us)%20%7C%20local%20nav%20locked%20%7C%20buy%22%2C%22prop57%22%3A%22www.us.macbookair%22%2C%22prop25%22%3A%22local%20nav%20locked%22%7D; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D7.6%22%5D%2C%22eVar94%22%3A%227.6%22%2C%22eVar93%22%3A%221%22%7D; s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526link%253Dbuy%252520-%252520%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%252520-%252520ac-localnav%2526region%253Dac-localnav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%2526ot%253DA',
}
cookies = {
    's_sq': 'appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526link%253Dbuy%252520-%252520%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%252520-%252520ac-localnav%2526region%253Dac-localnav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmacbook%252520air%252520-%252520overview%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fus%25252Fshop%25252Fgoto%25252Fbuy_mac%25252Fmacbook_air%2526ot%253DA',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mk_epub': '%7B%22btuid%22%3A%22vy62nu%22%2C%22eVar1%22%3A%22macbook%20air%20-%20overview%20(us)%20%7C%20local%20nav%20locked%20%7C%20buy%22%2C%22prop57%22%3A%22www.us.macbookair%22%2C%22prop25%22%3A%22local%20nav%20locked%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D7.6%22%5D%2C%22eVar94%22%3A%227.6%22%2C%22eVar93%22%3A%221%22%7D',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - etag: "5dd846c72f93833181e1188c441bfeab"
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:10 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-content-type-options: nosniff
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:10 GMT; Max-Age=315360000; Secure; HttpOnly
#   - expires: Sat, 28 Nov 2020 12:00:36 GMT
#   - x-request-id: 703f2c18-2d95-4643-a1ae-ed8e99c99ee0
#   - content-length: 37868
#   - content-type: text/html;charset=utf-8
#   - x-frame-options: DENY
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - date: Sat, 28 Nov 2020 11:59:10 GMT
#   - cache-control: private, max-age=86
#   - x-shred: 55653fe1a0688649fb9962dc48958493
#   - x-xss-protection: 1; mode=block
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:10 GMT; Path=/; Secure
#   - last-modified: Sat, 28 Nov 2020 11:58:36 GMT
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 12
# resource type: document

url = 'https://www.apple.com/macbook-air/'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; mk_epub=%7B%22btuid%22%3A%22177namr%22%2C%22eVar1%22%3A%22mac%20-%20index%2Ftab%20(us)%20%7C%20family%20browser%20%7C%20MacBook%20Air%5Cn%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5CtNew%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%2C%22prop25%22%3A%22family%20browser%22%7D; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D; s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmac%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmacbook%252520air%252520new%252520-%252520%25252Fmacbook-air%25252F%252520-%252520chapternav%2526region%253Dchapternav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmac%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmacbook-air%25252F%2526ot%253DA',
    'sec-fetch-mode': 'navigate',
    ':path': '/macbook-air/',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'document',
    'pragma': 'no-cache',
    'referer': 'https://www.apple.com/mac/',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    ':method': 'GET',
}
cookies = {
    'mk_epub': '%7B%22btuid%22%3A%22177namr%22%2C%22eVar1%22%3A%22mac%20-%20index%2Ftab%20(us)%20%7C%20family%20browser%20%7C%20MacBook%20Air%5Cn%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5Ct%5CtNew%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%2C%22prop25%22%3A%22family%20browser%22%7D',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    's_sq': 'appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmac%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmacbook%252520air%252520new%252520-%252520%25252Fmacbook-air%25252F%252520-%252520chapternav%2526region%253Dchapternav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmac%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmacbook-air%25252F%2526ot%253DA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-length: 30528
#   - date: Sat, 28 Nov 2020 11:59:00 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - cache-control: max-age=0
#   - server: Apache
#   - x-content-type-options: nosniff
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: SAMEORIGIN
#   - expires: Sat, 28 Nov 2020 11:59:00 GMT
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - content-type: text/html; charset=UTF-8
###############################################################################

###############################################################################
# request number: 13
# resource type: document

url = 'https://www.apple.com/mac/'
headers = {
    'sec-fetch-mode': 'navigate',
    'cache-control': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; mk_epub=%7B%22btuid%22%3A%22126h84u%22%2C%22eVar1%22%3A%22apple%20-%20index%2Ftab%20(us)%20%7C%20global%20nav%20%7C%20mac%22%2C%22prop57%22%3A%22www.us.homepage%22%2C%22prop25%22%3A%22global%20nav%22%7D; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D; s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmac%252520-%252520%25252Fmac%25252F%252520-%252520global%252520nav%2526region%253Dglobal%252520nav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmac%25252F%2526ot%253DA',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/mac/',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'document',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    ':method': 'GET',
}
cookies = {
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'mk_epub': '%7B%22btuid%22%3A%22126h84u%22%2C%22eVar1%22%3A%22apple%20-%20index%2Ftab%20(us)%20%7C%20global%20nav%20%7C%20mac%22%2C%22prop57%22%3A%22www.us.homepage%22%2C%22prop25%22%3A%22global%20nav%22%7D',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D',
    's_sq': 'appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmac%252520-%252520%25252Fmac%25252F%252520-%252520global%252520nav%2526region%253Dglobal%252520nav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmac%25252F%2526ot%253DA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - date: Sat, 28 Nov 2020 11:58:54 GMT
#   - content-length: 18977
#   - server: Apache
#   - x-content-type-options: nosniff
#   - expires: Sat, 28 Nov 2020 12:00:00 GMT
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: SAMEORIGIN
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - content-type: text/html; charset=UTF-8
#   - cache-control: max-age=66
###############################################################################

###############################################################################
# request number: 14
# resource type: document

url = 'https://www.apple.com/'
headers = {
    'sec-fetch-mode': 'navigate',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'sec-fetch-dest': 'document',
    'pragma': 'no-cache',
    'sec-fetch-site': 'none',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; mk_epub=%7B%22btuid%22%3A%22twoihc%22%2C%22prop57%22%3A%22www.us.homepage%22%7D; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    ':path': '/',
    'upgrade-insecure-requests': '1',
    ':method': 'GET',
}
cookies = {
    'mk_epub': '%7B%22btuid%22%3A%22twoihc%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-length: 10565
#   - expires: Sat, 28 Nov 2020 11:58:49 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - cache-control: max-age=0
#   - server: Apache
#   - x-content-type-options: nosniff
#   - date: Sat, 28 Nov 2020 11:58:49 GMT
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: SAMEORIGIN
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - content-type: text/html; charset=UTF-8
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
    ('browserHeight', '630'),
    ('mboxURL', 'https%3A%2F%2Fwww.apple.com%2F'),
    ('devicePixelRatio', '1'),
    ('mboxRid', 'e1e5810447114e1ea0db6ddfae46a383'),
    ('mboxHost', 'www.apple.com'),
    ('screenWidth', '1920'),
    ('mboxCount', '1'),
    ('mboxReferrer', ''),
    ('browserTimeOffset', '60'),
    ('colorDepth', '24'),
    ('browserWidth', '1420'),
    ('mboxPC', ''),
    ('mboxSession', 'bb7cc510c65f4f4eaba6b8ef81b5547f'),
    ('mboxVersion', '1.5.0'),
    ('screenHeight', '1080'),
    ('mbox', 'target-global-mbox'),
    ('mboxPage', '28a825d8368e433fb1840aed16581b46'),
    ('mboxTime', '1606568330064'),
    ('screenOrientation', 'landscape'),
    ('webGLRenderer', 'Intel%20HD%20Graphics%205000%20OpenGL%20Engine'),
]
rc = s.get(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 16
# resource type: xhr

url = 'https://www.apple.com/ac/localeswitcher/3/it_IT/content/localeswitcher.json'
headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; mk_epub=%7B%22btuid%22%3A%22twoihc%22%2C%22prop57%22%3A%22www.us.homepage%22%7D; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
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
    'mk_epub': '%7B%22btuid%22%3A%22twoihc%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 12:08:06 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - date: Sat, 28 Nov 2020 11:58:50 GMT
#   - accept-ranges: bytes
#   - last-modified: Fri, 08 May 2020 00:10:56 GMT
#   - content-type: application/json
#   - server: Apache
#   - x-content-type-options: nosniff
#   - cache-control: max-age=556
#   - content-length: 390
#   - vary: Accept-Encoding
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 17
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
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
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; mk_epub=%7B%22btuid%22%3A%22fae48u%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.apple.com',
}
cookies = {
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'mk_epub': '%7B%22btuid%22%3A%22fae48u%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
}
params = [
    ('locale', 'en_US'),
    ('src', 'globalnav'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 12:00:50 GMT
#   - cache-control: max-age=119
#   - date: Sat, 28 Nov 2020 11:58:51 GMT
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-type: application/json
#   - content-length: 579
#   - x-content-type-options: nosniff
#   - x-frame-options: DENY
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: SAMEORIGIN
#   - strict-transport-security: max-age=31536000; includeSubdomains
###############################################################################

###############################################################################
# request number: 18
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    ':path': '/favicon.ico',
    'sec-fetch-mode': 'no-cors',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-site': 'same-origin',
    'referer': 'https://www.apple.com/',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; mk_epub=%7B%22btuid%22%3A%22fae48u%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    ':method': 'GET',
    'sec-fetch-dest': 'image',
    ':authority': 'www.apple.com',
}
cookies = {
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'mk_epub': '%7B%22btuid%22%3A%22fae48u%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-type: image/x-icon
#   - date: Sat, 28 Nov 2020 11:58:51 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 12:02:30 GMT
#   - server: Apache
#   - x-content-type-options: nosniff
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - content-length: 22382
#   - cache-control: max-age=219
###############################################################################

###############################################################################
# request number: 19
# resource type: xhr

url = 'https://www.apple.com/ac/localeswitcher/3/it_IT/content/localeswitcher.json'
headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'referer': 'https://www.apple.com/mac/',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D; s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmac%252520-%252520%25252Fmac%25252F%252520-%252520global%252520nav%2526region%253Dglobal%252520nav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmac%25252F%2526ot%253DA; mk_epub=%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    ':path': '/ac/localeswitcher/3/it_IT/content/localeswitcher.json',
    ':authority': 'www.apple.com',
}
cookies = {
    'mk_epub': '%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D',
    's_sq': 'appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmac%252520-%252520%25252Fmac%25252F%252520-%252520global%252520nav%2526region%253Dglobal%252520nav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmac%25252F%2526ot%253DA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 12:08:06 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - date: Sat, 28 Nov 2020 11:58:56 GMT
#   - accept-ranges: bytes
#   - last-modified: Fri, 08 May 2020 00:10:56 GMT
#   - content-type: application/json
#   - server: Apache
#   - x-content-type-options: nosniff
#   - cache-control: max-age=550
#   - content-length: 390
#   - vary: Accept-Encoding
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 20
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'referer': 'https://www.apple.com/mac/',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D; s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmac%252520-%252520%25252Fmac%25252F%252520-%252520global%252520nav%2526region%253Dglobal%252520nav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmac%25252F%2526ot%253DA; mk_epub=%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.apple.com',
}
cookies = {
    'mk_epub': '%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D',
    's_sq': 'appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526link%253Dmac%252520-%252520%25252Fmac%25252F%252520-%252520global%252520nav%2526region%253Dglobal%252520nav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dapple%252520-%252520index%25252Ftab%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fmac%25252F%2526ot%253DA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
}
params = [
    ('locale', 'en_US'),
    ('src', 'globalnav'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 12:00:50 GMT
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - date: Sat, 28 Nov 2020 11:58:56 GMT
#   - content-type: application/json
#   - content-length: 579
#   - x-content-type-options: nosniff
#   - x-frame-options: DENY
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: SAMEORIGIN
#   - strict-transport-security: max-age=31536000; includeSubdomains
#   - cache-control: max-age=114
###############################################################################

###############################################################################
# request number: 21
# resource type: xhr

url = 'https://www.apple.com/us/shop/mcm/product-price'
headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'referer': 'https://www.apple.com/mac/',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D; mk_epub=%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D; s_sq=%5B%5BB%5D%5D',
    ':path': '/us/shop/mcm/product-price?parts=MACBOOKAIR_M1,MBP2020_13_M1,MACMINI_M1,MBP2019_16',
    ':authority': 'www.apple.com',
}
cookies = {
    'mk_epub': '%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    's_sq': '%5B%5BB%5D%5D',
}
params = [
    ('parts', 'MACBOOKAIR_M1,MBP2020_13_M1,MACMINI_M1,MBP2019_16'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-content-type-options: nosniff
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:28:57 GMT; Path=/; Secure
#   - etag: "60ea5ead92cc30e1804649558a97a272"
#   - x-shred: dbfbac688d155a494f8955f574b628a5
#   - expires: Sat, 28 Nov 2020 12:00:57 GMT
#   - cache-control: private, max-age=120
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:58:57 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - last-modified: Sat, 28 Nov 2020 11:51:56 GMT
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - content-type: application/json; encoding=UTF8;charset=UTF-8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-request-id: 0b429fd6-ebf1-4609-960a-1387d30b403d
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:58:57 GMT; Max-Age=315360000; Secure; HttpOnly
#   - set-cookie: as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; Path=/; Domain=apple.com; Secure; HttpOnly
#   - x-xss-protection: 1; mode=block
#   - content-length: 285
#   - date: Sat, 28 Nov 2020 11:58:57 GMT
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - as_pcts: JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 22
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    ':path': '/favicon.ico',
    'sec-fetch-mode': 'no-cors',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'referer': 'https://www.apple.com/mac/',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'sec-fetch-dest': 'image',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D; mk_epub=%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D; s_sq=%5B%5BB%5D%5D; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc',
    ':authority': 'www.apple.com',
}
cookies = {
    'mk_epub': '%7B%22btuid%22%3A%221c9w4un%22%2C%22prop57%22%3A%22www.us.mac.tab%2Bother%22%7D',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.84%22%5D%2C%22eVar94%22%3A%223.84%22%2C%22eVar93%22%3A%221%22%7D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    's_sq': '%5B%5BB%5D%5D',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-type: image/x-icon
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 12:02:30 GMT
#   - server: Apache
#   - x-content-type-options: nosniff
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - content-length: 22382
#   - cache-control: max-age=213
#   - date: Sat, 28 Nov 2020 11:58:57 GMT
###############################################################################

###############################################################################
# request number: 23
# resource type: xhr

url = 'https://www.apple.com/ac/localeswitcher/3/it_IT/content/localeswitcher.json'
headers = {
    'referer': 'https://www.apple.com/macbook-air/',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D; mk_epub=%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D; s_sq=%5B%5BB%5D%5D',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    ':path': '/ac/localeswitcher/3/it_IT/content/localeswitcher.json',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    'mk_epub': '%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 12:08:06 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - accept-ranges: bytes
#   - last-modified: Fri, 08 May 2020 00:10:56 GMT
#   - content-type: application/json
#   - cache-control: max-age=544
#   - server: Apache
#   - x-content-type-options: nosniff
#   - content-length: 390
#   - date: Sat, 28 Nov 2020 11:59:02 GMT
#   - vary: Accept-Encoding
#   - content-encoding: gzip
###############################################################################

###############################################################################
# request number: 24
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'referer': 'https://www.apple.com/macbook-air/',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D; mk_epub=%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D; s_sq=%5B%5BB%5D%5D',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    'mk_epub': '%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('locale', 'en_US'),
    ('src', 'globalnav'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 12:00:50 GMT
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-type: application/json
#   - content-length: 579
#   - x-content-type-options: nosniff
#   - x-frame-options: DENY
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: SAMEORIGIN
#   - date: Sat, 28 Nov 2020 11:59:02 GMT
#   - cache-control: max-age=108
#   - strict-transport-security: max-age=31536000; includeSubdomains
###############################################################################

###############################################################################
# request number: 25
# resource type: xhr

url = 'https://www.apple.com/us/shop/mcm/product-price'
headers = {
    'referer': 'https://www.apple.com/macbook-air/',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D; mk_epub=%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D; s_sq=%5B%5BB%5D%5D',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    ':path': '/us/shop/mcm/product-price?parts=MACBOOKAIR_M1,MBP2020_13_M1,MBP2019_16',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    'mk_epub': '%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts', 'MACBOOKAIR_M1,MBP2020_13_M1,MBP2019_16'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:02 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - x-content-type-options: nosniff
#   - x-request-id: 29565b7b-cb4b-42ee-a488-7623debcbdf7
#   - last-modified: Sat, 28 Nov 2020 11:28:55 GMT
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:02 GMT; Path=/; Secure
#   - cache-control: private, max-age=120
#   - x-frame-options: DENY
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - content-length: 246
#   - content-type: application/json; encoding=UTF8;charset=UTF-8
#   - x-shred: 59f5e5b31f6a82123e700bf0969372e6
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - etag: "024e35d489441dd22e1f37c0c8eacaaa"
#   - x-xss-protection: 1; mode=block
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:02 GMT; Max-Age=315360000; Secure; HttpOnly
#   - date: Sat, 28 Nov 2020 11:59:02 GMT
#   - expires: Sat, 28 Nov 2020 12:01:02 GMT
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 26
# resource type: xhr

url = 'https://www.apple.com/us/shop/mcm/tradein-credit'
headers = {
    'referer': 'https://www.apple.com/macbook-air/',
    ':path': '/us/shop/mcm/tradein-credit?ids=6822',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D; mk_epub=%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D; s_sq=%5B%5BB%5D%5D',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    'mk_epub': '%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('ids', '6822'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:02 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-security-policy: frame-ancestors 'none'
#   - x-content-type-options: nosniff
#   - last-modified: Sat, 28 Nov 2020 11:34:26 GMT
#   - content-length: 167
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:02 GMT; Path=/; Secure
#   - x-shred: 0ceb720d986857001b5a958353c1321d
#   - cache-control: private, max-age=120
#   - x-frame-options: DENY
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - content-type: application/json; encoding=UTF8;charset=UTF-8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - etag: "be841b98bcc65c680726447afde658d2"
#   - x-xss-protection: 1; mode=block
#   - x-request-id: cb6a65c9-4319-41a9-9acb-9ed3ae446c97
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:02 GMT; Max-Age=315360000; Secure; HttpOnly
#   - date: Sat, 28 Nov 2020 11:59:02 GMT
#   - expires: Sat, 28 Nov 2020 12:01:02 GMT
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 27
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    ':path': '/favicon.ico',
    'sec-fetch-mode': 'no-cors',
    'referer': 'https://www.apple.com/macbook-air/',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; s_aca_ct=%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D; mk_epub=%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D; s_sq=%5B%5BB%5D%5D',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'sec-fetch-dest': 'image',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    's_aca_ct': '%7B%22linkTrackVars%22%3A%5B%22eVar94%22%2C%22eVar93%22%2C%22events%22%5D%2C%22linkTrackEvents%22%3A%5B%22event210%22%2C%22event246%22%5D%2C%22events%22%3A%5B%22event246%22%2C%22event210%3D3.58%22%5D%2C%22eVar94%22%3A%223.58%22%2C%22eVar93%22%3A%221%22%7D',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    'mk_epub': '%7B%22btuid%22%3A%222964zv%22%2C%22prop57%22%3A%22www.us.macbookair%22%7D',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-type: image/x-icon
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 12:02:30 GMT
#   - server: Apache
#   - x-content-type-options: nosniff
#   - date: Sat, 28 Nov 2020 11:59:03 GMT
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - content-length: 22382
#   - cache-control: max-age=207
###############################################################################

###############################################################################
# request number: 28
# resource type: xhr

url = 'https://www.apple.com/shop/bag/status'
headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'empty',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    ':path': '/shop/bag/status?apikey=SJHJUH4YFCTTPD4F4',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    ':authority': 'www.apple.com',
}
cookies = {
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('apikey', 'SJHJUH4YFCTTPD4F4'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-request-id: b48e9f3e-7a41-4fd1-8b13-a58c0b577e76
#   - x-content-type-options: nosniff
#   - content-language: en-US
#   - cache-control: private, no-cache, no-store, must-revalidate
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 11:59:12 GMT
#   - last-modified: Sat, 28 Nov 2020 11:59:12 GMT
#   - content-type: application/json;charset=utf-8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:12 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-shred: 8a89837e83a5f9f46e92058a02259a36
#   - pragma: no-cache
#   - date: Sat, 28 Nov 2020 11:59:12 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:12 GMT; Max-Age=315360000; Secure; HttpOnly
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:12 GMT; Max-Age=1800; Secure
#   - content-length: 137
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 29
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    ':path': '/shop/delivery-message?parts.0=MGN63LL%2FA&parts.1=MGND3LL%2FA&parts.2=MGN93LL%2FA&mt=regular&_=1606564751169',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts.0', 'MGN63LL%2FA'),
    ('mt', 'regular'),
    ('_', '1606564751169'),
    ('parts.1', 'MGND3LL%2FA'),
    ('parts.2', 'MGN93LL%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-content-type-options: nosniff
#   - x-request-id: 03dc1d7d-38a6-4a78-af4f-3a3384966408
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 11:59:12 GMT
#   - last-modified: Sat, 28 Nov 2020 11:59:12 GMT
#   - etag: "29ec11b4361e2bd43431fc80abaded48"
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - content-length: 2619
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-shred: fe11c8e5bc714a00fe8f24e101f1fc9c
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:12 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - date: Sat, 28 Nov 2020 11:59:12 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:12 GMT; Max-Age=315360000; Secure; HttpOnly
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:12 GMT; Max-Age=1800; Secure
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 30
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'cache-control': 'no-cache',
    ':path': '/shop/delivery-message?parts.0=MGN73LL%2FA&parts.1=MGNE3LL%2FA&parts.2=MGNA3LL%2FA&mt=regular&_=1606564751170',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('mt', 'regular'),
    ('parts.0', 'MGN73LL%2FA'),
    ('_', '1606564751170'),
    ('parts.1', 'MGNE3LL%2FA'),
    ('parts.2', 'MGNA3LL%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-content-type-options: nosniff
#   - x-request-id: ae22c422-f75b-4ea8-b928-2c1c9b160603
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 11:59:12 GMT
#   - last-modified: Sat, 28 Nov 2020 11:59:12 GMT
#   - etag: "f1dc33a1bc6f26266fa75dd39892cf7f"
#   - x-shred: ca3cb5c31fa3b6c39550dfd82fe8fd52
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - content-length: 2619
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:12 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - date: Sat, 28 Nov 2020 11:59:12 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:12 GMT; Max-Age=315360000; Secure; HttpOnly
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:12 GMT; Max-Age=1800; Secure
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 31
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    ':path': '/shop/retail/pickup-message?parts.0=MGN63LL%2FA&parts.1=MGND3LL%2FA&parts.2=MGN93LL%2FA',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('parts.0', 'MGN63LL%2FA'),
    ('parts.1', 'MGND3LL%2FA'),
    ('parts.2', 'MGN93LL%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:13 GMT; Max-Age=315360000; Secure; HttpOnly
#   - expires: Sat, 28 Nov 2020 11:59:13 GMT
#   - last-modified: Sat, 28 Nov 2020 11:59:13 GMT
#   - x-content-type-options: nosniff
#   - etag: "85b8326af30304fc90fdc4226363d716"
#   - x-shred: 35b6794469e915901a08352fe9580c48
#   - x-frame-options: DENY
#   - x-request-id: 528d7d97-2da7-4774-bd0e-fbe6dbe95770
#   - date: Sat, 28 Nov 2020 11:59:13 GMT
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:13 GMT; Max-Age=315360000; Secure; HttpOnly
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-length: 678
#   - pragma: no-cache
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:13 GMT; Max-Age=1800; Secure
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 32
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    ':path': '/shop/retail/pickup-message?parts.0=MGN73LL%2FA&parts.1=MGNE3LL%2FA&parts.2=MGNA3LL%2FA',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
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
#   - content-security-policy: frame-ancestors 'none'
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:13 GMT; Max-Age=315360000; Secure; HttpOnly
#   - expires: Sat, 28 Nov 2020 11:59:13 GMT
#   - etag: "160c59faae07886437ad8f608e70d68a"
#   - last-modified: Sat, 28 Nov 2020 11:59:13 GMT
#   - x-content-type-options: nosniff
#   - x-shred: eb19244e18d35204ecc9bb94b193aea3
#   - x-frame-options: DENY
#   - date: Sat, 28 Nov 2020 11:59:13 GMT
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:13 GMT; Max-Age=315360000; Secure; HttpOnly
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-length: 678
#   - pragma: no-cache
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:13 GMT; Max-Age=1800; Secure
#   - x-request-id: 05e26a26-6a43-4f82-926f-9c601481e23d
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 33
# resource type: xhr

url = 'https://www.apple.com/shop/updateFinanceSummary'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D; pxro=1',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    ':path': '/shop/updateFinanceSummary?node=home/shop_mac/family/macbook_air&parts.0=MGN63LL%2FA&parts.1=MGND3LL%2FA&parts.2=MGN93LL%2FA&parts.3=MGN73LL%2FA&parts.4=MGNE3LL%2FA&parts.5=MGNA3LL%2FA&tia=&bfil=2',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('tia', ''),
    ('parts.0', 'MGN63LL%2FA'),
    ('parts.3', 'MGN73LL%2FA'),
    ('parts.5', 'MGNA3LL%2FA'),
    ('node', 'home/shop_mac/family/macbook_air'),
    ('parts.1', 'MGND3LL%2FA'),
    ('parts.4', 'MGNE3LL%2FA'),
    ('parts.2', 'MGN93LL%2FA'),
    ('bfil', '2'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:13 GMT; Max-Age=315360000; Secure; HttpOnly
#   - expires: Sat, 28 Nov 2020 12:01:13 GMT
#   - x-content-type-options: nosniff
#   - etag: "5bcb2ab803df32a2a73aeffdbade92ab"
#   - content-length: 579
#   - cache-control: private, max-age=120
#   - x-frame-options: DENY
#   - content-type: application/json;charset=utf-8
#   - vary: Accept-Encoding
#   - x-request-id: 4fc2504a-35ec-4da6-8d1d-7ba5fe79924e
#   - content-encoding: gzip
#   - date: Sat, 28 Nov 2020 11:59:13 GMT
#   - x-shred: 0dd9a43f1b36cf58415b8c91e1d52ee1
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:13 GMT; Max-Age=315360000; Secure; HttpOnly
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:13 GMT; Path=/; Secure
#   - last-modified: Sat, 28 Nov 2020 11:28:57 GMT
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 34
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s55089049129067'
headers = {
    'Referer': 'https://www.apple.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}
params = [
    ('c40', '10078'),
    ('c', '24'),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('j', '1.6'),
    ('k', 'Y'),
    ('bw', '1420'),
    ('AQB', '1'),
    ('pf', '1'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fmacbook-air%2F'),
    ('ndh', '1'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air'),
    ('t', '28%2F10%2F2020%2012%3A59%3A13%206%20-60'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('pageName', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('server', 'as-13.5.0'),
    ('events', 'event210%3D1.07%2Cevent246'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('pev2', 'Step%201'),
    ('bh', '630'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('lrt', '724'),
    ('v19', 'D%3Dc19'),
    ('v97', 's.tl-o'),
    ('c8', 'AOS%3A%20Mac'),
    ('AQE', '1'),
    ('v49', 'D%3Dr'),
    ('s', '1920x1080'),
    ('v94', '1.07'),
    ('c4', 'D%3Dg'),
    ('v14', 'en-us'),
    ('v', 'N'),
    ('v54', 'D%3Dg'),
    ('v4', 'D%3DpageName'),
    ('c14', 'macbook%20air%20-%20overview%20%28us%29'),
    ('c5', 'macintel'),
    ('v35', 'web%20apply%7Cdenied%7Cpre%3Anot%20safari'),
    ('cc', 'USD'),
    ('ce', 'UTF-8'),
    ('pe', 'lnk_o'),
]
rc = s.post(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 35
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D; pxro=1',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    ':authority': 'www.apple.com',
}
cookies = {
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
params = [
    ('locale', 'en_US'),
    ('src', 'globalnav'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 12:00:50 GMT
#   - date: Sat, 28 Nov 2020 11:59:13 GMT
#   - cache-control: max-age=97
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-type: application/json
#   - content-length: 579
#   - x-content-type-options: nosniff
#   - x-frame-options: DENY
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: SAMEORIGIN
#   - strict-transport-security: max-age=31536000; includeSubdomains
###############################################################################

###############################################################################
# request number: 36
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s57395114027206'
headers = {
    'Referer': 'https://www.apple.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}
params = [
    ('c40', '10078'),
    ('c', '24'),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('v94', '1.39'),
    ('j', '1.6'),
    ('k', 'Y'),
    ('bw', '1420'),
    ('AQB', '1'),
    ('pf', '1'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fmacbook-air%2F'),
    ('events', 'event33%2Cevent210%3D1.39%2Cevent246'),
    ('ndh', '1'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air'),
    ('t', '28%2F10%2F2020%2012%3A59%3A13%206%20-60'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('pageName', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('server', 'as-13.5.0'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('bh', '630'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('pev2', 'Cold'),
    ('v19', 'D%3Dc19'),
    ('v97', 's.tl-o'),
    ('c37', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect%7Ccold%20start'),
    ('c8', 'AOS%3A%20Mac'),
    ('AQE', '1'),
    ('v49', 'D%3Dr'),
    ('s', '1920x1080'),
    ('c4', 'D%3Dg'),
    ('v14', 'en-us'),
    ('v', 'N'),
    ('v54', 'D%3Dg'),
    ('v4', 'D%3DpageName'),
    ('c14', 'macbook%20air%20-%20overview%20%28us%29'),
    ('c5', 'macintel'),
    ('cc', 'USD'),
    ('ce', 'UTF-8'),
    ('pe', 'lnk_o'),
    ('lrt', '1'),
]
rc = s.post(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 37
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    ':path': '/favicon.ico',
    'sec-fetch-mode': 'no-cors',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D; pxro=1',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'sec-fetch-dest': 'image',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air',
    ':authority': 'www.apple.com',
}
cookies = {
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'geo': 'IT',
    'check': 'true',
    'as_dc': 'nc',
    'pxro': '1',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    's_cc': 'true',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-type: image/x-icon
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 12:02:30 GMT
#   - server: Apache
#   - x-content-type-options: nosniff
#   - date: Sat, 28 Nov 2020 11:59:14 GMT
#   - cache-control: max-age=196
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - content-length: 22382
###############################################################################

###############################################################################
# request number: 38
# resource type: xhr

url = 'https://store.storeimages.cdn-apple.com/4982/store.apple.com/shop/rs-external/rel/external.js'
headers = {
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Origin': 'https://www.apple.com',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.apple.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Site': 'cross-site',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Host': 'store.storeimages.cdn-apple.com',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - Content-Encoding: gzip
#   - Access-Control-Allow-Origin: *
#   - Date: Sat, 28 Nov 2020 11:59:14 GMT
#   - Expires: Sat, 28 Nov 2020 12:00:39 GMT
#   - x-shred: 73dc9cc218b4d274a506b1659d8cc044
#   - Server: Apple
#   - X-Frame-Options: DENY
#   - Accept-Ranges: bytes
#   - X-Cache: TCP_HIT from a92-122-95-84.deploy.akamaitechnologies.com (AkamaiGHost/10.2.2.1-31386017) (-)
#   - X-CDN: Akam
#   - Content-Length: 141036
#   - Vary: Accept-Encoding
#   - Last-Modified: Sat, 31 Oct 2020 06:14:18 GMT
#   - Connection: keep-alive
#   - ETag: "7dfa5-5b2f16c562280-gzip"
#   - X-XSS-Protection: 1; mode=block
#   - Cache-Control: max-age=85
#   - Access-Control-Expose-Headers: X-CDN
#   - Content-Type: application/javascript
#   - Content-Security-Policy: frame-ancestors 'none'
#   - Strict-Transport-Security: max-age=31536000
#   - X-Content-Type-Options: nosniff
###############################################################################

###############################################################################
# request number: 39
# resource type: other

url = 'https://xp.apple.com/report/2/xp_aos_clientperf'
headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://www.apple.com',
    'Access-Control-Request-Method': 'POST',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.apple.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Access-Control-Request-Headers': 'content-type',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Host': 'xp.apple.com',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
}
rc = s.options(url, headers=headers)


# response status code: 200
# response headers:
#   - Access-Control-Allow-Headers: content-type
#   - X-Apple-Application-Instance: 233
#   - Access-Control-Allow-Methods: POST
#   - X-Apple-Jingle-Correlation-Key: 2X6YU2T3HN72ZRDQTFTUHWKPTA
#   - Access-Control-Max-Age: 86400
#   - Content-Length: 0
#   - Date: Sat, 28 Nov 2020 11:59:14 GMT
#   - X-Apple-Application-Site: ST
#   - Connection: keep-alive
#   - Strict-Transport-Security: max-age=31536000
#   - Access-Control-Allow-Origin: https://www.apple.com
#   - Access-Control-Allow-Credentials: true
###############################################################################

###############################################################################
# request number: 40
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s56893829888064'
headers = {
    'Referer': 'https://www.apple.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}
params = [
    ('c40', '10078'),
    ('c', '24'),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('j', '1.6'),
    ('pev2', 'undefined%7CStep%201%20-%20Select%20Button%7Cselected'),
    ('k', 'Y'),
    ('bw', '1420'),
    ('AQB', '1'),
    ('pf', '1'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fmacbook-air%2F'),
    ('ndh', '1'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air'),
    ('server', 'as-13.5.0'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('pageName', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('lrt', '91'),
    ('bh', '630'),
    ('pageIDType', '1'),
    ('v6', 'D%3DpageName%2B%22%7C%7C%7CStep%201%20-%20Select%20Button%7Cselected%22'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('page', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('v19', 'D%3Dc19'),
    ('v94', '7.01'),
    ('v97', 's.tl-o'),
    ('activitymap.', ''),
    ('oid', 'proceed'),
    ('oidt', '3'),
    ('c8', 'AOS%3A%20Mac'),
    ('.activitymap', ''),
    ('AQE', '1'),
    ('events', 'event210%3D7.01%2Cevent246%2Cevent500'),
    ('v49', 'D%3Dr'),
    ('a.', ''),
    ('s', '1920x1080'),
    ('c4', 'D%3Dg'),
    ('v14', 'en-us'),
    ('region', 'body'),
    ('v', 'N'),
    ('t', '28%2F10%2F2020%2012%3A59%3A19%206%20-60'),
    ('v54', 'D%3Dg'),
    ('.a', ''),
    ('pid', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('.c', ''),
    ('v4', 'D%3DpageName'),
    ('c14', 'macbook%20air%20-%20overview%20%28us%29'),
    ('c5', 'macintel'),
    ('link', 'select%20apple%20m1%20chip%20with%208core%20cpu%20and%207core%20gpu%20%7C%20no%20href%20%7C%20body'),
    ('cc', 'USD'),
    ('c.', ''),
    ('ce', 'UTF-8'),
    ('pe', 'lnk_o'),
    ('pidt', '1'),
    ('ot', 'SUBMIT'),
]
rc = s.post(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 41
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    ':path': '/shop/delivery-message?parts.0=MGN63LL%2FA&option.0=065-C99M%2C065-C99Q%2C065-C9DG%2C065-C171%2C065-C172&mt=regular&_=1606564760188',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('_', '1606564760188'),
    ('parts.0', 'MGN63LL%2FA'),
    ('option.0', '065-C99M%2C065-C99Q%2C065-C9DG%2C065-C171%2C065-C172'),
    ('mt', 'regular'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-shred: 149ff2d0d584f4bc505369f987b35dc5
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:21 GMT; Max-Age=1800; Secure
#   - x-content-type-options: nosniff
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:21 GMT; Max-Age=315360000; Secure; HttpOnly
#   - date: Sat, 28 Nov 2020 11:59:21 GMT
#   - x-frame-options: DENY
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:21 GMT; Max-Age=315360000; Secure; HttpOnly
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-length: 1081
#   - pragma: no-cache
#   - etag: "78649f7e4831b77dc7e079f490707d00"
#   - expires: Sat, 28 Nov 2020 11:59:21 GMT
#   - last-modified: Sat, 28 Nov 2020 11:59:21 GMT
#   - x-xss-protection: 1; mode=block
#   - x-request-id: b5308b25-7b34-4be5-b7b9-07d9e520deb8
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 42
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s54378695892321'
headers = {
    'Referer': 'https://www.apple.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}
params = [
    ('c40', '10078'),
    ('c', '24'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air'),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('j', '1.6'),
    ('k', 'Y'),
    ('bw', '1420'),
    ('AQB', '1'),
    ('pf', '1'),
    ('v94', '0.96'),
    ('t', '28%2F10%2F2020%2012%3A59%3A21%206%20-60'),
    ('ndh', '1'),
    ('server', 'as-13.5.0'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('events', 'event210%3D0.96%2Cevent246'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('pev2', 'Step%201'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air%2Fspace-gray-apple-m1-chip-with-8%25E2%2580%2591core-cpu-and-7%25E2%2580%2591core-gpu-256gb%23'),
    ('lrt', '598'),
    ('bh', '630'),
    ('c14', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('v19', 'D%3Dc19'),
    ('v97', 's.tl-o'),
    ('c8', 'AOS%3A%20Mac'),
    ('AQE', '1'),
    ('v49', 'D%3Dr'),
    ('s', '1920x1080'),
    ('c4', 'D%3Dg'),
    ('v14', 'en-us'),
    ('v', 'N'),
    ('v54', 'D%3Dg'),
    ('v4', 'D%3DpageName'),
    ('c5', 'macintel'),
    ('v35', 'web%20apply%7Cdenied%7Cpre%3Anot%20safari'),
    ('cc', 'USD'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('ce', 'UTF-8'),
    ('pe', 'lnk_o'),
    ('pageName', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
]
rc = s.post(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 43
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('locale', 'en_US'),
    ('src', 'globalnav'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 12:00:50 GMT
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - date: Sat, 28 Nov 2020 11:59:22 GMT
#   - content-type: application/json
#   - content-length: 579
#   - x-content-type-options: nosniff
#   - x-frame-options: DENY
#   - cache-control: max-age=88
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: SAMEORIGIN
#   - strict-transport-security: max-age=31536000; includeSubdomains
###############################################################################

###############################################################################
# request number: 44
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
    ':scheme': 'https',
    ':path': '/shop/retail/pickup-message?parts.0=MGN63LL%2FA&option.0=065-C99M%2C065-C99Q%2C065-C9DG%2C065-C171%2C065-C172',
    'sec-fetch-site': 'same-origin',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('parts.0', 'MGN63LL%2FA'),
    ('option.0', '065-C99M%2C065-C99Q%2C065-C9DG%2C065-C171%2C065-C172'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - content-length: 292
#   - x-content-type-options: nosniff
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - etag: "775cdf1983cc35d0363d91d0132a6700"
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - expires: Sat, 28 Nov 2020 11:59:22 GMT
#   - x-shred: 38f3b09344ed283b0fe7a29c188c5bd5
#   - last-modified: Sat, 28 Nov 2020 11:59:22 GMT
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:22 GMT; Max-Age=1800; Secure
#   - pragma: no-cache
#   - date: Sat, 28 Nov 2020 11:59:22 GMT
#   - x-xss-protection: 1; mode=block
#   - x-request-id: ceaba216-9341-4e35-ba5a-ff1cb9336699
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 45
# resource type: xhr

url = 'https://www.apple.com/shop/configUpdate/MGN63LL/A'
headers = {
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    ':path': '/shop/configUpdate/MGN63LL/A?node=home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig&option.memory__dummy_z124=065-C99M&option.hard_drivesolid_state_drive__dummy_z124=065-C99Q&option.keyboard_and_documentation_z124=065-C9DG&option.sw_final_cut_pro_x_z124=065-C171&option.sw_logic_pro_x_z124=065-C172&product=MGN63LL%2FA&step=config&bfil=2',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('option.sw_final_cut_pro_x_z124', '065-C171'),
    ('option.sw_logic_pro_x_z124', '065-C172'),
    ('option.keyboard_and_documentation_z124', '065-C9DG'),
    ('product', 'MGN63LL%2FA'),
    ('option.hard_drivesolid_state_drive__dummy_z124', '065-C99Q'),
    ('node', 'home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('option.memory__dummy_z124', '065-C99M'),
    ('step', 'config'),
    ('bfil', '2'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:22 GMT; Path=/; Secure
#   - cache-control: private, max-age=59
#   - x-content-type-options: nosniff
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-length: 1970
#   - x-frame-options: DENY
#   - x-request-id: 4910bd54-cca2-4f95-9e07-045127c24e79
#   - vary: Accept-Encoding
#   - content-encoding: gzip
#   - content-type: application/json; encoding=UTF8;charset=UTF-8
#   - x-shred: 80020217b73f20b8728c4453e23d4864
#   - etag: "23991255b5e8a8029161ec433ec0ca9f"
#   - server: Apple
#   - last-modified: Sat, 28 Nov 2020 11:58:22 GMT
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - date: Sat, 28 Nov 2020 11:59:22 GMT
#   - x-xss-protection: 1; mode=block
#   - expires: Sat, 28 Nov 2020 12:00:21 GMT
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 46
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s5719408662668'
headers = {
    'Referer': 'https://www.apple.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}
params = [
    ('c40', '10078'),
    ('c', '24'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air'),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('j', '1.6'),
    ('t', '28%2F10%2F2020%2012%3A59%3A22%206%20-60'),
    ('k', 'Y'),
    ('bw', '1420'),
    ('AQB', '1'),
    ('pf', '1'),
    ('ndh', '1'),
    ('server', 'as-13.5.0'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air%2Fspace-gray-apple-m1-chip-with-8%25E2%2580%2591core-cpu-and-7%25E2%2580%2591core-gpu-256gb%23'),
    ('bh', '630'),
    ('c14', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('pev2', 'Cold'),
    ('v19', 'D%3Dc19'),
    ('v97', 's.tl-o'),
    ('c8', 'AOS%3A%20Mac'),
    ('AQE', '1'),
    ('events', 'event33%2Cevent210%3D1.33%2Cevent246'),
    ('v49', 'D%3Dr'),
    ('s', '1920x1080'),
    ('c4', 'D%3Dg'),
    ('v14', 'en-us'),
    ('v', 'N'),
    ('v54', 'D%3Dg'),
    ('v4', 'D%3DpageName'),
    ('c5', 'macintel'),
    ('cc', 'USD'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('v94', '1.33'),
    ('ce', 'UTF-8'),
    ('pe', 'lnk_o'),
    ('lrt', '1'),
    ('pageName', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
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
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    ':path': '/shop/delivery-message?parts.0=MGN63LL%2FA&option.0=065-C99J%2C065-C99M%2C065-C99Q%2C065-C9CL%2C065-C9DG%2C065-C9CK%2C065-C9CH%2C065-C9CJ%2C065-C171%2C065-C172&mt=regular&_=1606564760189',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('_', '1606564760189'),
    ('parts.0', 'MGN63LL%2FA'),
    ('mt', 'regular'),
    ('option.0', '065-C99J%2C065-C99M%2C065-C99Q%2C065-C9CL%2C065-C9DG%2C065-C9CK%2C065-C9CH%2C065-C9CJ%2C065-C171%2C065-C172'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-content-type-options: nosniff
#   - x-request-id: ab4e08a8-7bea-468a-be73-7d4c6a0bf9d2
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - expires: Sat, 28 Nov 2020 11:59:22 GMT
#   - last-modified: Sat, 28 Nov 2020 11:59:22 GMT
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-shred: b65116103131a52806499f238a7dbd8a
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-cache: TCP_MISS from a92-122-95-54.deploy.akamaitechnologies.com (AkamaiGHost/10.2.2.1-31386017) (-)
#   - content-length: 1081
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:22 GMT; Max-Age=1800; Secure
#   - pragma: no-cache
#   - etag: "78649f7e4831b77dc7e079f490707d00"
#   - date: Sat, 28 Nov 2020 11:59:22 GMT
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 48
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
    ':path': '/shop/retail/pickup-message?parts.0=MGN63LL%2FA&option.0=065-C99J%2C065-C99M%2C065-C99Q%2C065-C9CL%2C065-C9DG%2C065-C9CK%2C065-C9CH%2C065-C9CJ%2C065-C171%2C065-C172',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('parts.0', 'MGN63LL%2FA'),
    ('option.0', '065-C99J%2C065-C99M%2C065-C99Q%2C065-C9CL%2C065-C9DG%2C065-C9CK%2C065-C9CH%2C065-C9CJ%2C065-C171%2C065-C172'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - content-length: 292
#   - x-content-type-options: nosniff
#   - x-shred: 96084d670cdc4332526624b546ad82a8
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - etag: "775cdf1983cc35d0363d91d0132a6700"
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - expires: Sat, 28 Nov 2020 11:59:22 GMT
#   - last-modified: Sat, 28 Nov 2020 11:59:22 GMT
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:22 GMT; Max-Age=315360000; Secure; HttpOnly
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:22 GMT; Max-Age=1800; Secure
#   - pragma: no-cache
#   - date: Sat, 28 Nov 2020 11:59:22 GMT
#   - x-request-id: 19ebd534-a76e-4c5f-896b-b22c19e016bf
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 49
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    ':path': '/favicon.ico',
    'sec-fetch-mode': 'no-cors',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    ':method': 'GET',
    'sec-fetch-dest': 'image',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air/space-gray-apple-m1-chip-with-8%E2%80%91core-cpu-and-7%E2%80%91core-gpu-256gb',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyMA|bd24f42caddadc789d311b27afde1f05fc9262f2',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-type: image/x-icon
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 12:02:30 GMT
#   - date: Sat, 28 Nov 2020 11:59:22 GMT
#   - server: Apache
#   - x-content-type-options: nosniff
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - cache-control: max-age=188
#   - content-length: 22382
###############################################################################

###############################################################################
# request number: 50
# resource type: xhr

url = 'https://store.storeimages.cdn-apple.com/4982/store.apple.com/shop/rs-external/rel/external.js'
headers = {
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Origin': 'https://www.apple.com',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.apple.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Site': 'cross-site',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Host': 'store.storeimages.cdn-apple.com',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - Content-Encoding: gzip
#   - Access-Control-Allow-Origin: *
#   - Expires: Sat, 28 Nov 2020 12:00:39 GMT
#   - Cache-Control: max-age=76
#   - x-shred: 73dc9cc218b4d274a506b1659d8cc044
#   - Server: Apple
#   - X-Frame-Options: DENY
#   - Accept-Ranges: bytes
#   - X-Cache: TCP_HIT from a92-122-95-84.deploy.akamaitechnologies.com (AkamaiGHost/10.2.2.1-31386017) (-)
#   - X-CDN: Akam
#   - Content-Length: 141036
#   - Date: Sat, 28 Nov 2020 11:59:23 GMT
#   - Vary: Accept-Encoding
#   - Last-Modified: Sat, 31 Oct 2020 06:14:18 GMT
#   - Connection: keep-alive
#   - ETag: "7dfa5-5b2f16c562280-gzip"
#   - X-XSS-Protection: 1; mode=block
#   - Access-Control-Expose-Headers: X-CDN
#   - Content-Type: application/javascript
#   - Content-Security-Policy: frame-ancestors 'none'
#   - Strict-Transport-Security: max-age=31536000
#   - X-Content-Type-Options: nosniff
###############################################################################

###############################################################################
# request number: 51
# resource type: other

url = 'https://xp.apple.com/report/2/xp_aos_clientperf'
headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://www.apple.com',
    'Access-Control-Request-Method': 'POST',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.apple.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Access-Control-Request-Headers': 'content-type',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Host': 'xp.apple.com',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
}
rc = s.options(url, headers=headers)


# response status code: 200
# response headers:
#   - Access-Control-Allow-Headers: content-type
#   - Access-Control-Allow-Methods: POST
#   - X-Apple-Jingle-Correlation-Key: FONLIHFLXSISLWNNV27DGHXK64
#   - Date: Sat, 28 Nov 2020 11:59:23 GMT
#   - X-Apple-Application-Instance: 245
#   - Access-Control-Max-Age: 86400
#   - Content-Length: 0
#   - X-Apple-Application-Site: ST
#   - Connection: keep-alive
#   - Strict-Transport-Security: max-age=31536000
#   - Access-Control-Allow-Origin: https://www.apple.com
#   - Access-Control-Allow-Credentials: true
###############################################################################

###############################################################################
# request number: 52
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s5737338969557'
headers = {
    'Referer': 'https://www.apple.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}
params = [
    ('events', 'scAdd%2Cevent210%3D3.37%2Cevent246%2Cevent500'),
    ('c40', '10078'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air'),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('c', '24'),
    ('j', '1.6'),
    ('page', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('k', 'Y'),
    ('bw', '1420'),
    ('AQB', '1'),
    ('pf', '1'),
    ('v94', '3.37'),
    ('ndh', '1'),
    ('server', 'as-13.5.0'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('oid', 'add-to-cart'),
    ('t', '28%2F10%2F2020%2012%3A59%3A24%206%20-60'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air%2Fspace-gray-apple-m1-chip-with-8%25E2%2580%2591core-cpu-and-7%25E2%2580%2591core-gpu-256gb%23'),
    ('pev2', 'CTO'),
    ('pageIDType', '1'),
    ('pid', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('c14', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fselect'),
    ('bh', '630'),
    ('products', 'macbook_air%3BMGN63%3B1%3B999.00%3B%3B'),
    ('lrt', '62'),
    ('oidt', '3'),
    ('v19', 'D%3Dc19'),
    ('v97', 's.tl-o'),
    ('activitymap.', ''),
    ('c8', 'AOS%3A%20Mac'),
    ('.activitymap', ''),
    ('AQE', '1'),
    ('v49', 'D%3Dr'),
    ('a.', ''),
    ('s', '1920x1080'),
    ('c4', 'D%3Dg'),
    ('v14', 'en-us'),
    ('region', 'body'),
    ('v', 'N'),
    ('v54', 'D%3Dg'),
    ('.a', ''),
    ('.c', ''),
    ('v4', 'D%3DpageName'),
    ('c5', 'macintel'),
    ('v5', 'D%3DpageName%2B%22%7C%7CCTO%7CAdd%20to%20Bag%22'),
    ('cc', 'USD'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('c.', ''),
    ('ce', 'UTF-8'),
    ('pe', 'lnk_o'),
    ('link', 'add%20to%20bag%20%28inner%20text%29%20%7C%20no%20href%20%7C%20body'),
    ('pidt', '1'),
    ('ot', 'SUBMIT'),
    ('pageName', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
]
rc = s.post(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 53
# resource type: xhr

url = 'https://www.apple.com/shop/bag/status'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'empty',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    ':path': '/shop/bag/status?apikey=SJHJUH4YFCTTPD4F4',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('apikey', 'SJHJUH4YFCTTPD4F4'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-request-id: 8951d6e0-5f95-4e54-bce1-0a92dddc9d6c
#   - expires: Sat, 28 Nov 2020 11:59:26 GMT
#   - x-content-type-options: nosniff
#   - last-modified: Sat, 28 Nov 2020 11:59:26 GMT
#   - content-language: en-US
#   - x-shred: 4757fcd44d5092fa330c8c24b9a3d3a8
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:26 GMT; Max-Age=1800; Secure
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:26 GMT; Max-Age=315360000; Secure; HttpOnly
#   - cache-control: private, no-cache, no-store, must-revalidate
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:26 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-frame-options: DENY
#   - content-type: application/json;charset=utf-8
#   - date: Sat, 28 Nov 2020 11:59:26 GMT
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - pragma: no-cache
#   - content-length: 137
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 54
# resource type: xhr

url = 'https://www.apple.com/shop/buyFlowAttachConfigProductSummary/MGN63LL/A'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    ':path': '/shop/buyFlowAttachConfigProductSummary/MGN63LL/A?node=home/shop_mac/family/macbook_air&step=attach&bfil=2&product=MGN63LL%2FA&step=attach&option.sw_logic_pro_x_z124=065-C172&option.keyboard_and_documentation_z124=065-C9DG&option.memory__dummy_z124=065-C99M&complete=true&option.hard_drivesolid_state_drive__dummy_z124=065-C99Q&option.sw_final_cut_pro_x_z124=065-C171&proceed=proceed',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('option.sw_final_cut_pro_x_z124', '065-C171'),
    ('option.sw_logic_pro_x_z124', '065-C172'),
    ('option.keyboard_and_documentation_z124', '065-C9DG'),
    ('node', 'home/shop_mac/family/macbook_air'),
    ('complete', 'true'),
    ('proceed', 'proceed'),
    ('product', 'MGN63LL%2FA'),
    ('option.hard_drivesolid_state_drive__dummy_z124', '065-C99Q'),
    ('step', 'attach'),
    ('option.memory__dummy_z124', '065-C99M'),
    ('bfil', '2'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-content-type-options: nosniff
#   - last-modified: Sat, 28 Nov 2020 11:59:13 GMT
#   - x-request-id: 42e3edab-922f-467f-aaf9-f3234fe64051
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:26 GMT; Max-Age=315360000; Secure; HttpOnly
#   - cache-control: private, max-age=103
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:26 GMT; Max-Age=315360000; Secure; HttpOnly
#   - expires: Sat, 28 Nov 2020 12:01:09 GMT
#   - x-frame-options: DENY
#   - vary: Accept-Encoding
#   - date: Sat, 28 Nov 2020 11:59:26 GMT
#   - content-encoding: gzip
#   - content-type: application/json; encoding=UTF8;charset=UTF-8
#   - set-cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:26 GMT; Path=/; Secure
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - content-length: 804
#   - x-shred: 55c0b6ad27ff3f8361949ab2cc096398
#   - x-xss-protection: 1; mode=block
#   - etag: "514f19dee4342585b61cc2d5593eed3d"
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 55
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    ':path': '/shop/delivery-message?parts.0=S6124LL%2FA&parts.1=MJ1M2AM%2FA&parts.2=MX0K2AM%2FA&mt=compact&_=1606564765355',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('parts.0', 'S6124LL%2FA'),
    ('_', '1606564765355'),
    ('parts.2', 'MX0K2AM%2FA'),
    ('parts.1', 'MJ1M2AM%2FA'),
    ('mt', 'compact'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-request-id: 9ecaa922-0b00-459b-b585-bf80822d353c
#   - x-content-type-options: nosniff
#   - etag: "9869b80006656e76fd565f180c59cf7e"
#   - content-length: 1112
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-shred: d5695525be89f566d66f0bf9367b04c1
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 56
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    ':path': '/shop/delivery-message?parts.0=MLA02LL%2FA&parts.1=MUF82AM%2FA&parts.2=MRQM2ZM%2FA&mt=compact&_=1606564765356',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('parts.0', 'MLA02LL%2FA'),
    ('parts.2', 'MRQM2ZM%2FA'),
    ('_', '1606564765356'),
    ('mt', 'compact'),
    ('parts.1', 'MUF82AM%2FA'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-request-id: ebe0f017-1e99-4609-8e3a-b8a5b61685bc
#   - x-content-type-options: nosniff
#   - etag: "db4d166b1b34516deb40fe2d756af67d"
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - server: Apple
#   - content-length: 1117
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-shred: b58d219ecf4ac5aa8bcf5107d7aed020
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 57
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    ':path': '/shop/delivery-message?parts.0=MUFG2AM%2FA&parts.1=MQ4H2AM%2FA&parts.2=MWP22AM%2FA&mt=compact&_=1606564765357',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('parts.0', 'MUFG2AM%2FA'),
    ('parts.1', 'MQ4H2AM%2FA'),
    ('mt', 'compact'),
    ('parts.2', 'MWP22AM%2FA'),
    ('_', '1606564765357'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-request-id: 14383983-3353-4512-9619-9c24c11763ff
#   - x-content-type-options: nosniff
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - etag: "7bb2939718ef8efa7be606d9e24d8ee8"
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
#   - content-length: 1119
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - x-shred: 76fa3376927b710e8fba7d20f586cef3
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 58
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    ':path': '/shop/delivery-message?parts.0=MV7N2AM%2FA&parts.1=MRXJ2AM%2FA&parts.2=MMEL2AM%2FA&mt=compact&_=1606564765358',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('parts.2', 'MMEL2AM%2FA'),
    ('_', '1606564765358'),
    ('parts.0', 'MV7N2AM%2FA'),
    ('parts.1', 'MRXJ2AM%2FA'),
    ('mt', 'compact'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-content-type-options: nosniff
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
#   - content-length: 1119
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-request-id: 28ef2c16-5533-4835-8de6-4af1a01735b2
#   - etag: "295c45334086e5878080e8c4be15e2d7"
#   - x-shred: 59cac7873ddac86c5ce0e54b36cdf169
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 59
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':path': '/shop/delivery-message?parts.0=HMUA2VC%2FA&parts.1=HMUB2LL%2FA&parts.2=MK122LL%2FA&mt=compact&_=1606564765359',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('parts.2', 'MK122LL%2FA'),
    ('_', '1606564765359'),
    ('parts.0', 'HMUA2VC%2FA'),
    ('parts.1', 'HMUB2LL%2FA'),
    ('mt', 'compact'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-content-type-options: nosniff
#   - etag: "172c9c75800a5b0a2fe480f7103f933b"
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - server: Apple
#   - content-length: 1127
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-shred: fabff9c77206f5d10bb52b9b3c5cc8dd
#   - pragma: no-cache
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - x-request-id: 50c022da-3af2-4d45-9972-9c47fe20b9b8
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 60
# resource type: xhr

url = 'https://www.apple.com/shop/delivery-message'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    ':path': '/shop/delivery-message?parts.0=HMU22ZM%2FA&parts.1=HPA02ZM%2FA&mt=compact&_=1606564765360',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('parts.1', 'HPA02ZM%2FA'),
    ('parts.0', 'HMU22ZM%2FA'),
    ('mt', 'compact'),
    ('_', '1606564765360'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-request-id: 34dd6b13-21bc-4643-a3be-85fe069ee775
#   - x-content-type-options: nosniff
#   - x-shred: d6fa087576d99bc3fdb2337ccd5b937b
#   - etag: "a8496c7f3f1fb0a543a1148cb00009e9"
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - x-xss-protection: 1; mode=block
#   - content-length: 873
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 61
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':path': '/shop/retail/pickup-message?parts.0=S6124LL%2FA&parts.1=MJ1M2AM%2FA&parts.2=MX0K2AM%2FA&little=true',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('parts.2', 'MX0K2AM%2FA'),
    ('parts.1', 'MJ1M2AM%2FA'),
    ('parts.0', 'S6124LL%2FA'),
    ('little', 'true'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-shred: 02b2ca61d50382d030ab9047d0938ab7
#   - x-content-type-options: nosniff
#   - x-request-id: cecdb21c-0e80-4bb8-801c-529cbb4b0c04
#   - etag: "b9e91d6c67a36c5d5d86e2200e136c79"
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - content-length: 475
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 62
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    ':path': '/shop/retail/pickup-message?parts.0=MLA02LL%2FA&parts.1=MUF82AM%2FA&parts.2=MRQM2ZM%2FA&little=true',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('parts.0', 'MLA02LL%2FA'),
    ('parts.1', 'MUF82AM%2FA'),
    ('parts.2', 'MRQM2ZM%2FA'),
    ('little', 'true'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-shred: fa795f1fdb35467d1ee9d56246bd0d93
#   - date: Sat, 28 Nov 2020 11:59:28 GMT
#   - x-content-type-options: nosniff
#   - etag: "69a6bdeb11f22a603cb18448e69980ea"
#   - x-frame-options: DENY
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - expires: Sat, 28 Nov 2020 11:59:28 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - last-modified: Sat, 28 Nov 2020 11:59:28 GMT
#   - content-length: 715
#   - pragma: no-cache
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - x-xss-protection: 1; mode=block
#   - x-request-id: 44cb7e08-cac9-4a4f-b28a-f3a756a52d6a
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 63
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    ':authority': 'www.apple.com',
    'accept-language': 'en-US,en;q=0.9',
    ':path': '/shop/retail/pickup-message?parts.0=MUFG2AM%2FA&parts.1=MQ4H2AM%2FA&parts.2=MWP22AM%2FA&little=true',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('parts.1', 'MQ4H2AM%2FA'),
    ('parts.2', 'MWP22AM%2FA'),
    ('parts.0', 'MUFG2AM%2FA'),
    ('little', 'true'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-shred: 34e378b8a5eb20677ffd5a8cea3c785f
#   - content-length: 661
#   - date: Sat, 28 Nov 2020 11:59:28 GMT
#   - x-content-type-options: nosniff
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:28 GMT; Max-Age=1800; Secure
#   - x-frame-options: DENY
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-request-id: 5c0986a4-f3b8-4969-94dc-74c845c75826
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:28 GMT; Max-Age=315360000; Secure; HttpOnly
#   - etag: "f0fd7822f3da9297934ca54ed51bd8a1"
#   - expires: Sat, 28 Nov 2020 11:59:28 GMT
#   - last-modified: Sat, 28 Nov 2020 11:59:28 GMT
#   - pragma: no-cache
#   - x-xss-protection: 1; mode=block
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:28 GMT; Max-Age=315360000; Secure; HttpOnly
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 64
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    ':path': '/shop/retail/pickup-message?parts.0=MV7N2AM%2FA&parts.1=MRXJ2AM%2FA&parts.2=MMEL2AM%2FA&little=true',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('parts.2', 'MMEL2AM%2FA'),
    ('parts.0', 'MV7N2AM%2FA'),
    ('parts.1', 'MRXJ2AM%2FA'),
    ('little', 'true'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - date: Sat, 28 Nov 2020 11:59:28 GMT
#   - content-length: 697
#   - x-content-type-options: nosniff
#   - x-frame-options: DENY
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - expires: Sat, 28 Nov 2020 11:59:28 GMT
#   - x-shred: 643ee9168a2909d998e0ed4b328ee159
#   - x-request-id: e85f738a-d42f-4cab-be7c-0662b0bd6554
#   - last-modified: Sat, 28 Nov 2020 11:59:28 GMT
#   - etag: "30f5777bcf377a3e177d1c9923bd1b23"
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 65
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    ':scheme': 'https',
    ':path': '/shop/retail/pickup-message?parts.0=HMUA2VC%2FA&parts.1=HMUB2LL%2FA&parts.2=MK122LL%2FA&little=true',
    'sec-fetch-site': 'same-origin',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('parts.0', 'HMUA2VC%2FA'),
    ('parts.2', 'MK122LL%2FA'),
    ('parts.1', 'HMUB2LL%2FA'),
    ('little', 'true'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - content-length: 665
#   - x-content-type-options: nosniff
#   - etag: "a07d206f3ec3c8e28e298fcac08537b3"
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - x-request-id: 89807fde-3ee0-4947-bfdc-1d839c86f113
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-shred: a98c8e51d835d9bc14c21c64ef4fe6aa
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 66
# resource type: xhr

url = 'https://www.apple.com/shop/retail/pickup-message'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    ':path': '/shop/retail/pickup-message?parts.0=HMU22ZM%2FA&parts.1=HPA02ZM%2FA&little=true',
    'accept-language': 'en-US,en;q=0.9',
    ':authority': 'www.apple.com',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-site': 'same-origin',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('parts.1', 'HPA02ZM%2FA'),
    ('parts.0', 'HMU22ZM%2FA'),
    ('little', 'true'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - content-security-policy: frame-ancestors 'none'
#   - x-content-type-options: nosniff
#   - content-length: 540
#   - x-frame-options: DENY
#   - expires: Sat, 28 Nov 2020 11:59:27 GMT
#   - last-modified: Sat, 28 Nov 2020 11:59:27 GMT
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-request-id: 83de65dd-fbe3-4160-9c52-1fb08ce2145f
#   - etag: "25d909e1f4f92ef25e1622ccd030755d"
#   - date: Sat, 28 Nov 2020 11:59:27 GMT
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:27 GMT; Max-Age=315360000; Secure; HttpOnly
#   - pragma: no-cache
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:27 GMT; Max-Age=1800; Secure
#   - x-shred: 36a8946356b07871d144bff4a7bf39f2
#   - x-xss-protection: 1; mode=block
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 67
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('locale', 'en_US'),
    ('src', 'globalnav'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 12:00:50 GMT
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - date: Sat, 28 Nov 2020 11:59:28 GMT
#   - content-type: application/json
#   - content-length: 579
#   - cache-control: max-age=82
#   - x-content-type-options: nosniff
#   - x-frame-options: DENY
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: SAMEORIGIN
#   - strict-transport-security: max-age=31536000; includeSubdomains
###############################################################################

###############################################################################
# request number: 68
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s52456596436101'
headers = {
    'Referer': 'https://www.apple.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}
params = [
    ('c40', '10078'),
    ('c', '24'),
    ('t', '28%2F10%2F2020%2012%3A59%3A28%206%20-60'),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('j', '1.6'),
    ('c14', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fconfig'),
    ('k', 'Y'),
    ('bw', '1420'),
    ('AQB', '1'),
    ('pf', '1'),
    ('lrt', '2503'),
    ('ndh', '1'),
    ('server', 'as-13.5.0'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('bh', '630'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air%3Fbfil%3D2%26product%3DMGN63LL%2FA%26step%3Dattach'),
    ('c37', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fattach%7Ccold%20start'),
    ('v94', '2.88'),
    ('pageName', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fattach'),
    ('pev2', 'Cold'),
    ('v19', 'D%3Dc19'),
    ('v97', 's.tl-o'),
    ('c8', 'AOS%3A%20Mac'),
    ('AQE', '1'),
    ('events', 'event33%2Cevent210%3D2.88%2Cevent246'),
    ('v49', 'D%3Dr'),
    ('s', '1920x1080'),
    ('c4', 'D%3Dg'),
    ('v14', 'en-us'),
    ('v', 'N'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air%2Fspace-gray-apple-m1-chip-with-8%25E2%2580%2591core-cpu-and-7%25E2%2580%2591core-gpu-256gb'),
    ('v54', 'D%3Dg'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fattach'),
    ('v4', 'D%3DpageName'),
    ('c5', 'macintel'),
    ('cc', 'USD'),
    ('ce', 'UTF-8'),
    ('pe', 'lnk_o'),
]
rc = s.post(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 69
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    ':path': '/favicon.ico',
    'sec-fetch-mode': 'no-cors',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'referer': 'https://www.apple.com/shop/buy-mac/macbook-air?bfil=2&product=MGN63LL/A&step=attach',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'sec-fetch-dest': 'image',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-type: image/x-icon
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 12:02:30 GMT
#   - date: Sat, 28 Nov 2020 11:59:29 GMT
#   - server: Apache
#   - x-content-type-options: nosniff
#   - cache-control: max-age=181
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - content-length: 22382
###############################################################################

###############################################################################
# request number: 70
# resource type: xhr

url = 'https://store.storeimages.cdn-apple.com/4982/store.apple.com/shop/rs-external/rel/external.js'
headers = {
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Origin': 'https://www.apple.com',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.apple.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Site': 'cross-site',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Host': 'store.storeimages.cdn-apple.com',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - Content-Encoding: gzip
#   - Access-Control-Allow-Origin: *
#   - Expires: Sat, 28 Nov 2020 12:00:39 GMT
#   - x-shred: 73dc9cc218b4d274a506b1659d8cc044
#   - Server: Apple
#   - X-Frame-Options: DENY
#   - Accept-Ranges: bytes
#   - X-Cache: TCP_HIT from a92-122-95-84.deploy.akamaitechnologies.com (AkamaiGHost/10.2.2.1-31386017) (-)
#   - X-CDN: Akam
#   - Content-Length: 141036
#   - Vary: Accept-Encoding
#   - Date: Sat, 28 Nov 2020 11:59:30 GMT
#   - Last-Modified: Sat, 31 Oct 2020 06:14:18 GMT
#   - Connection: keep-alive
#   - ETag: "7dfa5-5b2f16c562280-gzip"
#   - X-XSS-Protection: 1; mode=block
#   - Cache-Control: max-age=69
#   - Access-Control-Expose-Headers: X-CDN
#   - Content-Type: application/javascript
#   - Content-Security-Policy: frame-ancestors 'none'
#   - Strict-Transport-Security: max-age=31536000
#   - X-Content-Type-Options: nosniff
###############################################################################

###############################################################################
# request number: 71
# resource type: other

url = 'https://xp.apple.com/report/2/xp_aos_clientperf'
headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://www.apple.com',
    'Access-Control-Request-Method': 'POST',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.apple.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Access-Control-Request-Headers': 'content-type',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Host': 'xp.apple.com',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
}
rc = s.options(url, headers=headers)


# response status code: 200
# response headers:
#   - Access-Control-Allow-Headers: content-type
#   - Access-Control-Allow-Methods: POST
#   - X-Apple-Application-Instance: 246
#   - Access-Control-Max-Age: 86400
#   - Date: Sat, 28 Nov 2020 11:59:30 GMT
#   - Content-Length: 0
#   - X-Apple-Jingle-Correlation-Key: ULPZODFXG2RFWYZZ5FVCBTIXGY
#   - X-Apple-Application-Site: ST
#   - Connection: keep-alive
#   - Strict-Transport-Security: max-age=31536000
#   - Access-Control-Allow-Origin: https://www.apple.com
#   - Access-Control-Allow-Credentials: true
###############################################################################

###############################################################################
# request number: 72
# resource type: xhr

url = 'https://www.apple.com/shop/bag/status'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; as_xs=flc=; as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; s_sq=%5B%5BB%5D%5D',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'referer': 'https://www.apple.com/shop/bag',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'sec-fetch-dest': 'empty',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    ':path': '/shop/bag/status?apikey=SJHJUH4YFCTTPD4F4',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xs': 'flc=',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    'as_xsm': '1&TsS1k4znjEvnGjBoAe_vvw',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('apikey', 'SJHJUH4YFCTTPD4F4'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - last-modified: Sat, 28 Nov 2020 11:59:32 GMT
#   - content-security-policy: frame-ancestors 'none'
#   - x-shred: 076f68c1c717e2a5694dc93e60255ed1
#   - x-request-id: 0f191352-02fb-4708-9389-131847f017fa
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:32 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-content-type-options: nosniff
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:32 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-language: en-US
#   - date: Sat, 28 Nov 2020 11:59:32 GMT
#   - cache-control: private, no-cache, no-store, must-revalidate
#   - x-frame-options: DENY
#   - content-type: application/json;charset=utf-8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:32 GMT; Max-Age=1800; Secure
#   - pragma: no-cache
#   - content-length: 137
#   - x-xss-protection: 1; mode=block
#   - expires: Sat, 28 Nov 2020 11:59:32 GMT
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 73
# resource type: xhr

url = 'https://www.apple.com/shop/recommendedForYou-full'
headers = {
    ':method': 'POST',
    'origin': 'https://www.apple.com',
    'referer': 'https://www.apple.com/shop/bag',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'x-aos-stk': '9b49e9bc',
    ':path': '/shop/recommendedForYou-full?partsInCart.0=MGN63LL/A&inline=true&recentAddedPart=MGN63LL/A',
    ':authority': 'www.apple.com',
    'accept-language': 'en-US,en;q=0.9',
    'syntax': 'graviton',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; as_xs=flc=; as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; s_sq=%5B%5BB%5D%5D',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'sec-fetch-dest': 'empty',
    'x-aos-model-page': 'cart',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'content-type': 'application/x-www-form-urlencoded',
    'modelversion': 'v2',
    'content-length': '0',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xs': 'flc=',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    'as_xsm': '1&TsS1k4znjEvnGjBoAe_vvw',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('recentAddedPart', 'MGN63LL/A'),
    ('partsInCart.0', 'MGN63LL/A'),
    ('inline', 'true'),
]
rc = s.post(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - last-modified: Sat, 28 Nov 2020 11:59:32 GMT
#   - content-security-policy: frame-ancestors 'none'
#   - x-shred: 5cc55ea61f50b8ff9215e484c70a0e3d
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:32 GMT; Max-Age=315360000; Secure; HttpOnly
#   - x-content-type-options: nosniff
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:32 GMT; Max-Age=315360000; Secure; HttpOnly
#   - access-control-allow-origin: https://www.apple.com
#   - date: Sat, 28 Nov 2020 11:59:32 GMT
#   - set-cookie: as_xs=flc=; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:32 GMT; Max-Age=15552000; Secure; HttpOnly
#   - x-request-id: f3c431bd-e6b5-4411-bdfd-f884c43b93b0
#   - x-frame-options: DENY
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - content-type: application/json;encoding=UTF8;charset=UTF-8
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - set-cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:32 GMT; Max-Age=1800; Secure
#   - etag: "88836b1c32feac9edc46b3e946530b53"
#   - content-length: 12731
#   - pragma: no-cache
#   - access-control-allow-credentials: true
#   - set-cookie: as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:32 GMT; Max-Age=15552000; Secure; HttpOnly
#   - x-xss-protection: 1; mode=block
#   - expires: Sat, 28 Nov 2020 11:59:32 GMT
# response cookies:
#   - as_xs: flc=
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - as_xsm: 1&TsS1k4znjEvnGjBoAe_vvw
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 74
# resource type: xhr

url = 'https://www.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; as_xs=flc=; as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; s_sq=%5B%5BB%5D%5D',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    ':path': '/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US',
    'referer': 'https://www.apple.com/shop/bag',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'sec-fetch-mode': 'cors',
    ':method': 'GET',
    'sec-fetch-dest': 'empty',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xs': 'flc=',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    'as_xsm': '1&TsS1k4znjEvnGjBoAe_vvw',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('locale', 'en_US'),
    ('src', 'globalnav'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - expires: Sat, 28 Nov 2020 12:00:50 GMT
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - date: Sat, 28 Nov 2020 11:59:32 GMT
#   - content-type: application/json
#   - content-length: 579
#   - x-content-type-options: nosniff
#   - x-frame-options: DENY
#   - x-xss-protection: 1; mode=block
#   - x-frame-options: SAMEORIGIN
#   - cache-control: max-age=78
#   - strict-transport-security: max-age=31536000; includeSubdomains
###############################################################################

###############################################################################
# request number: 75
# resource type: other

url = 'https://www.apple.com/favicon.ico'
headers = {
    ':path': '/favicon.ico',
    'sec-fetch-mode': 'no-cors',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; as_xs=flc=; as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; s_sq=%5B%5BB%5D%5D',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'referer': 'https://www.apple.com/shop/bag',
    'accept-language': 'en-US,en;q=0.9',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    ':method': 'GET',
    'sec-fetch-dest': 'image',
    ':authority': 'www.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xs': 'flc=',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    'as_xsm': '1&TsS1k4znjEvnGjBoAe_vvw',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
rc = s.get(url, headers=headers, cookies=cookies)


# response status code: 200
# response headers:
#   - content-type: image/x-icon
#   - cache-control: max-age=177
#   - x-cache: TCP_MEM_HIT from a92-122-95-54.deploy.akamaitechnologies.com (AkamaiGHost/10.2.2.1-31386017) (-)
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - accept-ranges: bytes
#   - expires: Sat, 28 Nov 2020 12:02:30 GMT
#   - server: Apache
#   - x-content-type-options: nosniff
#   - date: Sat, 28 Nov 2020 11:59:33 GMT
#   - last-modified: Fri, 04 May 2018 17:15:31 GMT
#   - content-length: 22382
###############################################################################

###############################################################################
# request number: 76
# resource type: xhr

url = 'https://store.storeimages.cdn-apple.com/4982/store.apple.com/shop/rs-external/rel/external.js'
headers = {
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Origin': 'https://www.apple.com',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.apple.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Site': 'cross-site',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Host': 'store.storeimages.cdn-apple.com',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - Content-Encoding: gzip
#   - Access-Control-Allow-Origin: *
#   - Expires: Sat, 28 Nov 2020 12:00:39 GMT
#   - Date: Sat, 28 Nov 2020 11:59:33 GMT
#   - x-shred: 73dc9cc218b4d274a506b1659d8cc044
#   - Server: Apple
#   - X-Frame-Options: DENY
#   - Cache-Control: max-age=66
#   - Accept-Ranges: bytes
#   - X-Cache: TCP_HIT from a92-122-95-84.deploy.akamaitechnologies.com (AkamaiGHost/10.2.2.1-31386017) (-)
#   - X-CDN: Akam
#   - Content-Length: 141036
#   - Vary: Accept-Encoding
#   - Last-Modified: Sat, 31 Oct 2020 06:14:18 GMT
#   - Connection: keep-alive
#   - ETag: "7dfa5-5b2f16c562280-gzip"
#   - X-XSS-Protection: 1; mode=block
#   - Access-Control-Expose-Headers: X-CDN
#   - Content-Type: application/javascript
#   - Content-Security-Policy: frame-ancestors 'none'
#   - Strict-Transport-Security: max-age=31536000
#   - X-Content-Type-Options: nosniff
###############################################################################

###############################################################################
# request number: 77
# resource type: other

url = 'https://xp.apple.com/report/2/xp_aos_clientperf'
headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://www.apple.com',
    'Access-Control-Request-Method': 'POST',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.apple.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Access-Control-Request-Headers': 'content-type',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Host': 'xp.apple.com',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
}
rc = s.options(url, headers=headers)


# response status code: 200
# response headers:
#   - Access-Control-Allow-Headers: content-type
#   - X-Apple-Jingle-Correlation-Key: 7T6U7HPVMXMQL3V57DTOS33MAM
#   - Access-Control-Allow-Methods: POST
#   - X-Apple-Application-Instance: 251
#   - Access-Control-Max-Age: 86400
#   - Content-Length: 0
#   - X-Apple-Application-Site: ST
#   - Connection: keep-alive
#   - Strict-Transport-Security: max-age=31536000
#   - Access-Control-Allow-Origin: https://www.apple.com
#   - Access-Control-Allow-Credentials: true
#   - Date: Sat, 28 Nov 2020 11:59:33 GMT
###############################################################################

###############################################################################
# request number: 78
# resource type: other

url = 'https://securemetrics.apple.com/b/ss/applestoreww,appleglobal/1/JS-2.17.0/s52405784184661'
headers = {
    'Referer': 'https://www.apple.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}
params = [
    ('c40', '10078'),
    ('c', '24'),
    ('lrt', '61'),
    ('g', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbag'),
    ('c20', 'AOS%3A%20US%20Consumer'),
    ('j', '1.6'),
    ('r', 'https%3A%2F%2Fwww.apple.com%2Fshop%2Fbuy-mac%2Fmacbook-air%3Fbfil%3D2%26product%3DMGN63LL%2FA%26step%3Dattach'),
    ('t', '28%2F10%2F2020%2012%3A59%3A37%206%20-60'),
    ('pid', 'AOS%3A%20bag'),
    ('oid', 'Check%20Out'),
    ('k', 'Y'),
    ('bw', '1420'),
    ('AQB', '1'),
    ('pf', '1'),
    ('pev2', 'shoppingCart.actions.t.checkout'),
    ('ndh', '1'),
    ('events', 'event210%3D6.08%2Cevent246%2Cevent500'),
    ('server', 'as-13.5.0'),
    ('fid', '0EE10F1DE7BC5EFE-229AB97ADA08D75A'),
    ('v3', 'AOS%3A%20US%20Consumer'),
    ('v94', '6.08'),
    ('bh', '630'),
    ('c8', 'AOS%3A%20Bag'),
    ('pageIDType', '1'),
    ('c19', 'AOS%3A%20US%20Consumer%3A%20bag'),
    ('oidt', '3'),
    ('v19', 'D%3Dc19'),
    ('v39', 'D%3DpageName%2B%22%7C%7CBag%7CStandardCheckout%22'),
    ('v97', 's.tl-o'),
    ('activitymap.', ''),
    ('AQE', '1'),
    ('.activitymap', ''),
    ('c14', 'AOS%3A%20home%2Fshop_mac%2Ffamily%2Fmacbook_air%2Fattach'),
    ('v49', 'D%3Dr'),
    ('a.', ''),
    ('s', '1920x1080'),
    ('c4', 'D%3Dg'),
    ('v14', 'en-us'),
    ('region', 'body'),
    ('v', 'N'),
    ('link', 'check%20out%20%28inner%20text%29%20%7C%20no%20href%20%7C%20body'),
    ('v54', 'D%3Dg'),
    ('pageName', 'AOS%3A%20bag'),
    ('.a', ''),
    ('.c', ''),
    ('v4', 'D%3DpageName'),
    ('c5', 'macintel'),
    ('page', 'AOS%3A%20bag'),
    ('cc', 'USD'),
    ('c.', ''),
    ('ce', 'UTF-8'),
    ('pe', 'lnk_o'),
    ('pidt', '1'),
    ('ot', 'SUBMIT'),
]
rc = s.post(url, headers=headers, params=params)


# response status code: 0
###############################################################################

###############################################################################
# request number: 79
# resource type: xhr

url = 'https://www.apple.com/shop/bagx/checkout_now'
headers = {
    ':method': 'POST',
    'origin': 'https://www.apple.com',
    'referer': 'https://www.apple.com/shop/bag',
    'cache-control': 'no-cache',
    'modelversion': 'v2',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'x-aos-stk': '9b49e9bc',
    'content-length': '322',
    ':authority': 'www.apple.com',
    'accept-language': 'en-US,en;q=0.9',
    'syntax': 'graviton',
    'cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; as_atb=1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2; as_xs=flc=; as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; s_sq=%5B%5BB%5D%5D',
    'x-requested-with': 'XMLHttpRequest',
    'pragma': 'no-cache',
    ':scheme': 'https',
    'x-aos-model-page': 'cart',
    ':path': '/shop/bagx/checkout_now?_a=checkout&_m=shoppingCart.actions',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-fetch-dest': 'empty',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'as_atb': '1.0|MjAyMC0xMS0yOCAwMzo1OToyNQ|1945caae5ed90d551fce0ba742bca42cdd655de2',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xs': 'flc=',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    'as_xsm': '1&TsS1k4znjEvnGjBoAe_vvw',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
}
params = [
    ('_a', 'checkout'),
    ('_m', 'shoppingCart.actions'),
]
rc = s.post(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - x-content-type-options: nosniff
#   - x-frame-options: SAMEORIGIN
#   - set-cookie: as_xs=flc=; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:38 GMT; Max-Age=15552000; Secure; HttpOnly
#   - content-type: application/json; charset=UTF-8; encoding=UTF8
#   - expires: Sat, 28 Nov 2020 11:59:38 GMT
#   - vary: Accept-Encoding
#   - last-modified: Sat, 28 Nov 2020 11:59:38 GMT
#   - content-encoding: gzip
#   - content-security-policy: frame-ancestors 'self'
#   - set-cookie: as_xsm=1&TsS1k4znjEvnGjBoAe_vvw; Path=/; Domain=apple.com; Expires=Thu, 27-May-2021 11:59:38 GMT; Max-Age=15552000; Secure; HttpOnly
#   - x-shred: 41d5c228bf6f7c4837131d5832491a41
#   - cache-control: private, no-cache, no-store, must-revalidate, proxy-revalidate, post-check=0, pre-check=0
#   - set-cookie: as_dc=nc; version="1"; max-age=1800; expires=Sat, 28-Nov-2020 12:29:38 GMT; path=/; domain=apple.com; secure
#   - server: Apple
#   - strict-transport-security: max-age=31536000; includeSubDomains
#   - x-request-id: 6ba1df9e-ab94-4b93-a68a-1e67a87686fb
#   - set-cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:38 GMT; Max-Age=315360000; Secure; HttpOnly
#   - content-length: 345
#   - x-serverprocessingtime: 72
#   - pragma: no-cache
#   - date: Sat, 28 Nov 2020 11:59:38 GMT
#   - x-xss-protection: 1; mode=block
#   - set-cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:38 GMT; Max-Age=315360000; Secure; HttpOnly
# response cookies:
#   - as_xs: flc=
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - as_xsm: 1&TsS1k4znjEvnGjBoAe_vvw
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 80
# resource type: xhr

url = 'https://secure2.store.apple.com/shop/bag/status'
headers = {
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Sec-Fetch-Mode': 'cors',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://secure2.store.apple.com/shop/sign_in?c=aHR0cHM6Ly93d3cuYXBwbGUuY29tL3Nob3AvYmFnfDFhb3NjY2QxZjg4ZGZjYjY4YWRhNWZmMmY5ZTY5YWMzNjE0OTYyMjZlOWMz&o=O01HTjYz&r=SXYD4UDAPXU7P7KXF&s=aHR0cHM6Ly9zZWN1cmUyLnN0b3JlLmFwcGxlLmNvbS9zaG9wL2NoZWNrb3V0L3N0YXJ0P3BsdG49QTZGNDNFMER8MWFvczg4MjgzMjY3MzJkNWEzNjIxMTQxMDE0ZTU4NmZiNTY5MjEzZGEyY2M&t=SXYD4UDAPXU7P7KXF&up=t',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    'Host': 'secure2.store.apple.com',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
}
params = [
    ('apikey', 'SKCXTKATUYT9JK4HD'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - Expires: Fri, 27 Nov 2020 11:59:39 GMT
#   - Set-Cookie: dssid2=0deece74-9857-4594-b36e-273d7f7dec11; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:39 GMT; Max-Age=315360000; Secure; HttpOnly
#   - Server: Apple
#   - X-Frame-Options: DENY
#   - Content-Type: application/json;charset=utf-8
#   - Set-Cookie: dssf=1; Path=/; Domain=apple.com; Expires=Tue, 26-Nov-2030 11:59:39 GMT; Max-Age=315360000; Secure; HttpOnly
#   - Vary: accept-encoding
#   - Strict-Transport-Security: max-age=31536000; includeSubDomains
#   - Expires: Thu, 01 Jan 1970 00:00:00 GMT
#   - Pragma: no-cache
#   - Content-Length: 17
#   - Connection: keep-alive
#   - Date: Sat, 28 Nov 2020 11:59:39 GMT
#   - x-request-id: e61cbda2-c288-4106-bf0b-19c7fa14ea48
#   - Cache-Control: private, no-store, no-cache, must-revalidate, no-siteapp
#   - X-XSS-Protection: 1; mode=block
#   - Last-Modified: Sat, 28 Nov 2020 11:59:39 GMT
#   - x-shred: 0d13b5754739951f74c61bb7f47ef962
#   - Set-Cookie: as_dc=nc; Path=/; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:39 GMT; Max-Age=1800; Secure
#   - Content-Language: en-US
#   - Content-Security-Policy: frame-ancestors 'none'
#   - X-Content-Type-Options: nosniff
# response cookies:
#   - dssid2: 0deece74-9857-4594-b36e-273d7f7dec11
#   - as_dc: nc
#   - dssf: 1
###############################################################################

###############################################################################
# request number: 81
# resource type: xhr

url = 'https://secure2.store.apple.com/search-services/suggestions/defaultlinks/'
headers = {
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Sec-Fetch-Mode': 'cors',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://secure2.store.apple.com/shop/sign_in?c=aHR0cHM6Ly93d3cuYXBwbGUuY29tL3Nob3AvYmFnfDFhb3NjY2QxZjg4ZGZjYjY4YWRhNWZmMmY5ZTY5YWMzNjE0OTYyMjZlOWMz&o=O01HTjYz&r=SXYD4UDAPXU7P7KXF&s=aHR0cHM6Ly9zZWN1cmUyLnN0b3JlLmFwcGxlLmNvbS9zaG9wL2NoZWNrb3V0L3N0YXJ0P3BsdG49QTZGNDNFMER8MWFvczg4MjgzMjY3MzJkNWEzNjIxMTQxMDE0ZTU4NmZiNTY5MjEzZGEyY2M&t=SXYD4UDAPXU7P7KXF&up=t',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    'Host': 'secure2.store.apple.com',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
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
#   - Content-Encoding: gzip
#   - Content-Length: 8204
#   - Edge-Control: !no-store, cache-maxage=120
#   - x-shred: b0abdff3ab738ad2a74bf72156baf7e1
#   - Content-Type: text/html;charset=utf-8
#   - Server: Apple
#   - X-Frame-Options: DENY
#   - Vary: accept-encoding
#   - Set-Cookie: as_dc=nc; Domain=apple.com; Expires=Sat, 28-Nov-2020 12:29:39 GMT; Path=/; Secure
#   - Strict-Transport-Security: max-age=31536000; includeSubDomains
#   - ETag: "b81a098cfd586c44ab4211da0183e7c1"
#   - x-request-id: 1d2be014-eeb4-43b8-b909-5a91a3ecff31
#   - Last-Modified: Sat, 28 Nov 2020 11:53:16 GMT
#   - Connection: keep-alive
#   - Date: Sat, 28 Nov 2020 11:59:39 GMT
#   - X-XSS-Protection: 1; mode=block
#   - Cache-Control: private, max-age=120
#   - Expires: Sat, 28 Nov 2020 12:01:39 GMT
#   - Content-Security-Policy: frame-ancestors 'none'
#   - X-Content-Type-Options: nosniff
# response cookies:
#   - as_dc: nc
###############################################################################

###############################################################################
# request number: 82
# resource type: document

url = 'https://idmsa.apple.com/appleauth/auth/authorize/signin'
headers = {
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q',
    'Sec-Fetch-Mode': 'navigate',
    'Host': 'idmsa.apple.com',
    'Referer': 'https://secure2.store.apple.com/',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Dest': 'iframe',
    'Cache-Control': 'no-cache',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
}
params = [
    ('iframeId', 'auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj'),
    ('frame_id', 'auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj'),
    ('response_type', 'code'),
    ('language', 'en_US'),
    ('state', 'auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj'),
    ('response_mode', 'web_message'),
    ('client_id', 'a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b'),
    ('redirect_uri', 'https://secure2.store.apple.com'),
]
rc = s.get(url, headers=headers, cookies=cookies, params=params)


# response status code: 200
# response headers:
#   - Content-Encoding: gzip
#   - Transfer-Encoding: chunked
#   - X-BuildVersion: R2
#   - X-FRAME-OPTIONS: ALLOW-FROM https://secure2.store.apple.com
#   - Cache-Control: no-store
#   - Set-Cookie: site=USA; Domain=apple.com; Path=/; Secure; HttpOnly
#   - vary: accept-encoding
#   - Server: Apple
#   - Cache-Control: no-cache
#   - Expires: Thu, 01 Jan 1970 00:00:00 GMT
#   - Date: Sat, 28 Nov 2020 11:59:40 GMT
#   - Pragma: no-cache
#   - X-Apple-Auth-Attributes: dic0tBi4vhC93orxwirSFqhMve5dYbsQPWFmvVU/gdFdeqbKLQpUuUOsUCxX8FHl/ZGJjs4OnbXsmni0Xl/Yyutsbp8ogC3bXvj0tHXlrafJstxkI8ghdxz9G9oopF/AbMjQ5snnEE18nVXm4yvlfF2esocAC4tujG28cg==
#   - Content-Security-Policy: default-src 'self'; script-src 'self' https://*.apple.com https://*.cdn-apple.com ; object-src 'self' https://*.apple-mapkit.com; style-src 'unsafe-inline' https://*.apple.com https://*.cdn-apple.com https://*.apple-mapkit.com ; img-src 'self' data: https://*.apple.com https://*.cdn-apple.com https://*.icloud.com https://*.mzstatic.com https://*.apple-mapkit.com ; media-src * data:; connect-src 'self' https://*.apple-mapkit.com; font-src 'self' https://*.apple.com https://*.cdn-apple.com; frame-src https://appleid.apple.com;  frame-ancestors https://secure2.store.apple.com;
#   - Connection: keep-alive
#   - scnt: 8093ff807ba9fcfb78f018de1f0a2305
#   - Set-Cookie: aa=991DE1862A229067497F55E997BAE2F5; Domain=idmsa.apple.com; Path=/; Secure; HttpOnly
#   - X-XSS-Protection: 1; mode=block
#   - Set-Cookie: dslang=US-EN; Domain=apple.com; Path=/; Secure; HttpOnly
#   - Content-Type: text/html;charset=UTF-8
#   - Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
#   - X-Apple-I-Request-ID: 8f1b031d-51f5-4d12-b2af-4b89ec8cce52
#   - Content-Language: en-US-x-lvariant-USA
#   - X-Content-Type-Options: nosniff
# response cookies:
#   - site: USA
#   - dslang: US-EN
#   - aa: 991DE1862A229067497F55E997BAE2F5
###############################################################################

###############################################################################
# request number: 83
# resource type: xhr

url = 'https://store.storeimages.cdn-apple.com/4982/store.apple.com/shop/rs-external/rel/external.js'
headers = {
    'Origin': 'https://secure2.store.apple.com',
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Sec-Fetch-Mode': 'cors',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Site': 'cross-site',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://secure2.store.apple.com/',
    'Host': 'store.storeimages.cdn-apple.com',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
}
rc = s.get(url, headers=headers)


# response status code: 200
# response headers:
#   - Content-Encoding: gzip
#   - Access-Control-Allow-Origin: *
#   - Expires: Sat, 28 Nov 2020 12:00:39 GMT
#   - x-shred: 73dc9cc218b4d274a506b1659d8cc044
#   - X-Cache: TCP_HIT from a92-122-95-84.deploy.akamaitechnologies.com (AkamaiGHost/10.2.2.1-31386017) (A)
#   - Server: Apple
#   - X-Frame-Options: DENY
#   - Cache-Control: max-age=59
#   - Accept-Ranges: bytes
#   - X-CDN: Akam
#   - Date: Sat, 28 Nov 2020 11:59:40 GMT
#   - Content-Length: 141036
#   - Vary: Accept-Encoding
#   - Last-Modified: Sat, 31 Oct 2020 06:14:18 GMT
#   - Connection: keep-alive
#   - ETag: "7dfa5-5b2f16c562280-gzip"
#   - X-XSS-Protection: 1; mode=block
#   - Access-Control-Expose-Headers: X-CDN
#   - Content-Type: application/javascript
#   - Content-Security-Policy: frame-ancestors 'none'
#   - Strict-Transport-Security: max-age=31536000
#   - X-Content-Type-Options: nosniff
###############################################################################

###############################################################################
# request number: 84
# resource type: other

url = 'https://xp.apple.com/report/2/xp_aos_clientperf'
headers = {
    'Origin': 'https://secure2.store.apple.com',
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Access-Control-Request-Method': 'POST',
    'Sec-Fetch-Mode': 'cors',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Access-Control-Request-Headers': 'content-type',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://secure2.store.apple.com/',
    'Host': 'xp.apple.com',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
}
rc = s.options(url, headers=headers)


# response status code: 200
# response headers:
#   - Access-Control-Allow-Headers: content-type
#   - Date: Sat, 28 Nov 2020 11:59:40 GMT
#   - Access-Control-Allow-Methods: POST
#   - Access-Control-Max-Age: 86400
#   - Content-Length: 0
#   - Access-Control-Allow-Origin: https://secure2.store.apple.com
#   - X-Apple-Jingle-Correlation-Key: RBYLFZFQYQLAQWWURGWXTWP4WA
#   - X-Apple-Application-Site: ST
#   - X-Apple-Application-Instance: 248
#   - Connection: keep-alive
#   - Strict-Transport-Security: max-age=31536000
#   - Access-Control-Allow-Credentials: true
###############################################################################

###############################################################################
# request number: 85
# resource type: xhr

url = 'https://idmsa.apple.com/appleauth/jslog'
headers = {
    'Accept': 'application/json',
    'Pragma': 'no-cache',
    'Sec-Fetch-Mode': 'cors',
    'Cache-Control': 'no-cache',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; aa=991DE1862A229067497F55E997BAE2F5; dslang=US-EN; site=USA',
    'scnt': '',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Content-Length': '280',
    'Accept-Language': 'en-US,en;q=0.9',
    'x-csrf-token': '',
    'Referer': 'https://idmsa.apple.com/appleauth/auth/authorize/signin?frame_id=auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj&language=en_US&iframeId=auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj&client_id=a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b&redirect_uri=https://secure2.store.apple.com&response_type=code&response_mode=web_message&state=auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj',
    'Host': 'idmsa.apple.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Dest': 'empty',
    'Origin': 'https://idmsa.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'dslang': 'US-EN',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'aa': '991DE1862A229067497F55E997BAE2F5',
}
rc = s.post(url, headers=headers, cookies=cookies)


# response status code: 204
# response headers:
#   - Pragma: no-cache
#   - X-XSS-Protection: 1; mode=block
#   - Cache-Control: no-cache
#   - Set-Cookie: site=USA; Domain=apple.com; Path=/; Secure; HttpOnly
#   - Content-Security-Policy: default-src 'self'; script-src 'self' https://*.apple.com https://*.cdn-apple.com ; object-src 'self' https://*.apple-mapkit.com; style-src 'unsafe-inline' https://*.apple.com https://*.cdn-apple.com https://*.apple-mapkit.com ; img-src 'self' data: https://*.apple.com https://*.cdn-apple.com https://*.icloud.com https://*.mzstatic.com https://*.apple-mapkit.com ; media-src * data:; connect-src 'self' https://*.apple-mapkit.com; font-src 'self' https://*.apple.com https://*.cdn-apple.com; frame-src https://appleid.apple.com;
#   - Set-Cookie: dslang=US-EN; Domain=apple.com; Path=/; Secure; HttpOnly
#   - Date: Sat, 28 Nov 2020 11:59:41 GMT
#   - Server: Apple
#   - Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
#   - X-BuildVersion: R2
#   - X-Apple-I-Request-ID: cd293672-d66b-45c1-884f-eed28001cdbb
#   - scnt: b44963741cc0a2b8ff76999a2a4d3369
#   - Connection: keep-alive
#   - Cache-Control: no-store
#   - X-FRAME-OPTIONS: DENY
#   - Expires: Thu, 01 Jan 1970 00:00:00 GMT
#   - X-Content-Type-Options: nosniff
# response cookies:
#   - site: USA
#   - dslang: US-EN
###############################################################################

###############################################################################
# request number: 86
# resource type: other

url = 'https://secure2.store.apple.com/favicon.ico'
headers = {
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Sec-Fetch-Mode': 'no-cors',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Dest': 'image',
    'Referer': 'https://secure2.store.apple.com/shop/sign_in?c=aHR0cHM6Ly93d3cuYXBwbGUuY29tL3Nob3AvYmFnfDFhb3NjY2QxZjg4ZGZjYjY4YWRhNWZmMmY5ZTY5YWMzNjE0OTYyMjZlOWMz&o=O01HTjYz&r=SXYD4UDAPXU7P7KXF&s=aHR0cHM6Ly9zZWN1cmUyLnN0b3JlLmFwcGxlLmNvbS9zaG9wL2NoZWNrb3V0L3N0YXJ0P3BsdG49QTZGNDNFMER8MWFvczg4MjgzMjY3MzJkNWEzNjIxMTQxMDE0ZTU4NmZiNTY5MjEzZGEyY2M&t=SXYD4UDAPXU7P7KXF&up=t',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Site': 'same-origin',
    'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'secure2.store.apple.com',
    'Cache-Control': 'no-cache',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; dslang=US-EN; site=USA',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'dslang': 'US-EN',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'geo': 'IT',
    'as_dc': 'nc',
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
#   - ETag: "2366-4fd2591660cbc"
#   - Last-Modified: Tue, 01 Jul 2014 18:01:41 GMT
#   - X-XSS-Protection: 1; mode=block
#   - x-shred: f7bb3b171d6b570205a5f584a50ba929
#   - Date: Sat, 28 Nov 2020 11:59:41 GMT
#   - Server: Apple
#   - X-Frame-Options: DENY
#   - Content-Type: image/x-icon
#   - Content-Length: 9062
#   - Accept-Ranges: bytes
#   - Expires: Sun, 29 Nov 2020 11:59:41 GMT
#   - Content-Security-Policy: frame-ancestors 'none'
#   - Cache-Control: max-age=86400
#   - Connection: keep-alive
#   - Edge-Control: !no-store, cache-maxage=1440m
#   - Strict-Transport-Security: max-age=31536000; includeSubDomains
#   - X-Content-Type-Options: nosniff
###############################################################################

###############################################################################
# request number: 87
# resource type: xhr

url = 'https://idmsa.apple.com/appleauth/jslog'
headers = {
    'Accept': 'application/json',
    'Pragma': 'no-cache',
    'Sec-Fetch-Mode': 'cors',
    'Cache-Control': 'no-cache',
    'Content-Length': '399',
    'scnt': '',
    'Cookie': 'geo=IT; ccl=Kdn52WwZ2zpMXc5ABjC73A==; check=true; mbox=session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556; s_fid=0EE10F1DE7BC5EFE-229AB97ADA08D75A; s_cc=true; s_vi=[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]; dssid2=0deece74-9857-4594-b36e-273d7f7dec11; dssf=1; as_pcts=JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke; as_dc=nc; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; xp_ci=3z18Z3F8zC6gz55bzBPQzTOhDqgGy; s_sq=%5B%5BB%5D%5D; as_xs=flc=&idmsl=1; as_xsm=1&93mZGW_YVaxBa9JRiFse-Q; aa=991DE1862A229067497F55E997BAE2F5; dslang=US-EN; site=USA',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'x-csrf-token': '',
    'Referer': 'https://idmsa.apple.com/appleauth/auth/authorize/signin?frame_id=auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj&language=en_US&iframeId=auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj&client_id=a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b&redirect_uri=https://secure2.store.apple.com&response_type=code&response_mode=web_message&state=auth-bbfc2b43-ol01-rowz-a4jz-l79n3zhj',
    'Host': 'idmsa.apple.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Dest': 'empty',
    'Origin': 'https://idmsa.apple.com',
}
cookies = {
    'dssid2': '0deece74-9857-4594-b36e-273d7f7dec11',
    'check': 'true',
    's_cc': 'true',
    'mbox': 'session#bb7cc510c65f4f4eaba6b8ef81b5547f#1606566556',
    'xp_ci': '3z18Z3F8zC6gz55bzBPQzTOhDqgGy',
    'dslang': 'US-EN',
    's_sq': '%5B%5BB%5D%5D',
    'as_pcts': 'JL+lxkMf1kjWAQTYt2GskuGVDw8znwk71-I-NVSCf8uZS0oApzy36fX3ooRv-qe7ZdyyZyWpPgHke',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'as_xsm': '1&93mZGW_YVaxBa9JRiFse-Q',
    'geo': 'IT',
    'as_dc': 'nc',
    'pxro': '1',
    'site': 'USA',
    's_vi': '[CS]v1|2FE11DAC8515EE05-60000A946BBC0874[CE]',
    'ccl': 'Kdn52WwZ2zpMXc5ABjC73A==',
    's_fid': '0EE10F1DE7BC5EFE-229AB97ADA08D75A',
    'dssf': '1',
    'as_xs': 'flc=&idmsl=1',
    'aa': '991DE1862A229067497F55E997BAE2F5',
}
rc = s.post(url, headers=headers, cookies=cookies)


# response status code: 204
# response headers:
#   - scnt: b558191cfd30dcaf5ca07a6a03a3042c
#   - Pragma: no-cache
#   - X-XSS-Protection: 1; mode=block
#   - Cache-Control: no-cache
#   - Set-Cookie: site=USA; Domain=apple.com; Path=/; Secure; HttpOnly
#   - Content-Security-Policy: default-src 'self'; script-src 'self' https://*.apple.com https://*.cdn-apple.com ; object-src 'self' https://*.apple-mapkit.com; style-src 'unsafe-inline' https://*.apple.com https://*.cdn-apple.com https://*.apple-mapkit.com ; img-src 'self' data: https://*.apple.com https://*.cdn-apple.com https://*.icloud.com https://*.mzstatic.com https://*.apple-mapkit.com ; media-src * data:; connect-src 'self' https://*.apple-mapkit.com; font-src 'self' https://*.apple.com https://*.cdn-apple.com; frame-src https://appleid.apple.com;
#   - Set-Cookie: dslang=US-EN; Domain=apple.com; Path=/; Secure; HttpOnly
#   - Date: Sat, 28 Nov 2020 11:59:41 GMT
#   - X-Apple-I-Request-ID: 4f86ec7e-c89c-41f4-bdf0-a60cdb207c01
#   - Server: Apple
#   - Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
#   - X-BuildVersion: R2
#   - Connection: keep-alive
#   - Cache-Control: no-store
#   - X-FRAME-OPTIONS: DENY
#   - Expires: Thu, 01 Jan 1970 00:00:00 GMT
#   - X-Content-Type-Options: nosniff
# response cookies:
#   - site: USA
#   - dslang: US-EN
###############################################################################

