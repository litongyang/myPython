# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import MySQLdb


class CreateTable:
    def __init__(self):
        self.db_name = 'STOCK_INFO_2015'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.file_name = 'company_industry_ratio'
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name, port=self.db_port)
        self.cur = self.conn.cursor()

    def create_table(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute(
                    "CREATE TABLE IF NOT EXISTS %s "
                    "("
                    "company_code varchar(100) comment '公司代码',"
                    "year varchar(20) comment '年份',"
                    "industry_ratio decimal(10,2) comment '公司在行业所占比重',"
                    "PRIMARY KEY (`company_code`,`year`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                    % self.file_name)
        except Exception, e:
            print Exception, e

if __name__ == '__main__':
    test = CreateTable()
    test.create_table()