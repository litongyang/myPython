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
        self.table_name = 'jd_bid_info'
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                    port=self.db_port)
        self.cur = self.conn.cursor()

    # 利率和成交量的每日数据
    def create_table_jd_bid_info(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.table_name)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "id varchar(100) comment '产品id',"
                "title varchar(100) comment '产品名称',"
                "amount double comment '产品募集金额',"
                "buy_amount double comment '当前募集总额',"
                "merchant_id varchar(100) comment '经销商方ID',"
                "merchant_name varchar(100) comment '经销商方名称',"
                "insurance_code varchar(100) comment '担保方id',"
                "insurance_name varchar(100) comment '担保方名称',"
                "insurance_type varchar(50) comment '保险类型',"
                "insurance_type_name varchar(100) comment '保险类型名称',"
                "min_amount double comment '最小投资金额',"
                "max_amount double comment '最大投资金额',"
                "max_num int(8) comment '最大投资比数',"
                "days int(8) comment '期限',"
                "sale_begin_date varchar(50) comment '售卖开始时间',"
                "sale_end_date varchar(50) comment '售卖截止时间',"
                "rate double comment '历史收益率',"
                "refund_info varchar(200) comment '退款说明',"
                "is_support_part_refund int(3) comment '是否支持持有期之前退款',"
                "is_support_ins_append int(3) comment '是否支持追加',"
                "status int(10) comment '标的状态',"
                "ts varchar(20) comment '爬取时间',"
                "PRIMARY KEY (`id`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.table_name)
        except Exception, e:
            print Exception, e


if __name__ == '__main__':
    test = CreateTable()
    test.create_table_jd_bid_info()

    # test.create_table()
