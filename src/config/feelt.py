import os

import yaml


def read_SESSION_yaml_file(sessionid32416):
    current_path = os.path.abspath(os.path.dirname(__file__))
    print(current_path)
    print(current_path + 'feelt.yaml')
    with open(current_path + '/feelt.yaml', 'r', encoding='utf-8') as feelt:
        fi = feelt.read()
        temp = yaml.load(fi, Loader=yaml.FullLoader)
        print(temp)
        return temp[sessionid32416]

read_SESSION_yaml_file("sessionid32416")

