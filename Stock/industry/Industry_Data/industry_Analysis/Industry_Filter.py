# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# 通过行业指标进行行业筛选

import MySQLdb
import matplotlib.pyplot as plt


class IndustryFilter:
    def __init__(self):
        self.db_name = 'STOCK_INFO_2015'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.fileName = 'industry_data'
        self.industry_name = []
        self.parameters = []
        self.industry_data = []
        self.last_year = 2014
        self.now_year = 2015
        self.industry_name_roe_selected = set()  # 通过roe选择出的行业
        self.industry_name_gross_margin_ratio_selected = set()  # 通过销售毛利率选择出的行业
        self.industry_name_net_profit_growth_ratio_industry_selected = set()  # 通过净利润增长率选择出的行业
        self.industry_name_selected = set()  # 通过每个指标选出的行业的交集

    # 从数据库获取相应数据
    def get_data(self):
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')

            # 选出行业名称
            sql_string = cur.execute("SELECT industry_name FROM %s " % self.fileName + "GROUP BY  industry_name")
            industry_name_db = cur.fetchmany(sql_string)
            for i in range(0, len(industry_name_db)):
                self.industry_name.append(industry_name_db[i][0])

            # 选出行业参数名称
            sql_string = cur.execute("SELECT paramters FROM %s " % self.fileName + "GROUP BY  paramters")
            parameters = cur.fetchmany(sql_string)
            for i in range(0, len(parameters)):
                self.parameters.append(parameters[i][0])

            # 行业数据
            sql_string = cur.execute("SELECT * FROM %s " % self.fileName)
            industry_data = cur.fetchmany(sql_string)
            for i in range(0, len(industry_data)):
                self.industry_data.append(industry_data[i])
                # print self.industry_data[0][3]
        except Exception, e:
            print Exception, ":", e

    # 制定规则
    def rule(self, industry_name, parameter_name):
        for i in range(0, len(self.industry_name)):
            parameters_value_2014 = 0
            parameters_value_2013 = 0
            for j in range(0, len(self.industry_data)):
                if int(self.industry_data[j][1]) == self.now_year or int(self.industry_data[j][1]) == self.last_year:
                    if self.industry_data[j][0] == self.industry_name[i]:
                        if self.industry_data[j][2] == parameter_name:
                            if int(self.industry_data[j][1]) == self.now_year:
                                parameters_value_2014 = float(self.industry_data[j][3])
                            elif int(self.industry_data[j][1]) == self.last_year:
                                parameters_value_2013 = float(self.industry_data[j][3])
                                # print "name,year,value:", self.industry_data[j][0],self.industry_data[j][1],self.industry_data[j][3]
                                # print parameters_value_2013,parameters_value_2014
            if parameters_value_2014 >= parameters_value_2013 and parameters_value_2014 > 0:
                industry_name.add(self.industry_name[i])
                # print parameter_name
                # for d in self.industry_name:
                #     print (d)
                # print "************"
                # print self.industry_name_selected

    # 画图
    def drawing(self, parameter_name):
        x = []
        y = []
        for i in range(0, len(self.industry_data)):
            if self.industry_data[i][0] == '运输设备' and self.industry_data[i][2] == parameter_name:
                x.append(int(self.industry_data[i][1]))
                y.append(int(self.industry_data[i][3]))
        plt.plot(x, y)
        plt.show()


if __name__ == '__main__':
    industryFilter = IndustryFilter()
    industryFilter.get_data()
    industryFilter.rule(industryFilter.industry_name_roe_selected, '净资产收益率(%)')
    industryFilter.rule(industryFilter.industry_name_gross_margin_ratio_selected, '销售毛利率(%)')
    industryFilter.rule(industryFilter.industry_name_net_profit_growth_ratio_industry_selected, '净利润增长率(%)')
    industryFilter.industry_name_selected = industryFilter.industry_name_roe_selected & industryFilter.industry_name_gross_margin_ratio_selected \
                                            & industryFilter.industry_name_net_profit_growth_ratio_industry_selected
    for i in industryFilter.industry_name_selected:
        print i
    industryFilter.drawing('净资产收益率(%)')
    industryFilter.drawing('销售毛利率(%)')
    industryFilter.drawing('净利润增长率(%)')
