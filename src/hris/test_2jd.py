# -*- coding: utf-8 -*-
# @Time:        2019/9/25 20:14
# @Author:      LTH
import requests
import json
import pytest

from src.hris.test_1login import test_login

#查询JD列表
def test_jdlist(job_name=None,department_id=None,submitter_name=None,time_start=None,time_end=None,page_size=100,page_num=1):
    session_id = test_login()
    url = 'http://hr-api-tra.flashexpress.com/jd/jdList'
    params = {
        "job_name": job_name,
        "department_id": department_id,
        "submitter_name": submitter_name,
        "time_start": time_start,
        "time_end": time_end,
        "page_size": page_size,
        "page_num": page_num
    }
    headers = {
        'X-FLE-SESSION-ID': session_id
    }
    response = requests.post(url=url, data=json.dumps(params), headers=headers)
    if response.status_code == 200 and len(json.loads(response.text)['data']) > 0:
        print('get JD list successful')
    assert response.status_code == 200
    assert len(json.loads(response.text)['data']) > 0
    return None

#获取部门
def test_getSysList():
    url = 'http://hr-api-tra.flashexpress.com/sysList/getSysList'
    prams = {
        "type_code": "getDepartmentList"
    }
    headers = {
        'X-FLE-SESSION-ID': test_login()
    }
    response = requests.post(url=url, data=prams, headers=headers)
    if len(json.loads(response.text)['data']) > 10 and 'getDepartmentList' in json.loads(response.text)['data']:
        print('获取汇报线成功')
    assert len(json.loads(response.text)['data']) ==3 and 'getDepartmentList' in json.loads(response.text)['data']
    return None

#获取汇报线
def test_reportingLine():
    url = 'http://hr-api-tra.flashexpress.com/jd/reportingLine'
    prams = None
    headers = {
        'X-FLE-SESSION-ID': test_login()
    }
    response = requests.post(url=url,data=prams,headers=headers)
    if len(json.loads(response.text)['data']) == 3:
        print('获取汇报线成功')
    assert len(json.loads(response.text)['data']) ==3
    return None


