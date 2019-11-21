import os
import random
import json
import time
import requests

from src.config.feelt import getsessionid
from src.banche.test_by_gonggong import *


class Test_by_jingli_case1:
    host1 = "https://api-training.flashexpress.com/"
    host2 = "http://backyard-api-tra.flashexpress.com/"
    headers = None
    payload = None
    response = None

    def testGetAuditlistPermission(self):  # 检查是否有加班车申请权限
        print("下面是检查32419是否有加班车申请权限:")
        url = self.host2 + "api/_/audit/getAuditlistPermission"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32419),
            "TIMEZONE": "+07:00"
        }
        self.response = requests.request("post", url=url, data=self.payload, headers=headers, verify=False)
        fleet = json.loads(self.response.text)["data"]["fleet"]
        if fleet == 1:
            print("该账号有申请加班车权限")
        # 断言是否有申请加班车权限
        assert fleet == 1
        return None

    def get_waitAuditNum(self):
        print("下面32419是获取32419待审批条数:")
        url = self.host2 + "api/_/audit/waitAuditNum"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32419),
            "TIMEZONE": "+07:00"
        }
        response1 = requests.request("post", url=url, data=self.payload, headers=headers, verify=False)
        num = int(json.loads(response1.text)["data"]["num"])
        if num > 1:
            print("获取32419待审批条数successful")
        assert num > 1
        return num

    def testAddFleet(self):  # 正常申请加班车

        print("下面是正常申请加班车")
        url = self.host2 + "api/_/fleet/addFleet"
        headers = {
            'Accept-Language': "zh",
            'X-BY-SESSION-ID': getsessionid(32419),
            'TIMEZONE': "+07:00",
        }
        reason = "laitaihua32419自动创建于:" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        payload = {
            "car_type": 100,
            "capacity": str(random.randint(1, 5000)),
            "start_store": "TH01010101",
            "end_store": testGetStoreList(),
            "reason": reason,
            "arrive_time": str(time.strftime("%Y-%m-%d %H:%M:00", time.localtime(time.time() + 7200))),
            "image_path": []
        }
        response1 = requests.request("post", url=url, data=payload, headers=headers, verify=False)  # 正常创建
        assert json.loads(response1.text)["code"] == 1
        assert json.loads(response1.text)["msg"] == "请求成功!"
        assert json.loads(response1.text)["data"] is None




jingli = Test_by_jingli_case1()
jingli.testAddFleet()
