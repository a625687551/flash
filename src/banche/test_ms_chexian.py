import random
import json
import time

import requests
from src.method.chushihua import *
from src.config.feelt import *

requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告


class Test_ms_central_control_approval:
    """"中控审批 """
    host = "https://sapi-training.flashexpress.com/"
    headers = {"X-MS-SESSION-ID": getsessionid(31161)}
    payload = None
    response = None

    def test_get_stor(self):
        url = self.host + "ms/api/setting/store/manager/van/line"
        response1 = requests.request("GET", url=url, headers=self.headers, verify=False)
        assert len(json.loads(response1.text)["data"]) > 2000

    def test_query(self):  # 组合查询审批列表
        url = self.host + "ms/api/fleet/line/approve"
        params = {"serialNo": "VA5267241431040", "applyStartDate": "", "applyEndDate": "", "sortingNo": "B",
                  "originStoreId": "TH01470301", "targetStoreId": "TH01010107", "state": "2", "pageSize": "20",
                  "pageNum": "1"}
        response1 = requests.request("get", url=url, params=params, headers=self.headers, verify=False)
        assert json.loads(response1.text)["data"]["items"] is not None


ji = Test_ms_central_control_approval()
ji.test_get_stor()
