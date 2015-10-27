# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

import Stock.company_code_noexit.find_company_code_noexit as find_company_code_noexit
import MySQLdb

class ProcessTableNonExit():
	def __init__(self):
		self.db_name = 'mystock'  # 数据库名,如果与现有数据库冲突，可改为其他名字
		self.db_host = 'localhost'  # 主机名
		self.db_port = 3306  # 端口号
		self.username = 'root'  # 用户名
		self.password = '123'  # 密码

	def process_table_non_exit(self):
		company_code_non_exit = find_company_code_noexit.CompanyCodeNonExit()
		company_code_non_exit.find_company_code_exit()
		company_code_non_exit.find_company_code_non_exit()
		print company_code_non_exit.Company_code_noexit

if __name__ == '__main__':
	process_table = ProcessTableNonExit()
	process_table.process_table_non_exit()