import os
import random
import json
import time
import requests
from src.config.feelt import getsessionid
from src.banche.test_gonggong import *


class Test_by_jingli_case1:
    """经理的操作"""
    host1 = "https://api-training.flashexpress.com/"
    host2 = "http://backyard-api-tra.flashexpress.com/"
    headers = None
    payload = None
    response = None

    # 检查是否有加班车申请权限
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

    # 获取32419待审批条数
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

    # 正常申请加班车
    def testAddFleet(self):  # 正常申请加班车
        # 申请前先查询中控的待审批
        num1 = test_get_xianlu_shenpi()["待审批"]
        print("下面是正常申请加班车")
        url = self.host2 + "api/_/fleet/addFleet"
        headers = {
            'Accept-Language': "zh",
            'X-BY-SESSION-ID': getsessionid(32419),
            'TIMEZONE': "+07:00",
        }
        reason = "laitaihua32419（经理）自动创建于:" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
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
        assert test_get_xianlu_shenpi()["待审批"] - num1 == 1  # 对比中控的待审批条数

    # 查看经理待审批列表
    def test_getlist1(self):
        url = self.host2 + "api/_/auditList/getList"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32419),
            "TIMEZONE": "+07:00"
        }
        payload = {
            "audit_show_type": 2,
            "audit_state_type": 1,
            "page_num": 1
        }
        response1 = requests.request("post", url=url, data=payload, headers=headers, verify=False)
        d = {"type": json.loads(response1.text)["data"]["dataList"][0]["type"],
             "id": json.loads(response1.text)["data"]["dataList"][0]["id"]}
        # 返回最上面一个申请的 type和id
        return d

    # 查看经理已审批列表
    def test_getlist2(self):
        url = self.host2 + "api/_/auditList/getList"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32419),
            "TIMEZONE": "+07:00"
        }
        payload = {
            "audit_show_type": 2,
            "audit_state_type": 2,
            "page_num": 1
        }
        response = requests.request("post", url=url, data=payload, headers=headers, verify=False)
        d = {"type": json.loads(response.text)["data"]["dataList"][0]["type"],
             "id": json.loads(response.text)["data"]["dataList"][0]["id"]}
        # 返回最上面一个申请的 type和id
        return d

    # 查看经理待审核的第一条记录
    def test_detail(self):
        url = self.host2 + "api/_/auditlist/detail"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32419),
            "TIMEZONE": "+07:00"
        }
        id_type = self.test_getlist1()
        payload = {
            "id": id_type["id"],
            "type": id_type["type"],
            "isCommit": 2
        }
        response1 = requests.request("post", url=url, headers=headers, data=payload)
        assert json.loads(response1.text)["data"]["detail"] is not None
        return json.loads(response1.text)["data"]["head"]["id"]

    #   经理审批同意仓管加班车申请
    def test_approval_agree(self):
        # 先仓管创建条加班车申请
        test_cangguan_AddFleet()
        url = self.host2 + "api/_/fleet/updateFleet"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32419),
            "TIMEZONE": "+07:00"
        }
        # 获取到带审批的第一条的id
        num1 = self.test_getlist1()
        payload = {
            "status": 2,
            "audit_id": self.test_detail(),
            "reject_reason": "1"
        }
        response1 = requests.request("post", url=url, headers=headers, data=payload).text
        assert json.loads(response1)["code"] == 1
        assert json.loads(response1)["msg"] == "请求成功!"
        assert json.loads(response1)["data"] is None
        # 审批后待处理的数据应该跑到已处理中
        assert num1 == self.test_getlist2()

    #   经理审批驳回仓管加班车申请
    def test_approval_reject(self):
        # 先仓管创建条加班车申请
        test_cangguan_AddFleet()
        url = self.host2 + "api/_/fleet/updateFleet"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32419),
            "TIMEZONE": "+07:00"
        }
        # 获取到带审批的第一条的id
        num1 = self.test_getlist1()
        reject_reason = "laitaihua32419经理自动驳回于:" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        payload = {
            "status": 3,
            "audit_id": self.test_detail(),
            "reject_reason": reject_reason
        }
        response1 = requests.request("post", url=url, headers=headers, data=payload).text
        assert json.loads(response1)["code"] == 1
        assert json.loads(response1)["msg"] == "请求成功!"
        assert json.loads(response1)["data"] is None
        # 审批后待处理的数据应该跑到已处理中
        assert num1 == self.test_getlist2()


