# -*- coding: utf-8 -*-
import pandas as pd
import math
from sklearn.model_selection import train_test_split
import sklearn.linear_model  as linear_model
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
import pickle
"""
简介：通过测氧传感器输出电势、温度，来预测炉气碳势
"""


class CarbonRegression:
    def __init__(self):
        self.data = pd.read_excel('data.xls', encoding='utf-8')
        self.oxygen_data = ''  # 氧电势数据
        self.temperature = ''  # 温度数据
        self.carbon = ''  # 炉气碳数据
        self.train_x = []
        self.train_y = []

    def data_cleaning(self):
        self.oxygen_data = self.data[111]  # 获取氧电势数据
        # print self.oxygen_data
        self.temperature = self.data.columns.values[1:]  # 获取温度数据
        temp = self.data
        # print self.temperature
        for i in self.temperature:
            for j in range(0, len(self.data)):
                if not math.isnan(self.data[i][j]):
                    train_one_x = []
                    # print "i:", i
                    # print self.oxygen_data[j]
                    # print self.data[i][j]
                    train_one_x.append(i)
                    train_one_x.append(self.oxygen_data[j])
                    self.train_x.append(train_one_x)
                    self.train_y.append(self.data[i][j])
                    # print "============"
                else:
                    pass
        print len(self.train_x)
        print len(self.train_y)

        # self.carbon = temp.drop(columns=111).values  # 获取炉气碳数据
        # print self.carbon

    def train_data(self):
        X_train, X_test, Y_train, Y_test =train_test_split(self.train_x, self.train_y, test_size=0.3,random_state=0)
        print X_train
        print Y_test
        log_reg = linear_model.LinearRegression()
        model = log_reg.fit(X_train, Y_train)
        ypre = model.predict(X_test)

        """评估模型"""
        print mean_absolute_error(Y_test, ypre)  # 平均绝对误差
        print explained_variance_score(Y_test, ypre)  # 方差得分
        print mean_squared_error(Y_test, ypre)  # 均方差
        print r2_score(Y_test, ypre)  # 判定系数

        """保存模型"""
        with open('clf.pickle', 'wb') as f:
            pickle.dump(model, f)

        """读取模型"""
        with open('clf.pickle', 'rb') as f:
            clf2 = pickle.load(f)
            # 测试读取后的Model
            print(clf2.predict(X_test))




if __name__ == '__main__':
    carbon_regression = CarbonRegression()
    carbon_regression.data_cleaning()
    carbon_regression.train_data()
    # print carbon_regression.data
    # print carbon_regression.oxygen_data
    # print carbon_regression.temperature
    # print carbon_regression.carbon