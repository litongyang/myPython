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
                "sku_id varchar(100) comment 'skuid',"
                "title varchar(100) comment '产品名称',"
                "amount double comment '产品募集金额',"
                "available double comment '当前可投资金额',"
                "next_open_date varchar(100) comment '下一次开标日期',"
                "item_type varchar(50) comment '产品类型id',"
                "type_name varchar(100) comment '产品类型名称',"
                "merchant_id varchar(100) comment '经销商ID',"
                "merchant_name varchar(100) comment '经销商名称',"
                "step_amount double comment '每笔投资单位金额',"
                "min_amount double comment '最小投资金额',"
                "max_amount double comment '最大投资金额',"
                "sale_begin_date varchar(50) comment '起售时间',"
                "sale_end_date varchar(50) comment '截止时间',"
                "begin_date varchar(50) comment '计息时间',"
                "end_date varchar(50) comment '到期时间',"
                "rate double comment '历史收益率',"
                "period_type varchar(20) comment '期限类型',"
                "period_value int(8) comment '期限值',"
                "status int(10) comment '标的状态',"
                "create_time varchar(50) comment '创建时间',"
                "update_time varchar(50) comment '更新时间',"
                "label_info varchar(100) comment '赎回说明',"
                "repayment_type int(2) comment '偿还类型',"
                "interest_type int(2) comment '利息类型',"
                "version_id int(8) comment '版本id',"
                "ts varchar(20) comment '爬取时间',"
                "PRIMARY KEY (`id`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.table_name)
        except Exception, e:
            print Exception, e


if __name__ == '__main__':
    test = CreateTable()
    test.create_table_jd_bid_info()

    # test.create_table()
