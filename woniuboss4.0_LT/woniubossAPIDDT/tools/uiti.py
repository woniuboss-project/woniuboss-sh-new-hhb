# -*- coding: utf-8 -*-
import json




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
            URL=contents.cell(i,test_info['URLCOL']).value
            METHOD=contents.cell(i,test_info['METHODCOL']).value
            DATA = contents.cell(i,test_info["DATACOL"]).value
            CODE=contents.cell(i,test_info['CODECOL']).value
            CONTENT=contents.cell(i,test_info['CONTENTCOL']).value
            temp=DATA.split('\n')
            dic={}
            for j in temp:
                dic[j.split('=')[0]]=j.split('=')[1]
            EXPECT=contents.cell(i,test_info["EXPECTCOL"]).value
            dic1={'URL':URL,'METHOD':METHOD,'DATA':dic,'CODE':CODE,'CONTENT':CONTENT,'EXPECT':EXPECT}
            info.append(dic1)
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

    #判断两个值是否相等
    @classmethod
    def assert_equal(cls,expect,content):
        if expect==content:
            return True
        else:
            return  False

    # 获取数据库连接
    # 依赖于配置文件的规则
    @classmethod
    def getConn(cls, base_conf_path):
        import pymysql
        db_info = cls.get_json(base_conf_path)
        # 依赖于json数据格式
        return pymysql.connect(db_info['HOST'], db_info['DBUSER'], db_info['DBPASSWORD'], db_info['DBNAME'],
                               charset='utf8')

    @classmethod
    def query_one(cls, base_conf_path, sql):
        # 获取数据库连接对象
        conn = cls.getConn(base_conf_path)
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        # 返回一维元组
        return result











