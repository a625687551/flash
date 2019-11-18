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
    def __init__(self):
        self.host1 = "https://api-training.flashexpress.com/"
        self.host2 = "http://backyard-api-tra.flashexpress.com/"
        self.headers = {
            "Accept-Language": "zh",
            "TIMEZONE": "+07:00"
        }
        self.payload = None
        self.response = None

    def get_waitAuditNum(self):
        url = self.host2 + "api/_/audit/waitAuditNum"
        self.headers.update({"X-BY-SESSION-ID": getsessionid(32419)})
        print(25)
        print(self.headers)
        # response1 = requests.request("post", url=url, data=self.payload, headers=headers, verify=False)


lisi = Test_by_jingli_case1()
lisi.get_waitAuditNum()
