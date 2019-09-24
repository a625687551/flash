# -*- coding: utf-8 -*-
# @Time:        2019/8/28 10:33
# @Author:      LTH
import requests


"""
pytest  运行当前路径下所有测试文件的所有测试方法 递归遍历每个子目录
pytest src\student\testpackage\test_testfile01.py   指定路径运行
pytest src\student\testpackage\test_testfile01.py::test_case01   指定方法运行

"""
def fun1(a=1,b=2):
    return fun2()+b

def fun2():
    return 2

print(fun1())