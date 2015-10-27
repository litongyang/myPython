# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

import MySQLdb


class PARAMETER_ANALYSIS():
	def __init__(self):
		self.net_profit = []  # 净利润
		self.business_income = []  # 营业收入
		self.nonbusiness_income = []  # 营业外收入
		self.total_profit = []  # 利润总额
		self.interest_expense = []  # 利息支出(有些公司没有此项)
		self.total_assets_avg = []  # 总资产平均值
		self.business_profit = []  # 营业利润
		self.cost_in_business = []  # 营业成本
		self.remainder = []  # 存货
		self.remainder_avg = []  # 存货平均值
		self.accounts_receivable_avg = []  # 应收账款平均值
		self.liquid_assets = []  # 流动资产
		self.current_liabilities = []  # 流动负债
		self.cash = []  # 货币资金
		self.trading_financial_assets = []  # 交易性金融资产
		self.Net_operating_cash_flow = []  # 经营现金流量净额
		self.total_liabilities = []  # 负债总额
		self.shareholders_equity = []  # 股东权益
		self.intangible_assets = []  # 无形资产

		self.ROE = []  # 净资产收益率
		self.Gross_margin = []  # 销售毛利率
		self.Sales_net_profit_rate = []  # 销售净利率
		self.Rate_of_return_on_total_assets = []  # 总资产回报率
		self.Rate_of_return_on_assets = []  # 资产报酬率
		self.Main_business_profit_rate = []  # 主营业务利润率
		self.Inventory_turnover_days = []  # 存货周转天数
		self.Total_assets_turnover_days = []  # 总资产周转天数
		self.Accounts_receivable_turnover_days = []  # 应收账款周转天数
		self.Business_cycle = []  # 营业周期
		self.Quick_ratio = []  # 速动比率
		self.Cash_ratio = []  # 现金比率
		self.Cash_liabilities_rate = []  # 现金负债总额比
		self.Rate_of_assets_and_liabilities = []  # 资产负债率
		self.Equity_ratio = []  # 产权比率
		self.Debt_to_tangible_assets_ratio = []  # 有形净值债务率
		self.Operating_profit_ratio = []  # 营业利润比率
		# self.Revised_revenue_realization_rate = []  # 修正后的收益变现率
		self.Sales_revenue_growth_rate = []  # 销售收入增长率
		self.Pre_tax_profit_growth_rate = []  # 税前利润增长率
		self.Total_assets_growth_rate = []  # 总资产增长率
		self.Asset_growth_rate = []  # 净资产增长率
		self.Net_profit_growth_rate = []  # 净利润增长率

		self.Company_code = 1  # 600741
		self.data_file = 'stock_' + str("%06d" % self.Company_code)
		self.fileName = 'parameters_' + str("%06d" % self.Company_code)

		self.db_name = 'STOCK_INFO_2014'  # 数据库名,如果与现有数据库冲突，可改为其他名字
		self.db_host = 'localhost'  # 主机名
		self.db_port = 3306  # 端口号
		self.username = 'root'  # 用户名
		self.password = '123'  # 密码

	# -------------------净资产收益率--------------------------

	def Parameter_ROE(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			# y = "SELECT * FROM %s WHERE SUBJECT='净资产收益率'" % self.data_file
			# print y
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='净资产收益率'" % self.data_file)
			results = cur.fetchmany(count)
			print self.data_file
			if len(results) == 0:
				self.ROE = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.ROE.append(results[0][i])
			self.ROE = [round(self.ROE[i], 2) for i in range(0, len(self.ROE))]
			temp = "'1'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'净资产收益率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.ROE[j]) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			# x = "insert into %s values(%s)" % (self.fileName, temp)
			# print x
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except Exception, e:
			pass

	# -------------------销售毛利率--------------------------
	def Parameter_Gross_margin(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='销售毛利率'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.Gross_margin = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.Gross_margin.append(results[0][i])
			self.Gross_margin = [round(self.Gross_margin[i], 2) for i in range(0, len(self.Gross_margin))]
			temp = "'2'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'销售毛利率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Gross_margin[j]) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------销售净利率----------------------------
	# 公式:销售净利率=净利润/营业收入
	# ---------------------------------------------------------
	def Parameter_Sales_net_profit_rate(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='净利润'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.net_profit = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.net_profit.append(results[0][i] * 10000)
		except:
			pass

		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='营业收入'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.business_income = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					if results[0][i] != 0:
						self.business_income.append(results[0][i] * 10000)
					else:
						self.business_income.append(-1)
			self.Sales_net_profit_rate = [self.net_profit[i] / self.business_income[i] for i in
			                              range(0, len(self.business_income))]
			self.Sales_net_profit_rate = [round(self.Sales_net_profit_rate[i], 4) * 100 for i in
			                              range(0, len(self.Sales_net_profit_rate))]

			temp = "'3'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'销售净利率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Sales_net_profit_rate[j]) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------总资产回报率-----------------------------------------
	# 公式:总资产报酬率=（利润总额+利息支出）/总资产平均值
	# 公式:总资产平均值=（期初资产总额+期末资产总额）÷2
	# ----------------------------------------------------------------------
	def Parameter_Rate_of_return_on_total_assets(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='利润总额'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.total_profit = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.total_profit.append(results[0][i] * 10000)
		except:
			pass

		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='应付利息'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.interest_expense = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.interest_expense.append(results[0][i] * 10000)
		except:
			pass

		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='资产总计'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.total_assets_avg = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					if (results[0][i] + results[0][i + 1]) / 2 * 10000 != 0:
						self.total_assets_avg.append((results[0][i] + results[0][i + 1]) / 2 * 10000)
					else:
						self.total_assets_avg.append(-1)
			temp1 = [self.total_profit[i] + self.interest_expense[i] for i in range(0, len(self.total_profit))]
			self.Rate_of_return_on_total_assets = [temp1[i] / self.total_assets_avg[i] for i in
			                                       range(0, len(self.total_assets_avg))]
			self.Rate_of_return_on_total_assets = [round(self.Rate_of_return_on_total_assets[i], 4) * 100 for i in
			                                       range(0, len(self.Rate_of_return_on_total_assets))]
			temp = "'4'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'总资产回报率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Rate_of_return_on_total_assets[j]) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------资产报酬率---------------------------------------
	# 公式:资产报酬率=利润总额/总资产平均值
	# 公式:总资产平均值=（期初资产总额+期末资产总额）÷2
	# ------------------------------------------------------------------
	def Parameter_Rate_of_return_on_assets(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			self.Rate_of_return_on_assets = [self.total_profit[i] / self.total_assets_avg[i] for i in
			                                 range(0, len(self.total_profit))]
			self.Rate_of_return_on_assets = [round(self.Rate_of_return_on_assets[i], 4) * 100 for i in
			                                 range(0, len(self.Rate_of_return_on_assets))]
			temp = "'5'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'资产报酬率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Rate_of_return_on_assets[j]) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------主营业务利润率----------------------------
	# 公式:主营业务利润率=营业利润/营业收入
	# -----------------------------------------------------------
	def Parameter_Main_business_profit_rate(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='营业利润'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.business_profit = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.business_profit.append(results[0][i] * 10000)
			self.Main_business_profit_rate = [self.business_profit[i] / self.business_income[i] for i in
			                                  range(0, len(self.business_income))]
			self.Main_business_profit_rate = [round(self.Main_business_profit_rate[i], 4) * 100 for i in
			                                  range(0, len(self.Main_business_profit_rate))]

			temp = "'6'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'主营业务利润率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Main_business_profit_rate[j]) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------存货周转天数----------------------------------------------
	# 公式:存货周转天数=365/存货周转率
	# 存货周转率=主营业务成本/存货平均余额
	# ---------------------------------------------------------------------------
	def Parameter_Inventory_turnover_days(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='营业成本'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.cost_in_business = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.cost_in_business.append(results[0][i] * 10000)
		except:
			pass
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='存货'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.remainder = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.remainder.append(results[0][i] * 10000)
					self.remainder_avg.append((results[0][i] + results[0][i + 1]) / 2 * 10000)
			temp1 = [self.cost_in_business[i] / self.remainder_avg[i] for i in range(0, len(self.cost_in_business))]
			self.Inventory_turnover_days = [int(365 / temp1[i]) for i in range(0, len(temp1))]

			temp = "'7'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'存货周转天数(天)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Inventory_turnover_days[j]) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------总资产周转天数---------------------------------------
	# 公式:总资产周转天数=365/总资产周转次数
	# 总资产周转次数=主营业务收入(销售收入)/总资产资产平均余额
	# ----------------------------------------------------------------------
	def Parameter_Total_assets_turnover_days(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			temp1 = [self.business_income[i] / self.total_assets_avg[i] for i in range(0, len(self.business_income))]
			self.Total_assets_turnover_days = [int(365 / temp1[i]) for i in range(0, len(temp1))]
			temp = "'8'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'总资产周转天数(天)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Total_assets_turnover_days[j]) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------应收账款周转天数---------------------------------------
	# 公式:应收账款周转天数=365/应收账款周转率
	# 应收账款周转率=当期销售净收入(销售收入)/应收账款平均余额
	# ------------------------------------------------------------------------
	def Parameter_Accounts_receivable_turnover_days(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='应收账款'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.accounts_receivable_avg = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.accounts_receivable_avg.append((results[0][i] + results[0][i + 1]) / 2 * 10000)
			temp1 = [self.business_income[i] / self.accounts_receivable_avg[i] for i in
			         range(0, len(self.accounts_receivable_avg))]
			self.Accounts_receivable_turnover_days = [365 / temp1[i] for i in range(0, len(temp1))]
			self.Accounts_receivable_turnover_days = [round(self.Accounts_receivable_turnover_days[i], 2) for i in
			                                          range(0, len(self.Accounts_receivable_turnover_days))]

			temp = "'9'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'应收账款周转天数(天)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Accounts_receivable_turnover_days[j]) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------------营业周期----------------------------------------------
	# 公式:营业周期=应收账款周转天数+存货周转天数
	# ------------------------------------------------------------------------------
	def Parameter_Business_cycle(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			self.Business_cycle = [self.Inventory_turnover_days[i] + self.Accounts_receivable_turnover_days[i] for i in
			                       range(0, len(self.accounts_receivable_avg))]
			temp = "'10'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'营业周期(天)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Business_cycle[j]) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号

			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------------速动比率----------------------------------------------
	# 公式:速动比率=（流动资产-存货）/流动负债
	# ------------------------------------------------------------------------------
	def Parameter_Quick_ratio(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='流动资产合计'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.accounts_receivable_avg = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.liquid_assets.append(results[0][i] * 10000)

		except:
			pass
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='流动负债合计'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.current_liabilities = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.current_liabilities.append(results[0][i] * 10000)

			temp1 = [self.liquid_assets[i] - self.remainder[i] for i in range(0, len(self.liquid_assets))]
			Quick_ratio = [temp1[i] / self.current_liabilities[i] for i in range(0, len(temp1))]

			temp = "'11'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'速动比率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(Quick_ratio[j] * 100) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))

		except:
			pass

	# -------------------现金比率----------------------------------------------
	# 公式:现金比率=货币资金(或现金等价物)+交易性金融资产/流动负债
	# -------------------------------------------------------------------------
	def Parameter_Cash_ratio(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='货币资金'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.cash = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.cash.append(results[0][i] * 10000)
		except:
			pass

		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='交易性金融资产'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.trading_financial_assets = [0 for i in range(10)]
			else:
				for i in range(3, 13):
					self.trading_financial_assets.append(results[0][i] * 10000)
			temp1 = [self.cash[i] + self.trading_financial_assets[i] for i in range(0, len(self.cash))]
			self.Cash_liabilities_rate = [temp1[i] / self.current_liabilities[i] for i in
			                              range(0, len(self.current_liabilities))]

			temp = "'12'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'现金比率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Cash_liabilities_rate[j] * 100) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------现金负债总额比----------------------------------------------
	# 公式:现金负债总额比=经营活动现金净流量/期末负债总额
	# -------------------------------------------------------------------------------
	def Parameter_Cash_liabilities_rate(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='经营现金流量净额'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.Net_operating_cash_flow = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.Net_operating_cash_flow.append(results[0][i] * 10000)
		except:
			pass

		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='负债合计'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.total_liabilities = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.total_liabilities.append(results[0][i] * 10000)
			self.Cash_liabilities_rate = [self.Net_operating_cash_flow[i] / self.total_liabilities[i] for i in
			                              range(0, len(self.cash))]  # Net_operating_cash_flow;

			temp = "'13'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'现金负债总额比(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Cash_liabilities_rate[j] * 100) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))

		except:
			pass

	# ----------------------------资产负债率--------------------------------------------
	def Parameter_Rate_of_assets_and_liabilities(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='资产负债比率'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.Rate_of_assets_and_liabilities = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.Rate_of_assets_and_liabilities.append(results[0][i])
			temp = "'14'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'资产负债率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Rate_of_assets_and_liabilities[j]) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# --------------------------产权比率---------------------------------------------
	# 公式:产权比率=负债总额/股东权益
	# -------------------------------------------------------------------------------
	def Parameter_Equity_ratio(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='股东权益合计'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.shareholders_equity = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.shareholders_equity.append(results[0][i] * 10000)
			self.Equity_ratio = [self.total_liabilities[i] / self.shareholders_equity[i] for i in
			                     range(0, len(self.total_liabilities))]
			temp = "'15'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'产权比率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Equity_ratio[j] * 100) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# --------------------------有形净值债务率---------------------------------------------
	# 公式:有形净值债务率=负债总额/（股东权益-无形资产净值）
	# -------------------------------------------------------------------------------------
	def Parameter_Debt_to_tangible_assets_ratio(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='无形资产'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.intangible_assets = [0 for i in range(10)]
			else:
				for i in range(3, 13):
					self.intangible_assets.append(results[0][i] * 10000)
			self.Debt_to_tangible_assets_ratio = [self.shareholders_equity[i] - self.intangible_assets[i] for i in
			                                      range(0, len(self.shareholders_equity))]
			self.Debt_to_tangible_assets_ratio = [self.total_liabilities[i] / self.Debt_to_tangible_assets_ratio[i] for
			                                      i in range(0, len(self.total_liabilities))]
			temp = "'16'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'有形净值债务率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Debt_to_tangible_assets_ratio[j] * 100) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# --------------------------营业利润比率---------------------------------------------
	# 公式:营业利润比率=营业利润/利润总额
	# ----------------------------------------------------------------
	def Parameter_Operating_profit_ratio(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			self.Operating_profit_ratio = [self.business_profit[i] / self.total_profit[i] for i in
			                               range(0, len(self.business_profit))]
			temp = "'17'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'营业利润比率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Operating_profit_ratio[j] * 100) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------销售收入增长率----------------------------
	# 公式:销售收入增长率=(本年营业收入-上年营业收入)/上年营业收入
	# ------------------------------------------------------------
	def Parameter_Sales_revenue_growth_rate(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='营业收入'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.Sales_revenue_growth_rate = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.Sales_revenue_growth_rate.append((results[0][i] - results[0][i + 1]) / results[0][i + 1])
			temp = "'18'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'销售收入增长率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Sales_revenue_growth_rate[j] * 100) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------税前利润增长率----------------------------
	# 公式:税前利润增长率=(本年利润总额-上年利润总额)/上年利润总额
	# -------------------------------------------------------------
	def Parameter_Pre_tax_profit_growth_rate(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='利润总额'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.Pre_tax_profit_growth_rate = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.Pre_tax_profit_growth_rate.append((results[0][i] - results[0][i + 1]) / results[0][i + 1])
			temp = "'19'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'税前利润增长率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Pre_tax_profit_growth_rate[j] * 100) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------总资产增长率----------------------------
	# 公式:总资产增长率=(本年资产总计-上年资产总计)/上年资产总计
	# ---------------------------------------------------------
	def Parameter_Total_assets_growth_rate(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='资产总计'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.Total_assets_growth_rate = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.Total_assets_growth_rate.append((results[0][i] - results[0][i + 1]) / results[0][i + 1])
			temp = "'20'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'总资产增长率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Total_assets_growth_rate[j] * 100) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------净资产增长率----------------------------------
	# 公式:净资产增长率=(本年每股净资产-上年每股净资产)/上年每股净资产
	# ----------------------------------------------------------------
	def Parameter_Asset_growth_rate(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='每股净资产'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.Asset_growth_rate = [-1 for i in range(10)]
			else:
				for i in range(3, 13):
					self.Asset_growth_rate.append((results[0][i] - results[0][i + 1]) / results[0][i + 1])
			temp = "'21'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'净资产增长率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Total_assets_growth_rate[j] * 100) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------净利润增长率----------------------------------
	def Parameter_Net_profit_growth_rate(self):
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
			                       port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			count = cur.execute("SELECT * FROM %s WHERE SUBJECT='净利润同比增长率'" % self.data_file)
			results = cur.fetchmany(count)
			if len(results) == 0:
				self.Net_profit_growth_rate = [0 for i in range(10)]
			else:
				for i in range(3, 13):
					self.Net_profit_growth_rate.append(results[0][i])
			temp = "'22'" + ',' + '\'' + str("%06d" % self.Company_code) + '\'' + ',' + "'净利润增长率(%)'" + ','
			for j in range(0, 10):
				temp += '\'' + str(self.Net_profit_growth_rate[j]) + '\'' + ','
			temp = temp[0:-1]  # 去除最后一个逗号
			cur.execute("insert into %s values(%s)" % (self.fileName, temp))
		except:
			pass

	# -------------------清空函数----------------------------------
	def Parameter_Clear_fun(self):
		self.net_profit = []  # 净利润
		self.business_income = []  # 营业收入
		self.nonbusiness_income = []  # 营业外收入
		self.total_profit = []  # 利润总额
		self.interest_expense = []  # 利息支出(有些公司没有此项)
		self.total_assets_avg = []  # 总资产平均值
		self.business_profit = []  # 营业利润
		self.cost_in_business = []  # 营业成本
		self.remainder = []  # 存货
		self.remainder_avg = []  # 存货平均值
		self.accounts_receivable_avg = []  # 应收账款平均值
		self.liquid_assets = []  # 流动资产
		self.current_liabilities = []  # 流动负债
		self.cash = []  # 货币资金
		self.trading_financial_assets = []  # 交易性金融资产
		self.Net_operating_cash_flow = []  # 经营现金流量净额
		self.total_liabilities = []  # 负债总额
		self.shareholders_equity = []  # 股东权益
		self.intangible_assets = []  # 无形资产

		self.ROE = []  # 净资产收益率
		self.Gross_margin = []  # 销售毛利率
		self.Sales_net_profit_rate = []  # 销售净利率
		self.Rate_of_return_on_total_assets = []  # 总资产回报率
		self.Rate_of_return_on_assets = []  # 资产报酬率
		self.Main_business_profit_rate = []  # 主营业务利润率
		self.Inventory_turnover_days = []  # 存货周转天数
		self.Total_assets_turnover_days = []  # 总资产周转天数
		self.Accounts_receivable_turnover_days = []  # 应收账款周转天数
		self.Business_cycle = []  # 营业周期
		self.Quick_ratio = []  # 速动比率
		self.Cash_ratio = []  # 现金比率
		self.Cash_liabilities_rate = []  # 现金负债总额比
		self.Rate_of_assets_and_liabilities = []  # 资产负债率
		self.Equity_ratio = []  # 产权比率
		self.Debt_to_tangible_assets_ratio = []  # 有形净值债务率
		self.Operating_profit_ratio = []  # 营业利润比率
		self.Revised_revenue_realization_rate = []  # 修正后的收益变现率
		self.Sales_revenue_growth_rate = []  # 销售收入增长率
		self.Pre_tax_profit_growth_rate = []  # 税前利润增长率
		self.Total_assets_growth_rate = []  # 总资产增长率
		self.Asset_growth_rate = []  # 净资产增长率
		self.Net_profit_growth_rate = []  # 净利润增长率


if __name__ == '__main__':

	Parameter = PARAMETER_ANALYSIS()
	for Parameter.Company_code in range(1, 604000):
		if (1100 <= Parameter.Company_code < 1600) or (3000 < Parameter.Company_code <= 300000) or (
				300400 < Parameter.Company_code <= 599999) or (602000 < Parameter.Company_code <= 602999):
			continue
		Parameter.data_file = 'stock_' + str("%06d" % Parameter.Company_code)
		Parameter.fileName = 'parameters_' + str("%06d" % Parameter.Company_code)
		Parameter.Parameter_ROE()
		Parameter.Parameter_Gross_margin()
		Parameter.Parameter_Sales_net_profit_rate()
		Parameter.Parameter_Rate_of_return_on_total_assets()
		Parameter.Parameter_Rate_of_return_on_assets()
		Parameter.Parameter_Main_business_profit_rate()
		Parameter.Parameter_Inventory_turnover_days()
		Parameter.Parameter_Total_assets_turnover_days()
		Parameter.Parameter_Accounts_receivable_turnover_days()
		Parameter.Parameter_Business_cycle()
		Parameter.Parameter_Quick_ratio()
		Parameter.Parameter_Cash_ratio()
		Parameter.Parameter_Cash_liabilities_rate()
		Parameter.Parameter_Rate_of_assets_and_liabilities()
		Parameter.Parameter_Equity_ratio()
		Parameter.Parameter_Debt_to_tangible_assets_ratio()
		Parameter.Parameter_Operating_profit_ratio()
		Parameter.Parameter_Sales_revenue_growth_rate()
		Parameter.Parameter_Pre_tax_profit_growth_rate()
		Parameter.Parameter_Total_assets_growth_rate()
		Parameter.Parameter_Asset_growth_rate()
		Parameter.Parameter_Net_profit_growth_rate()
		Parameter.Parameter_Clear_fun()
		Parameter.Company_code += 1
