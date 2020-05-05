import random
import time



from woniubossUIDDT.tools.service import Service


class Use_manage:

    def click_system(self,driver):
        ele = driver.find_element_by_partial_link_text('系统管理')
        ele.click()

    def click_user(self,driver):
        ele = driver.find_element_by_partial_link_text('用户管理')
        ele.click()

    def input_name(self,driver,value):
        ele = driver.find_element_by_name('empName')
        Service.input(ele,value)

    def input_userName(self,driver,value):
        ele = driver.find_element_by_name('userName')
        Service.input(ele,value)

    def click_query(self,driver):
        ele = driver.find_element_by_css_selector('button.btn:nth-child(5)')
        ele.click()

    def do_query(self,driver,user_info):
        self.click_system(driver)
        self.click_user(driver)
        driver.implicitly_wait(5)
        self.input_name(driver,user_info['name'])
        self.input_userName(driver,user_info['userName'])
        self.click_query(driver)
        time.sleep(3)

    def click_random_edit(self,driver):
        num = random.randint(1,10)
        ele = driver.find_element_by_xpath(
            f'//table[@id="user-table"]/tbody/tr[{num}]/td[8]/button[2]')
        driver.implicitly_wait(4)
        ele.click()

    def select_statue(self,driver,index):
        ele = driver.find_element_by_name('user.status')
        from selenium.webdriver.support.select import Select
        Select(ele).select_by_index(index)

    def input_remark(self,driver,content):
        ele = driver.find_element_by_name('user.des')
        Service.input(ele,content)

    def click_save(self,driver):
        ele = driver.find_element_by_id('saveSetUser')
        ele.click()

    def do_edit(self,driver,edit_info):
        self.click_system(driver)
        self.click_user(driver)
        driver.implicitly_wait(5)
        self.click_random_edit(driver)
        self.select_statue(driver,edit_info['index'])
        self.input_remark(driver,edit_info['content'])
        self.click_save(driver)
        time.sleep(3)

    def click_random_passwd(self, driver):
        num = random.randint(1, 10)
        ele = driver.find_element_by_xpath(
            f'//table[@id="user-table"]/tbody/tr[{num}]/td[8]/button[3]')
        driver.implicitly_wait(4)
        ele.click()

    def select_type(self,driver,index):
        ele = driver.find_element_by_name('pwdType')
        from selenium.webdriver.support.select import Select
        Select(ele).select_by_index(index)

    def input_passwd(self,driver,passwd):
        ele = driver.find_element_by_name('pwd')
        Service.input(ele,passwd)

    def click_commit(self,driver):
        ele = driver.find_element_by_id('saveReset')
        ele.click()


    def do_reset_passwd(self,driver,reset_info):
        self.click_system(driver)
        self.click_user(driver)
        driver.implicitly_wait(5)
        self.click_random_passwd(driver)
        self.select_type(driver,reset_info['index'])
        self.input_passwd(driver,reset_info['passwd'])
        self.click_commit(driver)
        time.sleep(3)

    def click_role(self,driver):
        ele = driver.find_element_by_partial_link_text('角色管理')
        ele.click()

    def input_role(self,driver,roleName):
        ele = driver.find_element_by_name('role_name')
        Service.input(ele,roleName)

    def click_query_button(self,driver):
        ele = driver.find_element_by_css_selector('.col-lg-12 > button:nth-child(2)')
        ele.click()

    def do_role_query(self, driver, role_info):
        self.click_system(driver)
        self.click_role(driver)
        driver.implicitly_wait(5)
        self.input_role(driver, role_info['role_name'])
        self.click_query_button(driver)
        time.sleep(3)

    def click_add(self,driver):
        ele = driver.find_element_by_css_selector('div.pull-right:nth-child(3) > button:nth-child(1)')
        ele.click()

    def input_add_role(self,driver,roleName):
        ele = driver.find_element_by_css_selector('#addRole-form > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele,roleName)

    def input_add_desc(self,driver,desc):
        ele = driver.find_element_by_css_selector('#addRole-form > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > textarea:nth-child(2)')
        Service.input(ele,desc)

    def click_save_button(self,driver):
        ele = driver.find_element_by_id('saveAddRole')
        ele.click()

    def click_confirm(self,driver):
        ele = driver.find_element_by_css_selector('.bootbox > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)')
        ele.click()

    def do_add(self,driver,add_info):
        self.click_system(driver)
        self.click_role(driver)
        driver.implicitly_wait(5)
        self.click_add(driver)
        self.input_add_role(driver,add_info['roleName'])
        self.input_add_desc(driver,add_info['desc'])
        self.click_save_button(driver)
        time.sleep(2)
        self.click_confirm(driver)
        time.sleep(2)

    def click_edit(self,driver):
        num = random.randint(1, 10)
        ele = driver.find_element_by_xpath(
            f'//table[@id="role-table"]/tbody/tr[{num}]/td[6]/button[2]')
        driver.implicitly_wait(4)
        ele.click()

    def input_edit_role(self,driver,roleName):
        ele = driver.find_element_by_css_selector('#editRole-form > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele,roleName)

    def input_edit_desc(self,driver,desc):
        ele = driver.find_element_by_css_selector('#editRole-form > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > textarea:nth-child(2)')
        Service.input(ele,desc)

    def click_save_edit(self,driver):
        ele = driver.find_element_by_id('saveEidtRole')
        ele.click()

    def do_edit_role(self, driver, editRole_info):
        self.click_system(driver)
        self.click_role(driver)
        driver.implicitly_wait(5)
        self.click_edit(driver)
        self.input_edit_role(driver, editRole_info['roleName'])
        self.input_edit_desc(driver, editRole_info['desc'])
        self.click_save_edit(driver)
        time.sleep(2)

    def click_meniu(self,driver):
        ele = driver.find_element_by_partial_link_text('菜单管理')
        ele.click()

    def click_single_edit(self, driver,num):
        ele = driver.find_element_by_xpath(
            f'//table[@id="res-table"]/tbody/tr[{num}]/td[6]/button')
        driver.implicitly_wait(4)
        ele.click()

    def input_role_name(self,driver,roleName):
        ele = driver.find_element_by_css_selector('#editRes-form > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele,roleName)

    def input_path(self,driver,path):
        ele = driver.find_element_by_css_selector('#editRes-form > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele,path)

    def input_power(self,driver,mark):
        ele = driver.find_element_by_css_selector('#editRes-form > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele,mark)

    def input_meniu_desc(self,driver,desc):
        ele = driver.find_element_by_css_selector('div.row:nth-child(5) > div:nth-child(1) > textarea:nth-child(2)')
        Service.input(ele,desc)

    def click_save_bto(self,driver):
        ele = driver.find_element_by_id('saveEditRes')
        ele.click()

    def click_edit_button(self,driver):
        ele = driver.find_element_by_xpath('/html/body/div[12]/div/div/div[3]/button')
        ele.click()

    def do_meniu_edit(self,driver,edit_info):
        self.click_system(driver)
        self.click_meniu(driver)
        driver.implicitly_wait(3)
        self.click_single_edit(driver,edit_info['num'])
        self.input_role_name(driver,edit_info['roleName'])
        self.input_path(driver,edit_info['path'])
        self.input_power(driver,edit_info['mark'])
        self.input_meniu_desc(driver,edit_info['desc'])
        self.click_save_bto(driver)
        time.sleep(4)
        self.click_edit_button(driver)
        time.sleep(5)

    def click_dict(self,driver):
        ele = driver.find_element_by_partial_link_text('字典管理')
        ele.click()

    def input_dict_name(self,driver,dict_name):
        ele = driver.find_element_by_name('dict_typename')
        Service.input(ele,dict_name)

    def click_dict_query(self,driver):
        ele = driver.find_element_by_css_selector('#queryArea > button:nth-child(2)')
        ele.click()

    def do_dict_query(self,driver,dict_info):
        self.click_system(driver)
        self.click_dict(driver)
        driver.implicitly_wait(3)
        self.input_dict_name(driver,dict_info['dict_name'])
        self.click_dict_query(driver)
        time.sleep(3)

    def click_dict_add(self,driver):
        ele = driver.find_element_by_css_selector('#dict-type-table > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(6) > button:nth-child(1)')
        ele.click()

    def input_key(self,driver,dict_key):
        ele = driver.find_element_by_css_selector('#addOption-form > div:nth-child(3) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele,dict_key)

    def input_value(self,driver,dict_value):
        ele = driver.find_element_by_css_selector('#addOption-form > div:nth-child(3) > div:nth-child(2) > input:nth-child(2)')
        Service.input(ele,dict_value)

    def input_num(self,driver,num):
        ele = driver.find_element_by_css_selector('#addOption-form > div:nth-child(4) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele,num)

    def input_dict_desc(self,driver,desc):
        ele = driver.find_element_by_css_selector('#addOption-form > div:nth-child(5) > div:nth-child(1) > textarea:nth-child(2)')
        Service.input(ele,desc)

    def click_dict_save(self,driver):
        ele = driver.find_element_by_css_selector('#addOption-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)')
        ele.click()

    def click_dict_confirm(self,driver):
        ele = driver.find_element_by_css_selector('.bootbox > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)')
        ele.click()



    def do_dict_add(self,driver,dict_add_info):
        self.click_system(driver)
        self.click_dict(driver)
        driver.implicitly_wait(3)
        self.click_dict_add(driver)
        driver.implicitly_wait(2)
        self.input_key(driver,dict_add_info['dict_key'])
        self.input_value(driver,dict_add_info['dict_value'])
        self.input_num(driver,dict_add_info['num'])
        self.input_dict_desc(driver,dict_add_info['desc'])
        self.click_dict_save(driver)
        time.sleep(3)
        self.click_dict_confirm(driver)

    def click_dict_edit(self,driver):
        ele = driver.find_element_by_css_selector('#dict-type-table > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(6) > button:nth-child(2)')
        ele.click()

    def input_dict_edit_name(self,driver,dict_name):
        ele = driver.find_element_by_name('dt.dict_typename')
        Service.input(ele, dict_name)

    def input_dict_edit_desc(self,driver,desc):
        ele = driver.find_element_by_css_selector('#editType-form > div:nth-child(4) > div:nth-child(1) > textarea:nth-child(2)')
        Service.input(ele,desc)

    def click_dict_edit_button(self,driver):
        ele = driver.find_element_by_css_selector('#editType-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)')
        ele.click()

    def click_dict_edit_confirm(self,driver):
        ele = driver.find_element_by_css_selector('.bootbox > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)')
        ele.click()

    def do_dict_edit(self,driver,edit_info):
        self.click_system(driver)
        self.click_dict(driver)
        driver.implicitly_wait(3)
        self.click_dict_edit(driver)
        driver.implicitly_wait(2)
        self.input_dict_edit_name(driver, edit_info['dict_name'])
        self.input_dict_edit_desc(driver, edit_info['desc'])
        self.click_dict_edit_button(driver)
        time.sleep(3)

    def click_detail(self,driver):
        ele = driver.find_element_by_css_selector('#dict-type-table > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(6) > button:nth-child(3)')
        ele.click()

    def click_detail_edit(self,driver):
        ele = driver.find_element_by_css_selector('#dict-detail-table > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(6) > button:nth-child(1)')
        ele.click()

    def input_detail_name(self,driver,dict_name):
        ele = driver.find_element_by_css_selector('#edit-dictDetail-form > div:nth-child(3) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele,dict_name)

    def input_detail_tag(self,driver,tag):
        ele = driver.find_element_by_css_selector('#edit-dictDetail-form > div:nth-child(5) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele,tag)

    def input_detail_num(self,driver,num):
        ele = driver.find_element_by_css_selector(
            'div.row:nth-child(7) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele, num)

    def input_detail_desc(self,driver,desc):
        ele = driver.find_element_by_css_selector(
            'div.row:nth-child(8) > div:nth-child(1) > textarea:nth-child(2)')
        Service.input(ele, desc)

    def click_detail_save(self,driver):
        ele = driver.find_element_by_css_selector('#edit-detail-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)')
        ele.click()

    def do_detail(self,driver,detail_info):
        self.click_system(driver)
        self.click_dict(driver)
        driver.implicitly_wait(3)
        self.click_detail(driver)
        driver.implicitly_wait(2)
        self.click_detail_edit(driver)
        self.input_detail_name(driver, detail_info['dict_name'])
        self.input_detail_tag(driver, detail_info['tag'])
        time.sleep(2)
        self.input_detail_num(driver,detail_info['num'])
        self.input_detail_desc(driver, detail_info['desc'])
        self.click_detail_save(driver)
        time.sleep(5)