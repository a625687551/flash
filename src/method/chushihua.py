import requests
import json
requests.packages.urllib3.disable_warnings()    # 禁用安全请求警告
def loginms():
    url = "https://sapi-training.flashexpress.com/ms/api/auth/signin"

    payload = {"login": "10000", "password": "goflasher"}
    headers = {
        "Connection": "keep-alive",
        "Content-Length": "40",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN",
        "Content-Type": "application/json;charset=UTF-8"
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)
    if response.status_code == 200:
        print("登录超级管理员成功")
    return json.loads(response.text)["data"]["session_id"]

def update16966():
    #去掉16966的网点经理和主管的角色
    url = "https://sapi-training.flashexpress.com/ms/api/setting/store/staffs/16966/edit"
    payload = {"id":16966,"company_name":None,"name":"อาทิตยา ปานทองคำ （测试账号）","organization_name":"Testing（北京团队测试用）","organization_id":"TH01010101","organization_type":1, "department_id":None,"department_name":None,"positions_text":"快递员,仓管,网点出纳",\
               "administrative_area":"กรุงเทพ คลองเตย","mobile":"0123456789","email":"","state":1,"state_text":"在职","hire_date":"2018-01-29","leave_date":"2018-04-30","stop_duties_date":None,"job_title_name":"Van Courier","vehicle":0,"vehicle_text":"Bike","formal":1,\
               "formal_text":"编制","formal_list":[{"code":0,"text":"非编制"},{"code":1,"text":"编制"}],"state_list":[{"code":1,"text":"在职"},{"code":2,"text":"离职"},{"code":3,"text":"停职"}],"positions":[1,2,4],"position_category_list":[{"code":1,"text":"快递员"},\
                {"code":2,"text":"仓管"},{"code":3,"text":"网点经理"},{"code":4,"text":"网点出纳"},{"code":0,"text":"分配员"},{"code":18,"text":"网点主管"},{"code":21,"text":"区域经理"},{"code":40,"text":"加班车申请员"}]}
    headers = {
        "Connection": "keep-alive",
        "Content-Length": "40",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN",
        "Content-Type": "application/json;charset=UTF-8",
        "X-MS-SESSION-ID": loginms()
    }
    response = requests.request("post",url,data=json.dumps(payload),headers=headers,verify=False)
    if response.status_code == 200:
        print("修改16966成功")


def updata32419():
    # 把32419设置为网点经理
    url = "http://bi-training.flashexpress.com/v1/staffs/create"

    payload = {
        "id": 8769,
        "staff_info_id": 32419,
        "emp_id": None,
        "name": "网点经理仓管",
        "name_en": None,
        "sex": "0",
        "identity": "4325234534254",
        "mobile": "6525234543",
        "mobile_company": "",
        "email": "3234@flashexpress.com",
        "job_title": "15",
        "sys_store_id": "TH01010101",
        "sys_department_id": "25",
        "formal": "1",
        "company_name_ef": None,
        "state": "1",
        "hire_date": "2019-09-25 00:00:00",
        "leave_date": None,
        "updated_at": "2019-11-12 07:03:06",
        "branch": None,
        "uuid": "5e99c687-d8bb-4037-b740-0b9a703dbf44",
        "hire_date_origin": None,
        "is_sub_staff": 0,
        "payment_state": 1,
        "leave_reason": "",
        "creater": 17245,
        "is_auto_system_change": 0,
        "bank_no": "",
        "payment_markup": None,
        "stop_duties_date": None,
        "personal_email": None,
        "oil_card_deposit": 0,
        "bank_type": 2,
        "stop_duties_count": 0,
        "wait_leave_state": 0,
        "health_status": 2,
        "disability_certificate": "223WDSDSD",
        "vehicle_source": 0,
        "vehicle_use_date": None,
        "staff_type": 1,
        "bank_no_name": "45 45",
        "bank_name": "TMB",
        "staff_car_type": "",
        "staff_car_no": "",
        "driver_license": "",
        "outsourcing_type": "",
        "position_category": [2, 3],
        "position_category_name": "仓管  网点经理  ",
        "job_title_name": "Branch Manager",
        "sys_department_name": "Hub",
        "sys_store_name": "Testing（北京团队测试用）",
        "manager": "16882",
        "manager_name": "นาย พีรภัทร ชุ่มอินทร์จักร์",
        "manager_state": "1",
        "sys_district": "0",
        "email_state": 0,
        "email_suffix": 1,
        "area_manager_strore": [],
        "profile_object_key": None
    }
    headers = {
        "Content-Length": "1406",
        "Accept": "application/json, text/plain, */*",
        "Authorization": "Bearer ZDk4MTQxYTU4YTY5NWQ5ZTcxMzAxOTcxMTg1NjIyNjk=",
        "Content-Type": "application/json;charset=UTF-8"
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)
    if response.status_code == 200:
        print("设置32419为网点经理成功")


def updata32417():
    # 把32417设置为仓管
    url = "http://bi-training.flashexpress.com/v1/staffs/create"

    payload = {
        "id": 8766,
        "staff_info_id": 32416,
        "emp_id": None,
        "name": "仓管",
        "name_en": None,
        "sex": "0",
        "identity": "4325234534254",
        "mobile": "4358234543",
        "mobile_company": "0988887654",
        "email": "",
        "job_title": "165",
        "sys_store_id": "TH01010101",
        "sys_department_id": "4",
        "formal": "1",
        "company_name_ef": None,
        "state": "1",
        "hire_date": "2019-09-25 00:00:00",
        "leave_date": None,
        "updated_at": "2019-11-08 14:48:44",
        "branch": None,
        "uuid": "9f168a64-fc06-4d11-961d-130bd1f6f8f8",
        "hire_date_origin": None,
        "is_sub_staff": 0,
        "payment_state": 1,
        "leave_reason": "",
        "creater": 17245,
        "is_auto_system_change": 0,
        "bank_no": "",
        "payment_markup": None,
        "stop_duties_date": None,
        "personal_email": None,
        "oil_card_deposit": 0,
        "bank_type": 2,
        "stop_duties_count": 0,
        "wait_leave_state": 0,
        "health_status": 1,
        "disability_certificate": "",
        "vehicle_source": 0,
        "vehicle_use_date": None,
        "staff_type": 1,
        "bank_no_name": "45 45",
        "bank_name": "TMB",
        "staff_car_type": "",
        "staff_car_no": "",
        "driver_license": "",
        "outsourcing_type": "",
        "position_category": [2],
        "position_category_name": "分配员  仓管  ",
        "job_title_name": "Network and Transportation Manager",
        "sys_department_name": "Operations",
        "sys_store_name": "Testing（北京团队测试用）",
        "manager": "32419",
        "manager_name": "นาย วิเชษฐ์ มาสุข",
        "manager_state": "2",
        "sys_district": "TH070901",
        "email_state": "-1",
        "email_suffix": "-1",
        "area_manager_strore": [],
        "profile_object_key": None
    }
    headers = {
        "Content-Length": "1406",
        "Accept": "application/json, text/plain, */*",
        "Authorization": "Bearer ZDk4MTQxYTU4YTY5NWQ5ZTcxMzAxOTcxMTg1NjIyNjk=",
        "Content-Type": "application/json;charset=UTF-8"
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)
    if response.status_code == 200:
        print("设置32416仓管成功")
def chushihua_traning_zhanghao():
    update16966()
    updata32419()
    updata32417()
    print("初始化账号成功")
    return None