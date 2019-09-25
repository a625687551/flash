# -*- coding: utf-8 -*-
# @Time:        2019/8/28 11:24
# @Author:      LTH
import requests
import pytest
import json
@pytest.mark.login1
@pytest.mark.parametrize('user,pw',[(10000,123456),(10000,123)])
def test_login(user,pw):
    print(111111111111111111)
    url = 'http://192.168.0.228:8080/ms/api/auth/signin'
    params = {"login":user,"password":pw}
    headers = {'Content-Type':'application/json;charset=UTF-8','Accept-Language':'zh-CN'}
    response = requests.post(url=url,data=json.dumps(params),headers=headers)
    print(response.status_code)
    assert response.status_code == 200
    assert json.loads(response.text)['data']['profile']['id'] ==10000
    assert str(response.url) == 'http://192.168.0.228:8080/ms/api/auth/signin'


if __name__ == '__name__':
    pytest.main()

a = '554545aa'
print()