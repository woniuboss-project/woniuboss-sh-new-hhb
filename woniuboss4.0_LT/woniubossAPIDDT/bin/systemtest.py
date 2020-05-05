import unittest

from parameterized import parameterized

from woniubossAPIDDT.lib.system import System
from woniubossAPIDDT.tools.uiti import uiti

test_info = uiti.get_json('..\\conf\\testdata.conf')
query_infos = uiti.trans_dict_tup(test_info[1])
set_infos = uiti.trans_dict_tup(test_info[2])
edit_infos = uiti.trans_dict_tup(test_info[3])
reset_infos = uiti.trans_dict_tup(test_info[4])
role_query_infos = uiti.trans_dict_tup(test_info[5])
rolAdd_infos = uiti.trans_dict_tup(test_info[6])
authorize_infos = uiti.trans_dict_tup(test_info[7])
role_edit_infos = uiti.trans_dict_tup(test_info[8])
source_edit_infos = uiti.trans_dict_tup(test_info[9])
dict_query_infos = uiti.trans_dict_tup(test_info[10])
dic_add_infos = uiti.trans_dict_tup(test_info[11])
dic_ed_infos = uiti.trans_dict_tup(test_info[12])
detail_ed_infos = uiti.trans_dict_tup(test_info[13])
status_infos = uiti.trans_dict_tup(test_info[14])
class systemTest(unittest.TestCase):

    def setUp(self):
        print("begin test")

    def tearDown(self):
        print("test over")

    # 用户管理查询资源测试
    @parameterized.expand(query_infos)
    def test_system_query(self, query_url, METHOD, DATA, CODE, CONTENT, expect):
        query_data = {'pageSize': DATA['pageSize'],'pageIndex': DATA['pageIndex'],'userName': DATA['userName'],'empName': DATA['empName']}
        resp = System('..\\conf\\base.conf').do_query(query_url, query_data)
        num = resp.json()
        if num['totalRow'] != 0:
            if DATA['userName'] == 'WNCD008':
                counts = uiti.query_one('..\\conf\\base.conf','SELECT COUNT(id) FROM system_user  WHERE name="WNCD008"')
                if counts[0] == num['totalRow']:
                    actual = 'query ok'
                else:
                    actual = 'query fail'
            elif DATA['userName'] == '':
                counts = uiti.query_one('..\\conf\\base.conf',
                                        'SELECT COUNT(id) FROM system_user where passwd_status=1 and passwd2_status=1')
                print(counts)
                if counts[0] == num['totalRow']:
                    actual = 'query ok'
                else:
                    actual = 'query fail'
        else:
            actual = 'query fail'
        self.assertEqual(actual,expect)

    # 用户管理角色设置测试
    @parameterized.expand(set_infos)
    def test_system_set(self, set_url, METHOD, DATA, CODE, CONTENT, expect):
        set_data = {'userId': DATA['userId'],'roleId[]': DATA['roleId[]']}
        resp = System('..\\conf\\base.conf').do_role_set(set_url, set_data)
        content = resp.text
        if content == '角色设置成功':
            actual = 'set ok'
        elif content == '角色设置失败':
            actual = 'set fail'
        self.assertEqual(actual, expect)
    
    # 用户管理修改用户测试
    @parameterized.expand(edit_infos)
    def test_edit(self, edit_url, METHOD, DATA, CODE, CONTENT, expect):
        edit_data = {'user.id': DATA['user.id'], 'user.name': DATA['user.name'],
                     'user.status': DATA['user.status'], 'user.des': DATA['user.des']}
        resp = System('..\\conf\\base.conf').do_edit(edit_url, edit_data)
        content = resp.text
        if content == '修改成功':
            actual = 'edit ok'
        else:
            actual = 'edit fail'
        self.assertEqual(actual, expect)
    
    # 用户管理重置密码测试
    @parameterized.expand(reset_infos)
    def test_reset(self, reset_url, METHOD, DATA, CODE, CONTENT, expect):
        reset_data = {'userId': DATA['userId'], 'pwdType': DATA['pwdType'],
                     'pwd': DATA['pwd']}
        resp = System('..\\conf\\base.conf').do_edit(reset_url, reset_data)
        content = resp.text
        if content == '重置成功':
            actual = 'reset ok'
        elif content == '重置失败':
            actual = 'reset fail'
        self.assertEqual(actual, expect)
    
    # 角色管理查询资源测试
    @parameterized.expand(role_query_infos)
    def test_role_query(self, query_url, METHOD, DATA, CODE, CONTENT, expect):
        query_data = {'pageSize': DATA['pageSize'], 'pageIndex': DATA['pageIndex'],
                      'roleName': DATA['roleName']}
        resp = System('..\\conf\\base.conf').do_role_query(query_url, query_data)
        num = resp.json()
        if num['totalRow'] != 0:
            if DATA['roleName'] == '系统管理员':
                counts = uiti.query_one('..\\conf\\base.conf',
                                        'SELECT COUNT(id) FROM system_role  where name="系统管理员"')
                if counts[0] == num['totalRow']:
                    actual = 'query ok'
                else:
                    actual = 'query fail'
            elif DATA['roleName'] == '':
                counts = uiti.query_one('..\\conf\\base.conf',
                                        'SELECT COUNT(id) FROM system_role ')

                if counts[0] == num['totalRow']:
                    actual = 'query ok'
                else:
                    actual = 'query fail'
        else:
            actual = 'query fail'
        self.assertEqual(actual, expect)
    
    # 角色管理新增资源测试
    @parameterized.expand(rolAdd_infos)
    def test_role_rolAdd(self, add_url, METHOD, DATA, CODE, CONTENT, expect):
        add_data = {'role.name': DATA['role.name'], 'role.des': DATA['role.des']}
        resp = System('..\\conf\\base.conf').do_rolAdd(add_url, add_data)
        if 'success' in resp.text:
            actual = 'add ok'
        else:
            actual = 'add fail'

        self.assertEqual(actual, expect)
    
    # 角色管理授权资源测试
    @parameterized.expand(authorize_infos)
    def test_authorize(self, auth_url, METHOD, DATA, CODE, CONTENT, expect):
        auth_data = {'resId[]': DATA['resId[]'], 'roleId': DATA['roleId']}
        resp = System('..\\conf\\base.conf').do_authorize(auth_url, auth_data)
        content = resp.text
        if content == '授权成功':
            actual = 'authorize ok'
        else:
            actual = 'authorize fail'
        self.assertEqual(actual, expect)
    
    @parameterized.expand(role_edit_infos)
    def test_role_edit(self, edit_url, METHOD, DATA, CODE, CONTENT, expect):
        edit_data = {'role.id': DATA['role.id'], 'role.name': DATA['role.name'],
                     'role.des': DATA['role.des']}
        resp = System('..\\conf\\base.conf').do_role_edit(edit_url, edit_data)
        content = resp.text
        if content == 'success':
            actual = 'edit ok'
        else:
            actual = 'edit fail'
        self.assertEqual(actual, expect)
    
    # 菜单管理修改资源测试
    @parameterized.expand(source_edit_infos)
    def test_menu_edit(self, edit_url, METHOD, DATA, CODE, CONTENT, expect):
        edit_data = {'res.id': DATA['res.id'], 'res.name': DATA['res.name'],
                    'res.url': DATA['res.url'], 'res.permission': DATA['res.permission'],'res.des': DATA['res.des']}
        resp = System('..\\conf\\base.conf').do_source_edit(edit_url, edit_data)
        content = resp.text
        if content == 'success':
            actual = 'edit ok'
        else:
            actual = 'edit fail'
        self.assertEqual(actual, expect)
    
    # 字典管理查询资源测试
    @parameterized.expand(dict_query_infos)
    def test_dict_query(self, query_url, METHOD, DATA, CODE, CONTENT, expect):
        query_data = {'pageSize': DATA['pageSize'], 'pageIndex': DATA['pageIndex'],
                      'typename': DATA['typename']}
        resp = System('..\\conf\\base.conf').do_dic_query(query_url, query_data)
        num = resp.json()
        if num['totalRow'] != 0:
            if DATA['typename'] == '员工状态':
                counts = uiti.query_one('..\\conf\\base.conf',
                                        'SELECT COUNT(dict_type_id) FROM dictionary_type  WHERE dict_typename="员工状态"')
                if counts[0] == num['totalRow']:
                    actual = 'query ok'
                else:
                    actual = 'query fail'
            elif DATA['typename'] == '':
                counts = uiti.query_one('..\\conf\\base.conf',
                                        'SELECT COUNT(dict_type_id) FROM dictionary_type ')

                if counts[0] == num['totalRow']:
                    actual = 'query ok'
                else:
                    actual = 'query fail'
        else:
            actual = 'query fail'
        self.assertEqual(actual, expect)
    
    # 字典管理新增资源测试
    @parameterized.expand(dic_add_infos)
    def test_dic_add(self, add_url, METHOD, DATA, CODE, CONTENT, expect):
        add_data = {'dd.dict_type_id': DATA['dd.dict_type_id'], 'dd.dict_value': DATA['dd.dict_value'], 'dd.dict_key': DATA['dd.dict_key']
                    ,'dd.sort': DATA['dd.sort'],'dd.remarks': DATA['dd.remarks']}
        resp = System('..\\conf\\base.conf').do_dicAdd(add_url, add_data)
        if 'success' in resp.text:
            actual = 'add ok'
        else:
            actual = 'add fail'

        self.assertEqual(actual, expect)
    

    # 字典管理修改资源测试
    @parameterized.expand(dic_ed_infos)
    def test_dic_edit(self, edit_url, METHOD, DATA, CODE, CONTENT, expect):
        edit_data = {'dt.dict_type_id': DATA['dt.dict_type_id'], 'dt.dict_typename': DATA['dt.dict_typename'],
                     'dt.remarks': DATA['dt.remarks']}
        resp = System('..\\conf\\base.conf').do_dic_ed(edit_url, edit_data)
        content = resp.text
        if content == 'success':
            actual = 'edit ok'
        else:
            actual = 'edit fail'
        self.assertEqual(actual, expect)
    
    # 字典管理编辑资源测试
    @parameterized.expand(detail_ed_infos)
    def test_detail_edit(self, edit_url, METHOD, DATA, CODE, CONTENT, expect):
        edit_data = {'dd.dict_type_id': DATA['dd.dict_type_id'], 'dd.dict_data_id': DATA['dd.dict_data_id'],
                     'dict_typename': DATA['dict_typename']
            , 'dd.dict_value': DATA['dd.dict_value'], 'dd.sort': DATA['dd.sort'], 'dd.remarks': DATA['dd.remarks']}
        resp = System('..\\conf\\base.conf').do_detail_ed(edit_url, edit_data)
        if 'success' in resp.text:
            actual = 'edit ok'
        else:
            actual = 'edit fail'

        self.assertEqual(actual, expect)
    
    # 字典管理启停用资源测试
    @parameterized.expand(status_infos)
    def test_dic_status(self, status_url, METHOD, DATA, CODE, CONTENT, expect):
        status_data = {'dataId': DATA['dataId'], 'status': DATA['status']}
        resp = System('..\\conf\\base.conf').do_status(status_url, status_data)
        if 'success' in resp.text:
            actual = 'statu ok'
        else:
            actual = 'statu fail'

        self.assertEqual(actual, expect)




if __name__ == '__main__':
    unittest.main(verbosity=2)