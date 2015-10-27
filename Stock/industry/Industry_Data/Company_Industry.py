# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# 将每个公司所属的行业写入数据库

import MySQLdb


class CompanyIndustry:
    def __init__(self):
        self.db_name = 'STOCK_INFO_2014'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.fileName = 'company_industry'

        self.company_code = []
        self.company_name = []
        self.industry = []

    def create_table_company_industry(self):
        for line in open("/Users/litongyang/Desktop/industry.txt"):
            linone = line.split()
            self.company_code.append(linone[0])
            self.company_name.append(linone[1])
            self.industry.append(linone[2])

        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            for i in range(0, len(self.company_code)):  # len(self.company_code)):
                temp = '\'' + self.company_code[i] + '\'' + ',' + '\'' + self.company_name[i] + '\'' + ',' + '\'' + \
                       self.industry[i] + '\'' + ','
                temp = temp[0: -1]
                insert_sql = "insert into %s values(%s)" % (self.fileName, temp)
                print insert_sql
                cur.execute(insert_sql)
        except Exception, e:
            print Exception, ":", e


if __name__ == '__main__':
    company_industry = CompanyIndustry()
    company_industry.create_table_company_industry()
