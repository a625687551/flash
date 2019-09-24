# -*- coding: utf-8 -*-
# @Time:        2019/8/28 10:33
# @Author:      LTH
import requests

def fun1(a=1,b=2):
    return fun2()+b

def fun2():
    return 2

print(fun1())