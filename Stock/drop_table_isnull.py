# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

from __future__ import division
import MySQLdb
company_code_noexit = []

class DROP_TABLE_ISNULL():
	def __init__(self):
		self.Company_code = []
		self.Company_code_noexit = []
		self.db_name = 'STOCK_INFO_2014'  #数据库名,如果与现有数据库冲突，可改为其他名字
		self.db_host = 'localhost'  #主机名
		self.db_port = 3306  #端口号
		self.username = 'root'  #用户名
		self.password = '123'  #密码

	#------删除不存在公司的空表---------
	def drop_table_isnull(self):
		for line in open("/Users/litongyang/Desktop/perl/Data_Processing/company_code_noexit(20150518).txt"):
			content = line.replace("\n", "").split("\t")
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			for i in range(len(content)):
				company_code_noexit.append(content[i])
				data_file = 'parameters_'+ str(content[i])
				print data_file
				try:
					count = cur.execute("DROP TABLE %s" % data_file)
				except:
					pass
		except:
			pass

if __name__ == '__main__':
	downStockData_db = DROP_TABLE_ISNULL()
	downStockData_db.drop_table_isnull()