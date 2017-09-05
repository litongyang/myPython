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
        self.zhouheiya_area_dict = 'zhouheiya_area_dict'
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                    port=self.db_port)
        self.cur = self.conn.cursor()

    def create_table_zhouheiya_area_dict(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.zhouheiya_area_dict)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "province varchar(20) comment '省,直辖市名称',"
                "province_id varchar(100) comment '省,直辖市id',"
                "city varchar(20) comment '城市名称',"
                "city_id varchar(20) comment '城市id',"
                "area varchar(20) comment '区名称',"
                "area_id varchar(20) comment '区id',"
                "PRIMARY KEY (`area_id`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.zhouheiya_area_dict)
        except Exception, e:
            print Exception, e

if __name__ == '__main__':
    test = CreateTable()
    test.create_table_zhouheiya_area_dict()

