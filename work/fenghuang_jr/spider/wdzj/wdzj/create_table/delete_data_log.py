# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-
"""
删除历史数据
"""

import MySQLdb
import time
import datetime

class DeleteDataLog:
    def __init__(self):
        """
        self.db_name = 'spider'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = '10.10.202.16'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '1234abcd'  # 密码
        """
        self.db_name = 'test'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.now_time = datetime.datetime.now()
        self.yes_time = self.now_time + datetime.timedelta(days=-1)
        self.yes_date = self.yes_time.strftime('%Y-%m-%d')  # 昨天
        # self.time_stamp_tmp = time.time()
        # self.time_array = time.localtime(self.time_stamp_tmp)
        # self.date = time.strftime("%Y-%m-%d", self.time_array)
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                    port=self.db_port)
        self.cur = self.conn.cursor()
        self.table_list = [
            'wdzj_preference_info',
            'wdzj_basic_info_last90_type',
            'wdzj_basic_info_last90_deadline',
            'wdzj_basic_info_last90_amount',
            'wdzj_archives_interest_volume_daily',
            'wdzj_archives_repayment_inflow_daily',
            'wdzj_archives_invest_loan_daily'
        ]

    def delete__data(self):
        try:
            for v in self.table_list:
                self.cur.execute("delete from %s  where date<= %s" % (str(v), '\'' + self.yes_date + '\''))
        except Exception, e:
            print Exception, e
if __name__ == '__main__':
    delete_class = DeleteDataLog()
    delete_class.delete__data()