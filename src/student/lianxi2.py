import requests
requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告
url = "https://sapi-training.flashexpress.com/ms/api/fleet/line/approve"

querystring = {"serialNo":"","applyStartDate":"","applyEndDate":"","state":"2","pageSize":"20","pageNum":"1"}
headers = {
    'Connection': "keep-alive",
    'Accept': "application/json, text/plain, */*",
    'X-MS-SESSION-ID': "1574427638_b4eca2ffe8d5218b3a7aee91c88284ccf8de1a362638c07824d366e09976e399_31161",
    'Cache-Control': "no-cache",
    'Origin': "http://ms-training.flashexpress.com",
    'Accept-Language': "zh-CN",
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.19.0",
    'Postman-Token': "fc41bead-c1df-499a-bab2-a42ea9d8024e,9d15d32f-d785-42c1-a660-eb202c0f2fbf",
    'Host': "sapi-training.flashexpress.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "174",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring, verify=False)
# response = requests.get(url, data=payload, headers=headers, params=querystring,verify=False)

print(response.text)