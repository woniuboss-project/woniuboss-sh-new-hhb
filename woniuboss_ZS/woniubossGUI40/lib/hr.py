import time

from tools.service import Service
from tools.uiti import uiti


class Hr:

    #下拉框选择区域查询员工
    def select_regionSel(self,driver,hr_info):
        ele=driver.find_element_by_id('regionSel')
        uiti.select_index(ele,hr_info['regionSel'])

     #下拉框选择部门
    def select_department(self,driver,hr_info):
        ele=driver.find_element_by_name('department_id')
        uiti.select_index(ele,hr_info['department_id'])

    # 下拉框选择状态
    def select_last_status(self, driver, hr_info):
        ele = driver.find_element_by_name('last_status')
        uiti.select_index(ele, hr_info['last_status'])

    # 输入名称查询
    def input_empName(self, driver, hr_info):
        ele = driver.find_element_by_name('empName')
        Service.input(ele,hr_info['empName'])

    #点击查询按钮
    def click_query(self, driver):
        driver.find_element_by_css_selector('button.btn:nth-child(5)').click()

    #点击人事管理
    def click_hr(self,driver):
        driver.find_element_by_css_selector('div.panel:nth-child(12) > div:nth-child(1) > a:nth-child(1)').click()

    #点击员工管理
    def click_employees(self,driver):
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[12]/div[2]/div/ul/li[1]/a').click()

    #点击新增员工按钮
    def click_add_employees(self,driver):

        driver.find_element_by_css_selector('button.btn-padding:nth-child(1)').click()

    #选择新增的区域
    def add_regionSel(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > select:nth-child(2)')
        from selenium.webdriver.support.select import Select
        Select(ele).select_by_index(hr_info['region_id'])

    #选择新增的部门
    def add_department(self,driver,hr_info):
        time.sleep(1)
        ele=driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > select:nth-child(2)')
        uiti.select_index(ele,hr_info['department_id'])

    #新增职位
    def add_position(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > input:nth-child(2)')
        Service.input(ele,hr_info['position'])

    #新增姓名
    def add_empName(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele,hr_info['employee_name'])

    #选择性别
    def select_sex(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > select:nth-child(2)')
        uiti.select_index(ele, hr_info['sex'])

    #新增日期
    def add_time(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > input:nth-child(2)')
        # uiti.remove_readonly(driver,'#addEmp-form > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > input:nth-child(2)')
        ele.click()
        driver.find_element_by_css_selector('div.datetimepicker:nth-child(22) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(3)').click()

    #新增电话
    def add_phone(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele, hr_info['tel'])

    #新增邮箱
    def add_email(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > input:nth-child(2)')
        Service.input(ele, hr_info['email'])

    #新增QQ
    def add_QQ(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > input:nth-child(2)')
        Service.input(ele, hr_info['qq'])

    #新增学历
    def select_education(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > select:nth-child(2)')
        uiti.select_index(ele, hr_info['education'])

    #新增院校
    def add_university(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > input:nth-child(2)')
        Service.input(ele, hr_info['university'])

    #新增专业
    def add_major(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > input:nth-child(2)')
        Service.input(ele, hr_info['major'])

    #新增住址
    def add_address(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele, hr_info['address'])

    #新增户口
    def add_source(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(5) > div:nth-child(2) > input:nth-child(2)')
        Service.input(ele, hr_info['source'])

    #新增卡号
    def add_cardnum(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(5) > div:nth-child(3) > input:nth-child(2)')
        Service.input(ele, hr_info['cardnum'])

    # 新增身份证号码
    def add_identity(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele, hr_info['identity'])

    # 新增生日
    def add_birthday(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(6) > div:nth-child(2) > input:nth-child(2)')
        ele.click()
        driver.find_element_by_css_selector('div.datetimepicker:nth-child(23) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4)').click()

    #新增生日类型
    def select_birthday_type(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(6) > div:nth-child(3) > select:nth-child(2)')
        uiti.select_index(ele, hr_info['birthday_type'])

    # 新增联系人
    def add_emergency_contact(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele, hr_info['emergency_contact'])

    #新增联系人号码
    def add_emergency_tel(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(7) > div:nth-child(2) > input:nth-child(2)')
        Service.input(ele, hr_info['emergency_tel'])

    # 新增联系人与本人关系
    def add_emegency_relation(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(7) > div:nth-child(3) > input:nth-child(2)')
        Service.input(ele, hr_info['emegency_relation'])

    # 新增工号
    def add_work_id(self, driver, hr_info):
        time.sleep(1)
        ele = driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(8) > div:nth-child(1) > input:nth-child(2)')
        Service.input(ele, hr_info['work_id'])

    #点击新增保存
    def click_addEmpBtn(self,driver):
        driver.implicitly_wait(3)
        driver.find_element_by_id('addEmpBtn').click()

    # 下拉框选择查询员工
    def select_employees(self, driver, hr_info):
        self.click_hr(driver)
        self.click_employees(driver)
        self.select_regionSel(driver,hr_info)
        self.select_department(driver,hr_info)
        self.select_last_status(driver,hr_info)
        self.input_empName(driver,hr_info)
        self.click_query(driver)

    #新增员工
    def add_employess(self,driver,hr_info):
        driver.implicitly_wait(3)
        self.click_hr(driver)
        self.click_employees(driver)
        self.click_add_employees(driver)
        self.add_regionSel(driver,hr_info)
        self.add_department(driver,hr_info)
        self.add_position(driver,hr_info)
        self.add_empName(driver,hr_info)
        self.select_sex(driver,hr_info)
        self.add_time(driver,hr_info)
        self.add_phone(driver,hr_info)
        self.add_email(driver,hr_info)
        self.add_QQ(driver,hr_info)
        self.select_education(driver,hr_info)
        self.add_university(driver,hr_info)
        self.add_major(driver,hr_info)
        self.add_address(driver,hr_info)
        self.add_source(driver,hr_info)
        self.add_cardnum(driver,hr_info)
        self.add_identity(driver,hr_info)
        self.add_birthday(driver,hr_info)
        self.select_birthday_type(driver,hr_info)
        self.add_emergency_contact(driver,hr_info)
        self.add_emergency_tel(driver,hr_info)
        self.add_emegency_relation(driver, hr_info)
        self.add_work_id(driver,hr_info)
        self.click_addEmpBtn(driver)