# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
对用户历史投资固收的利率方差进行分类
"""

import sys
sys.path.append("/root/personas_fengjr")
import datetime
import logging
import logging.config
import numpy as np
from sklearn.cluster import KMeans
import personas.version_1.base_method.read_conf as read_conf


class InvestVarModelTraining:
    def __init__(self):
        self.fw = open(read_conf.ReadConf().get_options("path_invest_var", "input_invest_var_result_data_path"), 'wr')
        self.user_id = []
        self.var_list = []  # 方差list
        self.train_set = []  # 训练集
        self.pre_result_list = []  # 预测结果list
        self.pre_result_classification_list = []  # 预测分类结果list

    def get_train_data(self, is_success):
        logger = logging.getLogger('personas.get_train_data')
        try:
            fr = open(read_conf.ReadConf().get_options("path_invest_var", "user_invest_var_train_path"), 'r')
            for line in fr:
                line_one = line.split('\t')
                self.user_id.append(line_one[0])
                self.var_list.append(float(line_one[1]))
                tmp = [0, float(line_one[1])]
                self.train_set.append(tmp)
            is_success.append(1)
            logger.info("get_train_data is successed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_train_data is Exception !"
            logger.error(error_info)
            is_success.append(0)

    def kmeans_var(self, is_success):
        logger = logging.getLogger('personas.kmeans_var')
        try:
            train_data = np.array(self.train_set)
            # print train_data[:, 1]
            random_state = 170
            y_pre = KMeans(n_clusters=3, random_state=random_state).fit_predict(train_data)
            self.pre_result_list = np.ndarray.tolist(y_pre)
            is_success.append(1)
            logger.info("kmeans_var is successed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "kmeans_var is Exception !"
            logger.error(error_info)
            is_success.append(0)

    def get_classification_result(self, is_success):
        logger = logging.getLogger('personas.get_classification_result')
        try:
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
            is_success.append(1)
            logger.info("get_classification_result is successed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_classification_result is Exception !"
            logger.error(error_info)
            is_success.append(0)

    def get_result(self, is_success):
        logger = logging.getLogger('personas.get_result')
        try:
            for i in range(0, len(self.user_id)):
                self.fw.write(self.user_id[i])
                self.fw.write('\t')
                self.fw.write(str(self.var_list[i]))
                self.fw.write('\t')
                self.fw.write(str(self.pre_result_list[i]))
                self.fw.write('\t')
                self.fw.write(str(self.pre_result_classification_list[i]))
                self.fw.write('\n')
            is_success.append(1)
            logger.info("get_result is successed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_result is Exception !"
            logger.error(error_info)
            is_success.append(0)


if __name__ == '__main__':
    test = InvestVarModelTraining()
    # test.get_train_data()
    # test.kmeans_var()
    # test.get_classification_result()
    # test.get_result()
