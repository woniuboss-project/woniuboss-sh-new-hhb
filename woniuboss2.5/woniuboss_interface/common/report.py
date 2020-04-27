import requests
from utils.Utils import Utility



class Report:

    def __init__(self):
        self.session = Utility.get_login_session()
        self.session = Utility.get_second_code(self.session)

    def do_report(self, url, data):
        return self.session.post(url, data)
