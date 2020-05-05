# -*- coding: utf-8 -*-
import unittest

from parameterized import parameterized

from woniubossUIDDT.lib.login import Login
from woniubossUIDDT.tools.uiti import uiti
from woniubossUIDDT.tools.service import Service

test_info = uiti.get_json('..\\conf\\testdata.conf')
login_infos=uiti.trans_dict_tup(test_info[0])

class loginTest(unittest.TestCase):

    def setUp(self):
        self.driver=Service.get_driver('..\\conf\\base.conf')

    def tearDown(self):
        self.driver.quit()

    @parameterized.expand(login_infos)
    def test_login(self,userName,userPass,checkcode,expect):
        login_info ={'userName':userName,'userPass':userPass,'checkcode':checkcode}
        Login().do_login('..\\conf\\base.conf',self.driver,login_info)
        from selenium.webdriver.common.by import By
        flag= Service.is_element_present(self.driver,By.LINK_TEXT,'注销')
        if flag:
            actual= 'login_pass'
        else:
            actual = 'login_fail'
        self.assertEqual(actual,expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)

