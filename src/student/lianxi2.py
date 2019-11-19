import os
import random
import json
import time

import requests
from src.banche.test_by_testjingli import *
from src.method.chushihua import *
from src.method.get_randome import *
from src.config.feelt import getsessionid

url = "http://backyard-api-tra.flashexpress.com/api/_/fleet/addFleet"
headers = {
    'Accept-Language': "zh",
    'X-BY-SESSION-ID': "1574739110_ebca4f00ecfe232128a34b72df959ce9ca899ca8ec6e0c7a2064d29f651c1467_32416",
    'TIMEZONE': "+07:00",
}
reason = "laitaihua自动创建于:" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

#  车辆类型为空
payload1 = {
            "car_type": get_card_id(),
            "capacity": 5001,
            "start_store": "TH01010101",
            "end_store": "TH01010101",
            "reason": reason,
            "arrive_time": str(time.strftime("%Y-%m-%d %H:%M:00", time.localtime(time.time() + 7200))),
            "image_path": []
        }
response1 = requests.request("post", url=url, data=payload1, headers=headers)
print(response1.text)