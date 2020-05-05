from woniubossAPIDDT.tools.service import Service
from woniubossAPIDDT.tools.uiti import uiti


class System:
    def __init__(self,base_path):
        self.session = Service.get_session('..\\conf\\base.conf')


    # 用户管理查询功
    def do_query(self, query_url, query_data):
        resp = self.session.post(query_url, query_data)
        return resp

    # 用户管理角色设置
    def do_role_set(self, set_url, set_data):
        resp = self.session.post(set_url, set_data)
        return resp

    # 用户管理修改用户
    def do_edit(self, edit_url, edit_data):
        resp = self.session.post(edit_url, edit_data)
        return resp

    # 用户管理重置密码
    def do_reset(self, reset_url, reset_data):
        resp = self.session.post(reset_url, reset_data)
        return resp

    # 角色管理查询
    def do_role_query(self, query_url, query_data):
        resp = self.session.post(query_url, query_data)
        return resp

    # 角色管理新增功能
    def do_rolAdd(self, add_url, add_data):
        resp = self.session.post(add_url, add_data)
        return resp

    # 角色管理授权功能
    def do_authorize(self, auth_url, auth_data):
        resp = self.session.post(auth_url, auth_data)
        return resp

    # 角色管理修改功能
    def do_role_edit(self, edit_url, edit_data):
        resp = self.session.post(edit_url, edit_data)
        return resp

    # 资源树新增功能
    def do_source_edit(self, edit_url, edit_data):
        resp = self.session.post(edit_url, edit_data)
        return resp

    # 字典管理查询
    def do_dic_query(self, query_url, query_data):
        resp = self.session.post(query_url, query_data)
        return resp

    # 字典管理新增功能
    def do_dicAdd(self, add_url, add_data):
        resp = self.session.post(add_url, add_data)
        return resp

    # 字典编辑功能
    def do_dic_ed(self, edit_url, edit_data):
        resp = self.session.post(edit_url, edit_data)
        return resp

    # 详情编辑资源功能
    def do_detail_ed(self, edit_url, edit_data):
        resp = self.session.post(edit_url, edit_data)
        return resp

    # 字典管理启用/停用功能
    def do_status(self, status_url, status_data):
        resp = self.session.post(status_url, status_data)
        return resp