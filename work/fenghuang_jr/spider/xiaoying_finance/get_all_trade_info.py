# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import sys
import time
import json
import urllib2
import create_table
reload(sys)
sys.setdefaultencoding('utf-8')


class GetAllTradeInfo:
    def __init__(self):
        self.create_table = create_table.CreateTable()
        self.url = 'https://www.xiaoying.com/index/apiStats?_fromAjax_=1&_csrfToken_=d41d8cd98f00b204e9800998ecf8427e&_=1465109002260'

    def get_data(self):
        data = urllib2.urlopen(self.url).read()
        data_json = json.loads(data)
        for k, v in data_json.items():
            if k == 'data':
                tmp = [0] * 2
                for k1, v1 in v.items():
                    if k1 == 'totalInvest':
                        tmp[0] = str(v1)
                    if k1 == 'totalInvestProfit':
                        tmp[1] = str(v1)
                time_stamp_tmp = time.time()
                time_array = time.localtime(time_stamp_tmp)
                time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
                insert_sql = '\'' + time_stamp + '\'' + ','
                for i in range(0, len(tmp)):
                    insert_sql += '\'' + str(tmp[i]).encode("utf-8") + '\'' + ','
                insert_sql = insert_sql[0:-1]  # 去除最后一个逗号
                print insert_sql
                self.create_table.cur.execute('set names \'utf8\'')
                self.create_table.cur.execute("insert into %s values(%s)" % (self.create_table.table_name_total, insert_sql))

if __name__ == '__main__':
    get_all_trade_info = GetAllTradeInfo()
    get_all_trade_info.get_data()