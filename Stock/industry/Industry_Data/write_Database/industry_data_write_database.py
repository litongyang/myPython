# __author__ = 'litongyanfg'
# -*- coding: utf-8 -*-

# 将行业数据写入数据库

import MySQLdb
import Stock.industry.Industry_Data.industryDataMean as industryDataMean
import Stock.industry.Industry_Data.industryData as industryDataSum


class IndustryDataWriteDataBase:
    def __init__(self):
        self.db_name = 'STOCK_INFO_2014'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.industry_data_table_name = "industry_data"  # 数据表名
        self.industry_data_mean = industryDataMean.IndustryDataMean()
        self.industry_data_sum = industryDataSum.IndustryData()

        self.parameters_dictionary = {}  # 求和参数和求均值参数合并字典

    # 获取行业数据
    def data_process(self):
        self.industry_data_mean.create_parameters_dictionary()
        for key, value in self.industry_data_mean.parameters_dictionary.items():
            self.industry_data_mean.parameters_mean_ratio(key,value, self.industry_data_mean.year)  # mean

        self.industry_data_sum.divided_group_industry()
        self.industry_data_sum.create_parameters_dictionary()
        for key, value in self.industry_data_sum.parameters_dictionary.items():
            self.industry_data_sum.parameters_sum(key,value)  # sum

        self.parameters_dictionary = dict(self.industry_data_mean.parameters_dictionary.items() +
                                          self.industry_data_sum.parameters_dictionary.items())  # merge

    # 將行业参数数据写入数据库
    def write_database(self):
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            for parameters, parameter_value_industry in self.parameters_dictionary.items():
                for industry_name, value in parameter_value_industry.items():
                    year = 2014
                    for i in range(0, len(value)):
                        temp = '\'' + industry_name + '\'' + ',' + '\'' + str(year) + '\'' + ',' + '\'' + parameters + '\'' + ',' + '\'' + str(value[i]) + '\''
                        insert_sql = "insert into %s values(%s)" % (self.industry_data_table_name, temp)
                        year -= 1
                        print insert_sql
                        cur.execute(insert_sql)
        except Exception, e:
            print Exception, ":", e


if __name__ == '__main__':
    industryDataWriteDataBase = IndustryDataWriteDataBase()
    industryDataWriteDataBase.data_process()
    industryDataWriteDataBase.write_database()