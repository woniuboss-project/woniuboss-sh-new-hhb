import requests

from util.service import Service


class Finance:
    def __init__(self):
        self.session = Service.get_session()

    def query_finance(self,finance_url,finance_data):
        return  self.session.post(finance_url,finance_data)

    def add_finance(self,finance_url,finance_data):
        return  self.session.post(finance_url,finance_data)

