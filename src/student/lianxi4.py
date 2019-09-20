import requests
url = "http://192.168.0.230:8100/interview/interviewResumeList"
payload = "{\r\n\t\"store_id\": \"0\",\r\n\t\"page_size\": 860,\r\n\t\"page_num\": 1\r\n}"
headers = {
    'Content-Type': "application/json",
    'X-FLE-SESSION-ID': "1568705034_c360279de6b410b1303f222fa62ac1a4d79c053d_22206",
    'User-Agent': "PostmanRuntime/7.16.3",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "d392f028-e813-419f-bafe-14f9a2c6498a,48ac3b45-fa30-4603-a9ff-8ebf7c9aa4df",
    'Host': "192.168.0.230:8100",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "58",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)


a = response.json()['data']['dataList']
print(len(a))
#print(type(a))
list = []
for i in a:
    list.append(i['resume_id'])
#print(list)
print(len(list))
b = set(list) #字典有去重功能，如果相等则表示没有重复
print(len(b))