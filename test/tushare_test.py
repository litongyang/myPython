# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-
import tushare as ts
import pandas.core.frame
from sqlalchemy import create_engine
# x = ts.get_stock_basics()
# for index, row in x.iterrows():
#     print index
print ts.get_stock_basics().ix['600016']['timeToMarket']
# print x1['code'].values
# print len(x1)
# df = ts.get_index()
x = ts.get_k_data('600016', autype='hfq', start='2012-12-21', end='2016-12-26')
print x['date'].values
print x['open'].values
# print df
# y = ts.get_today_all()
# print y
# x = ts.get_h_data('600016', autype='hfq', start='2002-12-21', end='2016-12-21')  # 一次性获取全部日k线数据
# print x
# print type(x)
# engine = create_engine('mysql://root:123@127.0.0.1/test?charset=utf8')
# x.to_sql('get_h_data', engine)
# print x.date
# x.to_json('600016.json', orient='columns', date_format='epoch')
# # x = ts.get_today_all()
# print x
