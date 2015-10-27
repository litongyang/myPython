# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# -----------------------------------------
# 获取不存在公司的代码
# -------------------------------------------

from __future__ import division
import MySQLdb
import os
import shutil


class CompanyCodeNonExit:
	def __init__(self):
		self.Company_code = []
		self.Company_code_noexit = []
		self.db_name = 'mystock'  # 数据库名,如果与现有数据库冲突，可改为其他名字
		self.db_host = 'localhost'  # 主机名
		self.db_port = 3306  # 端口号
		self.username = 'root'  # 用户名
		self.password = '123'  # 密码

	# -------------------找到存在的公司代码-------------------------

	def find_company_code_exit(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT Company_Code FROM  company_code ")
			results = cur.fetchmany(count)
			for i in range(len(results)):
				self.Company_code.append(results[i][0])
		except:
			pass

	# -------------------找到不存在的公司代码-------------------------
	def find_company_code_non_exit(self):
		count = 1
		i = 0
		while i < len(self.Company_code):
			if (1100 <= count < 1600) or (3000 < count <= 300000) or (301000 < count <= 599999) or (602000 < count <= 602999):
				count += 1
				continue
			if self.Company_code[i] != count:
				self.Company_code_noexit.append(count)
				count += 1
			else:
				i += 1
				count += 1

	# -------将不存在公司的代码写入文件---------

	def write_company_code_non_exit(self):
		fl = open("/Users/litongyang/Desktop/company_code_noexit(20150518).txt", 'a')
		for i in range(len(self.Company_code_noexit)):
			fl.write(str("%06d" % self.Company_code_noexit[i]))
			fl.write('\t')

	# ----------删除不存在公司的文件----------
	def delete_company_code_non_exit(self):
		for i in range(len(self.Company_code_noexit)):
			if os.path.isdir("/Users/litongyang/Desktop/data_2014/" + str("%06d" % self.Company_code_noexit[i])):
				try:
					shutil.rmtree("/Users/litongyang/Desktop/data_2014/" + str("%06d" % self.Company_code_noexit[i]),
					              True)
					print "%s file is deleted!" % str("%06d" % self.Company_code_noexit[i])
				except:
					pass


if __name__ == '__main__':
	company_code_noexit = CompanyCodeNonExit()
	company_code_noexit.find_company_code_exit()
	company_code_noexit.find_company_code_non_exit()
# company_code_noexit.write_company_code_non_exit()
# company_code_noexit.delete_company_code_non_exit()
