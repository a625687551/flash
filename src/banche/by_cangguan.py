import requests
import json

from src.method.chushihua import chushihua_traning_zhanghao

requests.packages.urllib3.disable_warnings()    # 禁用安全请求警告
chushihua_traning_zhanghao()


