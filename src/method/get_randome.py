# -*- coding: utf-8 -*-
# @Time:        2019/9/26 17:28
# @Author:      LTH
import time
import random
import json


# 返回随机身份证号
def get_card_id():
    a = random.randint(111100001111, 9999888899998)
    b = random.choice('ABCDEFGHIJKLMN')
    card_id = b + str(a)
    return card_id


# 返回随机手机号
def get_phone():
    a = random.randint(1112223334, 9998887776)
    return a


# 返回一个字符串如（赵A）
def get_str():
    surname = random.choice('赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎') + \
              random.choice('ABCDEFGHIJKLMNOPQ')
    return surname


def getlocaltime():
    """
    时间戳换算时间
    now = time.time()
    tl = time.localtime(now)
    format_time = time.strftime("%Y-%m-%d %H:%M:%S", tl)
    """
    """
    时间换算成时间戳
    format_time = '2017-03-16 18:22:06'
    ts = time.strptime(format_time, "%Y-%m-%d %H:%M:%S")
    time.mktime(ts)
    """


def getdict(json1):
    return json.loads(json1)
