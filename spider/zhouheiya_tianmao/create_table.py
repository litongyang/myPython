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
        self.zhouheiya_area_dict = 'zhouheiya_tianmao_url'
        self.zhouheiya_tianmao_bid = 'zhouheiya_tianmao_bid'
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                    port=self.db_port)
        self.cur = self.conn.cursor()

    def create_table_zhouheiya_tianmao_url(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.zhouheiya_area_dict)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "name varchar(100) comment '产品名称',"
                "url varchar(200) comment '产品url',"
                "count_all varchar(20) comment '产品销量',"
                "evaluate_cnt varchar(20) comment '产品评价数',"
                "PRIMARY KEY (`name`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.zhouheiya_area_dict)
        except Exception, e:
            print Exception, e

    def create_table_zhouheiya_tianmao_bid(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.zhouheiya_tianmao_bid)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "url varchar(200) comment '产品url',"
                "price double comment '产品url',"
                "sale_cnt int comment '产品月销量',"
                "sales  double comment '产品月销售总额',"
                "PRIMARY KEY (`url`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.zhouheiya_tianmao_bid)
        except Exception, e:
            print Exception, e

    def insert_sql(self, table_name, insert_sql):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("insert into %s values (%s)" % (table_name, insert_sql))
        except Exception, e:
            print Exception, e

if __name__ == '__main__':
    test = CreateTable()
    # test.create_table_zhouheiya_tianmao_url()
    test.create_table_zhouheiya_tianmao_bid()


