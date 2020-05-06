

import requests, time
import unittest
from parameterized import parameterized
from werkzeug.wrappers import json

from util.utility import Utility
data_base_path='../config/base.conf'
data_config_path = '../config/testdata.conf'
data_config_info = Utility.get_json(data_config_path)
query_hr_info = Utility.get_excel_to_tuple(data_config_info[2])
add_hr_info = Utility.get_excel_to_tuple(data_config_info[3])
modify_hr_info = Utility.get_excel_to_tuple(data_config_info[4])
query_attendance_info = Utility.get_excel_to_tuple(data_config_info[5])

class HrTest(unittest.TestCase):
    @parameterized.expand(query_hr_info)
    def test_hr(self,url,method,test_data,resp_code,resp_content,expect):

        from common.HR import HR
        query_hr_resp = HR().query_HR(url,test_data)
        query_hr_resp_content = query_hr_resp.json()
        # print(query_hr_resp_content)
        print(query_hr_resp_content['totalRow'])
        #通过数据库查询数据的数量
        sql = 'select count(*) from employee;'
        sql_request=Utility.query_all(data_base_path, sql)
        print(sql_request[0][0])
        if  query_hr_resp_content['totalRow'] == sql_request[0][0] :
            actual = 'query-success'
        else:
            actual = 'query-fail'
        self.assertEqual(actual,expect)

    @parameterized.expand(add_hr_info)
    def test_hr(self, url, method, test_data, resp_code, resp_content, expect):

        # 通过数据库查询数据的数量
        sql = 'select count(*) from employee;'
        sql_request = Utility.query_all(data_base_path, sql)
        #新增员工
        from common.HR import HR
        add_hr_resp = HR().add_HR(url, test_data)
        # add_hr_resp_content = add_hr_resp.json()
        # print(query_hr_resp_content)
        # print(add_hr_resp_content['totalRow'])
        sql = 'select count(*) from employee;'
        sql_request1 = Utility.query_all(data_base_path, sql)

        if int(sql_request[0][0]) == int(sql_request1[0][0]) - 1:
            actual = 'add-success'
        else:
            actual = 'add-fail'
        self.assertEqual(actual, expect)

    @parameterized.expand(modify_hr_info)
    def test_hr(self, url, method, test_data, resp_code, resp_content, expect):

        from common.HR import HR
        modify_hr_resp = HR().modify_HR(url, test_data)
        modify_hr_resp_content = modify_hr_resp.text
        # print(modify_hr_resp_content)

        if modify_hr_resp_content == 'success':
            actual = 'modify-success'
        else:
            actual = 'modify-fail'
        self.assertEqual(actual, expect)

    @parameterized.expand(query_attendance_info)
    def test_hr(self, url, method, test_data, resp_code, resp_content, expect):

        from common.HR import HR
        query_hr_resp = HR().query_HR(url, test_data)
        query_attendance_resp_content = query_hr_resp.json()
        # print(query_hr_resp_content)
        print(query_attendance_resp_content['totalRow'])
        # 通过数据库查询数据的数量
        sql = 'select count(*) from attendance;'
        sql_request = Utility.query_all(data_base_path, sql)
        print(sql_request[0][0])
        if query_attendance_resp_content['totalRow'] == sql_request[0][0]:
            actual = 'query-success'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)