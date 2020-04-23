#-*- coding:utf-8 -*-
from tools.service import Service


class employment:
    def __init__(self,base_path):
        self.session = Service.get_session(base_path)

    #解密
    def decrypt(self,URL,decrypt_info):
        resp = self.session.post(URL,decrypt_info)
        return resp

    #查询学员通过情况
    def choose(self,URL,DATA):
        resp = self.session.post(URL,DATA)
        return  resp