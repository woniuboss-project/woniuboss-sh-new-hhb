# -*- coding: utf-8 -*-
from selenium import webdriver

from woniubossUIDDT.tools.uiti import uiti


class Service:

    #生成driver
    @classmethod
    def get_driver(cls,base_path):
        content =uiti.get_json(base_path)
        driver =getattr(webdriver,content['BROWSER'])()
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver

    #打开页面
    @classmethod
    def open_page(cls,base_path,driver):
        content=uiti.get_json(base_path)
        URL='%s://%s:%s/%s'%(content['PROTOCOL'],content['HOST'],content['PORT'],content['AURL'])
        driver.get(URL)

    #生成cookie
    @classmethod
    def miss_login(cls,driver,base_path):

        cls.open_page(driver, base_path)
        # 通过字典方式传递cookie信息

        contents = uiti.get_json(base_path)
        print(contents)
        driver.add_cookie({'name': 'userName', 'value': contents['username']})
        driver.add_cookie({'name': 'userPass', 'value': contents['password']})
        #driver.add_cookie({'name': '_jfinal_captcha', 'value': 'bd376432f81e4fc48c4063ec61bfd6b1'})
        #driver.add_cookie({'name': 'JSESSIONID', 'value': '3FE05CA43FFF846FA16DDED3B34A445B'})
        #driver.add_cookie({'name': 'token', 'value': '59D737296F85143ED98BD44C499DF5AE'})
        #driver.add_cookie({'name': 'workId', 'value': 'WNCD000'})
        #driver.implicitly_wait(5)
        #driver.refresh()
        cls.open_page(driver, base_path)
    #点击 清空 输入
    @classmethod
    def input(cls,ele,value):
        ele.click()
        ele.clear()
        ele.send_keys(value)

    #判断页面上是否有元素
    @classmethod
    def is_element_present(cls,driver,how,what):
        from selenium.common.exceptions import NoSuchElementException
        try:
            driver.find_element(by=how,value=what)
        except NoSuchElementException as e:
            return False
        return True




if __name__ == '__main__':
    Service.open_page('..\\conf\\base.conf')