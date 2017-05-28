#!/usr/bin/python

# http://docs.python-requests.org/en/master/user/quickstart/#make-a-request

import requests
from fake_useragent import UserAgent

timeout = 3

ua = UserAgent()
url = "http://127.0.0.1:7878/api"

header_random = {'User-Agent':str(ua.chrome)}
headers_static = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

payload = {'key1': 'value1'}

# GET
res_1 = requests.get(url, headers = header_random, timeout = timeout, params = payload)
#res_2 = requests.get(url, headers = headers_static, timeout = timeout)

text = res_1.text
status_code = res_1.status_code
header = res_1.headers

print text

#payload_1 = {'key1': 'value1', 'key2': 'value2'}
#payload_2 = {'key1': 'value1', 'key2': ['value2', 'value3']}

#r = requests.get(url, params = payload_1)
#r = requests.get(url, params = payload_2)

#print r.url

