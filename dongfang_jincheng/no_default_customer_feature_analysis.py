# __author__ = 'litongyang'
# -*- coding: utf-8 -*-
import re
import numpy as ny
from matplotlib.mlab import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import LogNorm

class FIRSTDATA():
    def __init__(self):
        self.code = []
        self.repaymentMethod = []
        self.loanAmount = []  # 贷款总额,连续型
        self.guaranteeMethod = []  # 担保方式
        self.mortgageObject = []  # 抵押物价，连续型
        self.contractNum = []
        self.conderCd = []
        self.birihdy = []  # 出生日期
        self.marriageCd = []  #
        self.degereeCd = []
        self.workBeginTime = []
        self.inhbitancy_status = []
        self.familyTatalAsset = []  # 家庭总收入，连续型
        self.industryCd = []
        self.operattionTerm = []
        self.principalBiz = []
        self.maintainPersonNum = []
        self.companyType = []
        self.professional = []
        self.indCustomerTypeCd = []
        self.customerSource = []
        self.employmentType = []

        self.loanAmount_isnotnull = []
        self.mortgageObject_isnotnull = []
        self.familyTatalAsset_isnotnull = []

        # 时间feature处理后的结果
        self.age = []
        self.work_age = []

        self.loanAmount_isnotnull_cnt = 0
        self.loanAmount_max = 0
        self.loanAmount_min = 0

    def get_data(self):
        for line in open("C:\\Users\\\Thinkpad\\Desktop\\data.dat"):
            linone = line.split()
            self.code.append(linone[0])
            self.repaymentMethod.append(linone[1])
            self.loanAmount.append(linone[2])
            self.guaranteeMethod.append(linone[3])
            self.mortgageObject.append(linone[4])
            self.contractNum.append(linone[5])
            self.conderCd.append(linone[6])
            self.birihdy.append(linone[7])
            self.marriageCd.append(linone[8])
            self.degereeCd.append(linone[9])
            self.workBeginTime.append(linone[14])
            self.inhbitancy_status.append(linone[15])
            self.familyTatalAsset.append(linone[18])
            self.industryCd.append(linone[19])
            self.operattionTerm.append(linone[20])
            self.principalBiz.append(linone[21])
            self.maintainPersonNum.append(linone[22])
            self.companyType.append(linone[23])
            self.professional.append(linone[24])
            self.indCustomerTypeCd.append(linone[25])
            self.customerSource.append(linone[26])
            self.employmentType.append(linone[35])
        print len(self.code)
        # print self.inhbitancy_status
        # fl = open("C:\\Users\\\Thinkpad\\Desktop\\log.dat", 'a')
        # for i in range(0, len(self.maintainPersonNum)):
        #     fl.write(self.maintainPersonNum[i])
        #     fl.write("\n")

        # print self.familyTatalAsset
        # print "inhbitancy_status", self.inhbitancy_status

    def data_process(self, feature, feature_isnull):
        for i in range(0, len(feature)):
            if feature[i] != 'null' and feature[i] != '2009/9/23' and feature[i] !='2013/6/3':
                self.loanAmount_isnotnull_cnt += 1
                temp = float(feature[i])
                feature_isnull.append(temp)
        print feature_isnull

    def discrete_feature_analysis(self, feature):
        fl = open("C:\\Users\\\Thinkpad\\Desktop\\log_discrete.dat", 'a')
        print feature
        myset = set(feature)
        print myset
        for item in myset:
            # fl.write(str(item))
            string_log = str(format(float(feature.count(item))/float(len(feature))*100, '.2f') + '%' +' of ')+ item
            fl.write(str(string_log))
            fl.write("\n")
        fl.write("\n")

    def continuous_feature_analysis(self, feature):
        # print max(feature)
        # print min(feature)
        # print ny.mean(feature)
        # print ny.median(feature)
        # print ny.var(feature)
        fl = open("C:\\Users\\\Thinkpad\\Desktop\\log_continuous.dat", 'a')
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

     # 处理时间相关feature
    def feature_time_process(self, featureTime, string, feature):
        # fl = open("C:\\Users\\\Thinkpad\\Desktop\\feature_time.dat", 'a')
        # fl.write(str(string))
        # fl.write("\n")
        regex = ur"\d{4}"
        for i in range(0, len(featureTime)):
            if re.search(regex, featureTime[i]):
                match = re.match(r'\d{4}', featureTime[i])
                year = match.group(0)
                year = int(year)
                year_now = 2015
                result = year_now - year
                if result>0:
                    feature.append(result)
                # fl.write(str(result))
                # fl.write("\n")
            else:
                pass
        print feature
        # fl.write("\n")

    def drawing(self):
        print self.loanAmount_isnotnull
        # plt.hist(self.loanAmount_isnotnull, 100, facecolor='green')
        plt.scatter(self.loanAmount_isnotnull)
        # x1 = 10 + 5 * np.random.randn(10000)
        # x2 = 20 + 5 * np.random.randn(10000)
        # num_bins = 50
        # plt.hist(x1, num_bins, normed=1, facecolor='green', alpha=0.5)
        # plt.hist(x2, num_bins, normed=1, facecolor='blue', alpha=0.5)
        # plt.title('Histogram')
        # plt.show()
        # x = [1,2,3]
        # y = [2,3,4]
        # polt.bar(x,y)
        plt.show()

if __name__ == '__main__':
    firstData = FIRSTDATA()
    firstData.get_data()

    # firstData.discrete_feature_analysis(firstData.repaymentMethod)
    # firstData.discrete_feature_analysis(firstData.guaranteeMethod)
    # firstData.discrete_feature_analysis(firstData.conderCd)
    # firstData.discrete_feature_analysis(firstData.marriageCd)
    # firstData.discrete_feature_analysis(firstData.degereeCd)
    firstData.discrete_feature_analysis(firstData.inhbitancy_status)
    # # firstData.discrete_feature_analysis(firstData.inhbitancy_status)
    # # #firstData.discrete_feature_analysis(firstData.operattionTerm)
    # # #firstData.discrete_feature_analysis(firstData.principalBiz)
    # firstData.discrete_feature_analysis(firstData.maintainPersonNum)
    # firstData.discrete_feature_analysis(firstData.companyType)
    # # firstData.discrete_feature_analysis(firstData.professional)
    # firstData.discrete_feature_analysis(firstData.indCustomerTypeCd)
    # firstData.discrete_feature_analysis(firstData.customerSource)
    # firstData.discrete_feature_analysis(firstData.employmentType)

    # firstData.data_process(firstData.loanAmount, firstData.loanAmount_isnotnull)
    # firstData.data_process(firstData.mortgageObject, firstData.mortgageObject_isnotnull)
    # firstData.data_process(firstData.familyTatalAsset, firstData.familyTatalAsset_isnotnull)
    #
    # firstData.continuous_feature_analysis(firstData.loanAmount_isnotnull)
    # firstData.continuous_feature_analysis(firstData.mortgageObject_isnotnull)
    # firstData.continuous_feature_analysis(firstData.familyTatalAsset_isnotnull)

    # 处理时间feature：距离现在的年份
    # firstData.feature_time_process(firstData.birihdy, "birihdy", firstData.age)
    # firstData.feature_time_process(firstData.workBeginTime,"workAge",firstData.work_age)
    # firstData.drawing()