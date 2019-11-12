import requests
import json
requests.packages.urllib3.disable_warnings()    # 禁用安全请求警告



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
        'Content-Length': "1406",
        'Accept': "application/json, text/plain, */*",
        'Authorization': "Bearer ZDk4MTQxYTU4YTY5NWQ5ZTcxMzAxOTcxMTg1NjIyNjk=",
        'Content-Type': "application/json;charset=UTF-8"
        }

response = requests.request("POST", url, data=json.dumps(payload), headers=headers,  verify=False)

print(response.text)