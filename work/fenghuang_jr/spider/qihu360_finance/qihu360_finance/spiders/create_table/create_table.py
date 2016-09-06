# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import MySQLdb


class CreateTable:
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
        self.table_name = 'qihu360_bid_info'
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                    port=self.db_port)
        self.cur = self.conn.cursor()

    # 利率和成交量的每日数据
    def create_table_guomei_bid_info(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.table_name)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "url varchar(200) comment '产品详情url',"
                "title varchar(100) comment '产品名称',"
                "open_date varchar(50) comment '开标日期',"
                "ratio varchar(100) comment '预期收益率',"
                "days varchar(50) comment '期限',"
                "repay_method varchar(100) comment '收益方式',"
                "start_date varchar(100) comment '起息日期',"
                "end_date varchar(100) comment '到期日期',"
                "profit_date varchar(100) comment '发放日',"
                "available varchar(100) comment '当前可投资金额',"
                "amount varchar(100) comment '募集金额',"
                "min_amount_info varchar(100) comment '起投金额信息',"
                "ts varchar(20) comment '爬取时间',"
                "PRIMARY KEY (`url`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.table_name)
        except Exception, e:
            print Exception, e


if __name__ == '__main__':
    test = CreateTable()
    test.create_table_guomei_bid_info()

    # test.create_table()
