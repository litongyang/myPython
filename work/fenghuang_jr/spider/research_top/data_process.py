# __author__ = 'lty'
# -*- coding: utf-8 -*-

"""
研究人员预测排名
对东方财富爬取的研报进行数据预处理
"""

import MySQLdb


class DataProcess:
    def __init__(self):
        self.db_name = 'test'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                    port=self.db_port)

        self.cur = self.conn.cursor()
        self.research_table_name = 'dongfang_research_test'
        self.research_process_table_name = 'dongfang_research_process'

    def data_process(self):
        try:
            self.cur.execute('set names \'utf8\'')
            count = self.cur.execute("SELECT * FROM %s" % self.research_table_name)
            results = self.cur.fetchmany(count)
            for i in range(0, len(results)):
            # for i in range(0, 10):
                author_tmp = results[i][8].split(',')
                for k in range(0, len(author_tmp)):
                    tmp = []  # 一行数据
                    for j in range(0, len(results[i])):
                        if j != 8:
                            tmp.append(results[i][j])
                        if j == 8:
                            tmp.append(author_tmp[k])

                    insert_sql = ''
                    for k1 in range(0, len(tmp)):
                        insert_sql += '\'' + str(tmp[k1]) + '\'' + ','
                    insert_sql = insert_sql[0:-1]  # 去除最后一个逗号
                    print insert_sql
                    self.cur.execute("insert into %s values(%s)" % (self.research_process_table_name, insert_sql))
                    # for v in tmp:
                    #     print v
                    # print "======"

        except Exception, e:
            error_info = Exception, e
            print error_info

if __name__ == '__main__':
    data_process = DataProcess()
    data_process.data_process()
