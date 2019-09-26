# -*- coding: utf-8 -*-
# @Time:        2019/9/25 20:32
# @Author:      LTH
import requests
import json
import pytest
#登录
def test_login(**params ):
    url = 'http://hr-api-tra.flashexpress.com/client/login'
    params = {
        "staff_id": "17245",
        "pwd": "666666",
        "os": "HIRS",
        "lang": "zh-CN"
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url=url, data=json.dumps(params), headers=headers)
    assert response.status_code == 200
    assert json.loads(response.text)['data'] is not None
    return json.loads(response.text)['data']['session_id']

# 获取静态列表
def test_getStaticSysList():
    url = 'http://hr-api-tra.flashexpress.com/sysList/getStaticSysList'
    headers = {
        'X-FLE-SESSION-ID': test_login(),
        'Accept-Language': 'zh-CN'
    }
    response = requests.get(url=url, headers=headers)
    assert len(json.loads(response.text)['data']['datalist']) == 12
    return None