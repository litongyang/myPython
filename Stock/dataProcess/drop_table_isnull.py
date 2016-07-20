# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

from __future__ import division
import MySQLdb

company_code_noexit = []


class DROP_TABLE_ISNULL():
    def __init__(self):
        self.Company_code = []
        self.Company_code_noexit = []
        self.db_name = 'STOCK_INFO_2015'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码

    # ------删除不存在公司的空表---------
    def drop_table_isnull(self):
        try:
            for line in open("code_no_exist.txt"):
                content = line.split()
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            for i in range(0, len(content)):
                company_code_noexit.append(content[i])
                parameters_data_file = 'parameters_' + str(content[i])
                stock_data_file = 'stock_' + str(content[i])
                try:
                    count = cur.execute("DROP TABLE if exists  %s" % parameters_data_file)
                    print "drop %s is successed!" % parameters_data_file
                    count1 = cur.execute("DROP TABLE if exists %s" % stock_data_file)
                    print "drop %s is successed!" % stock_data_file
                except Exception, e:
                    print Exception, e
        except Exception, e:
            print Exception, e


if __name__ == '__main__':
    downStockData_db = DROP_TABLE_ISNULL()
    downStockData_db.drop_table_isnull()
