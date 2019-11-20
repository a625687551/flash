import os
import json
import yaml
import requests


requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告


def loginby(user, password):
    url = "https://api-training.flashexpress.com/api/backyard/v1/auth/new_device_login"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
    }
    payload = {
        "login": user,
        "password": password,
        "clientid": "867245035784787520002063200047",
        "clientsd": "1566022761465",
        "os": "android",
        "version": "1.2.8"
    }
    response1 = requests.request("post", url=url, data=json.dumps(payload), headers=headers, verify=False)
    sessionid = json.loads(response1.text)["data"]["sessionid"]
    return sessionid


def loginms(user, password):
    url = "https://sapi-training.flashexpress.com/ms/api/auth/signin"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
    }
    payload = {
        "login": user,
        "password": password
    }
    response1 = requests.request("post", url=url, data=json.dumps(payload), headers=headers, verify=False)
    sessionid = json.loads(response1.text)["data"]["session_id"]
    return sessionid


def updatasessionid():
    a = {
        32419: loginby(32419, 666666),
        32416: loginby(32416, 666666),
        31161: loginms(31161, 666666)

    }
    # 获取当前脚本所在文件夹路径
    curPath = os.path.dirname(os.path.realpath(__file__))
    # 获取yaml文件路径
    yamlPath = os.path.join(curPath, "feelt.yaml")
    # 'a'代表持续写入，‘w’代表覆盖写入
    with open(yamlPath, 'w', encoding='utf-8') as yaml_file:
        yaml.dump(a, yaml_file)


def getsessionid(user):
    # 获取当前脚本所在文件夹路径
    curPath = os.path.dirname(os.path.realpath(__file__))
    # 获取yaml文件路径
    yamlPath = os.path.join(curPath, "feelt.yaml")

    # open方法打开直接读出来
    yaml_file = open(yamlPath, 'r', encoding='utf-8')
    cfg = yaml_file.read()

    d = yaml.load(cfg, Loader=yaml.FullLoader)  # 用load方法转字典
    return d[user]