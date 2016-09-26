# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import numpy as np


class MLTEST():
    def __init__(self):
        self.testdata = []

        self.Company_code = 600519
        self.data_file = 'stock_' + str("%06d" % self.Company_code)
        self.fileName = 'parameters_' + str("%06d" % self.Company_code)

        self.db_name = 'STOCK_INFO_2014'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码

    def data(self):
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            count = cur.execute("SELECT * FROM %s WHERE Parameters='净资产收益率(%%)'" % self.fileName)
            results = cur.fetchmany(count)
            if len(results) == 0:
                self.testdata = [-1 for i in range(0, 10)]
            else:
                for i in range(3, 13):
                    self.testdata.append(results[0][i])
        except:
            pass

    def drawing(self):
        year = [i for i in range(0, 10)]
        plt.plot(year, self.testdata)
        plt.grid()
        plt.xticks(range(min(year), max(year), 1))
        plt.show()

    def ml_regression(self):

        yTest = [[self.testdata[i]] for i in range(0, 9)]
        y = self.testdata[9]
        print yTest
        xTest = [[i] for i in range(0, 9)]

        clf = Pipeline([('poly', PolynomialFeatures(degree=2)), ('linear', LinearRegression(fit_intercept=False))])
        clf.fit(xTest, yTest)
        # 参数
        print('Coefficients: \n', clf.named_steps['linear'].coef_)

        # 均方误差
        print("Residual sum of squares: %.2f" % np.mean((clf.predict(9) - y) ** 2))
        print clf.predict(8)  # 预测值
        print y

        # Plot outputs
        plt.scatter(xTest, yTest, color='black')
        plt.plot(xTest, clf.predict(xTest), color='blue', linewidth=3)

        plt.xticks(())
        plt.yticks(())
        plt.show()


if __name__ == '__main__':
    Mltest = MLTEST()
    for Mltest.Company_code in range(600519, 600520):
        Mltest.data()
        # Mltest.drawing()
        Mltest.ml_regression()
        Mltest.Company_code += 1
        Mltest.data_file = 'parameters_' + str("%06d" % Mltest.Company_code)
