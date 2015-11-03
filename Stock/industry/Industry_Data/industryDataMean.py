# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# 求在行业中需要求均值的参数的最后结果

import MySQLdb
import Stock.industry.Industry_Data.industryData as industryData


class IndustryDataMean:
	def __init__(self):
		self.db_name = 'STOCK_INFO_2014'  # 数据库名,如果与现有数据库冲突，可改为其他名字
		self.db_host = 'localhost'  # 主机名
		self.db_port = 3306  # 端口号
		self.username = 'root'  # 用户名
		self.password = '123'  # 密码
		self.year = 2014  # 数据库最新的年份
		self.company_industry_ratio_fileName = "company_industry_ratio"  # 数据表名

		self.gross_margin_mean_ratio_industry = {}  # 销售毛利率(行业每年均值)
		self.ROE_mean_ratio_industry = {}  # ROE(行业每年均值)
		self.Sales_net_profit_rate_mean_ratio_industry = {}  # 销售净利率(行业每年均值)
		self.Rate_of_return_on_total_assets_mean_ratio_industry = {}  # 总资产回报率(行业每年均值)
		self.Rate_of_return_on_assets_mean_ratio_industry = {}  # 资产报酬率(行业每年均值)
		self.Main_business_profit_rate_mean_ratio_industry = {}  # 主营业务利润率(行业每年均值)
		self.Inventory_turnover_days_mean_ratio_industry = {}  # 存货周转天数(行业每年均值)
		self.Total_assets_turnover_days_mean_ratio_industry = {}  # 总资产周转天数(行业每年均值)
		self.Accounts_receivable_turnover_days_mean_ratio_industry = {}  # 应收账款周转天数(行业每年均值)
		self.Business_cycle_mean_ratio_industry = {}  # 营业周期(行业每年均值)
		self.Quick_ratio_mean_ratio_industry = {}  # 速动比率(行业每年均值)
		self.Cash_ratio_mean_ratio_industry = {}  # 现金比率(行业每年均值)
		self.Cash_liabilities_rate_mean_ratio_industry = {}  # 现金负债总额比(行业每年均值)
		self.Rate_of_assets_and_liabilities_mean_ratio_industry = {}  # 资产负债率(行业每年均值)
		self.Equity_ratio_mean_ratio_industry = {}  # 产权比率(行业每年均值)
		self.Debt_to_tangible_assets_ratio_mean_ratio_industry = {}  # 有形净值债务率(行业每年均值)
		self.Operating_profit_ratio_mean_ratio_industry = {}  # 营业利润比率(行业每年均值)
		self.Sales_revenue_growth_rate_mean_ratio_industry = {}  # 销售收入增长率(行业每年均值)
		self.Pre_tax_profit_growth_rate_mean_ratio_industry = {} # 税前利润增长率(行业每年均值)
		self.Total_assets_growth_rate_mean_ratio_industry = {}  # 总资产增长率(行业每年均值)
		self.Asset_growth_rate_mean_ratio_industry = {}  # 净资产增长率(行业每年均值)
		self.Net_profit_growth_rate_mean_ratio_industry = {}  # 净利润增长率(行业每年均值)

		self.parameters_dictionary = {}  # 参数字典

	def parameters_mean_ratio(self, string, parameters_mean_ratio_year, year):
		industry = industryData.IndustryData()
		industry.divided_group_industry()
		try:
			conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
								   port=self.db_port)
			cur = conn.cursor()
			cur.execute('set names \'utf8\'')
			for key, value in industry.company_industry.items():
				string_mean_ratio = []  # 某参数全行业的包含每个年份的加权平均值
				year = 2014
				for j in range(3, 13):
					# print year
					string_mean_ratio_year = 0  # 某参数全行业某年的加权均值
					for i in range(0, len(value)):
						stock_name = 'parameters_' + value[i]
						try:
							count = cur.execute(
								"SELECT industry_ratio FROM %s " % self.company_industry_ratio_fileName +
								"WHERE company_code=" + '\'' + value[i] + '\'' + "and year=" + '\'' + str(
									year) + '\'')
							results = cur.fetchmany(count)
							try:
								count1 = cur.execute(
									"SELECT * FROM %s " % stock_name + "WHERE Parameters=" + '\'' + string + '\'')
								results1 = cur.fetchmany(count1)
								# print len(results1)
								if len(results1) == 0:
									pass
								else:
									# print "key,code,year,ratio,string::", key, value[i], year, results[0][0], \
									# 	results1[0][j]
									string_mean_ratio_year += results[0][0] * results1[0][j]
							except Exception, e:
								pass
							# print Exception,":",e
						except Exception, e:
							pass
						# print Exception,":",e
					string_mean_ratio.append(string_mean_ratio_year)
					year -= 1
				parameters_mean_ratio_year[key] = string_mean_ratio
				print string, key, string_mean_ratio

		except Exception, e:
			pass
		# print Exception,":",e

	# 构建参数字典
	def create_parameters_dictionary(self):
		self.parameters_dictionary["销售毛利率(%)"] = self.gross_margin_mean_ratio_industry
		self.parameters_dictionary["净资产收益率(%)"] = self.ROE_mean_ratio_industry
		self.parameters_dictionary["销售净利率(%)"] = self.Sales_net_profit_rate_mean_ratio_industry
		self.parameters_dictionary["总资产回报率(%)"] = self.Rate_of_return_on_total_assets_mean_ratio_industry
		self.parameters_dictionary["资产报酬率(%)"] = self.Rate_of_return_on_assets_mean_ratio_industry
		self.parameters_dictionary["主营业务利润率(%)"] = self.Main_business_profit_rate_mean_ratio_industry
		self.parameters_dictionary["存货周转天数(天)"] = self.Inventory_turnover_days_mean_ratio_industry
		self.parameters_dictionary["总资产周转天数(天)"] = self.Total_assets_turnover_days_mean_ratio_industry
		self.parameters_dictionary["应收账款周转天数(天)"] = self.Accounts_receivable_turnover_days_mean_ratio_industry
		self.parameters_dictionary["营业周期(天)"] = self.Business_cycle_mean_ratio_industry
		self.parameters_dictionary["速动比率(%)"] = self.Quick_ratio_mean_ratio_industry
		self.parameters_dictionary["现金比率(%)"] = self.Cash_ratio_mean_ratio_industry
		self.parameters_dictionary["现金负债总额比(%)"] = self.Rate_of_assets_and_liabilities_mean_ratio_industry
		self.parameters_dictionary["资产负债率(%)"] = self.Quick_ratio_mean_ratio_industry
		self.parameters_dictionary["产权比率(%)"] = self.Equity_ratio_mean_ratio_industry
		self.parameters_dictionary["有形净值债务率(%)"] = self.Debt_to_tangible_assets_ratio_mean_ratio_industry
		self.parameters_dictionary["营业利润比率(%)"] = self.Operating_profit_ratio_mean_ratio_industry
		self.parameters_dictionary["销售收入增长率(%)"] = self.Sales_revenue_growth_rate_mean_ratio_industry
		self.parameters_dictionary["税前利润增长率(%)"] = self.Pre_tax_profit_growth_rate_mean_ratio_industry
		self.parameters_dictionary["总资产增长率(%)"] = self.Total_assets_growth_rate_mean_ratio_industry
		self.parameters_dictionary["净资产增长率(%)"] = self.Asset_growth_rate_mean_ratio_industry
		self.parameters_dictionary["净利润增长率(%)"] = self.Net_profit_growth_rate_mean_ratio_industry
		# for key, value in self.paramters_dictionary.items():
		# 	print key,value

if __name__ == '__main__':
	industryDataMean = IndustryDataMean()
	industryDataMean.create_parameters_dictionary()
	for key, value in industryDataMean.parameters_dictionary.items():
		if key == "销售毛利率(%)":
			industryDataMean.parameters_mean_ratio(key,value, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("销售毛利率(%)", industryDataMean.gross_margin_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("净资产收益率(%)", industryDataMean.ROE_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("销售净利率(%)", industryDataMean.Sales_net_profit_rate_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("总资产回报率(%)", industryDataMean.Rate_of_return_on_total_assets_mean_ratio_industry,industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("资产报酬率(%)", industryDataMean.Rate_of_return_on_assets_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("主营业务利润率(%)", industryDataMean.Main_business_profit_rate_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("存货周转天数(天)", industryDataMean.Inventory_turnover_days_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("总资产周转天数(天)", industryDataMean.Total_assets_turnover_days_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("应收账款周转天数(天)", industryDataMean.Accounts_receivable_turnover_days_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("营业周期(天)", industryDataMean.Business_cycle_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("速动比率(%)", industryDataMean.Quick_ratio_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("现金比率(%)", industryDataMean.Cash_ratio_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("现金负债总额比(%)", industryDataMean.Rate_of_assets_and_liabilities_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("资产负债率(%)", industryDataMean.Quick_ratio_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("产权比率(%)", industryDataMean.Equity_ratio_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("有形净值债务率(%)", industryDataMean.Debt_to_tangible_assets_ratio_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("营业利润比率(%)", industryDataMean.Operating_profit_ratio_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("销售收入增长率(%)", industryDataMean.Sales_revenue_growth_rate_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("税前利润增长率(%)", industryDataMean.Pre_tax_profit_growth_rate_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("总资产增长率(%)", industryDataMean.Total_assets_growth_rate_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("净资产增长率(%)", industryDataMean.Asset_growth_rate_mean_ratio_industry, industryDataMean.year)
	# industryDataMean.parameters_mean_ratio("净利润增长率(%)", industryDataMean.Net_profit_growth_rate_mean_ratio_industry, industryDataMean.year)
