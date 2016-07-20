# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

"""
将企业所属行业数据导入到数据库
1. 下载末日的股市数据
2. 复制到txt文件
3. 转成utf8
4. 跑程序
"""

import MySQLdb
import chardet


class CompanyIndustryToDB:
    def __init__(self):
        self.file_name = 'company_industry'
        self.code = []
        self.name = []
        self.industry_name = []
        self.file = 'C:\\Users\\tongyang.li\\Desktop\\test1.txt'  # 源数据

        self.db_name = 'STOCK_INFO_2015'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                    port=self.db_port)
        self.cur = self.conn.cursor()

    # 得到数据
    def get_data(self):
        for line in open(self.file, 'rb'):
            line_one = line.split('\t')
            self.code.append(line_one[0])
            self.name.append(line_one[1])
            self.industry_name.append(line_one[18])

    def create_table(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "company_code varchar(20) comment '公司代码',"
                "company_name varchar(100) comment '公司名称',"
                "industry varchar(100) comment '公司所属行业',"
                "PRIMARY KEY (`company_code`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.file_name)
        except Exception, e:
            print Exception, e

    # insert data to db
    def insert_data(self):
        try:
            self.cur.execute('set names \'utf8\'')
            intsert_sql = ''
            for i in range(1, len(self.code)):
                intsert_sql += '\'' + self.code[i] + '\'' + ','
                intsert_sql += '\'' + self.name[i] + '\'' + ','
                intsert_sql += '\'' + self.industry_name[i] + '\'' + ','
                intsert_sql = intsert_sql[0:-1]  # 去除最后一个逗号
                # print intsert_sql
                self.cur.execute("insert into %s values(%s)" % (self.file_name, intsert_sql))
                intsert_sql = ''
        except Exception, e:
            print Exception, e


if __name__ == '__main__':
    company_industry = CompanyIndustryToDB()
    company_industry.get_data()
    company_industry.insert_data()
