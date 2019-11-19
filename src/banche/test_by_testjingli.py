import os
import random
import json
import time

import requests
from src.method.chushihua import *
from src.method.get_randome import *
from src.config.feelt import getsessionid

requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告


class Test_by_jingli_case1():
    host1 = "https://api-training.flashexpress.com/"
    host2 = "http://backyard-api-tra.flashexpress.com/"
    headers = {
            "Accept-Language": "zh",
            "TIMEZONE": "+07:00"
    }
    payload = None
    response = None

    def get_waitAuditNum(self):
        url = self.host2 + "api/_/audit/waitAuditNum"
        self.headers.update({"X-BY-SESSION-ID": getsessionid(32419)})
        response1 = requests.request("post", url=url, data=self.payload, headers=self.headers, verify=False)
        num = int(json.loads(response1.text)["data"]["num"])
        assert num > 1
        return num

aa = Test_by_jingli_case1()
aa.get_waitAuditNum()