# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
根据以往的历史投资标的的利率,预测下一次投资的利率
"""

import sys
sys.path.append("/data/ml/tongyang/test/")
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import personas.version_1.base_method.read_conf as read_conf


class NextInvestBitPredictModelTraining:
    def __init__(self):
        self.fr = open(read_conf.ReadConf().get_options("path_next_invest_bid", "next_invest_ratio_train_path"), 'r')
        # self.fr = open("train.txt", 'r')  # 本地测试
        self.fw = open(read_conf.ReadConf().get_options("path_next_invest_bid", "next_invest_ratio_result_data_path"), 'wr')
        # self.fw = open("result.txt", 'wr') # 本地测试
        self.user_id_list = []
        self.rate_list = []  # 收益率list
        self.rate_pre_list = []  # 预测结果list
        # self.is_success = []  # 本地测试

    def get_train_data(self, is_success):
        try:
            for line in self.fr:
                line_one = line.split('\x01')
                # line_one = line.split('\t')  # 本地测试
                self.user_id_list.append(line_one[0])
                rate_tmp = line_one[2].split(',')
                rate_list_noe = []
                for i in rate_tmp:
                    rate_list_noe.append(int(i))
                self.rate_list.append(rate_list_noe)
            is_success.append(1)
        except Exception, e:
            print Exception, e
            is_success.append(0)

    def next_invest_predit_model_training(self, is_success):
        try:
            for i in range(0, len(self.rate_list)):
                y_train = [[self.rate_list[i][j]] for j in range(0, len(self.rate_list[i]))]
                # print y_train
                x_pre = [[len(self.rate_list[i])]]
                x_train = [[k] for k in range(0, len(self.rate_list[i]))]
                # print x_train
                clf = Pipeline([('poly', PolynomialFeatures(degree=5)), ('linear', LinearRegression(fit_intercept=False))])
                clf.fit(x_train, y_train)
                # 参数
                # print('Coefficients: \n', clf.named_steps['linear'].coef_)
                # print clf.predict(x_train)
                # 均方误差
                mean_error = np.mean((clf.predict(x_train) - y_train) ** 2)
                print("Residual sum of squares: %.2f" % mean_error)
                next_rate_pre = float(clf.predict(x_pre))
                if mean_error > 15 or next_rate_pre > 3 * self.rate_list[i][len(self.rate_list[i])-1] or next_rate_pre < self.rate_list[i][len(self.rate_list[i])-1]/3:
                    next_rate = np.mean(self.rate_list[i])
                else:
                    next_rate = round(float(clf.predict(x_pre)), 2)
                # print self.rate_pre_list
                # print "=============="
                self.fw.write(str(self.user_id_list[i]))
                self.fw.write('\t')
                self.fw.write(str(next_rate))
                self.fw.write('\n')

        except Exception, e:
            print Exception, e
            is_success.append(0)
        self.fw.close()


if __name__ == '__main__':
    test = NextInvestBitPredictModelTraining()
    # test.get_train_data(test.is_success)
    # test.next_invest_predit_model_training(test.is_success)

