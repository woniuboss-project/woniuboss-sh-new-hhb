import time
import unittest

from parameterized import parameterized
from selenium.webdriver.common.by import By

from lib.hr import Hr
from lib.login import Login
from tools.uiti import uiti
from tools.service import Service


base_path='..\\conf\\base.conf'
test_info = uiti.get_json('..\\conf\\testdata.conf')
query_hr_infos=uiti.trans_dict_tup(test_info[1])
add_hr_infos=uiti.trans_dict_tup(test_info[2])

class hrTest(unittest.TestCase):

    def setUp(self):
        self.driver=Service.get_driver('..\\conf\\base.conf')
        login_info = {'userName': 'WNCD000', 'userPass': 'woniu123', 'checkcode':'0000'}
        Login().do_login('..\\conf\\base.conf', self.driver, login_info)

    def tearDown(self):
        self.driver.quit()

    @parameterized.expand(query_hr_infos)
    def test_query_hr(self,regionSel,department_id,last_status,empName,expect):
        hr_info ={'regionSel':regionSel,'department_id':department_id,'last_status':last_status,'empName':empName}
        Hr().select_employees(self.driver,hr_info)
        sql = 'select count(*) from employee where region_id = 1'
        result=uiti.inquiry_all(base_path,sql)
        number = self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/div[2]/div[2]/div[4]/div[1]/span[2]/span/button/span[1]')

        print(number.text)
        eles = self.driver.find_elements_by_class_name('page-number')
        print(eles)
        num = 0
        totalcount = len(eles)
        print(totalcount + 1)
        for i in range(0, totalcount + 1):
            # eles[i].find_elements_by_tag_name('a').click()
            # print(eles[i])
            self.driver.find_element_by_xpath("//ul[@class='pagination']/li[%d+2]/a[contains(@href,'#')]" % i).click()
            time.sleep(5)
            newnum = len(self.driver.find_elements_by_xpath('//*[@id="employee-table"]/tbody/tr'))
            num = num + newnum

        if num == result[0][0]:
            actual = 'query_pass'
        else:
            actual = 'query_fail'
        self.assertEqual(actual, expect)

    @parameterized.expand(add_hr_infos)
    def test_add_hr(self, region_id, department_id, position, employee_name, sex,entry_time,
                    tel,email,qq,education,university,major,address,source,cardnum,identity,
                    birthday,birthday_type,emergency_contact,emergency_tel,emegency_relation,
                    work_id,expect):
        hr_info={'region_id':region_id,'department_id':department_id,'position':position,'employee_name':employee_name,
                 'sex':sex,'entry_time':entry_time,'tel':tel,'email':email,'qq':qq,'education':education,'university':university,
                 'major':major,'address':address,'source':source,'cardnum':cardnum,'identity':identity,'birthday':birthday,
                 'birthday_type':birthday_type,'emergency_contact':emergency_contact,'emergency_tel':emergency_tel,
                 'emegency_relation':emegency_relation,'work_id':work_id}

        sql = 'select count(*) from employee '
        result = uiti.inquiry_all(base_path, sql)
        print(result)
        Hr().add_employess(self.driver,hr_info)

        result1 = uiti.inquiry_all(base_path, sql)
        print(result1)
        if result != result1:
            actual = 'add_pass'
        else:
            actual = 'add_fail'
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
