import os
import random
import json
import time

import requests
from src.banche.test_by_testjingli import *
from src.method.chushihua import *
from src.method.get_randome import *
from src.config.feelt import getsessionid

# chushihua_traning_zhanghao() #每天都要一次初始化
requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告


class Test_by_cangguang_case1:
    host1 = "https://api-training.flashexpress.com/"
    host2 = "http://backyard-api-tra.flashexpress.com/"
    headers = {
        "Accept-Language": "zh",
        "TIMEZONE": "+07:00"
    }
    payload = None
    response = None

    # 初始化
    def test_chushihua(self):
        assert chushihua_traning_zhanghao() == True

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
            j = j + 1
            if j < 50:
                store_id.append(i["store_id"])

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
        #  正常创建
        reason = "laitaihua自动创建于:" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        payload = {
            "car_type": self.testGetCarType(),
            "capacity": str(random.randint(1, 5000)),
            "start_store": "TH01010101",
            "end_store": self.testGetStoreList(),
            "reason": reason,
            "arrive_time": str(time.strftime("%Y-%m-%d %H:%M:00", time.localtime(time.time() + 7200))),
            "image_path": []
        }
        # payload = dict(car_type=random.sample([100, 101, 200, 201, 203, 300], 1), capacity="35",
        #                start_store="TH01010101", end_store="TH47200101", reason="www.pgyer.com",
        #                arrive_time="2019-11-14 00:00", image_path=[])
        # self.response = requests.request("post", url=url, data=payload, headers=headers)
        num1 = Test_by_jingli_case1.get_waitAuditNum(self)
        response1 = requests.request("post", url=url, data=payload, headers=headers)  # 正常创建
        num2 = Test_by_jingli_case1.get_waitAuditNum(self)
        if response1.status_code == 200:
            print(getdict(response1.text)["msg"])
        assert getdict(response1.text)["code"] == 1
        assert getdict(response1.text)["msg"] == "请求成功!"
        assert getdict(response1.text)["data"] is None
        assert (num2 - num1) == 1

    def test_bad_addfleet(self):
        url = self.host2 + "api/_/fleet/addFleet"
        headers = {
            'Accept-Language': "zh",
            'X-BY-SESSION-ID': getsessionid(32416),
            'TIMEZONE': "+07:00",
        }
        num1 = Test_by_jingli_case1.get_waitAuditNum(self)  #网点经理的待审批数
        reason = "laitaihua自动创建于:" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

        #  1车辆类型为空
        print("1车辆类型为空:")
        payload1 = {
            "car_type": None,
            "capacity": str(random.randint(1, 5000)),
            "start_store": "TH01010101",
            "end_store": self.testGetStoreList(),
            "reason": reason,
            "arrive_time": str(time.strftime("%Y-%m-%d %H:%M:00", time.localtime(time.time() + 7200))),
            "image_path": []
        }
        response1 = requests.request("post", url=url, data=payload1, headers=headers)
        if response1.status_code == 200:
            print(json.loads(response1.text)["msg"])
        assert getdict(response1.text)["code"] == 0
        assert json.loads(response1.text)["msg"] == "“car_type”必须是整数"
        assert num1 == Test_by_jingli_case1.get_waitAuditNum(self)

        #  2装载数量超5000
        print("2装载数量超5000")
        payload2 = {
            "car_type": self.testGetCarType(),
            "capacity": 5001,
            "start_store": "TH01010101",
            "end_store": self.testGetStoreList(),
            "reason": reason,
            "arrive_time": str(time.strftime("%Y-%m-%d %H:%M:00", time.localtime(time.time() + 7200))),
            "image_path": []
        }
        response2 = requests.request("post", url=url, data=payload2, headers=headers)
        if response1.status_code == 200:
            print(json.loads(response2.text)["msg"])
        assert getdict(response2.text)["code"] == 0
        assert json.loads(response2.text)["msg"] == "“capacity”必须大于 0 小于等于 5000"
        assert num1 == Test_by_jingli_case1.get_waitAuditNum(self)

        #  3装载数量不填
        print("3装载数量不填")
        payload3 = {
            "car_type": self.testGetCarType(),
            "capacity": None,
            "start_store": "TH01010101",
            "end_store": self.testGetStoreList(),
            "reason": reason,
            "arrive_time": str(time.strftime("%Y-%m-%d %H:%M:00", time.localtime(time.time() + 7200))),
            "image_path": []
        }
        response3 = requests.request("post", url=url, data=payload3, headers=headers)
        if response3.status_code == 200:
            print(json.loads(response3.text)["msg"])
        assert getdict(response3.text)["code"] == 0
        assert getdict(response3.text)["msg"] == "“capacity”必须是整数"
        assert num1 == Test_by_jingli_case1.get_waitAuditNum(self)

        # 4始发网点和目的网点一致
        print("4始发网点和目的网点一致")
        payload4 = {
            "car_type": self.testGetCarType(),
            "capacity": str(random.randint(1, 5000)),
            "start_store": "TH01010101",
            "end_store": "TH01010101",
            "reason": reason,
            "arrive_time": str(time.strftime("%Y-%m-%d %H:%M:00", time.localtime(time.time() + 7200))),
            "image_path": []
        }
        response4 = requests.request("post", url=url, data=payload4, headers=headers)
        if response4.status_code == 200:
            print(getdict(response4.text)["msg"])
        assert getdict(response4.text)["code"] == 0
        assert getdict(response4.text)["msg"] == "出发网点与目的网点不能相同"
        assert num1 == Test_by_jingli_case1.get_waitAuditNum(self)

        # 5备注超长
        print("5备注超长")
        payload5 = {
            "car_type": self.testGetCarType(),
            "capacity": str(random.randint(1, 5000)),
            "start_store": "TH01010101",
            "end_store": self.testGetStoreList(),
            "reason": reason*1000,
            "arrive_time": str(time.strftime("%Y-%m-%d %H:%M:00", time.localtime(time.time() + 7200))),
            "image_path": []
        }
        response5 = requests.request("post", url=url, data=payload5, headers=headers)
        if response4.status_code == 200:
            print(json.loads(response5.text)["msg"])
        assert getdict(response5.text)["code"] == 0
        assert getdict(response5.text)["msg"] == "申请原因应该在500个字符以内!"
        assert num1 == Test_by_jingli_case1.get_waitAuditNum(self)

        # 6申请时间没有小于当前时间
        print("6申请时间没有大于当前时间")
        payload6 = {
            "car_type": self.testGetCarType(),
            "capacity": str(random.randint(1, 5000)),
            "start_store": "TH01010101",
            "end_store": self.testGetStoreList(),
            "reason": reason,
            "arrive_time": str(time.strftime("%Y-%m-%d %H:%M:00", time.localtime(time.time()-3600))),
            "image_path": []
        }
        response6 = requests.request("post", url=url, data=payload6, headers=headers)
        print(response6.text)
        if response6.status_code == 200:
            print(json.loads(response6.text)["msg"])
        print(num1, Test_by_jingli_case1.get_waitAuditNum(self))
        assert getdict(response6.text)["code"] == 0
        assert getdict(response6.text)["msg"] == "期望到达时间应晚于当前时间"
        assert num1 == Test_by_jingli_case1.get_waitAuditNum(self)




Azhang = Test_by_cangguang_case1()
# Azhang.testGetAuditlistPermission()
# Azhang.testGetPerson()
# Azhang.testGetCarType()
# Azhang.testGetStoreList()
# Azhang.testAddFleet()
Azhang.test_bad_addfleet()
