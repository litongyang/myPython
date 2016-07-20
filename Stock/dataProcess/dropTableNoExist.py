# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-
"""
删除不存在的公司的stock 和paramters 表
1.读取不存在公司的文本里所以公司代码
2.删除对应的stock和paramters数据表
"""
import MySQLdb


class DropTableNoExist:
    def __init__(self):
        self.code_no_exist = []  # 不存在公司的代码集合
        self.db_name = 'STOCK_INFO_2015'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                    port=self.db_port)
        self.cur = self.conn.cursor()

    def drop_table(self):
        for line in open('code_no_exist.txt'):
            self.code_no_exist = line.split()
        for i in range(0, len(self.code_no_exist)):
            try:
                table_stock = 'stock_' + str(self.code_no_exist[i])
                self.cur.execute("drop table if exists %s" % table_stock)
                print table_stock, " is droped !"
                table_paramters = 'parameters_' + str(self.code_no_exist[i])
                self.cur.execute("drop table if exists %s" % table_paramters)
                print table_paramters, " is droped !"
            except Exception, e:
                print Exception, e


if __name__ == '__main__':
    drop_table = DropTableNoExist()
    drop_table.drop_table()
