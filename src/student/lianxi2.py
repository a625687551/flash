import requests
import json
import pytest

from src.hris.test_1login import test_login
####################################################
url = 'http://hr-api-tra.flashexpress.com/sysList/getSysList'
prams = {
    "type_code": "getDepartmentList"
}
headers = {
    'X-FLE-SESSION-ID': test_login()
}
response = requests.post(url=url, data=prams, headers=headers)
#print(json.loads(response.text))
print('data' in json.loads(response.text) )










##############################################
print(response.text)