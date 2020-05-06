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


class hrTest:

    def setUp(self):
        driver=Service.get_driver('..\\conf\\base.conf')
        login_info = {'userName': 'WNCD000', 'userPass': 'woniu123', 'checkcode':'0000'}
        Login().do_login('..\\conf\\base.conf', driver, login_info)

        time.sleep(3)

        driver.find_element_by_css_selector('div.panel:nth-child(12) > div:nth-child(1) > a:nth-child(1)').click()

        time.sleep(3)
        driver.find_element_by_css_selector(
            '#list-8 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)').click()
        time.sleep(3)

        number = driver.find_element_by_xpath('/html/body/div[9]/div[2]/div[2]/div[2]/div[4]/div[1]/span[1]')

        print(number.text)
        eles = driver.find_elements_by_class_name('page-number')
        print(eles)
        num = 0
        totalcount = len(eles)
        print(totalcount + 1)
        for i in range(0, totalcount + 1):
            # eles[i].find_elements_by_tag_name('a').click()
            # print(eles[i])
            driver.find_element_by_xpath("//ul[@class='pagination']/li[%d+2]/a[contains(@href,'#')]" % i).click()
            time.sleep(5)
            newnum = len(driver.find_elements_by_xpath('//*[@id="employee-table"]/tbody/tr'))
            num = num + newnum
        print(num)
        driver.quit()




if __name__ == '__main__':
    hrTest().setUp()
