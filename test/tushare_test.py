# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-
import tushare as ts
from sqlalchemy import create_engine

x = ts.get_h_data('600016', autype='hfq', start='2016-07-01', end='2016-07-07')  # 一次性获取全部日k线数据
# print type(x)
# engine = create_engine('mysql://root:123@127.0.0.1/test?charset=utf8')
# x.to_sql('get_h_data', engine)
x.to_json('600016.json', orient='columns')
# x = ts.get_today_all()
# print x