import requests, time
import unittest
from parameterized import parameterized

from util.utility import Utility

data_config_path = '../config/testdata.conf'
data_base_path='../config/base.conf'
data_config_info = Utility.get_json(data_config_path)
query_finance_info = Utility.get_excel_to_tuple(data_config_info[1])

class FinanceTest(unittest.TestCase):
    @parameterized.expand(query_finance_info)
    def test_finance(self,url,method,test_data,resp_code,resp_content,expect):
        print(expect)
        from common.finance import Finance
        query_finance_resp = Finance().query_finance(url,test_data)
        query_finance_resp_content = query_finance_resp.text
        print(query_finance_resp_content)
        sql=''
        Utility.query_all(data_base_path,sql)
        if '"totalRow":3,"pageNumber":1,"firstPage":true,"lastPage":true,"totalPage":1,"pageSize":10' \
            in str(query_finance_resp_content) :
            actual = 'query-success'
        else:
            actual = 'query-fail'
        self.assertEqual(actual,expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)