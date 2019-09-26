# -*- coding: utf-8 -*-
# @Time:        2019/9/25 20:14
# @Author:      LTH
import requests
import json
import random
import pytest
from src.hris.test_1login import test_login
from src.method.get_randome import get_str

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
        'X-FLE-SESSION-ID': session_id,
        'Accept-Language': 'zh-CN'
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
    params = {
        "type_code": "getDepartmentList"
    }
    headers = {
        'X-FLE-SESSION-ID': test_login(),
        'Accept-Language': 'zh-CN'
    }
    response = requests.post(url=url, data=params, headers=headers)
    if len(json.loads(response.text)['data']['getDepartmentList']) > 10 and 'getDepartmentList' in json.loads(response.text)['data']:
        print('获取部门线成功')
    assert len(json.loads(response.text)['data']['getDepartmentList']) > 10 and 'getDepartmentList' in json.loads(response.text)['data']
    #随机返回了个部门ID
    return random.choices(json.loads(response.text)['data']['getDepartmentList'])[0]['id']

#获取汇报线
def test_getreportingLine():
    url = 'http://hr-api-tra.flashexpress.com/jd/reportingLine'
    params = None
    headers = {
        'X-FLE-SESSION-ID': test_login(),
        'Accept-Language': 'zh-CN'
    }
    response = requests.post(url=url,data=params,headers=headers)
    if len(json.loads(response.text)['data']) == 3:
        print('获取汇报线成功')
    assert len(json.loads(response.text)['data']) == 3
    #随机返回个汇报线ID
    return  random.choices(json.loads(response.text)['data'])[0]['id']

# s随机创建jd
def test_jdAdd():
    jd_name = 'auto_jd'+get_str()
    url = 'http://hr-api-tra.flashexpress.com/jd/jdAdd'
    params = {
        "job_name": jd_name,
        "department_id": random.choices([3, 8, 9, 16, 17, 18, 26]),
        "job_description": "<p><strong><em><u>这是一个自动建的jd岗的位描述</u></em></strong></p>",
        "position_id": None,
        "report_superior_id": test_getreportingLine(),
        "type": random.randint(1, 3)
    }
    headers = {
        'X-FLE-SESSION-ID': test_login(),
        'Accept-Language': 'zh-CN'
    }
    response = requests.post(url=url, data=params, headers=headers)
    # 返回一个jd_id
    assert json.loads(response.text)['data']['job_id'] is not None
    return json.loads(response.text)['data']['job_id']

#查看jd详情
# def test_jobDetail():
#     url = 'http://hr-api-tra.flashexpress.com/jd/jobDetail'
#     params = {
#         "job_id": test_jdAdd()
#     }
#     headers = {
#         'X-FLE-SESSION-ID': test_login(),
#         'Accept-Language': 'zh-CN'
#     }
#     response = requests.post(url=url, data=params, headers=headers)
#
# #修改jd
# def test_modify_jd():
#     jd_info = test_jdlist()
#     url = 'http://hr-api-tra.flashexpress.com/jd/jdAdd'
#     params = {
#         "job_id": "10039",
#         "type": 2,
#         "job_name": "规划局规",
#         "job_description": "<p>jd说明</p>",
#         "department_id": "9",
#         "position_id": null,
#         "report_superior_id": "3",
#         "submitter_id": "17245",
#         "submitter_name": "diweijie",
#         "state": "1",
#         "created_at": "2019-08-23 19:33:40",
#         "updated_at": "2019-08-23 19:33:40",
#         "report_name": "BeiJing",
#         "department_name": "Admin & Procurement",
#         "type_name": "摩托车快递员",
#         "submitter_department_name": "",
#         "submitter_job_title": "",
#         "submitter": "(17245)diweijie  "
#         }
#
#     headers = {
#         'X-FLE-SESSION-ID': test_login(),
#         'Accept-Language': 'zh-CN'
#     }

#删除jd
def test_jobDel():
    url = 'http://hr-api-tra.flashexpress.com/jd/jobDel'
    params = {
        "job_id": test_jdAdd()
    }
    headers = {
        'X-FLE-SESSION-ID': test_login(),
        'Accept-Language': 'zh-CN'
    }
    response = requests.post(url=url, data=params, headers=headers)
    assert response.status_code == 200
    print(response.text)
    return None