# __author__ = 'lty'
# -*- coding: utf-8 -*-

import logging
import logging.config
import sys
sys.path.append("/root/personas_fengjr")
import time
import numpy as np
from sklearn.cluster import KMeans
import personas.version_1.base_method.read_conf as read_conf


class UserAgeModelTraining:
    def __init__(self):
        self.fr = open(read_conf.ReadConf().get_options("path_user_age", "user_age_train_path"), 'wr')
        self.fw = open(read_conf.ReadConf().get_options("path_user_age", "input_user_age_result_data_path"), 'wr')
        self.user_id = []
        self.age_list = []
        self.train_set = []  # 训练集
        self.pre_result_list = []  # 预测结果list
        self.pre_result_classification_list = []  # 预测分类结果list

    def get_train_data(self, is_success):
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('personas.get_train_data')
        try:
            fr = open(read_conf.ReadConf().get_options("path_user_age", "user_age_train_path"), 'r')
            for line in fr:
                line_one = line.split('\t')
                self.user_id.append(line_one[0])
                self.age_list.append(line_one[1])
            for i in range(0, len(self.age_list)):
                tmp = [int(self.age_list[i])]
                self.train_set.append(tmp)
            logger.info("get_train_data is successed !")
            is_success.append(1)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_train_data is Exception !"
            logger.error(error_info)
            is_success.append(0)

    def kmeans_age(self, is_success):
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('personas.kmeans_age')
        try:
            age_set = np.array(self.train_set)
            random_state = 170
            y_pre = KMeans(n_clusters=5, random_state=random_state).fit_predict(age_set)
            self.pre_result_list = np.ndarray.tolist(y_pre)
            logger.info("kmeans_age is successed !")
            is_success.append(1)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "kmeans_age is Exception !"
            logger.error(error_info)
            is_success.append(0)

    def get_classification_result(self, is_success):
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('personas.get_classification_result')
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
            logger.info("get_classification_result is successed !")
            is_success.append(1)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_classification_result is Exception !"
            logger.error(error_info)
            is_success.append(0)

    def get_result(self, is_success):
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('personas.get_train_data')
        try:
            for i in range(0, len(self.user_id)):
                self.fw.write(self.user_id[i])
                self.fw.write('\t')
                self.fw.write(str(self.age_list[i]).replace('\n', ''))
                self.fw.write('\t')
                self.fw.write(str(self.pre_result_list[i]))
                self.fw.write('\t')
                self.fw.write(str(self.pre_result_classification_list[i]))
                self.fw.write('\n')
            logger.info("get_result is successed !")
            is_success.append(1)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_result is Exception !"
            logger.error(error_info)
            is_success.append(0)


if __name__ == '__main__':
    test = UserAgeModelTraining()
