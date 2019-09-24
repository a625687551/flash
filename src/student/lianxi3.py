# -*- coding: utf-8 -*-
# @Time:        2019/8/28 10:33
# @Author:      LTH
import requests

url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
params = {'theRegionCode': 311101}  # 键值对格式
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.post(url=url, data=params, headers=headers)
print(response.text)