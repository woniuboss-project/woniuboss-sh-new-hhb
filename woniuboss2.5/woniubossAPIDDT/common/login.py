from tools.service import Service

import requests

class Login:


    def do_login(self,URL,login_info):
        session=requests.session()
        resp=session.post(URL,login_info)
        return resp



