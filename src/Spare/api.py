# -*- coding: utf-8 -*-
# @Time:        2019/9/20 22:08
# @Author:      LTH
class Api():
    '''这是用来发送请求的'''
    def __init__(self,url,headers,params):
        self.url = url
        self.headers = headers
        self.params = params
    def post_1(self):
        url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
        params = {'theRegionCode': 311101}  # 键值对格式
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(url=url, data=params, headers=headers)
        print(response.text)


def post_1(self):
    url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
    arams = {'theRegionCode': 311101}  # 键值对格式
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url=url, data=params, headers=headers)
    print(response.text)