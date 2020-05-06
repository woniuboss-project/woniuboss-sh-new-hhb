import requests

from util.service import Service


class Login:
    def __init__(self):
        self.session = Service.get_session()


    def do_login(self,login_url,login_data):
        return  self.session.post(login_url,login_data)
