from tools.service import Service
from tools.uiti import uiti


class Login:

    # �����û���
    def input_usrname(self, driver, login_info):
        ele = driver.find_element_by_name('userName')
        Service.input(ele, login_info['userName'])

    # ��������
    def input_password(self, driver, login_info):
        ele = driver.find_element_by_name('userPass')
        Service.input(ele, login_info['userPass'])

    # ������֤��
    def input_checkcode(self, driver, login_info):
        ele = driver.find_element_by_name('checkcode')
        Service.input(ele, login_info['checkcode'])

    # �����¼��ť
    def click_login(self, driver):
        driver.find_element_by_css_selector('.btn').click()

    # ���ϵ�¼����
    def do_login(self, base_path, driver, login_info):
        Service.open_page(base_path, driver)
        self.input_usrname(driver, login_info)
        self.input_password(driver, login_info)
        self.input_checkcode(driver, login_info)
        self.click_login(driver)
