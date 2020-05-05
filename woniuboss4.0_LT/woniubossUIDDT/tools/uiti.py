# -*- coding: utf-8 -*-
import json

from selenium.webdriver.support.select import Select


class uiti:

    #json获取字典数据
    @classmethod
    def get_json(cls, path):
        with open(path, encoding='utf8') as file:
            content = json.load(file)
        return content

    #读取excel文件为【{}，{}】格式
    @classmethod
    def get_xlrd_dic(cls,test_info):
        import xlrd
        workbook=xlrd.open_workbook(test_info["DATAPATH"])
        contents=workbook.sheet_by_name(test_info['SHEETNAME'])
        info = []
        for i in range(test_info["STARTROW"],test_info["ENDROW"]):
            content = contents.cell(i,test_info["DATACOL"]).value
            temp=content.split('\n')
            dic={}
            for j in temp:
                dic[j.split('=')[0]]=j.split('=')[1]
            expect=contents.cell(i,test_info["EXPECTCOL"]).value
            dic["expect"]=expect
            info.append(dic)
        return info

    #将字典【{}，{}】转换成()、（）
    @classmethod
    def trans_dict_tup(cls,test_info):
        contents=cls.get_xlrd_dic(test_info)
        info=[]
        for content in contents:
            tup=()
            tup = tuple(content.values())
            info.append(tup)
        return info

    #读取文件为txt
    @classmethod
    def get_txt(cls,data_path):
        with open(data_path,encoding='utf8') as f:
            contents = f.readlines()
            return contents
    #读取文件为string

    @classmethod
    def get_str(cls,data_path):
        contents=cls.get_txt(data_path)
        li =[]
        for content in contents:
            if not content.startswith('#'):
                content=content.strip()
                li.append(content)
        return li

    #随机选择下拉框项目
    @classmethod
    def random_index(cls,selector):
        import random
        random_index =  random.randint(0,len(Select(selector).options)-1)
        Select(selector).select_by_index(random_index)

    #去掉某个元素的只读属性
    @classmethod
    def remove_readonly(cls, driver, ele_id):
        driver.execute_script('document.getElementById("%s").readOnly=false' % (ele_id))


    #连接数据库
    @classmethod
    def get_connection(cls,base_path):
        contents=cls.get_json(base_path)
        import pymysql
        return pymysql.connect(host=contents['HOST'], user=contents['USER'], password=contents['PWD'],
                               port=3306, autocommit=True, database=contents['DB'], charset='utf8')

    #查询单条记录
    @classmethod
    def inquiry_one(cls,base_path,sql):
        connect = cls.get_connection(base_path)
        cursor = connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        connect.close()
        return result




if __name__ == '__main__':
    test_info=uiti.get_json('..\\conf\\testdata.conf')
    uiti.trans_dict_tup(test_info[0])

