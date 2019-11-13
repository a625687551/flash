import requests
import json
def updata32417():
    # 把32417设置为仓管
    url = "http://bi.test.fe.com/ajax.do"

    payload = "f=dc_unsignedformanager&time=3"
    headers = {
        'Accept': "application/json, text/javascript, */*; q=0.01,*/*",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cache-Control': "no-cache,no-cache",
        'Content-Length': "30",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Cookie': "_ga=GA1.2.1642456327.1560851912; lang=zh-CN; _gid=GA1.2.1579722277.1573462282; PHPSESSID=ko66q3u7mujpbduqajmie584f; token=MDQwMTA1OGYwOTQ0ODQ0YjczNTgwYWE2NDg2Y2IxN2M=; _gat_gtag_UA_145656102_1=1",
        'Host': "bi.test.fe.com",
        'Origin': "http://bi.test.fe.com",
        'Pragma': "no-cache",
        'Proxy-Connection': "keep-alive",
        'Referer': "http://bi.test.fe.com/dc/unsignedformanager",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
        'X-Requested-With': "XMLHttpRequest",
        'Postman-Token': "717bec76-6157-4ddd-9b7a-0645ad3536c0,212ea0e9-234f-433c-b27c-64edbbf209dc",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers, verify=False)
    print(response.json())
    if response.status_code == 200:
        print("设置32416仓管成功")
updata32417()