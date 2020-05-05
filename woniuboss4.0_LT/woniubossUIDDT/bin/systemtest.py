import time
import unittest

from parameterized import parameterized


from woniubossUIDDT.lib.login import Login
from woniubossUIDDT.lib.system_manage import Use_manage
from woniubossUIDDT.tools.service import Service
from woniubossUIDDT.tools.uiti import uiti
login_info ={'userName':'WNCD000','userPass':'woniu123','checkcode':'0000'}
test_info = uiti.get_json('..\\conf\\testdata.conf')
query_infos=uiti.trans_dict_tup(test_info[1])
edit_infos=uiti.trans_dict_tup(test_info[2])
reset_infos=uiti.trans_dict_tup(test_info[3])
roleQuery_infos=uiti.trans_dict_tup(test_info[4])
add_infos = uiti.trans_dict_tup(test_info[5])
editRole_infos = uiti.trans_dict_tup(test_info[6])
meniu_infos = uiti.trans_dict_tup(test_info[7])
dict_infos = uiti.trans_dict_tup(test_info[8])
dict_addInfos = uiti.trans_dict_tup(test_info[9])
dict_editInfos = uiti.trans_dict_tup(test_info[10])
detail_infos = uiti.trans_dict_tup(test_info[11])
class userTest(unittest.TestCase):

    def setUp(self):
        self.driver=Service.get_driver('..\\conf\\base.conf')
        from selenium.common.exceptions import NoSuchElementException
        try:
            Login().do_login('..\\conf\\base.conf',self.driver,login_info)
            self.driver.implicitly_wait(15)
        except NoSuchElementException as e:
            return False

    def tearDown(self):
        self.driver.quit()

    @parameterized.expand(query_infos)
    def test_query(self,name,userName,expect):
        user_info ={'name':name,'userName':userName}
        Use_manage().do_query(self.driver,user_info)
        time.sleep(3)
        content = self.driver.find_element_by_css_selector('.pagination-info').text
        if '总共' in content:
            con = content.split(' ')[5]
            #print(con)
            if user_info['name'] == '' and user_info['userName'] == '':
                sql = 'SELECT COUNT(*) FROM system_user WHERE passwd_status = 1 AND passwd2_status = 1;'
                result = uiti.inquiry_one('..\\conf\\base.conf',sql)
                #print(result)
                if int(con) == result[0]:
                    actual = 'query ok'
                else:
                    actual = 'query fail'
            elif int(con) == 1:
                actual = 'query ok'
            else:
                actual = 'query fail'
        else:
            actual = 'query fail'
        self.assertEqual(actual,expect)
     
    @parameterized.expand(edit_infos)
    def test_edit(self,index,content, expect):
        edit_info = {'index': index, 'content': content}
        Use_manage().do_edit(self.driver, edit_info)
        result = self.driver.find_element_by_css_selector('.bootbox-body').text
        if '修改成功' in result:
            actual = 'edit ok'
        else:
            actual = 'edit fail'
        self.assertEqual(actual,expect)
    
    @parameterized.expand(reset_infos)
    def test_reset(self, index,passwd, expect):
        reset_info = {'index': index, 'passwd': passwd}
        Use_manage().do_reset_passwd(self.driver, reset_info)
        result = self.driver.find_element_by_css_selector('.bootbox-body').text
        if '重置成功' in result:
            actual = 'reset ok'
        else:
            actual = 'reset fail'
        self.assertEqual(actual, expect)
    
    @parameterized.expand(roleQuery_infos)
    def test_roleQuery(self,role_name, expect):
        role_info = {'role_name': role_name}
        Use_manage().do_role_query(self.driver, role_info)
        content = self.driver.find_element_by_css_selector('.pagination-info').text
        if '总共' in content:
            con = content.split(' ')[5]
            if role_info['role_name'] == '':
                sql = 'SELECT COUNT(*) FROM system_role;'
                result = uiti.inquiry_one('..\\conf\\base.conf', sql)
                # print(result)
                if int(con) == result[0]:
                    actual = 'query ok'
                else:
                    actual = 'query fail'
            elif int(con) == 1:
                actual = 'query ok'
            else:
                actual = 'query fail'
        else:
            actual = 'query fail'
        self.assertEqual(actual, expect)
    
    @parameterized.expand(add_infos)
    def test_add(self, roleName,desc,expect):
        sql = 'SELECT COUNT(*) FROM system_role;'
        old_result = uiti.inquiry_one('..\\conf\\base.conf', sql)
        add_info = {'roleName':roleName,'desc':desc }
        Use_manage().do_add(self.driver, add_info)
        new_result = uiti.inquiry_one('..\\conf\\base.conf', sql)
        result = new_result[0] - old_result[0]
        if result == 1:
            actual = 'add ok'
        else:
            actual = 'add fail'
        self.assertEqual(actual,expect)
    
    @parameterized.expand(editRole_infos)
    def test_editRole(self, roleName, desc, expect):
        editRole_info = {'roleName': roleName, 'desc': desc}
        Use_manage().do_edit_role(self.driver, editRole_info)
        result = self.driver.find_element_by_css_selector('.bootbox-body').text
        if '修改成功' in result:
            actual = 'edit ok'
        else:
            actual = 'edit fail'
        self.assertEqual(actual, expect)

    @parameterized.expand(meniu_infos)
    def test_meniu(self,num, roleName, path,mark,desc, expect):
        edit_info = {'num':num,'roleName': roleName, 'path':path,'mark':mark,'desc': desc}
        Use_manage().do_meniu_edit(self.driver, edit_info)
        if edit_info['num'] == '2':
            content = self.driver.find_element_by_xpath('//table[@id="res-table"]/tbody/tr[2]/td[3]').text
            if '/resource' in content:
                actual = 'edit ok'
        elif edit_info['num'] == '4':
            content = self.driver.find_element_by_xpath('//table[@id="res-table"]/tbody/tr[4]/td[1]').text
            if '人事' in content:
                actual = 'edit ok'
            else:
                actual = 'edit fail'
        elif edit_info['num'] == '3':
            content = self.driver.find_element_by_xpath('//table[@id="res-table"]/tbody/tr[3]/td[3]').text
            if 'null' in content:
                actual = 'edit ok'
        elif edit_info['num'] == '1':
            content = self.driver.find_element_by_xpath('//table[@id="res-table"]/tbody/tr[1]/td[2]').text
            if content == '-':
                actual = 'edit ok'
        self.assertEqual(actual,expect)
    
    @parameterized.expand(dict_infos)
    def test_dict(self, dict_name, expect):
        dict_info = {'dict_name': dict_name}
        Use_manage().do_dict_query(self.driver, dict_info)
        content = self.driver.find_element_by_css_selector('.pagination-info').text
        if '总共' in content:
            con = content.split(' ')[5]
            if dict_info['dict_name'] == '' :
                sql = 'SELECT COUNT(*) FROM dictionary_type;'
                result = uiti.inquiry_one('..\\conf\\base.conf', sql)
                if int(con) == result[0]:
                    actual = 'query ok'
                else:
                    actual = 'query fail'
            elif int(con) == 1:
                actual = 'query ok'
            else:
                actual = 'query fail'
        else:
            actual = 'query fail'
        self.assertEqual(actual, expect)
    
    @parameterized.expand(dict_addInfos)
    def test_dict_add(self,dict_key,dict_value,num, desc, expect):
        sql = 'SELECT count(*) FROM dictionary_data;'
        old_result = uiti.inquiry_one('..\\conf\\base.conf', sql)
        dict_add_info = {'dict_key': dict_key, 'dict_value': dict_value,'num':num,'desc':desc}
        Use_manage().do_dict_add(self.driver, dict_add_info)
        new_result = uiti.inquiry_one('..\\conf\\base.conf', sql)
        result = new_result[0] - old_result[0]
        if result == 1:
            actual = 'add ok'
        else:
            actual = 'add fail'
        self.assertEqual(actual, expect)
    
    @parameterized.expand(dict_editInfos)
    def test_dict_edit(self,dict_name,desc, expect):
        edit_info = {'dict_name': dict_name, 'desc': desc}
        Use_manage().do_dict_edit(self.driver, edit_info)
        result = self.driver.find_element_by_css_selector('.bootbox-body').text
        if '修改成功' in result:
            actual = 'edit ok'
        else:
            actual = 'edit fail'
        self.assertEqual(actual, expect)

    @parameterized.expand(detail_infos)
    def test_detal(self,dict_name,tag,num,desc,expect):
        detail_info = {'dict_name': dict_name, 'tag': tag,'num':num,'desc':desc}
        Use_manage().do_detail(self.driver, detail_info)
        content = self.driver.find_element_by_css_selector(
            '#dict-detail-table > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(2)').text
        result = self.driver.find_element_by_css_selector(
            '#dict-detail-table > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(4)').text

        if 'A4纸' in content:
            actual = 'edit ok'
        elif '其他' in content:
            actual = 'edit ok'
        elif '-' in result:
            actual = 'edit ok'
        self.assertEqual(actual,expect)




if __name__ == '__main__':
    unittest.main(verbosity=2)