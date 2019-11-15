import random

import requests
import pytest
import json

from src.method.chushihua import chushihua_traning_zhanghao

requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告


# chushihua_traning_zhanghao()  # 每天都要初始化traning账号


class TestCase1():
    host1 = "https://api-training.flashexpress.com/"
    host2 = "http://backyard-api-tra.flashexpress.com/"
    headers = {
        "Accept-Language": "zh",
        "TIMEZONE": "+07:00"
    }
    payload = None
    response = None

    # 获取仓管32416 sessionid
    def testLonginCangguang(self, user=32416, password=666666):  # 获取仓管32416 sessionid

        url = self.host1 + "api/backyard/v1/auth/new_device_login"
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
        }
        payload = {
            "login": user,
            "password": password,
            "clientid": "867245035784787520002063200047",
            "clientsd": "1566022761465",
            "os": "android",
            "version": "1.2.8"
        }
        print(url)
        response1 = requests.request("post", url=url, data=json.dumps(payload), headers=headers, verify=False)
        sessionid = json.loads(response1.text)["data"]["sessionid"]
        # 断言是否获取到 sessionid
        assert sessionid is not None
        return sessionid

    # 检查是否有加班车申请权限
    def testGetAuditlistPermission(self):  # 检查是否有加班车申请权限
        url = self.host2 + "api/_/audit/getAuditlistPermission"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": self.testLonginCangguang(),
            "TIMEZONE": "+07:00"
        }
        self.response = requests.request("post", url=url, data=self.payload, headers=headers, verify=False)
        fleet = json.loads(self.response.text)["data"]["fleet"]
        # 断言是否有申请加班车权限
        assert fleet == 1
        return None

    # 获取角色、所属网点、直线上级等信息
    def testGetPerson(self):  # 获取角色、所属网点、直线上级等信息
        url = self.host2 + "api/_/personinfo/person"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": self.testLonginCangguang(),
            "TIMEZONE": "+07:00"
        }
        response1 = requests.request("post", url=url, data=self.payload, headers=headers)
        superiorid = json.loads(response1.text)["data"]["superior_id"]
        print(superiorid)
        # 断言直线上级是否为32419
        assert superiorid == 32419
        return None

    # 获取车辆类型
    def testGetCarType(self):  # 获取车辆类型
        url = self.host2 + "api/_/fleet/getCarType"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": self.testLonginCangguang(),
            "TIMEZONE": "+07:00"
        }
        self.response = requests.request("post", url=url, data=self.payload, headers=headers)
        # 断言车辆类型是不是只6种
        dataList = json.loads(self.response.text)["data"]["dataList"]
        print(dataList)
        assert len(dataList) == 6

    # 获取网点
    def testGetStoreList(self):  # 获取网点
        url = self.host2 + "api/_/fleet/storeList"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": self.testLonginCangguang(),
            "TIMEZONE": "+07:00"
        }
        self.response = requests.request("post", url=url, data=self.payload, headers=headers)
        # 断言网点超过100个
        assert len(json.loads(self.response.text))["data"]["dataList"] > 100
        return None

    # 正常申请加班车
    def testAddFleet(self):  # 正常申请加班车
        url = self.host2 + "api/_/fleet/addFleet"
        headers = {
            'Accept-Language': "zh",
            'X-BY-SESSION-ID': self.testLonginCangguang(),
            'TIMEZONE': "+07:00",
        }
        payload = {
            "car_type": 300,
            "capacity": "35",
            "start_store": "TH01010101",
            "end_store": "TH47200101",
            "reason": "www.pgyer.com",
            "arrive_time": "2019-11-14 00:00",
            "image_path": []
        }
        self.response = requests.request("post", url=url, data=payload, headers=headers)
        # payload = dict(car_type=random.sample([100, 101, 200, 201, 203, 300], 1), capacity="35",
        #                start_store="TH01010101", end_store="TH47200101", reason="www.pgyer.com",
        #                arrive_time="2019-11-14 00:00", image_path=[])
        # self.response = requests.request("post", url=url, data=payload, headers=headers)
        msg = json.loads(self.response.text)["msg"]
        print(msg)
        # 断言是否返回请求成功


pp = TestCase1()
pp.testAddFleet()
