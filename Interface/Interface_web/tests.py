# -*- coding: utf-8 -*-
from django.test import TestCase

# Create your tests here.


import MySQLdb


class GetDataToDb:
    def __init__(self):
        self.db_name = 'stock_info_2014'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码

        self.data = []

    def get_data(self):
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM industry_data")
            results = cur.fetchmany(count)
            self.data.append(results[0][0])
            print self.data
            cur.close()
            conn.close()
        except:
            pass


if __name__ == '__main__':
    get_data = GetDataToDb()
    get_data.get_data()
