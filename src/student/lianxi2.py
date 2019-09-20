# -*- coding: utf-8 -*-
# @Time:        2019/8/28 10:28
# @Author:      LTH
import requests
import unittest
class lianxi2(unittest.TestCase):
    def test_case02(self):
        url = 'https://sapi-training.flashexpress.com/ms/api/auth/signin'
        params = {"login":"10000","password":"goflasher"}  # 键值对格式
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        response = requests.post(url=url, data=params, headers=headers)
        print(response.text)
        self.assertEqual('实际结果','预期结果','两者不等时输出“实际与预期不一致”')
if __name__ == '__name__':
    unittest.main()