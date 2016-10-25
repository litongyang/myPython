# __author__ = 'lty'
# -*- coding: utf-8 -*-

"""
得到每个股票的历史交易数据(向后复权)
"""
import tushare as tus
import time
import numpy as np
import pandas as pd
import create_table.create_table as mysqldb


class GetDataTradeHistroy:
    def __init__(self):
        self.code = str(600009)
        self.time_stamp_tmp = time.time()
        self.time_array = time.localtime(self.time_stamp_tmp)
        self.date = time.strftime("%Y-%m-%d", self.time_array)  # 当前日期
        self.company_code_list = []  # 公司代码list
        self.mysqldb = mysqldb.CreateTable()

        self.db_name = 'test'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = ''  # 密码


    def get_company_code(self):
        company_industry = tus.get_industry_classified()
        self.company_code_list = company_industry['code'].values
        # self.company_code_list = ['600009']

        # x.to_json('test.json')

    def get_trade_data(self):
        for i in range(0, len(self.company_code_list)):
            try:
                start_date = tus.get_stock_basics().ix[self.company_code_list[i]]['timeToMarket']  # 上市日期YYYYMMDD
                start_date = str(start_date)[0:4] + '-' + str(start_date)[4:6] + '-' + str(start_date)[6:8]
                company_trade_histroy = tus.get_h_data(self.company_code_list[i], autype=None, start='2016-09-30', end=self.date)
                print self.company_code_list[i]
                """ 获取日期 """
                pydate_array = company_trade_histroy.index.to_pydatetime()
                date_array = np.vectorize(lambda s: s.strftime('%Y-%m-%d'))(pydate_array)
                date_series = pd.Series(date_array)
                print date_series

                """ 获取参数 """
                print company_trade_histroy['open'].values
                print company_trade_histroy['close'].values
                print company_trade_histroy['high'].values
                print company_trade_histroy['low'].values
                print company_trade_histroy['volume'].values
                print company_trade_histroy['amount'].values
                print "===================="

                for j in range(0, len(date_series)):
                    insert_sql = '\'' + str(self.company_code_list[i]) + '\'' + ','
                    insert_sql += '\'' + str(date_series[j]) + '\'' + ','
                    insert_sql += '\'' + str(company_trade_histroy['open'][j]) + '\'' + ','
                    insert_sql += '\'' + str(company_trade_histroy['high'][j]) + '\'' + ','
                    insert_sql += '\'' + str(company_trade_histroy['close'][j]) + '\'' + ','
                    insert_sql += '\'' + str(company_trade_histroy['low'][j]) + '\'' + ','
                    insert_sql += '\'' + str(company_trade_histroy['volume'][j]) + '\'' + ','
                    insert_sql += '\'' + str(company_trade_histroy['amount'][j]) + '\'' + ','
                    insert_sql = insert_sql[0:-1]  # 去除最后一个逗号
                    self.mysqldb.insert_data(self.mysqldb.table_trade_history_data, insert_sql)
                    print insert_sql
            except:
                pass
        # print company_trade_histroy

if __name__ == '__main__':
    test = GetDataTradeHistroy()
    test.get_company_code()
    test.get_trade_data()
