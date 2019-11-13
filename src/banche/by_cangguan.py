import requests
import pytest
import json

from src.method.chushihua import chushihua_traning_zhanghao

requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告

#chushihua_traning_zhanghao()  # 每天都要初始化traning账号


class TestCase1():
    host1 = 'https://api-training.flashexpress.com/'
    host2 = "http://backyard-api-tra.flashexpress.com/"
    headers = None
    payload = None
    response = None

    def testLonginCangguang(self):  # 获取仓管32416 sessionid

        url = self.host1 + "api/backyard/v1/auth/new_device_login"
        headers = {
            'X-DEVICE-ID': "867245035784787520002063200047",
            'Accept-Language': "zh-CN",
            'By-Platform': "FB_BACKYARD",
            'X-FLE-EQUIPMENT-TYPE': "backyard",
            'Content-Type': "application/json; charset=UTF-8",
            'Content-Length': "141",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip,gzip, deflate"
        }
        payload = {
            "login": "32416",
            "password": "666666",
            "clientid": "867245035784787520002063200047",
            "clientsd": "1566022761465",
            "os": "android",
            "version": "1.2.7"
        }
        print(url)
        self.response = requests.request("post", url=url, data=json.dumps(payload), headers=headers, verify=False)
        sessionid = json.loads(self.response.text)["data"]["sessionid"]
        assert sessionid is not None
        return sessionid

    def testGetAuditlistPermission(self):       #检查是否有加班车申请权限
        url = self.host1 + "api/_/audit/getAuditlistPermission"
        headers = {
            'Content-Length': "0",
            'Pragma': "no-cache",
            'Cache-Control': "no-cache",
            'Origin': "http://backyard-ui-tra.flashexpress.com",
            'Accept-Language': "zh",
            'X-BY-SESSION-ID': "1574241346_57aeb6e803f1b1e916abc81ed120478d42836454b43db91059ebe05792677c46_32416",
            'Accept': "application/json, text/plain, */*",
            'BY-PLATFORM': "FB_ANDROID",
            'TIMEZONE': "+07:00",
            'X-Requested-With': "com.flashexpress.backyard.training",
            'Referer': "http://backyard-ui-tra.flashexpress.com/",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'Postman-Token': "5ab25aa6-ab84-4d9b-b4be-888adf0ddc32,ff4fbb8a-af7e-4d6c-9c76-e166ca014b7b",
            'host1': "backyard-api-tra.flashexpress.com",
            'cache-control': "no-cache"
            }
        self.response = requests.request("post",url=url,data=self.payload,headers=headers,verify=False)
        fleet = json.loads(self.response.text)["data"]["fleet"]
        assert fleet == 1
        return None

    def testGetPerson(self):            #获取角色、所属网点、直线上级等信息
        url = self.host2 + "api/_/personinfo/person"


ee = TestCase1()
print(ee.testLonginCangguang())
