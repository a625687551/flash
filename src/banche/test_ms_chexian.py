import random
import json
import time

import requests
from src.method.chushihua import *

requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告


class Test_ms_zhohongkong():
    host = "https://sapi-training.flashexpress.com/"
    headers = ""
    payload = None
    response = None

    def test_get_daishengpi(self):  # 查询待审批条数
        pass
