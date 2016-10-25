# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
对用户历史投资固收的利率方差进行分类
"""


import numpy as np
from sklearn.cluster import KMeans


class TrainDdata:
    def __init__(self):
        self.fr = open('user_var.txt', 'r')
        self.fw = open('result_user_var.txt', 'wr')
        self.user_id = []
        self.var_list = []  # 方差list
        self.train_set = []  # 训练级
        self.pre_result_list = []  # 预测结果list
        self.pre_result_classification_list = []  # 预测分类结果list

    def get_train_data(self):
        for line in self.fr:
            line_one = line.split()
            self.user_id.append(line_one[0])
            self.var_list.append(float(line_one[1]))
            tmp = [0, float(line_one[1])]
            self.train_set.append(tmp)

    def kmeans_var(self):
        train_data = np.array(self.train_set)
        # print train_data[:, 1]
        random_state = 170
        y_pre = KMeans(n_clusters=3, random_state=random_state).fit_predict(train_data)
        self.pre_result_list = np.ndarray.tolist(y_pre)
        # plt.scatter(train_data[:, 0], train_data[:, 1], c=self.pre_result_list)
        # plt.title("test")
        # plt.show()

    def get_classification_result(self):
        value_0 = ''  # 聚类等于0的值
        value_1 = ''  # 聚类等于1的值
        value_2 = ''  # 聚类等于2的值
        classification = {}

        for i in range(0, len(self.pre_result_list)):
            if self.pre_result_list[i] == 0:
                value_0 = self.var_list[i]
            elif self.pre_result_list[i] == 1:
                value_1 = self.var_list[i]
            else:
                value_2 = self.var_list[i]
        tmp = [value_0, value_1, value_2]
        sort_value = sorted(tmp)
        for i in range(0, len(tmp)):
            if sort_value[0] == tmp[i]:
                classification[i] = 'low'
        for i in range(0, len(tmp)):
            if sort_value[1] == tmp[i]:
                classification[i] = 'mid'
        for i in range(0, len(tmp)):
            if sort_value[2] == tmp[i]:
                classification[i] = 'high'
        for i in range(0, len(self.pre_result_list)):
            self.pre_result_classification_list.append(classification[self.pre_result_list[i]])
        # print self.pre_result_list
        # print self.pre_result_classification_list

    def get_result(self):
        for i in range(0, len(self.user_id)):
            self.fw.write(self.user_id[i])
            self.fw.write('\t')
            self.fw.write(str(self.var_list[i]))
            self.fw.write('\t')
            self.fw.write(str(self.pre_result_list[i]))
            self.fw.write('\t')
            self.fw.write(str(self.pre_result_classification_list[i]))
            self.fw.write('\n')


if __name__ == '__main__':
    test = TrainDdata()
    test.get_train_data()
    test.kmeans_var()
    test.get_classification_result()
    test.get_result()