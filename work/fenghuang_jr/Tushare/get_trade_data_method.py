# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
获取交易数据封装的方法
"""

import tushare as tus
import time
import numpy as np
import pandas as pd
import create_table.create_table as mysqldb
import read_conf as read_conf
import send_mail as send_mail


class GetDataTradeHistroy:
    def __init__(self):
        self.company_code_list = []  # 公司代码list
        self.mysqldb = mysqldb.CreateTable()
        self.except_cnt = 0  # 异常计数器
        self.mail_tolist = read_conf.ReadConf().get_options("mail_send", "mail_tolist")
        self.mail_host = read_conf.ReadConf().get_options("mail_send", "mail_host")
        self.mail_user = read_conf.ReadConf().get_options("mail_send", "mail_user")
        self.mail_password = read_conf.ReadConf().get_options("mail_send", "mail_password")
        self.mail_postfix = read_conf.ReadConf().get_options("mail_send", "mail_postfix")

    def get_company_code(self):
        company_data = tus.get_stock_basics()
        for index, row in company_data.iterrows():
            self.company_code_list.append(str(index))

    def get_trade_data(self, company_code_list, begin_date, end_date, autype,table_name):
        for i in range(0, len(company_code_list)):
            try:
                company_trade_histroy = tus.get_k_data(company_code_list[i], autype=autype, start=begin_date, end=end_date)
                print company_code_list[i]

                """ 获取参数 """
                print company_trade_histroy['date'].values
                print company_trade_histroy['open'].values
                print company_trade_histroy['close'].values
                print company_trade_histroy['high'].values
                print company_trade_histroy['low'].values
                print company_trade_histroy['volume'].values
                print "===================="

                for j in range(0, len(company_trade_histroy['date'])):
                    insert_sql = '\'' + str(company_code_list[i]) + '\'' + ','
                    insert_sql += '\'' + str(company_trade_histroy['date'].values[j]) + '\'' + ','
                    insert_sql += '\'' + str(company_trade_histroy['open'].values[j]) + '\'' + ','
                    insert_sql += '\'' + str(company_trade_histroy['high'].values[j]) + '\'' + ','
                    insert_sql += '\'' + str(company_trade_histroy['close'].values[j]) + '\'' + ','
                    insert_sql += '\'' + str(company_trade_histroy['low'].values[j]) + '\'' + ','
                    insert_sql += '\'' + str(company_trade_histroy['volume'].values[j]) + '\'' + ','
                    insert_sql += '\'' + str(0) + '\'' + ','
                    insert_sql = insert_sql[0:-1]  # 去除最后一个逗号
                    self.mysqldb.insert_data(table_name, insert_sql)
                    print insert_sql
            except Exception, e:
                self.except_cnt += 1
                print Exception, e
        #if self.except_cnt >= 4:
            #send_mail.send_mail(self.mail_tolist, self.mail_host, self.mail_user, self.mail_password, self.mail_postfix, "tushare_GetDataTradeHistroy_error", "exception_cnt:%s" % self.except_cnt)
        # print company_trade_histroy

if __name__ == '__main__':
    test = GetDataTradeHistroy()
    test.get_company_code()
    # test.get_trade_data()

