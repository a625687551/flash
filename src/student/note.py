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
def get_1():
    url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString?'
    params = {'theRegionCode':'3113'}
    response = requests.get(url=url,params=params)
def get_2():
    url2 = 'https://www.baidu.com/s?ie=UTF-8&wd=带参数的get'
    response = requests.get(url=url2)

#键值对格式
def post_1():
    url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
    params = {'theRegionCode': 311101} # 键值对格式
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    response = requests.post(url=url,data=params,headers=headers)
    print(response.text)
def post_2():
    url = 'http://192.168.0.230:8100/jd/jdList'
    params = {"job_name":"","department_id":"","submitter_name":"","time_start":"","time_end":"","page_size":100,"page_num":1}  #data字典
    headers = {'Content-Type':'application/json;charset=UTF-8','X-BY-SESSION-ID':'1569246054_551192c8c71572797efdb0feed40dbd0027c9310_22202'}
    response = requests.post(url=url,data=params,headers=headers)
def post_3():
    url = 'http://192.168.0.230:8100/jd/jdList'
    params = '{"job_name":"","department_id":"","submitter_name":"","time_start":"","time_end":"","page_size":100,"page_num":1}'   #data是json字符
    headers = {'Content-Type':'application/json;charset=UTF-8','X-BY-SESSION-ID':'1569246054_551192c8c71572797efdb0feed40dbd0027c9310_22202'}
    response = requests.post(url=url,data=json.dumps(params),headers=headers)

#raw文本提交 soap
def post_soap():
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
    count（）统计某个元素的个数  list.count（'laitauhua'）
    index(目标元素，从第几位开始，在第几位结束) 查找某元素的位置返回 下标  list（'lai',2）
    extend() 扩展列表    list.extend（list2）
    l = list（range（2,10,2）） 创建list
元组
    元组不能修改
    tup = ()   tup = (1,)
    count（）统计
    index（）查找
    cmp（tup2，tup2） 比较两个元组
    min（）
    max（)
字典
    dict = ()    dict = {'key1':'value1','key2':'value2'}
    dict = dict(naem = 'laitaihua',age=18)
    访问
        dict[key]
        dict.get(key)   返回key对应的值
        dict.get（key，2） 如果不存在key则返回默认值2
    添加或修改元素
        dict['anme'] = lai
        dict.update(name='lai')
    删除
        dict.pop（key）
    判断key是否存在    返回布尔值
        key in dict
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
        列表实参
            def fun(list_list):
                print(list_list[-1])
            a = []
            fun(a[:])
        元组:任意数量的实参      
            def fun（age,*name） #*是高数python创建个元组
                print（name）
            fun（12,'lai','tai','hua'）
        字典：任意数量的实参
            def fun（age,**name） #*是高数python创建个字典
                print（name）
            fun（12,'lai',name='赖太华'，work='flash'）
    递归函数    一个函数在内部调用它自己    把复杂的问题简化
        
模块
    导入模块 import module_name
    调用模块的方法  module_nem.function_name()
    导入模块中的所有函数 from module_nme import *
    导入特定函数 module import function1_name1,functionl_name2
    给导入的函数起名 module import function1_name1 as fun1,functionl_name2 as fun2
类 class
    类名首字母大写
    类需要文档字符串
        class Dog（）：
            """ 这是一个狗类 """
             def __init__(self, name, age):
            """初始化属性name和age"""
                self.name = name
                self.age = age
            def sit(self):
                """模拟小狗被命令时蹲下"""
                print(self.name.title() + " is now sitting.")
            def roll_over(self):
                """模拟小狗被命令时打滚"""
                print(self.name.title() + " rolled over!")
            # 创建类实例
            my_dog = Dog（'tony','3'）
            # 调用类函数
            my_dog.sit()
            调用属性
            my_dog.age            
    __init__() 初始化 创建类实例时自动调用，
        __init_()必须包含self形参，且必须放在最前面，它是指向示例本身的引用，每个与类相关联的方法都自动传递实参self（所以在创建类示例时，不用提供传递值）
继承
    class Fulei():   #父类，超类  父类必须位于子类前面
        pass
    class Zilei（Fulei）：       #子类
        pass
    子类
        在_init_方法内，必须初始化父类所需要的信息，使用super().__init__()方法初始化父类属性
        子类特有的属性只包含在子类的实例中，父类的实例并不包含
        重写父类方法
            方法名与父类一致
'''
'''
字符串
    unicode  统一码万国码
        unicode_str = u"我"
        utf8_str = unicode_str.encode('utf-8') #  使用encode(翻译成中文是编码)方法、utf-8来编码unicode字符
            print（utf8_str）= '\xe6\x88\x91'
        utf8_str.decode('utf-8') #  使用decode(翻译成中文是解)方法、utf-8来解码unicode字符
            print（utf8_str.decode）= u'\u6211'
    计算特定字符在字符串出现的数量
        str.count（''）
    是否以指定字符开头或结尾  返回布尔值
        str.startswith（''）
    转化大小写
        str.lower（）
        str.upper()
    查找  find返回首个结果位置，否则返回-1   rfind 后往前
        str.find（'ab'）
    替换 str.replace（'ab','b'） 由ab替换为b
    首字母大写：str.title（）   全部大写 str.upper（） 全部小写 str.lower（）
    拼接 
        +   乘 str*3
        join    把字符/字符串列表（或者可迭代对象均可）拼接起来
            s1 = ['ab', 'cd', 'ef']
            print(''.join(s1))  >   'abcdef'
            print('.'.join(s1))  >   'ab.cd.ef'
            s2 = 'abcdefg'
            print('.'.join(s2))  >   'a.b.c.d.e.f.g'
            
    换行 \n
    strip  开头删除空白 lstrip 末尾删除空白 rstrip 两端删除空白 strip  去除指定字符串  s = '\n\t abc  \n\t' ；s.strip('\t')；'\n\t abc  \n'
    格式化输出
        print('我是%s人%s' % ('我', '吗'))
        print('我是{what}人'.format(what='好'))
        
'''
'''
运算
    除
        两个整数相除，得到了是商的整数部分
        运算时，如果需要准确结果，可以把其中一个转为小数:5 / float(2)
    取模
        5.0 % 2   返回1.0
    幂
        2**3  等于2*2*2
    比较
        <   >   ==  !=  <=  >=
    逻辑  None 、 空字符串 、空字典 、数字0 在进行逻辑运算时都会被当做 False
        and与    or或     非not True
    成员运算
        in 
        not in    
    while 当AAA条件为真的时候，执行XXXX
        while num>0：
            pass
    
'''
'''
内置函数
    isinstance('abc',str)    判断一个对象是否是一个已知的类型
    abs()
    all()   判断一个可迭代对象里的元素是否全为真，全为真返回真，否则返回假
    any()   判断一个可迭代对象，里面的元素全为假时才返回假，只要有一个为真就为真:
    gettattr()   获取指定对象属性:
    round()   四舍五入
    divmod ()   除法函数，但返回商和余数
'''
'''
装饰器--高阶函数--把函数传给函数，再返回函数，也称包装器
迭代器
    iter()              记住遍历的位置的对象。
        list=[1,2,3,4]
        it = iter(list)    # 创建迭代器对象,第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
            print (next(it))    >>>1  # 输出迭代器的下一个元素
            print (next(it))    >>>12
    next()
生成器         是一个返回迭代器的函数，只能用于迭代操作
'''
'''
常用库
    time
        time.time（）返回当前时间戳
        time.localtime（time.time） 返回本地时间
        
'''
"""
pytest
    pytest -v 详细显示每个测试方法（用例）的运行结果
    pytest  运行当前路径下所有测试文件的所有测试方法 递归遍历每个子目录
    pytest src\student\testpackage\test_testfile01.py   指定路径运行
    pytest src\student\testpackage\test_testfile01.py::test_case01   指定方法运行
    pytest --collect-only 即将执行的用例
    pytest -k  xx 执行包含xx的测试用例
    @pytest.mark.xx 给类或者方法标记，通过 pytest -m xx来执行带标记的方法
    pytest -m "xx and yy"   pytest -m "xx and not yy"
    @pytest.mark.xfail  运行此用例但是预期失败
    .（passed） 测试通过          F（failed）   测试失败
    s（skipped）测试未执行        x（xfail）     预期测试失败
    X（xpass）预期测试失败但是运行
    E（error） 测试用例之外的代码触发了异常
    @pytest.mark.parametrize（argnames，argvalues） 参数化数据驱动
        argnames 用来接收每项数据作为测试用例的参数
        argvalues   n组测试数据的集合[(),(),()]
    -s
    -x 遇到失败用例停止运行
    --failmax=num 失败num次用例后停止运行
    --if
    --ff
    @pytest.fixture()   标记为fixture函数
Fixture    执行配置初始化或销毁逻辑
    UI
        前置脚本    启动浏览器、访问初始地址
        收尾脚本    关闭浏览器、关闭数据库连接、关闭文件流
    API
        前置脚本    调用关联接口、设置地址、头信息
        收尾脚步    关闭资源、设置延时
    
        
"""