import random
import json
import time

import requests
from src.method.chushihua import *
from src.config.feelt import *

requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告


class Test_ms_central_control_approval:
    """"中控审批操作 """
    host = "https://sapi-training.flashexpress.com/"
    headers = {"X-MS-SESSION-ID": getsessionid(31161)}
    payload = None
    response = None

    # ms查询网点
    def test_get_store(self):
        url = self.host + "ms/api/setting/store/manager/van/line"
        response1 = requests.request("GET", url=url, headers=self.headers, verify=False)
        assert len(json.loads(response1.text)["data"]) > 2000

    # 组合查询审批列表
    def test_query(self):  # 组合查询审批列表
        url = self.host + "ms/api/fleet/line/approve"
        params = {"serialNo": "VA5267241431040", "applyStartDate": "", "applyEndDate": "", "sortingNo": "B",
                  "originStoreId": "TH01470301", "targetStoreId": "TH01010107", "state": "2", "pageSize": "20",
                  "pageNum": "1"}
        response1 = requests.request("get", url=url, params=params, headers=self.headers, verify=False)
        assert json.loads(response1.text)["data"]["items"] is not None

    # 获取到最新的一条申请记录
    def test_get_newest_pending_approval(self):
        headers = {"X-MS-SESSION-ID": getsessionid(31161)}
        url1 = self.host + "ms/api/fleet/line/approve"
        payload1 = {"serialNo": "", "applyStartDate": "", "applyEndDate": "", "state": "7", "pageSize": "20", "pageNum": "1"}
        response1 = requests.request("GET", url=url1, headers=headers, params=payload1, verify=False).text
        d = json.loads(response1)["data"]["pagination"]
        # 计算最后一页的编号
        n = None
        if d["total_count"] % d["per_page"] == 0:
            n = int(d["total_count"] / d["per_page"])
        else:
            n = int(d["total_count"] / d["per_page"]) + 1
        # 点击最后一页
        payload2 = {"serialNo": "", "applyStartDate": "", "applyEndDate": "", "state": "7", "pageSize": "20",
                    "pageNum": n}
        response2 = requests.request("GET", url=url1, headers=headers, params=payload2, verify=False).text
        # 获取到最新的一条申请记录
        newest = json.loads(response2)["data"]["items"][-1]
        return newest               #获取到id    newest["id"]

    # 审批待审批
    def test_pending_approval(self):

        pass

zhong = Test_ms_central_control_approval()
zhong.test_pending_approval()