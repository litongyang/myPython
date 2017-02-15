# __author__ = 'lty'
# -*- coding: utf-8 -*-
import sys
sys.path.append("/root/personas_fengjr/")
import logging
import logging.config
import personas.version_1.base_method.read_conf as read_conf
import cf


class UserRelationInvestModelTraining:
    def __init__(self):
        self.fw = open(read_conf.ReadConf().get_options("path_user_relation_invest", "input_user_relation_invest_bid_result_data_path"), 'wr')
        self.fw_user = open(read_conf.ReadConf().get_options("path_user_relation_invest", "input_user_relation_invest_user_result_data_path"), 'wr')
        # self.fr = open("/Users/litongyang/Desktop/train_data/train_user_relation.txt", "r")  # 本地测试
        # self.fw = open("result.txt", 'wr')  # 本地测试
        # self.fw_user = open("result_user.txt", 'wr')  # 本地测试
        self.user_id = []
        self.deadline_type = []  # 标的期限分类
        self.rate_tye = []  # 标的收益率分类
        self.buy_cnt = []   # 购买次数
        self.train_set = {}  # 训练集
        self.user_id_result_list = []
        self.recommend_bid_list = []  # 推荐的bid的list
        self.recommend_near_user_list = []  # 推荐相关度最大的user的list
        self.recommend_bid_cnt = 3
        self.is_success = []
        self.error_cnt = 0
        self.error_cnt_threshold = 10000

    def get_train_data(self, is_success):
        logger = logging.getLogger('personas.get_train_data')
        try:
            fr = open(read_conf.ReadConf().get_options("path_user_relation_invest", "user_relation_invest_train_path"), 'r')
            for line in fr:
                lines = line.strip().split('\t')
                # lines = line.strip().split('\x01')
                if lines[0] not in self.train_set:
                    self.train_set[lines[0]] = {}
                # users[lines[0]][lines[2]] = float(lines[1])
                key = ''
                for i in range(1, len(lines) - 1):
                    key += str(lines[i]) + '-'
                key = key[:len(key) - 1]
                self.train_set[lines[0]][key] = int(lines[len(lines) - 1])
            is_success.append(1)
            logger.info("get_train_data is successed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_train_data is Exception !"
            logger.error(error_info)
            is_success.append(0)

    """ 计算模型,并将最终结果存入 """
    def compute_model_save_result_data(self, is_success):
        logger = logging.getLogger('personas.compute_model_save_result_data')
        try:
            for user_id, v in self.train_set.items():
                try:
                    # if user_id == "EC3037B7-8845-43E5-A1D7-0CADDF448F34":
                    recommend_bid_list = []
                    cf_model = cf.Cf(self.train_set)
                    recommend_bid_list_tmp, self.recommend_near_user_list = cf_model.recommend("%s" % user_id)
                    if len(recommend_bid_list_tmp) <= self.recommend_bid_cnt:
                        for i in range(len(recommend_bid_list_tmp)):
                            recommend_bid_list.append(recommend_bid_list_tmp[i])
                    else:
                        for i in range(self.recommend_bid_cnt):
                            recommend_bid_list.append(recommend_bid_list_tmp[i])
                    # return bid_list, nearuser[:15]  # bid_list购买的产品，nearuser[:15]最近邻的15个用户
                    recommend_near_user_list = self.recommend_near_user_list[:3]
                    # print recommend_bid_list
                    # print self.recommend_near_user_list
                    # print "==========================="
                    # for i in range(0, len(self.user_id_result_list)):
                    for i in range(0, len(recommend_near_user_list)):
                        self.fw_user.write(str(user_id))
                        self.fw_user.write('\t')
                        self.fw_user.write(str(recommend_near_user_list[i][0]))
                        self.fw_user.write('\t')
                        self.fw_user.write(str(recommend_near_user_list[i][1]))
                        self.fw_user.write('\n')
                    if len(recommend_bid_list) > 0:
                        for j in range(0, len(recommend_bid_list)):
                            self.fw.write(str(user_id))
                            self.fw.write('\t')
                            self.fw.write(str(recommend_bid_list[j][0]))
                            self.fw.write('\t')
                            self.fw.write(str(recommend_bid_list[j][1]))
                            self.fw.write('\n')
                except Exception, e:
                    exception = Exception, e
                    error_info = str(exception) + "--------->>" + str(user_id) + " is Exception !"
                    logger.error(error_info)
                    self.error_cnt += 1
            if self.error_cnt < self.error_cnt_threshold:
                is_success.append(1)
            else:
                is_success.append(0)
            logger.info("compute_model_save_result_data is successed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "compute_model_save_result_data is Exception !"
            logger.error(error_info)
            is_success.append(0)
        self.fw.close()
        self.fw_user.close()

if __name__ == '__main__':
    test = UserRelationInvestModelTraining()
    test.get_train_data(test.is_success)
    test.compute_model_save_result_data(test.is_success)

