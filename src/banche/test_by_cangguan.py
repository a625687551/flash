import os
import random
import json
import datetime

import requests

from src.config.feelt import getsessionid

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
    """
    # 登录by,在初始化已实现
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
"""

    # -- 检查是否有加班车申请权限
    def testGetAuditlistPermission(self):  # 检查是否有加班车申请权限
        url = self.host2 + "api/_/audit/getAuditlistPermission"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32416),
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
            "X-BY-SESSION-ID": getsessionid(32416),
            "TIMEZONE": "+07:00"
        }
        response1 = requests.request("post", url=url, data=self.payload, headers=headers)
        superiorid = int(json.loads(response1.text)["data"]["superior_id"])
        # 断言直线上级是否为32419
        assert superiorid == 32419
        return None

    # 获取车辆类型
    def testGetCarType(self):  # 获取车辆类型
        url = self.host2 + "api/_/fleet/getCarType"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32416),
            "TIMEZONE": "+07:00"
        }
        self.response = requests.request("post", url=url, data=self.payload, headers=headers)

        dataList = json.loads(self.response.text)["data"]["dataList"]
        CarType = []
        for i in dataList:
            CarType.append(i["type"])
        # 断言车辆类型是不是只6种
        assert len(dataList) == 6
        return random.choice(CarType)

    # 获取网点
    def testGetStoreList(self):  # 获取网点
        url = self.host2 + "api/_/fleet/storeList"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32416),
            "TIMEZONE": "+07:00"
        }
        response1 = requests.request("post", url=url, data=self.payload, headers=headers)
        dataList = (json.loads(response1.text)["data"]["dataList"])
        store_id = []
        j = 0
        for i in dataList:
            j = j+1
            if j < 50:
                print(i["store_id"])
                store_id.append(i["store_id"])
        print(store_id)

        # 断言网点超过2200个
        assert len(json.loads(response1.text)["data"]["dataList"]) > 2200
        return random.choice(store_id)

    # 正常申请加班车
    def testAddFleet(self):  # 正常申请加班车
        url = self.host2 + "api/_/fleet/addFleet"
        headers = {
            'Accept-Language': "zh",
            'X-BY-SESSION-ID': getsessionid(32416),
            'TIMEZONE': "+07:00",
        }
        reason = "laitaihua自动创建于"+str(datetime.datetime.today())
        payload = {
            "car_type": self.testGetCarType(),
            "capacity": str(random.randint(1, 5000)),
            "start_store": "TH01010101",
            "end_store": self.testGetStoreList(),
            "reason": reason,
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


Azhang = TestCase1()
# Azhang.testGetAuditlistPermission()
# Azhang.testGetPerson()
# Azhang.testGetCarType()
Azhang.testGetStoreList()
# Azhang.testAddFleet()
