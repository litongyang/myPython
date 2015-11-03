# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# 求在行业中需要求和的参数的最后结果
import MySQLdb


class IndustryData:
    def __init__(self):
        self.db_name = 'STOCK_INFO_2014'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.fileName = 'company_industry'
        self.fileName_industry_data = 'industry_data'

        self.db_name_dim = 'dim_stock'

        self.company_code = []
        self.company_name = []
        self.industry = []

        self.company_industry = {}  # 每个行业包含的公司代码
        self.total_profit_sum_industry = {}  # 每个行业净利润总额总和(key:string,行业名字；value:list,每年对应的行业净利润总额总和)
        self.net_profit_sum_industry = {}  # 每个行业净利润总和(key:string,行业名字；value:list,每年对应的行业净利润总和)
        self.business_income_sum_industry = {}  # 每个行业营业总收入总和(key:string,行业名字；value:list,每年对应的行业营业收入总和)
        self.cost_in_business_sum_industry = {}  # 每个行业营业总成本总和(key:string,行业名字；value:list,每年对应的行业营业总成本总和)
        self.shareholders_equity_sum_industry = {}  # 每个行业股东权益合计和(key:string,行业名字；value:list,每年对应的行业股东权益合计总和)
        self.total_assets_sum_industry = {}  # 每个行业总资产总和(key:string,行业名字；value:list,每年对应的行业总资产总和)
        self.cash_sum_industry = {}  # 每个行业货币资金总和(key:string,行业名字；value:list,每年对应的行业货币资金总和)
        self.accounts_receivable_sum_industry = {}  # 每个行业应收账款总和(key:string,行业名字；value:list,每年对应的行业应收账款总和)
        self.advance_payment_sum_industry = {}  # 每个行业预付账款总和(key:string,行业名字；value:list,每年对应的行业预付账款总和)
        self.remainder_sum_industry = {}  # 每个行业存货总和(key:string,行业名字；value:list,每年对应的行业存货总和)
        self.total_liabilities_sum_industry = {}  # 每个行业负债合计总和(key:string,行业名字；value:list,每年对应的行业负债合计总和)

        self.parameters_dictionary = {}
        # self.net_profit_growth_rate_industry = {}  # 每个行业净利润增长率(key:string,行业名字；value:list,每年对应的行业净利润增长率)

    # 根据行业将上市
    # 公司进行划分
    def divided_group_industry(self):
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')

            # 获取行业名称做为字典的key
            count_industry = cur.execute("SELECT Industry  FROM %s GROUP BY Industry" % self.fileName)
            results_industry = cur.fetchmany(count_industry)

            for i in range(0, len(results_industry)):
                # 获取行业对应的company_code,作为字典的value
                count_code = cur.execute(
                    "SELECT Company_code  FROM %s WHERE Industry='%s'" % (self.fileName, results_industry[i][0]))
                results_code = cur.fetchmany(count_code)
                company_code = []
                for j in range(0, len(results_code)):
                    company_code.append(results_code[j][0])
                self.company_industry[results_industry[i][0]] = company_code
                # for key, value in self.company_industry.items():
                #     print value
        except Exception, e:
            print Exception, ":", e

    def create_parameters_dictionary(self):
        self.parameters_dictionary["利润总额"] = self.total_profit_sum_industry
        self.parameters_dictionary["净利润"] = self.net_profit_sum_industry
        self.parameters_dictionary["股东权益合计"] = self.shareholders_equity_sum_industry
        self.parameters_dictionary["营业总收入"] = self.business_income_sum_industry
        self.parameters_dictionary["营业总成本"] = self.cost_in_business_sum_industry
        self.parameters_dictionary["资产总计"] = self.total_assets_sum_industry
        self.parameters_dictionary["货币资金"] = self.cash_sum_industry
        self.parameters_dictionary["应收账款"] = self.accounts_receivable_sum_industry
        self.parameters_dictionary["预付账款"] = self.advance_payment_sum_industry
        self.parameters_dictionary["存货"] = self.remainder_sum_industry
        self.parameters_dictionary["负债合计"] = self.total_liabilities_sum_industry

    #  求和参数的通用函数
    def parameters_sum(self, string, parameters_sum_year):
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            for key, value in self.company_industry.items():
                industry_net_profit_sum_info = []
                for j in range(3, 13):
                    industry_year_net_profit_sum = 0  # 每个行业每年的净利润总和
                    for i in range(0, len(value)):
                        stock_name = 'stock_' + value[i]
                        try:
                            count = cur.execute(
                                "SELECT * FROM %s " % stock_name + "WHERE SUBJECT=" + '\'' + string + '\'')
                            results = cur.fetchmany(count)
                            industry_year_net_profit_sum += results[0][j]
                        except Exception, e:
                            pass
                            # print Exception, ":", e
                    industry_net_profit_sum_info.append(industry_year_net_profit_sum)
                # self.net_profit_sum_industry[key] = industry_net_profit_sum_info
                parameters_sum_year[key] = industry_net_profit_sum_info
                print string,key, ':', industry_net_profit_sum_info
            # print parameters_sum_year['白酒']
        except Exception, e:
            pass
            # print Exception, ":", e

    #  净利润增长率
    # def net_profit_growth_rate(self, string):
    #     try:
    #         conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
    #                                port=self.db_port)
    #         cur = conn.cursor()
    #         cur.execute('set names \'utf8\'')
    #         for key, value in self.company_industry.items():
    #             industry_net_profit_growth_rate_info = []
    #             for j in range(3, 13):
    #                 industry_year_net_profit_sum = 0  # 每个行业每年的净利润总和
    #                 for i in range(0, len(value)):
    #                     stock_name = 'parameters_' + value[i]
    #                     try:
    #                         count = cur.execute(
    #                             "SELECT * FROM %s " % stock_name + "WHERE Parameters=" + '\'' + string + '\'')
    #                         results = cur.fetchmany(count)
    #                         industry_year_net_profit_sum += results[0][j]
    #                     except Exception, e:
    #                         print Exception, ":", e
    #                 industry_net_profit_growth_rate_info.append(industry_year_net_profit_sum / len(value))
    #             self.net_profit_growth_rate_industry[key] = industry_net_profit_growth_rate_info
    #         # print key, ':', industry_net_profit_growth_rate_info
    #         year = [i for i in range(2014, 2004, -1)]
    #
    #         # 插入数据库
    #         for key, value in self.net_profit_growth_rate_industry.items():
    #             # print key, ':', value
    #             for i in range(0, len(year)):
    #                 temp = '\'' + key + '\'' + ',' + '\'' + str(year[i]) + '\'' + ',' + '\'' + str(value[i]) + '\''
    #                 print temp
    #                 insert_sql = "insert into %s values(%s)" % (self.fileName_industry_data, temp)
    #                 cur.execute(insert_sql)
    #                 # plt.scatter(x, self.net_profit_growth_rate_industry['生物制药'], marker='*')
    #                 # plt.plot(x, self.net_profit_growth_rate_industry['医药商业'], 'o-', linewidth=2)
    #                 # plt.show()
    #     except Exception, e:
    #         print Exception, ":", e


if __name__ == '__main__':
    Industry = IndustryData()
    Industry.divided_group_industry()
    Industry.create_parameters_dictionary()
    for key, value in Industry.parameters_dictionary.items():
        Industry.parameters_sum(key, value)
    # Industry.industry_net_profit()
    # Industry.parameters_sum("利润总额", Industry.total_profit_sum_industry)
    # Industry.parameters_sum("净利润", Industry.net_profit_sum_industry)
    # Industry.parameters_sum("股东权益合计", Industry.shareholders_equity_sum_industry)
    # Industry.parameters_sum("营业总收入", Industry.business_income_sum_industry)
    # Industry.parameters_sum("营业总成本", Industry.cost_in_business_sum_industry)
    # Industry.parameters_sum("资产总计", Industry.total_assets_sum_industry)
    # Industry.parameters_sum("货币资金", Industry.cash_sum_industry)
    # Industry.parameters_sum("应收账款", Industry.accounts_receivable_sum_industry)
    # Industry.parameters_sum("预付账款", Industry.advance_payment_sum_industry)
    # Industry.parameters_sum("存货", Industry.remainder_sum_industry)
    Industry.parameters_sum("负债合计", Industry.total_liabilities_sum_industry)

# Industry.parameters_sum("营业收入", Industry.business_income_industry)
# Industry.parameters_sum("资产总计", Industry.total_assets)
# Industry.net_profit_growth_rate("净利润增长率(%)")
