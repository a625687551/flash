# -*- coding: utf-8 -*-
# @Time:        2019/9/25 20:14
# @Author:      LTH
import requests
import json
import pytest
def login():
    url = 'http://hr-api-tra.flashexpress.com/client/login'
    params = {"staff_id": "17245","pwd": "666666","os": "HIRS","lang": "zh-CN"}
    headeers = {'Content-Type':'application/json'}
    response = requests.post(url=url,params=params,headeers=headeers)
    assert response
    assert json.loads(response.text)[data]