from util.service import Service


class HR:
    def __init__(self):
        self.session = Service.get_session()

    def query_HR(self,hr_url,hr_data):
        return  self.session.post(hr_url,hr_data)

    def add_HR(self,hr_url,hr_data):
        return  self.session.post(hr_url,hr_data)

    def modify_HR(self,hr_url,hr_data):
        return  self.session.post(hr_url,hr_data)