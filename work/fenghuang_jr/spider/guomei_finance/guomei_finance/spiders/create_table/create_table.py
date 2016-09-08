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
        self.table_name = 'guomei_bid_info'
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
                "id varchar(200) comment '产品id',"
                "title varchar(100) comment '产品名称',"
                "repay_method varchar(50) comment '偿还方式:BulletRepayment(一次性偿还)',"
                "amount double comment '产品募集金额',"
                "rate double comment '产品预期收益率',"
                "days int(8) comment '产品期限天数',"
                "min_amount double comment '最小投资金额',"
                "max_amount double comment '最大投资金额',"
                "step_amount double comment '每笔投资单位金额',"
                "time_open varchar(50) comment '开标时间',"
                "date_open varchar(20) comment '开标日期',"
                "time_finished varchar(50) comment '抓取日期date',"
                "bid_number int(9) comment '投资笔数',"
                "invest_amount double comment '投资金额',"
                "status varchar(20) comment '标的状态',"
                "invest_percent double comment '当前进度',"
                "available double comment '当前可投资金额',"
                "cooperative_name varchar(100) comment '合作机构名称',"
                "detail_url varchar(500) comment '公司详情页url',"
                "ts varchar(20) comment '爬取时间',"
                "PRIMARY KEY (`id`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.table_name)
        except Exception, e:
            print Exception, e


if __name__ == '__main__':
    test = CreateTable()
    test.create_table_guomei_bid_info()

    # test.create_table()
