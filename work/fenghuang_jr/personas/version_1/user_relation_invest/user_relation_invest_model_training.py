# __author__ = 'lty'
# -*- coding: utf-8 -*-
import sys
sys.path.append("/data/ml/tongyang/test/")
import numpy as np
from sklearn.cluster import KMeans
from math import sqrt
# import personas.version_1.base_method.read_conf as read_conf
import cf


class UserRelationInvestModelTraining:
    def __init__(self):
        # self.fr = open(read_conf.ReadConf().get_options("path_invest_var", "user_invest_var_train_path"), 'r')
        self.fr = open("/Users/litongyang/Desktop/train_data/train_user_relation.txt", "r")
        self.fw = open("result.txt", 'wr')
        self.user_id = []
        self.deadline_type = []  # 标的期限分类
        self.rate_tye = []  # 标的收益率分类
        self.buy_cnt = []   # 购买次数
        self.train_set = {}  # 训练集
        self.user_id_result_list = []
        self.recommend_bid_list = []  # 推荐的bid的list
        self.recommend_near_user_list = []  # 推荐相关度最大的user的list

    def get_train_data(self):
        try:
            for line in self.fr:
                # lines = line.strip().split(',')
                lines = line.strip().split()
                if lines[0] not in self.train_set:
                    self.train_set[lines[0]] = {}
                # users[lines[0]][lines[2]] = float(lines[1])
                key = ''
                for i in range(1, len(lines) - 1):
                    key += str(lines[i]) + '-'
                key = key[:len(key) - 1]
                self.train_set[lines[0]][key] = int(lines[len(lines) - 1])
            # is_success.append(1)
        except Exception, e:
            print Exception, e
            # is_success.append(0)

    def compute_model(self):
        for user_id, v in self.train_set.items():
            if user_id == "EC3037B7-8845-43E5-A1D7-0CADDF448F34":
                self.user_id_result_list.append(user_id)
                cf_model = cf.Cf(self.train_set)
                k, self.recommend_near_user_list = cf_model.recommend("%s" % user_id)
                for i in range(len(k)):
                    self.recommend_bid_list.append(k[i][0])
                # return bid_list, nearuser[:15]  # bid_list购买的产品，nearuser[:15]最近邻的15个用户
                self.recommend_near_user_list = self.recommend_near_user_list[:15]
                print self.recommend_bid_list
                print self.recommend_near_user_list
                print "==========================="
                for i in range(0, len(self.user_id_result_list)):
                    for j in range(0, len(self.recommend_bid_list)):
                        self.fw.write(str(self.user_id_result_list[i]))
                        self.fw.write('\t')
                        self.fw.write(str(self.recommend_bid_list[j]))
                        self.fw.write('\n')

    # def get_result(self):
    #     for i in range(0, len(self.user_id_result_list)):
    #         for j in range(0, len(self.recommend_bid_list)):
    #             self.fw.write(str(self.user_id_result_list[i]))
    #             self.fw.write('\t')
    #             self.fw.write(str(self.recommend_bid_list[j]))
    #             self.fw.write('\n')


if __name__ == '__main__':
    test = UserRelationInvestModelTraining()
    test.get_train_data()
    test.compute_model()
