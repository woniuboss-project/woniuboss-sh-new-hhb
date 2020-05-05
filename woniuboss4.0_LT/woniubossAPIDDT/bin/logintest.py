# -*- coding: utf-8 -*-
import unittest

from parameterized import parameterized

from woniubossAPIDDT.lib.login import Login
from woniubossAPIDDT.tools.service import Service
from woniubossAPIDDT.tools.uiti import uiti

test_info = uiti.get_json('..\\conf\\testdata.conf')
login_infos=uiti.trans_dict_tup(test_info[0])

class loginTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand(login_infos)
    def test_login(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        login_info ={'userName':DATA['userName'],'userPass':DATA['userPass'],'checkcode':DATA['checkcode']}
        resp=Login('..\\conf\\base.conf').do_login(URL,login_info)
        flag=uiti.assert_equal(str(resp.text),CONTENT)
        if flag:
            if str(resp.text)=='success':
                actual='login_pass'
            else:
                actual = 'login_fail'
        else:
            print('响应正文不正确')
        self.assertEqual(expect,actual)


if __name__ == '__main__':
    unittest.main(verbosity=2)

