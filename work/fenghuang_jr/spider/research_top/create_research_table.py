# __author__ = 'lty'
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
        self.research_table_name = 'dongfang_research_process'

        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                    port=self.db_port)
        self.cur = self.conn.cursor()

    def create_table_research(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.research_table_name)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "company_code varchar(50) comment '公司id',"
                "company_name varchar(100) comment '公司名称',"
                "research_title varchar(200) comment '研报标题',"
                "research_date varchar(30) comment '研报日期',"
                "ins_name varchar(50) comment '机构名称',"
                "ins_star varchar(20) comment '机构等级',"
                "rating_name varchar(30) comment '评级名称',"
                "rating_change varchar(30) comment '评级变动',"
                "author varchar(30) comment '作者名称',"
                "profitYear varchar(20) comment '收益起始年份',"
                "pe_list varchar(100) comment '预测市盈率',"
                "per_share_list varchar(100) comment '预测每股收益',"
                "net_profit_list varchar(100) comment '预测净利润',"
                "research_url varchar(1000) comment '研报url',"
                "date varchar(30) comment '抓取日期',"
                "KEY (`company_code`,`research_title`,`research_date`,`ins_name`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.research_table_name)
        except Exception, e:
            print Exception, e


if __name__ == '__main__':
    test = CreateTable()
    test.create_table_research()
