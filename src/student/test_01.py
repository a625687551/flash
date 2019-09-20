# -*- coding: utf-8 -*-
# @Time:        2019/8/28 11:10
# @Author:      LTH
import pytest
@pytest.mark.smoke
class Test_Demo1():
    def test_case01(self):
        a= 0+0
        print(a)
class Test_Demo2():
    def test_case01(self):
        b= 1+0
        print(b)
def test_case01():
    b = 0.5+0.5
    print(b)
@pytest.mark.smoke
@pytest.mark.hugeui
def test_case02():
    c = 1+1
    print(c)
