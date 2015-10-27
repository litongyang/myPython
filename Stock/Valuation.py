# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

from __future__ import division

import MySQLdb


# import chardet


class VALUATION():
    def __init__(self):
        self.Company_code = 1
        self.Sales_revenue_growth_rate_predict_pre = 0.0  # 预测的销售收入增长率
        self.risk_free_rate = 0.03  # 无风险利率
        self.beta = 1.2
        self.premium_rate_pre = 0.08  # 市场溢价率
        self.debt_cost = 0.05  # 债权成本

        self.business_income_predict = 0  # 预测的营业收入
        self.business_income = -10000  # 营业收入
        self.business_profit = 0  # 营业利润
        self.operating_margin_ratio = 0  # 税前经营利润率
        self.pre_tax_operating_profit = 0  # 税前经营利润
        self.income_tax = 0  # 所得税
        self.total_profit = -1  # 利润总额
        self.income_tax_rates = 0  # 所得税税率
        self.after_tax_operating_profit = 0  # 税后经营利润
        self.financial_assets = 0  # 金融资产
        self.financial_assets_last = 0  # 上一年的金融资产
        self.financial_liabilities = 0  # 金融负债
        self.financial_liabilities_last = 0  # 上一年金融负债
        self.shareholders_equity = 0  # 股东权益
        self.shareholders_equity_last = 0  # 上一年股东权益
        self.net_capital = 0  # 净资本
        self.net_capital_last = 0  # 上一年净资本
        self.net_investment = 0  # 本期净投资
        self.entity_cash_flow = 0  # 实体现金流量
        self.entity_cash_flow_t = []  # 预测期每年实体现金流量
        self.entity_cash_flow_predict = 0  # 预测期实体现金流量
        self.entity_value = 0  # 实体价值
        self.debt_value = 0  # 债务价值
        self.stock_value = 0  # 股权价值
        self.equity = -1  # 股本
        self.cost_equity = 0  # 股权成本
        self.net_assets_per_share = 0  # 每股净资产
        self.total_assets = -1  # 总资产
        self.WACC = 0  # 加权平均投资成本
        self.share_value = 0  # 每股价值
        self.cost_pre = 0

        self.db_name = 'STOCK_INFO_2014'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码

        self.file = 'stock_' + str("%06d" % self.Company_code)

    '''
    #--------------------------税后经营利润------------------------------------------------
    #公式: 税后经营利润 = 税前经营利润*(1-所得税税率)
    #所得税税率 =所得税÷利润总额
    #税前经营利润 = 预测的营业收入*税前经营利润率
    #税前经营利润率 = 营业利润÷营业收入
    #预测的营业收入 = 营业收入*(1+预测的销售收入增长率)
    ##---------------------------------------------------------------------------------------
    '''

    def after_tax_operating_profit_fun(self):
        self.file = 'stock_' + str("%06d" % self.Company_code)
        print self.file
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            '''
            content = '营业收入'
            my_char= chardet.detect(content)
            bian_ma = my_char['encoding']
            content = content.decode(bian_ma, 'ignore').encode('utf-8')
            '''
            count = cur.execute("SELECT * FROM %s WHERE SUBJECT='营业收入'" % self.file)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.business_income = -1
            else:
                self.business_income = results[0][3]

        except:
            pass

        self.business_income_predict = self.business_income * (
            1 + self.Sales_revenue_growth_rate_predict_pre)  # 预测的营业收入
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM %s WHERE SUBJECT='营业利润'" % self.file)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.business_profit = -1
            else:
                self.business_profit = results[0][3]
        except:
            pass
        if self.business_income == 0:
            self.business_income = -10000
        self.operating_margin_ratio = round(self.business_profit / self.business_income, 2)  # 税前经营利润率
        self.pre_tax_operating_profit = self.business_income_predict * self.operating_margin_ratio;  # 税前经营利润

        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM %s WHERE SUBJECT='利润总额'" % self.file)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.total_profit = -1
            else:
                self.total_profit = results[0][3]
        except:
            pass
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM %s WHERE SUBJECT='所得税'" % self.file)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.income_tax = -1
            else:
                self.income_tax = results[0][3]
        except:
            pass
        self.income_tax_rates = round(self.income_tax / self.total_profit, 2)  # 所得税税率
        self.after_tax_operating_profit = self.pre_tax_operating_profit * (1 - self.income_tax_rates)
        self.after_tax_operating_profit *= 10000  # 税后经营利润
        print "after_tax_operating_profit:%f" % self.after_tax_operating_profit

    '''
    ##--------------------------本期净投资------------------------------------------------
    #公式: 本期净投资 = 净资本-上一年净资本
    #净资本 = (金融负债-金融资产)+股东权益
    #金融负债 = 短期借款+长期借款+交易性金融负债+应付债券
    #金融资产 = 货币资金+交易性金融资产
    ##------------------------------------------------------------------------------------
    '''

    def net_investment_fun(self):
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM %s WHERE SUBJECT='货币资金'" % self.file)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.financial_assets = 0
                self.financial_assets_last = 0
            else:
                self.financial_assets = results[0][3]
                self.financial_assets_last = results[0][4]
        except:
            pass

        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM %s WHERE SUBJECT='交易性金融资产'" % self.file)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.financial_assets += 0
                self.financial_assets_last += 0
            else:
                self.financial_assets += results[0][3]
                self.financial_assets_last += results[0][4]
        except:
            pass

        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM %s WHERE SUBJECT='短期借款'" % self.file)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.financial_liabilities = 0
                self.financial_liabilities_last = 0
            else:
                self.financial_liabilities = results[0][3]
                self.financial_liabilities_last = results[0][4]
        except:
            pass

        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM %s WHERE SUBJECT='长期借款'" % self.file)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.financial_liabilities += 0
                self.financial_liabilities_last += 0
            else:
                self.financial_liabilities += results[0][3]
                self.financial_liabilities_last += results[0][4]
        except:
            pass

        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM %s WHERE SUBJECT='交易性金融负债'" % self.file)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.financial_liabilities += 0
                self.financial_liabilities_last += 0

            else:
                self.financial_liabilities += results[0][3]
                self.financial_liabilities_last += results[0][4]
        except:
            pass

        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM %s WHERE SUBJECT='应付债券'" % self.file)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.financial_liabilities += 0
                self.financial_liabilities_last += 0
            else:
                self.financial_liabilities += results[0][3]
                self.financial_liabilities_last += results[0][4]
        except:
            pass

        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM %s WHERE SUBJECT='股东权益合计'" % self.file)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.shareholders_equity += 0
                self.shareholders_equity_last += 0
            else:
                self.shareholders_equity += results[0][3]
                self.shareholders_equity_last += results[0][4]
        except:
            pass

        self.net_capital = (self.financial_liabilities - self.financial_assets) + self.shareholders_equity
        self.net_capital_last = (
                                    self.financial_liabilities_last - self.financial_assets_last) + self.shareholders_equity_last
        self.net_investment = self.net_capital - self.net_capital_last
        self.net_investment *= 10000  # 本期净投资
        print "net_investment:%f" % self.net_investment

    '''
    ##--------------------------实体现金流量------------------------------------------------
    #公式: 实体现金流量 = 税后经营利润-本期净投资
    ##---------------------------------------------------------------------------------------
    '''

    def entity_cash_flow_fun(self):
        self.entity_cash_flow = self.after_tax_operating_profit - self.net_investment
        print "entity_cash_flow:%f" % self.entity_cash_flow

    '''
    ##--------------------------加权平均投资成本(折现率)(代表公司整体平均资金成本)-----------------------------
    #公式: 加权平均投资成本(折现率) = (资产净值/总资产)*股权成本+(负债合计/总资产)*债权成本*(1-所得税税率)
    #股权成本 =无风险利率+β*市场溢价率
    #无风险利率=5年期国债利率
    #β=公司销售收入的增长率变化的惩罚值
    #市场溢价率=高于无风险利率的额外收益率
    ##--------------------------------------------------------------------------------------------------
    '''

    def WACC_fun(self):

        self.cost_pre = self.risk_free_rate + self.beta * self.premium_rate_pre  # 股权成本
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM %s WHERE SUBJECT='股本|万股'" % self.file)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.equity = 100000
            else:
                self.equity = results[0][3]
        except:
            pass
        self.equity *= 10000  # 股本

        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM %s WHERE SUBJECT='负债合计'" % self.file)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.debt_value = 0
            else:
                self.debt_value = results[0][3]
        except:
            pass

        self.debt_value *= 10000  # 债务价值

        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM %s WHERE SUBJECT='资产总计'" % self.file)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.total_assets = -1
            else:
                self.total_assets = results[0][3]
        except:
            pass

        self.total_assets *= 10000  # 总资产

        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM %s WHERE SUBJECT='每股净资产'" % self.file)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.net_assets_per_share = 0
            else:
                self.net_assets_per_share = results[0][3]
        except:
            pass
        self.WACC = (self.net_assets_per_share * self.equity / self.total_assets) * self.cost_pre + (
                                                                                                        self.debt_value / self.total_assets) * self.debt_cost * (
                                                                                                        1 - self.income_tax_rates)
        # self.WACC = round(self.WACC, 2)#加权平均投资成本

        # 加权平均投资成本应该大于预测的销售收入增长率
        if self.WACC <= self.Sales_revenue_growth_rate_predict_pre:
            # sys.exit("WACC should be more than Sales_revenue_growth_rate_predict_pre!")
            self.WACC = 100
        print "WACC:%f" % self.WACC

    '''
    ##--------------------------每股价值(一阶段增长模型)---------------------------------------------------
    #公式: 每股价值 = 股权价值/股本
    #股权价值 = 实体价值-债务价值
    #实体价值 = 下期实体现金流量 /(加权平均资本成本-永续增长率)
    #下期实体现金流量 = 当前实体现金流量*(1+永续增长率)
    ##-----------------------------------------------------------------------------------------------------
    '''

    def share_value_fun(self):
        self.entity_value = self.entity_cash_flow * (1 + self.Sales_revenue_growth_rate_predict_pre) / (
            self.WACC - self.Sales_revenue_growth_rate_predict_pre)
        self.stock_value = self.entity_value - self.debt_value  # 股权价值
        if self.equity == 0:
            self.equity = -1
        self.share_value = self.stock_value / self.equity
        self.share_value = int(self.share_value)  # 每股价值
        print "%s of share_value: %f" % (self.Company_code, self.share_value)

    def write_txt_fun(self):
        fl = open("C:\\Users\\Thinkpad\\Desktop\\Valuation1.txt", 'a')
        if self.share_value > 0:
            fl.write(str("%06d" % self.Company_code))
            fl.write('\t')
            fl.write(str(self.share_value))
            fl.write("\n")

    def write_log_fun(self):
        fl = open("C:\\Users\\\Thinkpad\\Desktop\\log1.txt", 'a')
        if self.share_value > 0:
            fl.write(str("%06d" % self.Company_code))
            fl.write('\n')
            fl.write(str("营业收入：%d" % self.business_income))
            fl.write('\n')
            fl.write(str("营业利润：%d" % self.business_profit))
            fl.write('\n')
            fl.write(str("净投资：%d" % self.net_capital))
            fl.write('\n')
            fl.write(str("利润总额：%d" % self.total_profit))
            fl.write('\n')
            fl.write(str("税后经营利润：%d" % self.after_tax_operating_profit))
            fl.write('\n')
            fl.write(str("今年净资本：%d" % self.net_capital))
            fl.write('\n')
            fl.write(str("本期净投资：%d" % self.net_investment))
            fl.write('\n')
            fl.write(str("实体现金流：%d" % self.entity_cash_flow))
            fl.write('\n')
            fl.write(str("总股本：%d" % self.equity))
            fl.write('\n')
            fl.write(str("负债合计：%d" % self.debt_value))
            fl.write('\n')
            fl.write(str("总资产：%d" % self.total_assets))
            fl.write('\n')
            fl.write(str("所得税税率：%f" % self.income_tax_rates))
            fl.write('\n')
            fl.write(str("WACC：%f" % self.WACC))
            fl.write("\n")
            fl.write("\n")

        '''
        fl = open("C:\\Users\\Thinkpad\\Desktop\\Valuation.txt", 'a')
        fl.write(str(self.file))
        fl.write('\t')
        fl.write(str(self.after_tax_operating_profit))
        fl.write("\t")
        fl.write(str(self.entity_cash_flow))
        fl.write("\t")
        fl.write(str(self.net_investment))
        fl.write("\t")
        fl.write(str(self.WACC))
        fl.write("\t")
        fl.write(str(self.share_value))
        fl.write("\n")
        '''

    # 清零函数
    def clear_fun(self):
        valuation.business_income_predict = 0  # 预测的营业收入
        valuation.business_income = -10000  # 营业收入
        valuation.business_profit = 0  # 营业利润
        valuation.operating_margin_ratio = 0  # 税前经营利润率
        valuation.pre_tax_operating_profit = 0  # 税前经营利润
        valuation.income_tax = 0  # 所得税
        valuation.total_profit = -1  # 利润总额
        valuation.income_tax_rates = 0  # 所得税税率
        valuation.after_tax_operating_profit = 0  # 税后经营利润
        valuation.financial_assets = 0  # 金融资产
        valuation.financial_assets_last = 0  # 上一年的金融资产
        valuation.financial_liabilities = 0  # 金融负债
        valuation.financial_liabilities_last = 0  # 上一年金融负债
        valuation.shareholders_equity = 0  # 股东权益
        valuation.shareholders_equity_last = 0  # 上一年股东权益
        valuation.net_capital = 0  # 净资本
        valuation.net_capital_last = 0  # 上一年净资本
        valuation.net_investment = 0  # 本期净投资
        valuation.entity_cash_flow = 0  # 实体现金流量
        valuation.entity_cash_flow_t = []  # 预测期每年实体现金流量
        valuation.entity_cash_flow_predict = 0  # 预测期实体现金流量
        valuation.entity_value = 0  # 实体价值
        valuation.debt_value = 0  # 债务价值
        valuation.stock_value = 0  # 股权价值
        valuation.equity = -1  # 股本
        valuation.cost_equity = 0  # 股权成本
        valuation.net_assets_per_share = 0  # 每股净资产
        valuation.total_assets = -1  # 总资产
        valuation.WACC = 0  # 加权平均投资成本
        valuation.share_value = 0  # 每股价值
        valuation.cost_pre = 0


if __name__ == '__main__':
    valuation = VALUATION()
    for valuation.Company_code in range(1, 604000):
        if (valuation.Company_code >= 1100 and valuation.Company_code < 1600) or (
                        valuation.Company_code > 3000 and valuation.Company_code <= 300000) or (
                        valuation.Company_code > 301000 and valuation.Company_code <= 599999) or (
                        valuation.Company_code > 602000 and valuation.Company_code <= 602999):
            continue
        valuation.after_tax_operating_profit_fun()
        valuation.net_investment_fun()
        valuation.entity_cash_flow_fun()
        valuation.WACC_fun()
        valuation.share_value_fun()
        valuation.write_txt_fun()
        valuation.write_log_fun()
        valuation.clear_fun()
        valuation.Company_code += 1
