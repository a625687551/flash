import requests

url = "https://sapi-training.flashexpress.com/ms/api/fleet/line/approve"

querystring = {"serialNo":"","applyStartDate":"","applyEndDate":"","state":"2","pageSize":"20","pageNum":"1"}


headers = {
    'Connection': "keep-alive",
    'Accept': "application/json, text/plain, */*",
    'X-MS-SESSION-ID': "1574427638_b4eca2ffe8d5218b3a7aee91c88284ccf8de1a362638c07824d366e09976e399_31161",
    'Cache-Control': "no-cache",
    'Origin': "http://ms-training.flashexpress.com",
    'Accept-Language': "zh-CN",
    'Content-Type': "application/json"
    }

response = requests.request("GET", url, url, headers=headers, params=querystring)

print(response.text)