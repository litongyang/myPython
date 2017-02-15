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
# import read_conf as read_conf
# import send_mail as send_mail


class GetDataTradeHistroy:
    def __init__(self):
        self.time_stamp_tmp = time.time()
        self.time_array = time.localtime(self.time_stamp_tmp)
        self.date = time.strftime("%Y-%m-%d", self.time_array)  # 当前日期
        #self.date = '2016-11-15'
        self.company_code_list = []  # 公司代码list
        self.mysqldb = mysqldb.CreateTable()
        self.except_cnt = 0  #  异常计数器
        # self.mail_tolist = read_conf.ReadConf().get_options("mail_send", "mail_tolist")
        # self.mail_host = read_conf.ReadConf().get_options("mail_send", "mail_host")
        # self.mail_user = read_conf.ReadConf().get_options("mail_send", "mail_user")
        # self.mail_password = read_conf.ReadConf().get_options("mail_send", "mail_password")
        # self.mail_postfix = read_conf.ReadConf().get_options("mail_send", "mail_postfix")

        self.db_name = 'tradedata'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = ''  # 密码

    def get_company_code(self):
        company_data = tus.get_stock_basics()
        for index, row in company_data.iterrows():
            self.company_code_list.append(str(index))
        print len(self.company_code_list)

    def get_trade_data(self):
        for i in range(0, len(self.company_code_list)):
            try:
                # for i in range(2000, 2017):
                #     print str(i) + '-' + '01-01'
                #     print str(i) + '-' + '12-31'
                start_date = tus.get_stock_basics().ix[self.company_code_list[i]]['timeToMarket']  # 上市日期YYYYMMDD
                start_date = str(start_date)[0:4] + '-' + str(start_date)[4:6] + '-' + str(start_date)[6:8]
                company_trade_histroy = tus.get_k_data(self.company_code_list[i], autype='hfq', start='2016-12-22', end='2016-12-22')
                print self.company_code_list[i]
                # """ 获取日期 """
                # pydate_array = company_trade_histroy.index.to_pydatetime()
                # date_array = np.vectorize(lambda s: s.strftime('%Y-%m-%d'))(pydate_array)
                # date_series = pd.Series(date_array)
                # print date_series

                """ 获取参数 """
                print company_trade_histroy['date'].values
                print company_trade_histroy['open'].values
                print company_trade_histroy['close'].values
                print company_trade_histroy['high'].values
                print company_trade_histroy['low'].values
                print company_trade_histroy['volume'].values
                # print company_trade_histroy['amount'].values
                print "===================="

                # for j in range(0, len(company_trade_histroy['date'])):
                #     insert_sql = '\'' + str(self.company_code_list[i]) + '\'' + ','
                #     insert_sql += '\'' + str(company_trade_histroy['date'].values[j]) + '\'' + ','
                #     insert_sql += '\'' + str(company_trade_histroy['open'].values[j]) + '\'' + ','
                #     insert_sql += '\'' + str(company_trade_histroy['high'].values[j]) + '\'' + ','
                #     insert_sql += '\'' + str(company_trade_histroy['close'].values[j]) + '\'' + ','
                #     insert_sql += '\'' + str(company_trade_histroy['low'].values[j]) + '\'' + ','
                #     insert_sql += '\'' + str(company_trade_histroy['volume'].values[j]) + '\'' + ','
                #     insert_sql += '\'' + str(0) + '\'' + ','
                #     insert_sql = insert_sql[0:-1]  # 去除最后一个逗号
                #     self.mysqldb.insert_data(self.mysqldb.table_trade_history_data, insert_sql)
                #     print insert_sql
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
