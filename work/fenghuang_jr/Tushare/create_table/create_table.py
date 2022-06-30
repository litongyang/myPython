# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import MySQLdb


class CreateTable:
    def __init__(self):

        self.db_name = 'test'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.table_trade_history_data = 'trade_history_data'
        self.table_trade_history_data_no = 'trade_history_data_no'
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                    port=self.db_port)
        self.cur = self.conn.cursor()

    # 利率和成交量的每日数据
    def create_table_archives_interest_volume_daily(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.table_trade_history_data)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "company_code varchar(20) comment '公司代码',"
                "date varchar(20) comment '交易日期',"
                "open float comment '开盘价',"
                "high float comment '最高价',"
                "close float comment '收盘价',"
                "low float comment '最低价',"
                "volume int(15) comment '成交量',"
                "amount int(20) comment '成交金额',"
                "PRIMARY KEY (`company_code`,`date`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.table_trade_history_data)
        except Exception, e:
            print Exception, e

    def insert_data(self, table_name, insert_sql):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("insert into %s values(%s)" % (table_name, insert_sql))
        except Exception, e:
            print Exception, e


if __name__ == '__main__':
    test = CreateTable()
    test.create_table_archives_interest_volume_daily()

