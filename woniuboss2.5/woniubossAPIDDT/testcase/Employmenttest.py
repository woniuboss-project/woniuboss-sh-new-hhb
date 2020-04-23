#-*- coding:utf-8 -*-
# author JTT
# @Time:2020/4/6 17:49
import  unittest
from parameterized import parameterized
import json
from common.Employment import employment
from tools.uiti import uiti

test_info=uiti.get_json('..\\conf\\jtttestdata.conf')
decrypt_infos=uiti.trans_dict_tup(test_info[0])
select_infos=uiti.trans_dict_tup(test_info[1])
record_skill_interview_infos=uiti.trans_dict_tup(test_info[2])

class EmploymentTest(unittest.TestCase):

    def setUp(self):
        print('*******start******')

    def tearDown(self):
        print('*******end*******')

    #测试解密
    @parameterized.expand(decrypt_infos)
    def test_decrypt(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        decrypt_info={'vp':DATA['vp']}
        resp = employment('..\\conf\\base.conf').decrypt(URL,decrypt_info)
        flag = uiti.assert_equal(resp.text,CONTENT)
        if flag:
            actual = 'vp_pass'
        else:
            actual = 'vp_fail'
        self.assertEqual(actual,expect)

    #测试查询学员技术面试功能
    @parameterized.expand(select_infos)
    def test_select(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        select_info = {'pageSize':DATA['pageSize'],'pageIndex':DATA['pageIndex']}
        resp = employment('..\\conf\\base.conf').decrypt(URL, select_info)
        result=len(resp.json()['list'])
        expect=int(expect)
        self.assertEqual(expect,result)
        



     




if __name__ == '__main__':
    unittest.main(verbosity=2)

