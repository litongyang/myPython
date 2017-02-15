# __author__ = 'lty'
# -*- coding: utf-8 -*-

import MySQLdb


class CreateTable:
    def __init__(self):

        self.db_name = 'user_value_predict'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = '10.10.202.24'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'search_db'  # 用户名
        self.password = 'abcd1234'  # 密码
        self.user_value_predict_result = 'user_value_predict_result'
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                    port=self.db_port)
        self.cur = self.conn.cursor()

    # 利率和成交量的每日数据
    def create_table_archives_interest_volume_daily(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.user_value_predict_result)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "user_id varchar(50) comment '用户id',"
                "predict_type varchar(20) comment '预测类型',"
                "predict_label varchar(20) comment '预测的结果',"
                "ts varchar(20) comment '入库时间戳',"
                "PRIMARY KEY (`user_id`,`predict_type`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.user_value_predict_result)
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

