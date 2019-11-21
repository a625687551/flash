import requests
import json
import random
from src.config.feelt import getsessionid
requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告

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
    if store_id != None:
        print("获取网点successful")
    # 断言网点超过2200个
    assert len(json.loads(response1.text)["data"]["dataList"]) > 2200
    return random.choice(store_id)


def test_getlist():
    print("下面是查询仓管的申请和已完成")
    url = "http://backyard-api-tra.flashexpress.com/api/_/auditList/getList"
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
    num1 = len(json.loads(response1.text)["data"]["dataList"])
    if json.loads(response1.text)["data"] is not None:
        print("查询仓管申请-进行中正常")

    pyload2 = {
        "audit_show_type": 1,
        "audit_state_type": 2,
        "page_num": 1
    }
    response2 = requests.request("post", url=url, data=pyload2, headers=headers, verify=False)
    num2 = len(json.loads(response2.text)["data"]["dataList"])
    if json.loads(response2.text)["data"] is not None:
        print("查询仓管申请-已完成中正常")
    assert json.loads(response2.text)["data"] is not None
    return num1, num2


def get_waitAuditNum():
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


def get_xianlu_shenpi():
    print("下面是查询ms中控人员的待审批和已通过和已驳回的条数")
    heraders = {"Content-Type": "application/json; charset=UTF-8", "X-MS-SESSION-ID": getsessionid(31161)}
    print(heraders)
    params = {
        "待审批": "https://sapi-training.flashexpress.com/ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=7&pageSize=20&pageNum=1",
        "已通过": "https://sapi-training.flashexpress.com/ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=2&pageSize=20&pageNum=1",
        "已驳回": "https://sapi-training.flashexpress.com/ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=3&pageSize=20&pageNum=1"
    }
    items = {}
    #
    # url1 = "https://sapi-training.flashexpress.com/ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=7&pageSize=20&pageNum=1"  # 待审批
    # url2 = "https://sapi-training.flashexpress.com/ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=2&pageSize=20&pageNum=1"  # 已通过
    # url3 = "https://sapi-training.flashexpress.com/ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=3&pageSize=20&pageNum=1"  # 已驳回

    for key in url:
        print(url[key])
        response = requests.request("get", url=url[key], heraders=heraders, verify=False)

        print(json.loads(response.text)["data"]["pagination"]["total_count"])
        items["key"] = json.loads(response.text)["data"]["pagination"]["total_count"]
    print(items)


get_xianlu_shenpi()
