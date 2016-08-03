# __author__ = 'lty'
# -*- coding: utf-8 -*-

"""
得到每个股票的历史交易数据(向后复权)
"""
import tushare as tus


class GetDataTradeHistroy:
    def __init__(self):
        self.code = str(600009)

    def get_trade_data(self):
        start_date = tus.get_stock_basics().ix[self.code]['timeToMarket']  # 上市日期YYYYMMDD
        start_date = str(start_date)[0:4] + '-' + str(start_date)[4:6] + '-' + str(start_date)[6:8]
        print start_date
        x = tus.get_h_data(self.code, autype='hfq', start=start_date, end='2016-07-07')
        print x

if __name__ == '__main__':
    test = GetDataTradeHistroy()
    test.get_trade_data()
