import requests
import json
import random
import time
from src.config.feelt import getsessionid

requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告


# BY获取网点  return TH01010101
def testGetStoreList():  # 获取网点
    print("下面是获取网点")
    url = "http://backyard-api-tra.flashexpress.com/api/_/fleet/storeList"
    headers = {
        "Accept-Language": "zh",
        "X-BY-SESSION-ID": getsessionid(32416),
        "TIMEZONE": "+07:00"
    }
    response1 = requests.request("post", url=url, data=None, headers=headers)
    dataList = (json.loads(response1.text)["data"]["dataList"])
    store_id = []
    j = 0
    for i in dataList:
        j = j + 1
        if j < 50:
            store_id.append(i["store_id"])
    if store_id is not None:
        print("获取网点successful")
    # 断言网点超过2200个
    assert len(json.loads(response1.text)["data"]["dataList"]) > 2200
    return random.choice(store_id)


# # 下面是查询仓管的申请和已完成
# def test_getlist():
#     print("下面是查询仓管的申请和已完成")
#     url = "http://backyard-api-tra.flashexpress.com/api/_/auditList/getList"
#     headers = {
#         "Accept-Language": "zh",
#         "X-BY-SESSION-ID": getsessionid(32416),
#         "TIMEZONE": "+07:00"
#     }
#     pyload1 = {
#         "audit_show_type": 1,
#         "audit_state_type": 1,
#         "page_num": 1
#     }
#     response1 = requests.request("post", url=url, data=pyload1, headers=headers, verify=False)
#     if json.loads(response1.text)["data"] is not None:
#         print("查询仓管申请-进行中正常")
#
#     pyload2 = {
#         "audit_show_type": 1,
#         "audit_state_type": 2,
#         "page_num": 1
#     }
#     response2 = requests.request("post", url=url, data=pyload2, headers=headers, verify=False)
#     if json.loads(response2.text)["data"] is not None:
#         print("查询仓管申请-已完成中正常")
#     assert json.loads(response2.text)["data"] is not None


# 下面32419是获取32419待审批条数  return  100
# 仓管正常申请加班车
def test_cangguan_AddFleet():
    url = "http://backyard-api-tra.flashexpress.com/api/_/fleet/addFleet"
    headers = {
        'Accept-Language': "zh",
        'X-BY-SESSION-ID': getsessionid(32416),
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
    response1 = requests.request("post", url=url, data=payload, headers=headers)
    assert json.loads(response1.text)["code"] == 1
    assert json.loads(response1.text)["msg"] == "请求成功!"
    assert json.loads(response1.text)["data"] is None


# 获取32419待审批条数
def test_get_waitAuditNum():
    print("下面32419是获取32419待审批条数:")
    url = "http://backyard-api-tra.flashexpress.com/api/_/audit/waitAuditNum"
    headers = {
        "Accept-Language": "zh",
        "X-BY-SESSION-ID": getsessionid(32419),
        "TIMEZONE": "+07:00"
    }
    response1 = requests.request("post", url=url, data=None, headers=headers, verify=False)
    num = int(json.loads(response1.text)["data"]["num"])
    if num > 1:
        print("获取32419待审批条数successful")
    assert num > 1
    return num


# 下面是查询ms中控人员的待审批和已通过和已驳回的条数    {'待审批': 42, '已通过': 68, '已驳回': 6}
def test_get_xianlu_shenpi():
    print("下面是查询ms中控人员的待审批和已通过和已驳回的条数")
    headers = {"X-MS-SESSION-ID": getsessionid(31161)}
    url = {
        "待审批": "https://sapi-training.flashexpress.com/ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=7&pageSize=20&pageNum=1",
        "已通过": "https://sapi-training.flashexpress.com/ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=2&pageSize=20&pageNum=1",
        "已驳回": "https://sapi-training.flashexpress.com/ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=3&pageSize=20&pageNum=1"
    }
    total_count = {}
    for key in url:
        response = requests.request("GET", url=url[key], headers=headers, verify=False)
        total_count[key] = json.loads(response.text)["data"]["pagination"]["total_count"]

    assert total_count is not None
    return total_count  # {'待审批': 42, '已通过': 68, '已驳回': 6}


