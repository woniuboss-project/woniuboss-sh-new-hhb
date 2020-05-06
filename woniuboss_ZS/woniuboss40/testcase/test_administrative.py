
import requests, time
import unittest
from parameterized import parameterized
from werkzeug.wrappers import json

from util.utility import Utility
data_base_path='../config/base.conf'
data_config_path = '../config/testdata.conf'
data_config_info = Utility.get_json(data_config_path)
query_assets_info = Utility.get_excel_to_tuple(data_config_info[6])#查询采购记录
add_assets_info = Utility.get_excel_to_tuple(data_config_info[7])#新增采购记录
addmore_assets_info = Utility.get_excel_to_tuple(data_config_info[8])#批量新增采购记录
modify_assets_info = Utility.get_excel_to_tuple(data_config_info[9])#修改采购记录
query_borlist_info = Utility.get_excel_to_tuple(data_config_info[10])#查询认领记录
add_bor_info = Utility.get_excel_to_tuple(data_config_info[11])#新增认领记录
modify_bor_info = Utility.get_excel_to_tuple(data_config_info[12])#修改认领记录
query_return_info = Utility.get_excel_to_tuple(data_config_info[13])#查询归还记录


class AdministrativeTest(unittest.TestCase):
    @parameterized.expand(query_assets_info)
    def test_administrative(self,url,method,test_data,resp_code,resp_content,expect):

        from common.administrative import Administrative
        query_assets_resp = Administrative().query_assets(url,test_data)
        query_assets_resp_content = query_assets_resp.json()
        # print(query_hr_resp_content)
        print(query_assets_resp_content['totalRow'])
        #通过数据库查询数据的数量
        sql = 'select count(*) from assets;'
        sql_request=Utility.query_all(data_base_path, sql)
        print(sql_request[0][0])
        if  query_assets_resp_content['totalRow'] == sql_request[0][0] :
            actual = 'query-success'
        else:
            actual = 'query-fail'
        self.assertEqual(actual,expect)

    @parameterized.expand(add_assets_info)
    def test_administrative(self, url, method, test_data, resp_code, resp_content, expect):

        # 通过数据库查询数据的数量
        sql = 'select count(*) from assets;'
        sql_request = Utility.query_all(data_base_path, sql)

        from common.administrative import Administrative
        add_assets_resp =Administrative().add_assets(url, test_data)
        sql = 'select count(*) from assets;'
        sql_request1 = Utility.query_all(data_base_path, sql)
        print(add_assets_resp.text)
        if int(sql_request[0][0]) == int(sql_request1[0][0]) - 1:
            actual = 'add-success'
        elif add_assets_resp.text =='AlreayExistCode':
            actual = 'add-alreay'
        else:
            actual = 'add-fail'
        self.assertEqual(actual, expect)

    @parameterized.expand(addmore_assets_info)
    def test_administrative(self, url, method, test_data, resp_code, resp_content, expect):

        # 通过数据库查询数据的数量
        sql = 'select count(*) from assets;'
        sql_request = Utility.query_all(data_base_path, sql)

        from common.administrative import Administrative
        add_assets_resp = Administrative().add_assets(url, test_data)
        # add_hr_resp_content = add_hr_resp.json()
        # print(query_hr_resp_content)
        # print(add_hr_resp_content['totalRow'])
        sql = 'select count(*) from assets;'
        sql_request1 = Utility.query_all(data_base_path, sql)
        print(add_assets_resp.text)
        if int(sql_request[0][0]) == int(sql_request1[0][0]) - 1:
            actual = 'add-success'
        elif add_assets_resp.text == 'AlreayExistCode':
            actual = 'add-alreay'
        else:
            actual = 'add-fail'
        self.assertEqual(actual, expect)

    @parameterized.expand(modify_assets_info)
    def test_administrative(self, url, method, test_data, resp_code, resp_content, expect):

        from common.administrative import Administrative
        modify_assets_resp = Administrative().modify_assets(url, test_data)
        modify_assets_resp_content = modify_assets_resp.text
        # print(modify_hr_resp_content)

        if modify_assets_resp_content == 'success':
            actual = 'modify-success'
        else:
            actual = 'modify-fail'
        self.assertEqual(actual, expect)

    @parameterized.expand(query_borlist_info)
    def test_administrative(self, url, method, test_data, resp_code, resp_content, expect):

        from common.administrative import Administrative
        query_borlist_resp = Administrative().query_assets(url, test_data)
        query_borlist_resp_content = query_borlist_resp.json()
        # print(query_hr_resp_content)
        print(query_borlist_resp_content['totalRow'])
        # 通过数据库查询数据的数量
        sql = 'select count(*) from borrow;'
        sql_request = Utility.query_all(data_base_path, sql)
        print(sql_request[0][0])
        if query_borlist_resp_content['totalRow'] == sql_request[0][0]:
            actual = 'query-success'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, expect)

    @parameterized.expand(add_bor_info)
    def test_administrative(self, url, method, test_data, resp_code, resp_content, expect):

        # 通过数据库查询数据的数量
        sql = 'select count(*) from borrow;'
        sql_request = Utility.query_all(data_base_path, sql)

        from common.administrative import Administrative
        add_assets_resp = Administrative().add_assets(url, test_data)
        sql = 'select count(*) from borrow;'
        sql_request1 = Utility.query_all(data_base_path, sql)
        print(add_assets_resp.text)
        if int(sql_request[0][0]) == int(sql_request1[0][0]) - 1:
            actual = 'add-success'
        elif add_assets_resp.text == 'AlreayExistCode':
            actual = 'add-alreay'
        else:
            actual = 'add-fail'
        self.assertEqual(actual, expect)

    @parameterized.expand(modify_bor_info)
    def test_administrative(self, url, method, test_data, resp_code, resp_content, expect):

        from common.administrative import Administrative
        modify_assets_resp = Administrative().modify_assets(url, test_data)
        modify_assets_resp_content = modify_assets_resp.text
        print(modify_assets_resp_content)

        if modify_assets_resp_content == 'success':
            actual = 'modify-success'
        else:
            actual = 'modify-fail'
        self.assertEqual(actual, expect)

    @parameterized.expand(query_return_info)
    def test_administrative(self, url, method, test_data, resp_code, resp_content, expect):

        from common.administrative import Administrative
        query_return_resp = Administrative().query_assets(url, test_data)
        query_return_resp_content = query_return_resp.json()
        # print(query_hr_resp_content)
        print(query_return_resp_content['totalRow'])
        # 通过数据库查询数据的数量
        sql = 'select count(*) from returns;'
        sql_request = Utility.query_all(data_base_path, sql)
        print(sql_request[0][0])
        if query_return_resp_content['totalRow'] == sql_request[0][0]:
            actual = 'query-success'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, expect)




if __name__ == '__main__':
    unittest.main(verbosity=2)
