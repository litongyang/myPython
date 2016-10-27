# __author__ = 'lty'
# -*- coding: utf-8 -*-
import sys
sys.path.append("/data/ml/tongyang/test/")
import numpy as np
from sklearn.cluster import KMeans
import personas.version_1.base_method.read_conf as read_conf


class UserAgeModelTraining:
    def __init__(self):
        self.fr = open(read_conf.ReadConf().get_options("path_user_age", "user_age_train_path"), 'r')
        self.fw = open(read_conf.ReadConf().get_options("path_user_age", "input_user_age_result_data_path"), 'wr')
        self.user_id = []
        self.age_list = []
        self.train_set = []  # 训练集
        self.pre_result_list = []  # 预测结果list
        self.pre_result_classification_list = []  # 预测分类结果list

    def get_train_data(self, is_success):
        try:
            for line in self.fr:
                line_one = line.split('\x01')
                self.user_id.append(line_one[0])
                self.age_list.append(line_one[1])
            for i in range(0, len(self.age_list)):
                tmp = [int(self.age_list[i])]
                self.train_set.append(tmp)
            is_success.append(1)
        except Exception, e:
            print Exception, e
            is_success.append(0)

    def kmeans_age(self, is_success):
        try:
            age_set = np.array(self.train_set)
            random_state = 170
            y_pre = KMeans(n_clusters=5, random_state=random_state).fit_predict(age_set)
            self.pre_result_list = np.ndarray.tolist(y_pre)
            is_success.append(1)
        except Exception, e:
            print Exception, e
            is_success.append(0)

    def get_classification_result(self, is_success):
        try:
            value_0 = ''  # 聚类等于0的值
            value_1 = ''  # 聚类等于1的值
            value_2 = ''  # 聚类等于2的值
            value_3 = ''  # 聚类等于3的值
            value_4 = ''  # 聚类等于4的值
            classification = {}

            for i in range(0, len(self.pre_result_list)):
                if self.pre_result_list[i] == 0:
                    value_0 = self.age_list[i]
                elif self.pre_result_list[i] == 1:
                    value_1 = self.age_list[i]
                elif self.pre_result_list[i] == 2:
                    value_2 = self.age_list[i]
                elif self.pre_result_list[i] == 3:
                    value_3 = self.age_list[i]
                else:
                    value_4 = self.age_list[i]
            tmp = [value_0, value_1, value_2, value_3, value_4]
            sort_value = sorted(tmp)
            for i in range(0, len(tmp)):
                if sort_value[0] == tmp[i]:
                    classification[i] = 'young'
            for i in range(0, len(tmp)):
                if sort_value[1] == tmp[i]:
                    classification[i] = 'young_mid'
            for i in range(0, len(tmp)):
                if sort_value[2] == tmp[i]:
                    classification[i] = 'mid'
            for i in range(0, len(tmp)):
                if sort_value[3] == tmp[i]:
                    classification[i] = 'mid_old'
            for i in range(0, len(tmp)):
                if sort_value[4] == tmp[i]:
                    classification[i] = 'old'
            for i in range(0, len(self.pre_result_list)):
                self.pre_result_classification_list.append(classification[self.pre_result_list[i]])
            is_success.append(1)
        except Exception, e:
            print Exception, e
            is_success.append(0)

    def get_result(self, is_success):
        try:
            for i in range(0, len(self.user_id)):
                self.fw.write(self.user_id[i])
                self.fw.write('\t')
                self.fw.write(str(self.age_list[i]))
                self.fw.write('\t')
                self.fw.write(str(self.pre_result_list[i]))
                self.fw.write('\t')
                self.fw.write(str(self.pre_result_classification_list[i]))
                self.fw.write('\n')
            is_success.append(1)
        except Exception, e:
            print Exception, e
            is_success.append(0)


if __name__ == '__main__':
    test = UserAgeModelTraining()
