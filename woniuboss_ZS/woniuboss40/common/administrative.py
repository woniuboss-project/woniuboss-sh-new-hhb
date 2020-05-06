import requests

from util.service import Service


class Administrative:
    def __init__(self):
        self.session = Service.get_session()

    def query_assets(self,assets_url,assets_data):
        return  self.session.post(assets_url,assets_data)

    def add_assets(self,assets_url,assets_data):
        return  self.session.post(assets_url,assets_data)

    def modify_assets(self,assets_url,assets_data):
        return  self.session.post(assets_url,assets_data)