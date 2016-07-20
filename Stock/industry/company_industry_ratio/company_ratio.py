# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# 得到公司的“股东权益合计”在行业的占比

import MySQLdb

import Stock.industry.Industry_Data.industryData as industryData


class CompanyRatio:
    def __init__(self):
        self.db_name = 'STOCK_INFO_2015'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.company_industry_ratio_fileName = "company_industry_ratio"  # 数据表名

    # 公司的“股东权益合计”
    # 在行业的占比 存入数据库
    def create_table_company_industry_ratio(self):
        industry = industryData.IndustryData()
        industry.divided_group_industry()
        industry.parameters_sum("股东权益合计", industry.shareholders_equity_sum_industry)
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            for key, value in industry.shareholders_equity_sum_industry.items():
                for k in range(0, len(industry.company_industry[key])):
                    file_name = "stock_" + industry.company_industry[key][k]
                    year = 2015
                    for j in range(0, len(value)):
                        try:
                            count = cur.execute(
                                "SELECT * FROM %s " % file_name + "WHERE SUBJECT= '股东权益合计' ")
                            results = cur.fetchmany(count)
                            ratio = results[0][j + 3] / value[j]
                            temp = '\'' + industry.company_industry[key][k] + '\'' + ',' + '\'' + str(
                                year) + '\'' + ',' + '\'' + str(ratio) + '\''
                            insert_sql = "insert into %s values(%s)" % (self.company_industry_ratio_fileName, temp)
                            year -= 1
                            cur.execute(insert_sql)
                        except Exception, e:
                            print Exception, ":", e
        except Exception, e:
            print Exception, ":", e


if __name__ == '__main__':
    CompanyRatio = CompanyRatio()
    CompanyRatio.create_table_company_industry_ratio()
