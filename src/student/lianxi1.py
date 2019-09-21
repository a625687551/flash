# -*- coding: utf-8 -*-
# @Time:        2019/8/27 20:43
# @Author:      LTH
import requests
import json
'''
表单提交，data传入字典 payload = {"key1":"value1","key2":"value2"}
X-WWW-form-urlencoder，headers增加配置 Content-Type：application/X-WWW-form-urlencoder data传入字典
raw文本提交
json形式字典转字符串
    data = {'sume':'data'}
    rsponse = requests.post(url,data=json.dumps(data))

解析响应
    json格式
        response.json（） --响应字符串转为json对象（字典）
    XML格式
        使用ElementTree
            1加载xml --两种方法 一是加载指定字符集，2是加载指定文件
                root = ElementTree.fromstring（text）
                root = ElementTree.parse（"D:/test.xml"）
            2获取对象
                find方法，支持部分xpath语法
                findall方法，支持部分xpath语法
            3获取值，属性
                .text
                .attrib['category']
            4添加命名空间
'''
# get方法
def get_shen_id_get():
    url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString?'
    params = {'theRegionCode':'3113'}
    response = None
    response = requests.get(url=url,params=params)
    print(response.text)
    url2 = 'https://www.baidu.com/s?ie=UTF-8&wd=带参数的get'
    response2 = requests.get(url=url2)
    print(response2.text)

def get_shi_id_get():
    url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
    params = {'theRegionCode':311101}
    response = requests.get(url=url, params=params)
    print(response.text)

def get_shi_id_post():
    url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
    params = {'theRegionCode': 311101} # 键值对格式
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    response = requests.post(url=url,data=params,headers=headers)
    print(response.text)
#raw文本提交
def get_shi_id_soap():
    url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx'
    params = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <getSupportCityString xmlns="http://WebXml.com.cn/">
      <theRegionCode>311101</theRegionCode>
    </getSupportCityString>
  </soap:Body>
</soap:Envelope>'''
    headers = {'Content-Type':'text/xml; charset=utf-8'}
    response = requests.post(url=url,data=params,headers=headers)
    print(response.text)
'''
单元测试
Test Case
    一个测试用例就是一个完整的测试单元，包含初始和收尾工作
    基本单元为函数
Test Suite
    一个功能往往有多个测试用例验证，用例的集合称为测试套件
Test Runner
    测试用例执行的的基本单元
用例组织
    方式1：函数是用例，集中在一个类中
    继承unittest.TestCase
    每个用例都是一个无参的成员方法
        方法名用test开头
        名为runTest
    主函数中调用unitest.main（）函数 运行类中以test开头的所有测试用例
    方式2：构造测试集合
        unittest.TestSuite（）
            .addTest（类名（"方法名"））
                类需要事先import
        unittest.TextTestRunner（）.run（suite）
        创建run.py
'''

'''
字符串：
    首字母大写：str.title（）   全部大写 str.upper（） 全部小写 str.lower（）
    拼接 +   乘 str*3
    换行 \n
    开头删除空白 lstrip 末尾删除空白 rstrip 两端删除空白 strip
    
'''
'''
list列表
    切记不要将列表赋值给一个列表，因为这样并不能得到两个列表 用list2 = list1[:]
    列表解析式 list = [value**2 for valiue in range(1,6,2)]  等价于 [1,9,25]
    列表切片 list[索引1:索引2] 含索引1不含索引2
    INdexError：out of range   索引错误
    IndenttationError 缩进错误
    list = []   访问 list[0]或lis[-1]
    增加：末尾增减    list.append（xx）；     插入（其他位置往后排） list.insert（索引，valuue）  
    删除：del list[索引]  ；pop 删除一个元素并返回它 a = list.pop（1） （不写默认为最后一个元素）
        remove删除指定值并返回 a = list.remove（value）
    sort 排序 list.sort()按数字字母永久排序，list.sort（reverse=True）倒叙
    sorted 临时排序 sorted（list）    sorted（list，reverse=True）
    reverse 反转 lsit.reverse（）
    for a in lsit  遍历
    l = list（range（2,10,2）） 创建list
元组
    tup = ()   tup = (1,)
字典
    dict = ()    dict = {'key1':'value1','key2':'value2'}
    遍历
        遍历所有键、值
            for key，value in dict.items（）
                print（"\nkey"+:key
                print（"\nvalue"+:value）
        遍历所有键 或 值
            for key in dict.keys（）
            for key in dict.values（）
        去除重复值
            for key in set（dict.values（））
        按特定顺序遍历字典的多有键
            for key in sorted（dict.keys）
        
'''
'''
常用函数
    range（num1，num2，steps）     启示（含） 终止（不含） 步常
    min（） 最小  min（list）
    max（）
    sum（）
    input（）    a=input（"请输入一个值，默认为str"）
 '''
'''
语句
    不区分大小小判断b列表元素是否在a中存在
        a = ['a','d','c']
        b = ['D','c']
        for b in b:
            if b.lower() in [a.lower() for a in a ]
                pint(b的元素在a中存在)          
'''
'''
函数
    调用
        关键字实参and默认参数
            def fun(name,age,high=180):
                print('名字是'+name，'年龄是'+age，'身高是'+high)
            fun(age=10,name='Uzi')
        
'''