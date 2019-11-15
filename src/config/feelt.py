import os

import yaml


def getsessionid(user):
    # 获取当前脚本所在文件夹路径
    curPath = os.path.dirname(os.path.realpath(__file__))
    # 获取yaml文件路径
    yamlPath = os.path.join(curPath, "feelt.yaml")

    # open方法打开直接读出来
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()

    d = yaml.load(cfg, Loader=yaml.FullLoader)  # 用load方法转字典
    return d[user]


def updatasessionid(user, yaml_fi=None):
    # 获取当前脚本所在文件夹路径
    curPath = os.path.dirname(os.path.realpath(__file__))
    # 获取yaml文件路径
    yamlPath = os.path.join(curPath, "feelt.yaml")
    with open(yamlPath, 'r', encoding='utf-8') as yaml_file:
        yaml_fi["32419"] = 546456236454566455644564656454654563654564
        yaml.dump(yaml_fi, yaml_file)


updatasessionid(32419)
print(getsessionid(32419))
