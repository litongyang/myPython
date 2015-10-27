# _author = 'litongyang'
# -*- coding: utf-8 -*-

import re
import numpy as ny
from numpy.random import randn
import matplotlib.pyplot as plt
import calendar
# 违约客户特征的数据分析
# -1:连续型


class FEATURE_ANALYSIS():
    def __init__(self):
        self.default_code = []
        self.repaymentMethod = []
        self.overdueDays = []  # 逾期天数 -1
        self.isPersonal = []
        self.overdueAccount = []  # 逾期金额 -1
        self.loanAccount = []  # 借款金额 -1
        self.guaranteeMethod = []  # 担保方式
        self.mortgageObject = []  # 抵押物价 -1
        self.contractNum = []
        self.judge = []
        self.customerNum = []
        self.genderCd = []  # 性别
        self.birihdy = []  # 出生日期
        self.marriageCd = []  # 婚姻状况
        self.degereeCd = []  # 学历状况
        self.permanentAddress = []  # 家庭住址
        self.workCompany = []  # 工作单位
        self.workBeginTime = []  # 参加工作时间
        self.inhbitancy_status = []  # 居住状况
        self.familyTatalAsset = []  # 家庭总收入 -1
        self.industryCd = []  # 所属行业
        self.maintainPersonNum = []  # 主要家庭成员数量
        self.companyType = []  # 公司类型
        self.employmentType = []  # 雇佣类型

        # 去除空值后的feature
        self.overdueDays_isnotnull = []
        self.overdueAccount_isnotnull = []
        self.loanAccount_isnotnull = []
        self.mortgageObject_isnotnull = []
        self.familyTatalAsset_isnotnull = []

        # 时间feature处理后的结果
        self.age = []
        self.work_age = []

    # 获取数据
    def get_data(self):
        for line in open("C:\\Users\\\Thinkpad\\Desktop\\default_customer.txt"):
            linone = line.split()
            self.default_code.append(linone[0])
            self.repaymentMethod.append(linone[1])
            self.overdueDays.append(linone[2])
            self.isPersonal.append(linone[3])
            self.overdueAccount.append(linone[4])
            self.loanAccount.append(linone[5])
            self.guaranteeMethod.append(linone[6])
            self.mortgageObject.append(linone[7])
            self.judge.append(linone[9])
            self.customerNum.append(linone[10])
            self.genderCd.append(linone[11])
            self.birihdy.append(linone[12])
            self.marriageCd.append(linone[13])
            self.degereeCd.append(linone[14])
            self.permanentAddress.append(linone[15])
            self.workCompany.append(linone[16])
            self.workBeginTime.append(linone[19])
            self.inhbitancy_status.append(linone[20])
            self.familyTatalAsset.append(linone[23])
            self.industryCd.append(linone[24])
            self.maintainPersonNum.append(linone[27])
            self.companyType.append(linone[28])
            self.employmentType.append(linone[30])

        print len(self.default_code)
        # print self.familyTatalAsset

    # 数据预处理：去除空值;应用于连续值
    def data_process(self, feature, feature_isnotnull):
        for i in range(0, len(feature)):
            if feature[i] != 'null':
                temp = float(feature[i])
                feature_isnotnull.append(temp)
        print feature_isnotnull

    # 连续型feature 分析
    def continuous_feature_analysis(self, feature, string):
        fl = open("C:\\Users\\\Thinkpad\\Desktop\\log_continuous.dat", 'a')
        fl.write(str(string))
        fl.write("\n")
        max_v = "max: " + str(max(feature))
        min_v = "min: " + str(min(feature))
        mean_v = "mean: " + str(ny.mean(feature))
        median_v = "median: " + str(ny.median(feature))
        var_v = "var: " + str(ny.var(feature))
        fl.write(str(max_v))
        fl.write("\n")
        fl.write(str(min_v))
        fl.write("\n")
        fl.write(str(mean_v))
        fl.write("\n")
        fl.write(str(median_v))
        fl.write("\n")
        fl.write(str(var_v))
        fl.write("\n")
        fl.write("\n")

    # 离散型feature处理：获取分布情况
    def discrete_feature_analysis(self, feature, string):
        fl = open("C:\\Users\\\Thinkpad\\Desktop\\log_discrete.dat", 'a')
        fl.write(str(string))
        fl.write("\n")
        print feature
        myset = set(feature)
        print myset
        for item in myset:
            # fl.write(str(item))
            string_log = str(
                format(float(feature.count(item)) / float(len(feature)) * 100, '.2f') + '%' + ' of ') + item
            fl.write(str(string_log))
            fl.write("\n")
        fl.write("\n")

    # 处理时间相关feature
    def feature_time_process(self, featureTime, string, feature):
        fl = open("C:\\Users\\\Thinkpad\\Desktop\\feature_time.dat", 'a')
        fl.write(str(string))
        fl.write("\n")
        regex = ur"\d{4}"
        for i in range(0, len(featureTime)):
            if re.search(regex, featureTime[i]):
                match = re.match(r'\d{4}', featureTime[i])
                year = match.group(0)
                year = int(year)
                year_now = 2015
                result = year_now - year
                feature.append(result)
                fl.write(str(result))
                fl.write("\n")
            else:
                pass
        print feature
        fl.write("\n")


    def show(self):
        feature = [1, 2,3,4]
        print feature
        data = randn(100)
        print data
        plt.hist(data)
        # plt.hist(data,bins=12, color=sns.desaturate("indianred", .8), alpha=.4)

if __name__ == '__main__':
    feature_analysis = FEATURE_ANALYSIS()
    feature_analysis.get_data()

    # 连续型feature处理
    feature_analysis.data_process(feature_analysis.overdueDays, feature_analysis.overdueDays_isnotnull)
    feature_analysis.data_process(feature_analysis.overdueAccount, feature_analysis.overdueAccount_isnotnull)
    feature_analysis.data_process(feature_analysis.loanAccount, feature_analysis.loanAccount_isnotnull)
    feature_analysis.data_process(feature_analysis.mortgageObject, feature_analysis.mortgageObject_isnotnull)
    feature_analysis.data_process(feature_analysis.familyTatalAsset, feature_analysis.familyTatalAsset_isnotnull)

    # feature_analysis.continuous_feature_analysis(feature_analysis.overdueDays_isnotnull, "overdueDays")
    # feature_analysis.continuous_feature_analysis(feature_analysis.overdueAccount_isnotnull, "overdueAccount")
    # feature_analysis.continuous_feature_analysis(feature_analysis.loanAccount_isnotnull, "loanAccount")
    # feature_analysis.continuous_feature_analysis(feature_analysis.mortgageObject_isnotnull, "mortgageObject")
    # feature_analysis.continuous_feature_analysis(feature_analysis.familyTatalAsset_isnotnull, "familyTatalAsset")

    # 离散型feature处理：查看分布
    # feature_analysis.discrete_feature_analysis(feature_analysis.repaymentMethod, "repaymentMethod")
    # feature_analysis.discrete_feature_analysis(feature_analysis.isPersonal, "isPersonal")
    # feature_analysis.discrete_feature_analysis(feature_analysis.guaranteeMethod, "guaranteeMethod")
    # feature_analysis.discrete_feature_analysis(feature_analysis.genderCd, "genderCd")
    # feature_analysis.discrete_feature_analysis(feature_analysis.marriageCd, "marriageCd")
    # feature_analysis.discrete_feature_analysis(feature_analysis.degereeCd, "degereeCd")
    # feature_analysis.discrete_feature_analysis(feature_analysis.inhbitancy_status, "inhbitancy_status")
    # feature_analysis.discrete_feature_analysis(feature_analysis.maintainPersonNum, "maintainPersonNum")
    # feature_analysis.discrete_feature_analysis(feature_analysis.companyType, "companyType")
    # feature_analysis.discrete_feature_analysis(feature_analysis.employmentType, "employmentType")

    # 处理时间feature：距离现在的年份
    # feature_analysis.feature_time_process(feature_analysis.birihdy, "birihdy", feature_analysis.age)
    # feature_analysis.feature_time_process(feature_analysis.workBeginTime, "workBeginTime", feature_analysis.work_age)

    # feature_analysis.show()