import requests
import json
import pytest
import random

from src.hris.test_1login import test_login


def test_getSysList():
    url = 'http://hr-api-tra.flashexpress.com/sysList/getSysList'
    params = {
        "type_code": "getDepartmentList"
    }
    headers = {
        'X-FLE-SESSION-ID': test_login(),
        'Accept-Language': 'zh-CN'
    }
    response = requests.post(url=url, data=params, headers=headers)
    print(response.text)
    if len(json.loads(response.text)['data']['getDepartmentList']) > 10 and 'getDepartmentList' in json.loads(response.text)['data']:
        print('获取汇报线成功')
    assert len(json.loads(response.text)['data']['getDepartmentList']) > 10 and 'getDepartmentList' in json.loads(response.text)['data']
    #随机返回了个部门ID
    return random.choices(json.loads(response.text)['data']['getDepartmentList'])[0]['id']
print(test_getSysList())