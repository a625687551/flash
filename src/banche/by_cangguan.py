import requests
import pytest
import json

from src.method.chushihua import chushihua_traning_zhanghao

requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告


# chushihua_traning_zhanghao()  # 每天都要初始化traning账号


class TestCase1():
    host1 = "https://api-training.flashexpress.com/"
    host2 = "http://backyard-api-tra.flashexpress.com/"
    headers = None
    payload = None
    response = None

    # 获取仓管32416 sessionid
    def testLonginCangguang(self,user=32416,password=666666):  # 获取仓管32416 sessionid

        url = self.host1 + "api/backyard/v1/auth/new_device_login"
        headers = {
            "X-DEVICE-ID": "867245035784787520002063200047",
            "Accept-Language": "zh-CN",
            "By-Platform": "FB_BACKYARD",
            "X-FLE-EQUIPMENT-TYPE": "backyard",
            "Content-Type": "application/json; charset=UTF-8",
            "Content-Length": "141",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip,gzip, deflate"
        }
        payload = {
            "login": user,
            "password": password,
            "clientid": "867245035784787520002063200047",
            "clientsd": "1566022761465",
            "os": "android",
            "version": "1.2.7"
        }
        print(url)
        self.response = requests.request("post", url=url, data=json.dumps(payload), headers=headers, verify=False)
        sessionid = json.loads(self.response.text)["data"]["sessionid"]
        #断言是否获取到sessionid
        assert sessionid is not None
        return sessionid

    # 检查是否有加班车申请权限
    def testGetAuditlistPermission(self):  # 检查是否有加班车申请权限
        url = self.host1 + "api/_/audit/getAuditlistPermission"
        headers = {
            "Content-Length": "0",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Origin": "http://backyard-ui-tra.flashexpress.com",
            "Accept-Language": "zh",
            "X-BY-SESSION-ID": self.testLonginCangguang(),
            "Accept": "application/json, text/plain, */*",
            "BY-PLATFORM": "FB_ANDROID",
            "TIMEZONE": "+07:00",
            "X-Requested-With": "com.flashexpress.backyard.training",
            "Referer": "http://backyard-ui-tra.flashexpress.com/",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Postman-Token": "5ab25aa6-ab84-4d9b-b4be-888adf0ddc32,ff4fbb8a-af7e-4d6c-9c76-e166ca014b7b",
            "host1": "backyard-api-tra.flashexpress.com",
            "cache-control": "no-cache"
        }
        self.response = requests.request("post", url=url, data=self.payload, headers=headers, verify=False)
        fleet = json.loads(self.response.text)["data"]["fleet"]
        #断言是否有申请加班车权限
        assert fleet == 1
        return None

    # 获取角色、所属网点、直线上级等信息
    def testGetPerson(self):  # 获取角色、所属网点、直线上级等信息
        url = self.host2 + "api/_/personinfo/person"
        headers = {
            "Content-Length": "0",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Origin": "http://backyard-ui-tra.flashexpress.com",
            "Accept-Language": "zh",
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; LDN-LX2 Build/HUAWEILDN-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.90 Mobile Safari/537.36,PostmanRuntime/7.19.0",
            "X-BY-SESSION-ID": self.testLonginCangguang(),
            "Accept": "application/json, text/plain, */*",
            "BY-PLATFORM": "FB_ANDROID",
            "TIMEZONE": "+07:00",
            "X-Requested-With": "com.flashexpress.backyard.training",
            "Referer": "http://backyard-ui-tra.flashexpress.com/",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Postman-Token": "8770f0e6-d163-4177-b082-5e9fbbb53023,3c1d9fe0-2de5-4b36-9241-83b046cfe1eb",
            "Host": "backyard-api-tra.flashexpress.com",
            "cache-control": "no-cache"
        }
        self.response = requests.request("post", url=url, data=self.payload, headers=headers)
        superiorid = json.loads(self.response.text)["data"]["job_number"]
        #断言直线上级是否为32419
        assert superiorid == 32416
        return None

    # 获取车辆类型
    @property
    def testGetCarType(self):           #获取车辆类型
        url = self.host2 + "api/_/fleet/getCarType"
        headers = {
            "Content-Length": "0",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Origin": "http://backyard-ui-tra.flashexpress.com",
            "Accept-Language": "zh",
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; LDN-LX2 Build/HUAWEILDN-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.90 Mobile Safari/537.36,PostmanRuntime/7.19.0",
            "X-BY-SESSION-ID": self.testLonginCangguang(),
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json, text/plain, */*",
            "BY-PLATFORM": "FB_ANDROID",
            "TIMEZONE": "+07:00",
            "X-Requested-With": "com.flashexpress.backyard.training",
            "Referer": "http://backyard-ui-tra.flashexpress.com/",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Postman-Token": "8770f0e6-d163-4177-b082-5e9fbbb53023,cfc2438a-b7d3-4793-b1db-3089861c7b98",
            "Host": "backyard-api-tra.flashexpress.com",
            "cache-control": "no-cache"
        }
        self.response = requests.request("post", url=url, data=self.payload, headers=headers)
        #断言车辆类型是不是只6种
        dataList = json.loads(self.response.text)["data"]["dataList"]
        assert len(dataList) == 6
        return None

    # 获取网点
    def testGetStoreList(self):         #获取网点
        url = self.host2 + "api/_/fleet/storeList"
        headers = {
            "Content-Length": "0",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Origin": "http://backyard-ui-tra.flashexpress.com",
            "Accept-Language": "zh",
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; LDN-LX2 Build/HUAWEILDN-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.90 Mobile Safari/537.36,PostmanRuntime/7.19.0",
            "X-BY-SESSION-ID": self.testLonginCangguang(),
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json, text/plain, */*",
            "BY-PLATFORM": "FB_ANDROID",
            "TIMEZONE": "+07:00",
            "X-Requested-With": "com.flashexpress.backyard.training",
            "Referer": "http://backyard-ui-tra.flashexpress.com/",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Postman-Token": "8770f0e6-d163-4177-b082-5e9fbbb53023,cfc2438a-b7d3-4793-b1db-3089861c7b98",
            "Host": "backyard-api-tra.flashexpress.com",
            "cache-control": "no-cache"
        }
        self.response = requests.request("post", url=url, data=self.payload, headers=headers)
        #断言网点超过100个
        assert len(json.loads(self.response.text))["data"]["dataList"] > 100

        return None

    # 正常申请加班车
    def testAddFleet(self):         # 正常申请加班车
        url = self.host2 + "api/_/fleet/addFleet"
        headers = {
            'Content-Length': "158",
            'Pragma': "no-cache",
            'Cache-Control': "no-cache",
            'Origin': "http://backyard-ui-tra.flashexpress.com",
            'Accept-Language': "zh",
            'User-Agent': "Mozilla/5.0 (Linux; Android 8.0.0; LDN-LX2 Build/HUAWEILDN-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.90 Mobile Safari/537.36,PostmanRuntime/7.19.0",
            'X-BY-SESSION-ID': "1574249163_bed4b8f021a4cb9c72af4f13b496dfd6e91d01cba8a40d4ef12198f935a5ef91_32416",
            'Content-Type': "application/json;charset=UTF-8",
            'Accept': "application/json, text/plain, */*",
            'BY-PLATFORM': "FB_ANDROID",
            'TIMEZONE': "+07:00",
            'X-Requested-With': "com.flashexpress.backyard.training",
            'Referer': "http://backyard-ui-tra.flashexpress.com/",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'Postman-Token': "8770f0e6-d163-4177-b082-5e9fbbb53023,c8654912-8132-48c9-83ff-a2c0ecb811c0",
            'Host': "backyard-api-tra.flashexpress.com",
            'cache-control': "no-cache"
        }
        payload = {
            "car_type":300,
            "capacity":"35",
            "start_store":"TH01010101",
            "end_store":"TH47200101",
            "reason":"www.pgyer.com",
            "arrive_time":"2019-11-14 00:00",
            "image_path":[]
        }
        self.response = requests.request("post", url=url, data=payload, headers=headers)
        msg = json.loads(self.response.text)["msg"]
        #断言是否返回请求成功


ee = TestCase1()
print(ee.testGetCarType)
