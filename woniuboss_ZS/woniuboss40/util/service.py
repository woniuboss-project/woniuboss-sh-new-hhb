# -*- coding: utf-8 -*-#

import requests

# from util.utility import Utility


class Service:

	@classmethod
	def get_session(cls):

		login_url= r'http://47.96.74.65:8080/WoniuBoss4.0/login/userLogin'
		login_data = {"userName":"WNCD000","userPass":"woniu123","checkcode":"0000","remember":"Y"}
		session = requests.session()
		session.post(login_url,login_data)
		return session

if __name__ == '__main__':
	Service.get_session()