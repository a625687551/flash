# -*- coding: utf-8 -*-
# @Time:        2019/8/28 11:10
# @Author:      LTH
import pytest
@pytest.mark.smoke
class Test_Demo1():
    @pytest.mark.lai
    def test_case01(self):
        assert True
        assert False
        print(111)

class Test_Demo2():
    def test_case01(self):
        b= 1+0
        print(222)

def test_case01():
    b = 0.5+0.5
    print(333)
@pytest.mark.smoke
@pytest.mark.huigui
def test_case02():
    c = 1+1
    print(4444)

if __name__ == '__name__':
    pytest.main()
