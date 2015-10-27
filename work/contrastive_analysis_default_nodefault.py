# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# 违约非违约客户特征对比分析

import matplotlib.pylab as plt
import seaborn as sns
import numpy as np
import work.no_default_customer_feature_analysis as nodefault
import work.default_customer_feature_analysis as default



class ContrastiveAnalysis:
    def __init__(self):
        self.overdueDays = []
        self.overdueAccount = []
        self.loanAccount_default = []
        self.mortgageObjectt_default = []
        self.familyTatalAsset_default = []
        self.age_default = []
        self.workAge_default = []
        self.loanAccount_nodefault = []
        self.mortgageObjectt_nodefault = []
        self.familyTatalAsset_nodefault = []
        self.age_nodefault = []
        self.workAge_nodefault = []

        self.loanAccount_nodefault_remove_noise = []
        self.mortgageObjectt_nodefault_remove_noise = []
        self.familyTatalAsset_defaultt_remove_noise = []
        self.familyTatalAsset_nodefaultt_remove_noise = []

    def continuous(self):
        # self.loanAccount_isnotnull
        default_class = default.FEATURE_ANALYSIS()
        default_class.get_data()
        default_class.data_process(default_class.overdueDays, default_class.overdueDays_isnotnull)
        default_class.data_process(default_class.overdueAccount, default_class.overdueAccount_isnotnull)
        default_class.data_process(default_class.loanAccount, default_class.loanAccount_isnotnull)
        default_class.data_process(default_class.mortgageObject, default_class.mortgageObject_isnotnull)
        default_class.data_process(default_class.familyTatalAsset, default_class.familyTatalAsset_isnotnull)
        default_class.feature_time_process(default_class.birihdy, "birihdy", default_class.age)
        default_class.feature_time_process(default_class.workBeginTime, "workAge", default_class.work_age)
        self.overdueDays = default_class.overdueDays_isnotnull
        self.overdueAccount = default_class.overdueAccount_isnotnull
        self.loanAccount_default = default_class.loanAccount_isnotnull
        self.mortgageObjectt_default = default_class.mortgageObject_isnotnull
        self.familyTatalAsset_default = default_class.familyTatalAsset_isnotnull
        self.age_default = default_class.age
        self.workAge_default = default_class.work_age

        nodefault_class = nodefault.FIRSTDATA()
        nodefault_class.get_data()
        nodefault_class.data_process(nodefault_class.loanAmount, nodefault_class.loanAmount_isnotnull)
        nodefault_class.data_process(nodefault_class.mortgageObject, nodefault_class.mortgageObject_isnotnull)
        nodefault_class.data_process(nodefault_class.familyTatalAsset, nodefault_class.familyTatalAsset_isnotnull)
        nodefault_class.feature_time_process(nodefault_class.birihdy, "birihdy", nodefault_class.age)
        nodefault_class.feature_time_process(nodefault_class.workBeginTime, "workAge", nodefault_class.work_age)
        self.loanAccount_nodefault = nodefault_class.loanAmount_isnotnull
        self.mortgageObjectt_nodefault = nodefault_class.mortgageObject_isnotnull
        self.familyTatalAsset_nodefault = nodefault_class.familyTatalAsset_isnotnull
        self.age_nodefault = nodefault_class.age
        self.workAge_nodefault = nodefault_class.work_age
        print "lty", self.workAge_default

    def some_feature_remove_noise(self, feature, num, feature_remove_nose):
        for i in range(0, len(feature)):
            if feature[i] < num:
                feature_remove_nose.append(feature[i])


    def drawing(self, data1, data2, label1, label2, title):
        # plt.hist(data1)
        sns.distplot(data1, kde=True, color="#FF0000", rug=True, hist=True, label=label1)
        plt.legend(title=title)
        sns.distplot(data2, kde=True, rug=True, hist=True, label=label2)
        plt.legend(title=title)
        plt.xlabel("value")
        plt.ylabel("probability density")
        plt.show()


if __name__ == '__main__':
    ContrastiveAnalysis = ContrastiveAnalysis()
    ContrastiveAnalysis.continuous()
    ContrastiveAnalysis.some_feature_remove_noise(ContrastiveAnalysis.mortgageObjectt_nodefault, 5.4e+06,
                                                  ContrastiveAnalysis.mortgageObjectt_nodefault_remove_noise)
    ContrastiveAnalysis.some_feature_remove_noise(ContrastiveAnalysis.loanAccount_nodefault, 6.1e+06,
                                                  ContrastiveAnalysis.loanAccount_nodefault_remove_noise)
    ContrastiveAnalysis.some_feature_remove_noise(ContrastiveAnalysis.familyTatalAsset_nodefault, 0.5e+08,
                                                  ContrastiveAnalysis.familyTatalAsset_nodefaultt_remove_noise)
    ContrastiveAnalysis.some_feature_remove_noise(ContrastiveAnalysis.familyTatalAsset_default, 0.5e+08,
                                                  ContrastiveAnalysis.familyTatalAsset_defaultt_remove_noise)
    # ContrastiveAnalysis.drawing(ContrastiveAnalysis.loanAccount_default,
    #                             ContrastiveAnalysis.loanAccount_nodefault_remove_noise, "default", "no_default", "loanAccount")
    # ContrastiveAnalysis.drawing(ContrastiveAnalysis.mortgageObjectt_default,
    #                             ContrastiveAnalysis.mortgageObjectt_nodefault_remove_noise, "default", "no_default", "mortgageObject")
    # ContrastiveAnalysis.drawing(ContrastiveAnalysis.familyTatalAsset_defaultt_remove_noise,
    #                             ContrastiveAnalysis.familyTatalAsset_nodefaultt_remove_noise, "default", "no_default", "familyTatalAsset")
    # ContrastiveAnalysis.drawing(ContrastiveAnalysis.age_default,
    #                             ContrastiveAnalysis.age_nodefault, "default", "no_default", "age")