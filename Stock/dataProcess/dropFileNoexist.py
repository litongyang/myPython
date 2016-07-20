# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import MySQLdb
import os


class DropFileNoExist:
    def __init__(self):
        self.db_name = 'STOCK_INFO_2015'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.data_file = 'company_code'  # 已经存在的公司数据表
        self.code_exist = []  # 已存在的公司代码
        self.code_exist_not = []  # 不存在的公司代码
        self.file_code_no_exist = 'code_no_exist.txt'
        self.file_path = 'E:\\perl\\data(20160513)\\'

    def get_code_exist(self):
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT company_code FROM %s " % self.data_file)
            results = cur.fetchmany(count)
            for i in range(0, len(results)):
                self.code_exist.append(results[i][0])
        except Exception, e:
            print Exception, e

    def get_code_no_exist(self):
        count = 1
        i = 0
        while i < len(self.code_exist) and count <= 604000:
            if (1100 <= count < 1600) or (3000 < count <= 300000) or (301000 < count <= 599999) or (
                    602000 < count <= 602999):
                count += 1
                continue
            if str(self.code_exist[i]) == str("%06d" % count):
                i += 1
                count += 1
            else:
                self.code_exist_not.append(str("%06d" % count))
                count += 1
        fi = open(self.file_code_no_exist, 'w')
        for v in self.code_exist_not:
            fi.write(v)
            fi.write("\t")
        print self.code_exist_not

    def drop_file_no_exist(self):
        # for file in self.code_exist_not:
        try:
            for i in range(0, len(self.code_exist_not)):
                file_path = self.file_path + str(self.code_exist_not[i])
                if os.path.exists(file_path):
                    print file_path + "is dropped!"
                    os.system('rd /S /Q %s' % file_path)  # 删除整个文件夹
                else:
                    print file_path + " is not exist!"
                    pass
        except Exception, e:
            print Exception, e

        # todo :test fileCount
        # code_list = []
        # for parent,dirnames,filenames in os.walk(self.file_path):
        #     code = parent.split('\\')
        #     code_list.append(code[3])
        # print len(self.code_exist)
        # print len(code_list)
        # ret = list(set(self.code_exist) ^ set(code_list))  # 已存在的code和清洗后的code之间的差集
        # print ret

if __name__ == '__main__':
    drop_file = DropFileNoExist()
    drop_file.get_code_exist()
    drop_file.get_code_no_exist()
    drop_file.drop_file_no_exist()
