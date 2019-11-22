import requests

url = "https://sapi-training.flashexpress.com/ms/api/fleet/line/approve"
querystring = {"serialNo": "", "applyStartDate": "", "applyEndDate": "", "state": "2", "pageSize": "20", "pageNum": "1"}
headers = {'X-MS-SESSION-ID': "1574427638_b4eca2ffe8d5218b3a7aee91c88284ccf8de1a362638c07824d366e09976e399_31161"}
response = requests.request("GET", url, headers=headers, params=querystring, verify=False)

print(response.text)