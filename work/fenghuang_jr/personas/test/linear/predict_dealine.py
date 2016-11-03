# __author__ = 'lty'
# -*- coding: utf-8 -*-

# __author__ = 'lty'
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


class LinearTest:
    def __init__(self):
        self.fl = open('train.txt', 'r')
        self.fw = open('predict_dealine_result.txt', 'wr')
        self.userid_list = []
        self.rate_list = []
        self.rate_pre_list = []

    def get_train_data(self):
        for line in self.fl:
            line_one = line.split()
            self.userid_list.append(line_one[0])
            rate_tmp = line_one[1].split(',')
            rate_list_noe = []
            for i in rate_tmp:
                rate_list_noe.append(int(i))
            self.rate_list.append(rate_list_noe)
        # print self.rate_list

    def ml_regression(self, rate_list_noe):
        y_train = [[rate_list_noe[i]] for i in range(0, len(rate_list_noe))]
        print y_train
        x_pre = [[len(rate_list_noe)]]
        x_train = [[i] for i in range(0, len(rate_list_noe))]
        print x_train

        clf = Pipeline([('poly', PolynomialFeatures(degree=8)), ('linear', LinearRegression(fit_intercept=False))])
        clf.fit(x_train, y_train)
        # 参数
        print('Coefficients: \n', clf.named_steps['linear'].coef_)
        print clf.predict(x_train)
        # 均方误差
        print("Residual sum of squares: %.2f" % np.mean((clf.predict(x_train) - y_train) ** 2))
        print clf.predict(3)  # 预测值
        self.rate_pre_list.append(str(clf.predict(x_pre)))

        # Plot outputs
        plt.scatter(x_train, y_train, color='black')
        plt.plot(x_train, clf.predict(x_train), color='blue', linewidth=3)

        plt.xticks(())
        plt.yticks(())
        plt.show()

    def get_result(self):
        for i in range(0, len(self.userid_list)):
            self.fw.write(self.userid_list[i])
            self.fw.write('\t')
            self.fw.write(self.rate_pre_list[i])
            self.fw.write('\n')

if __name__ == '__main__':
    test = LinearTest()
    test.get_train_data()
    for i in range(0, len(test.rate_list)):
        test.ml_regression(test.rate_list[i])
        print "============"
    test.get_result()
