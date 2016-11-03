# __author__ = 'lty'
# -*- coding: utf-8 -*-
import sys
sys.path.append("/data/ml/tongyang/test/")
# import personas.version_1.base_method.read_conf as read_conf
import cf


class UserRelationInvestViewModelTraining:
    def __init__(self):
        # self.fr = open(read_conf.ReadConf().get_options("path_user_relation_invest_view", "user_relation_invest_view_train_path"), 'r')
        # self.fw = open(read_conf.ReadConf().get_options("path_user_relation_invest_view", "input_user_relation_invest_view_result_data_path"), 'wr')
        self.fr = open("/Users/litongyang/Desktop/test.txt", "r")  # 本地测试
        # self.fr = open("/Users/litongyang/Desktop/test1.txt", "r")  # 本地测试
        # self.fw = open("result.txt", 'wr') # 本地测试
        self.user_id = []
        self.user_id_view_no_invest = []  # 只浏览不投资的用户id
        self.deadline_type = []  # 标的期限分类
        self.rate_tye = []  # 标的收益率分类
        self.view_bid_cnt = []  # 浏览标的次数
        self.buy_cnt = []   # 购买次数
        self.train_set = {}  # 训练集
        self.train_set_1 = {}  # 训练集
        self.user_id_result_list = []
        self.recommend_bid_list = []  # 推荐的bid的list
        self.recommend_near_user_list = []  # 推荐相关度最大的user的list
        self.is_success = []

    def get_train_data(self, is_success):
        try:
            for line in self.fr:
                lines = line.strip().split()
                # lines = line.strip().split('\x01')
                if lines[0] not in self.train_set:
                    self.train_set[lines[0]] = {}
                if lines[0] not in self.train_set_1:
                    self.train_set_1[lines[0]] = {}
                # users[lines[0]][lines[2]] = float(lines[1])
                key = ''
                for i in range(1, len(lines) - 2):
                    key += str(lines[i]) + '-'
                key = key[:len(key) - 1]
                self.train_set[lines[0]][key] = (int(lines[len(lines) - 2]))
                self.train_set_1[lines[0]][key] = (int(lines[len(lines) - 1]))
                # self.train_set[lines[0]][key].append(int(lines[len(lines) - 2]))
                # self.train_set[lines[0]][key].append(str(lines[len(lines) - 1]))
            is_success.append(1)
            print self.train_set
            print self.train_set_1
        except Exception, e:
            print Exception, e
            is_success.append(0)

    def get_view_not_invest_user(self):

        for k, v in self.train_set_1.items():
            flag = 0
            for k1, v1 in v.items():
                if v1 != 0:
                    flag = 1
                    break
                else:
                    flag = 0
            if flag == 0:
                self.user_id_view_no_invest.append(k)
        print self.user_id_view_no_invest


    """ 计算模型,并将最终结果存入 """
    def compute_model_save_result_data(self, is_success):
        for user_id, v in self.train_set.items():
            try:
                # if user_id == "EC3037B7-8845-43E5-A1D7-0CADDF448F34":
                self.user_id_result_list.append(user_id)
                cf_model = cf.Cf(self.train_set, self.train_set_1, self.user_id_view_no_invest)
                k, self.recommend_near_user_list = cf_model.recommend("%s" % user_id)
                # print "kkk", k
                for i in range(len(k)):
                    self.recommend_bid_list.append(k[i][0])
                # return bid_list, nearuser[:15]  # bid_list购买的产品，nearuser[:15]最近邻的15个用户
                self.recommend_near_user_list = self.recommend_near_user_list[:15]
                print self.recommend_bid_list
                print self.recommend_near_user_list
                print "==========================="
                # for i in range(0, len(self.user_id_result_list)):
                #     for j in range(0, len(self.recommend_bid_list)):
                #         self.fw.write(str(self.user_id_result_list[i]))
                #         self.fw.write('\t')
                #         self.fw.write(str(self.recommend_bid_list[j]))
                #         self.fw.write('\n')
                is_success.append(1)
            except Exception, e:
                print Exception, e
                is_success.append(0)
        # self.fw.close()

if __name__ == '__main__':
    test = UserRelationInvestViewModelTraining()
    test.get_train_data(test.is_success)
    test.get_view_not_invest_user()
    test.compute_model_save_result_data(test.is_success)

