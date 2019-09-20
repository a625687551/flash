# -*- coding: utf-8 -*-
# @Time:        2019/8/27 20:43
# @Author:      LTH
import requests
import json
def get_shen_id_get():
    url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince?'
    params = None
    response = None
    response = requests.get(url=url)
    print(response.text)

def get_shi_id_get():
    url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
    params = {'theRegionCode':311101}
    response = requests.get(url=url, params=params)
    print(response.text)

def get_shi_id_post():
    url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
    params = {'theRegionCode': 311101} # 键值对格式
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    response = requests.post(url=url,data=params,headers=headers)
    print(response.text)

def get_shi_id_soap():
    url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx'
    params = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <getSupportCityString xmlns="http://WebXml.com.cn/">
      <theRegionCode>311101</theRegionCode>
    </getSupportCityString>
  </soap:Body>
</soap:Envelope>'''
    headers = {'Content-Type':'text/xml; charset=utf-8'}
    response = requests.post(url=url,data=params,headers=headers)
    print(response.text)

