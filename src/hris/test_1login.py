# -*- coding: utf-8 -*-
# @Time:        2019/9/25 20:32
# @Author:      LTH
import requests
import json
import pytest
def test_login():
    url = 'http://hr-api-tra.flashexpress.com/client/login'
    params = {"staff_id": "17245","pwd": "666666","os": "HIRS","lang": "zh-CN"}
    headeers = {'Content-Type':'application/json'}
    response = requests.post(url=url,params=params,headeers=headeers)
    if response.status_code == 200:
        if json.loads(response.text)['data'] is not None
            print("login ")
    assert response.status_code == 200
    assert json.loads(response.text)['data'] is not None