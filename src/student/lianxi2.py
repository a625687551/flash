# -*- coding: utf-8 -*-
# @Time:        2019/8/28 10:28
# @Author:      LTH
import requests
import json

url = 'http://192.168.0.228:8080/ms/api/auth/signin'
params = {"login": "10000", "password": "123456"}
headers = {'Content-Type': 'application/json;charset=UTF-8', 'Accept-Language': 'zh-CN'}
response = requests.post(url=url, data=json.dumps(params), headers=headers)
print(response.status_code)
print(json.loads(response.text)['data']['profile']['id'])
print(str(response.url))