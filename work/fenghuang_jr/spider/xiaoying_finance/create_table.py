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
        self.table_name_product = 'xiaoying_finance_product'
        self.table_name_total = 'xiaoying_finance_total'
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name, port=self.db_port)
        self.cur = self.conn.cursor()

    def create_product_table(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.table_name_product)
            self.cur.execute(
                    "CREATE TABLE IF NOT EXISTS %s "
                    "("
                    "timestamp varchar(100) comment '时间戳',"
                    "title varchar(100) comment '产品名称',"
                    "identify varchar(100) comment '产品标识区分',"
                    "upper_limit_amount varchar(100) comment '投资额上限',"
                    "profit_ratio varchar(20) comment '到期收益率',"
                    "invest_cycle varchar(50) comment '投资周期',"
                    "repay_method varchar(50) comment '还款方式',"
                    "lowest_limit_amount varchar(50) comment '起投金额',"
                    "financing_total varchar(50) comment '融资总额',"
                    "interest_time_info   varchar(100) comment '起息时间说明',"
                    "safeguard_method varchar(20) comment '保障方式',"
                    "invested_cnt int comment '已投笔数',"
                    "additional_amount varchar(200) comment '剩余金额',"
                    "speed_invest varchar(20) comment '投资进度',"
                    "is_invest_info varchar(20) comment '是否可以投资说明',"
                    "PRIMARY KEY (`title`,`timestamp`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                    % self.table_name_product)
        except Exception, e:
            print Exception, e

    def create_total_trade_table(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.table_name_total)
            self.cur.execute(
                    "CREATE TABLE IF NOT EXISTS %s "
                    "("
                    "timestamp varchar(100) comment '时间戳',"
                    "total_invest double comment '累计交易额元',"
                    "earn_amount double comment '以为用户赚取总额元',"
                    "PRIMARY KEY (`timestamp`,`total_invest`,`earn_amount`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                    % self.table_name_total)
        except Exception, e:
            print Exception, e


if __name__ == '__main__':
    test = CreateTable()
    test.create_product_table()
    test.create_total_trade_table()
