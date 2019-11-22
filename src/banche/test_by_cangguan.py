import os
import random
import json
import time
import requests
from src.banche.test_by_testjingli import *
from src.method.chushihua import *
from src.config.feelt import *

# chushihua_traning_zhanghao()  # 每天都要一次初始化
requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告
jingli = Test_by_jingli_case1()


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
        print("下面是检查是否有加班车申请权限:")
        url = self.host2 + "api/_/audit/getAuditlistPermission"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32416),
            "TIMEZONE": "+07:00"
        }
        self.response = requests.request("post", url=url, data=self.payload, headers=headers, verify=False)
        fleet = json.loads(self.response.text)["data"]["fleet"]
        if fleet == 1:
            print("该账号有申请加班车权限")
        # 断言是否有申请加班车权限
        assert fleet == 1
        return None

    # 获取角色、所属网点、直线上级等信息
    def testGetPerson(self):  # 获取角色、所属网点、直线上级等信息
        print("下面是获取角色、所属网点、直线上级等信息")
        url = self.host2 + "api/_/personinfo/person"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32416),
            "TIMEZONE": "+07:00"
        }
        response1 = requests.request("post", url=url, data=self.payload, headers=headers)
        superiorid = int(json.loads(response1.text)["data"]["superior_id"])
        if superiorid == 32419:
            print("获取角色、所属网点、直线上级等信息Successful")
        # 断言直线上级是否为32419
        assert superiorid == 32419
        return None

    # 获取车辆类型
    def testGetCarType(self):  # 获取车辆类型
        print("下面是获取车辆类型")
        url = self.host2 + "api/_/fleet/getCarType"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32416),
            "TIMEZONE": "+07:00"
        }
        self.response = requests.request("post", url=url, data=self.payload, headers=headers)

        dataList = json.loads(self.response.text)["data"]["dataList"]
        if dataList != None:
            print("获取车辆类型successful")
        CarType = []
        for i in dataList:
            CarType.append(i["type"])
        # 断言车辆类型是不是只6种
        assert len(dataList) == 6
        return random.choice(CarType)

    # 获取网点
    def testGetStoreList(self):  # 获取网点
        print("下面是获取网点")
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
        if store_id != None:
            print("获取网点successful")
        # 断言网点超过2200个
        assert len(json.loads(response1.text)["data"]["dataList"]) > 2200
        return random.choice(store_id)

    # 正常申请加班车
    def testAddFleet(self):  # 正常申请加班车
        print("下面是正常申请加班车")
        url = self.host2 + "api/_/fleet/addFleet"
        headers = {
            'Accept-Language': "zh",
            'X-BY-SESSION-ID': getsessionid(32416),
            'TIMEZONE': "+07:00",
        }
        reason = "laitaihua32416自动创建于:" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
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
        num1 = jingli.get_waitAuditNum()
        response1 = requests.request("post", url=url, data=payload, headers=headers)  # 正常创建
        num2 = jingli.get_waitAuditNum()
        if (num2 - num1) == 1:
            print("正常申请加班车successful")
        assert json.loads(response1.text)["code"] == 1
        assert json.loads(response1.text)["msg"] == "请求成功!"
        assert json.loads(response1.text)["data"] is None
        assert (num2 - num1) == 1

    # 创建加班车反例
    def test_bad_addfleet(self):
        print("下面是创建加班车反例:")
        url = self.host2 + "api/_/fleet/addFleet"
        headers = {
            'Accept-Language': "zh",
            'X-BY-SESSION-ID': getsessionid(32416),
            'TIMEZONE': "+07:00",
        }
        num1 = jingli.get_waitAuditNum()  # 网点经理的待审批数
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
        assert json.loads(response1.text)["code"] == 0
        assert json.loads(response1.text)["msg"] == "“car_type”必须是整数"
        assert num1 == jingli.get_waitAuditNum()

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
        assert json.loads(response2.text)["code"] == 0
        assert json.loads(response2.text)["msg"] == "“capacity”必须大于 0 小于等于 5000"
        assert num1 == jingli.get_waitAuditNum()

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
        assert json.loads(response3.text)["code"] == 0
        assert json.loads(response3.text)["msg"] == "“capacity”必须是整数"
        assert num1 == jingli.get_waitAuditNum()
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
            print(json.loads(response4.text)["msg"])
        assert json.loads(response4.text)["code"] == 0
        assert json.loads(response4.text)["msg"] == "出发网点与目的网点不能相同"
        assert num1 == jingli.get_waitAuditNum()

        # 5备注超长
        print("5备注超长")
        payload5 = {
            "car_type": self.testGetCarType(),
            "capacity": str(random.randint(1, 5000)),
            "start_store": "TH01010101",
            "end_store": self.testGetStoreList(),
            "reason": reason * 1000,
            "arrive_time": str(time.strftime("%Y-%m-%d %H:%M:00", time.localtime(time.time() + 7200))),
            "image_path": []
        }
        response5 = requests.request("post", url=url, data=payload5, headers=headers)
        if response4.status_code == 200:
            print(json.loads(response5.text)["msg"])
        assert json.loads(response5.text)["code"] == 0
        assert json.loads(response5.text)["msg"] == "申请原因应该在500个字符以内!"
        assert num1 == jingli.get_waitAuditNum()
        # 6申请时间没有小于当前时间
        print("6申请时间没有大于当前时间")
        payload6 = {
            "car_type": self.testGetCarType(),
            "capacity": str(random.randint(1, 5000)),
            "start_store": "TH01010101",
            "end_store": self.testGetStoreList(),
            "reason": reason,
            "arrive_time": str(time.strftime("%Y-%m-%d %H:%M:00", time.localtime(time.time() - 3600))),
            "image_path": []
        }
        response6 = requests.request("post", url=url, data=payload6, headers=headers)
        if response6.status_code == 200:
            print(json.loads(response6.text)["msg"])
        assert json.loads(response6.text)["code"] == 0
        assert json.loads(response6.text)["msg"] == "期望到达时间应晚于当前时间"
        assert num1 == jingli.get_waitAuditNum()

    # 查询仓管申请的进行中
    def test_getlist1(self):
        print("下面是查询仓管的申请")
        url = self.host2 + "api/_/auditList/getList"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32416),
            "TIMEZONE": "+07:00"
        }
        pyload1 = {
            "audit_show_type": 1,
            "audit_state_type": 1,
            "page_num": 1
        }
        response1 = requests.request("post", url=url, data=pyload1, headers=headers, verify=False)
        if json.loads(response1.text)["data"] is not None:
            print("查询仓管申请-进行中正常")
        d = {"type": json.loads(response1.text)["data"]["dataList"][0]["type"], "id": json.loads(response1.text)["data"]["dataList"][0]["id"]}
        # 返回最上面一个申请的 type和id
        return d

    # 查询仓管的已完成
    def test_getlist2(self):
        url = self.host2 + "api/_/auditList/getList"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32416),
            "TIMEZONE": "+07:00"
        }
        pyload1 = {
            "audit_show_type": 1,
            "audit_state_type": 2,
            "page_num": 1
        }
        response1 = requests.request("post", url=url, data=pyload1, headers=headers, verify=False)
        if json.loads(response1.text)["data"] is not None:
            print("查询仓管申请-已完成中正常")
        d = {"type": json.loads(response1.text)["data"]["dataList"][0]["type"], "id": json.loads(response1.text)["data"]["dataList"][0]["id"]}
        # 返回最上面一个申请的 type和id
        return d

    # 查看我的审批 中申请记录的详情
    def test_check(self):
        url = self.host2 + "api/_/auditlist/detail"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32416),
            "TIMEZONE": "+07:00"
        }
        id_type = self.test_getlist1()
        payload = {
            "id": id_type["id"],
            "type": id_type["type"],
            "isCommit": 1
        }
        response1 = requests.request("post", url=url, headers=headers, data=payload)
        assert json.loads(response1.text)["data"]["detail"] is not None
        return json.loads(response1.text)["data"]["head"]["id"]

    # 仓管申请加班车后撤销
    def test_revoke(self):
        self.testAddFleet()  # 先建个申请
        url = self.host2 + "api/_/fleet/updateFleet"
        headers = {
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": getsessionid(32416),
            "TIMEZONE": "+07:00"
        }
        payload = {
            "status": 4,
            "audit_id": self.test_check(),
            "reject_reason": ""
        }
        #撤销前查询进行中的第一个申请
        no1 = self.test_getlist1()
        response = requests.request("post", url=url, data=payload, headers=headers)
        # 撤销后查询进行中的第一申请
        no2 = self.test_getlist2()
        #两者相等则证明作废成功
        assert no1 == no2


# cangguan = Test_by_cangguang_case1()
# # cangguan.testGetAuditlistPermission()
# # cangguan.testGetPerson()
# # cangguan.testGetCarType()
# # cangguan.testGetStoreList()
# # cangguan.testAddFleet()
# # cangguan.test_bad_addfleet()
# # cangguan.test_getlist()
# cangguan.test_revoke()