import unittest
from parameterized import parameterized
from utils.Utils import Utility
from common.login import Login

test_info = Utility.get_json('..\\config\\testdata.conf')
login_data = Utility.get_excel_to_tuple(test_info[0])

class LoginTest(unittest.TestCase):

    @parameterized.expand(login_data)
    def test_login(self,url,data,expect):
        resp = Login().do_login(url,data)
        content = resp.text
        self.assertEqual(content,expect)