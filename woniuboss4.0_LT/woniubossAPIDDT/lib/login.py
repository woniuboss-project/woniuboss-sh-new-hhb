from woniubossAPIDDT.tools.service import Service


class Login:
    def __init__(self,base_path):
        self.session=Service.get_session(base_path)

    def do_login(self,URL,login_info):
        resp=self.session.post(URL,login_info)
        print(resp.text)
        return resp



