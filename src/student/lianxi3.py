import requests
import json
import random
from src.config.feelt import getsessionid
requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告
headers = {"Content-Type": "application/json; charset=UTF-8", "X-MS-SESSION-ID": getsessionid(31161)}
url = "https://sapi-training.flashexpress.com/ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=7&pageSize=20&pageNum=1"


response = requests.request("GET", url, headers=headers,  verify=False)
# response = requests.get(url, data=payload, headers=headers, params=querystring,verify=False)

print(response.text)