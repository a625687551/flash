import requests
import json
import random
from src.config.feelt import getsessionid
requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告


heraders = {"Content-Type": "application/json; charset=UTF-8", "X-MS-SESSION-ID": getsessionid(31161)}
response = requests.request("get", url="https://sapi-training.flashexpress.com/ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=7&pageSize=20&pageNum=1",  params=None, heraders=heraders)
print(response.text)