# __author__ = 'lty'
# -*- coding: utf-8 -*-
import sys
sys.path.append("/root/personas_fengjr/")
import logging
import logging.config
import cf
import traceback
import personas.version_1.base_method.read_conf as read_conf


class UserRelationInvestViewModelTraining:
    def __init__(self):
        self.fw_bid = open(read_conf.ReadConf().get_options("path_user_relation_invest_view", "input_user_relation_invest_view_bid_result_data_path"), 'wr')
        self.fw_user = open(read_conf.ReadConf().get_options("path_user_relation_invest_view", "input_user_relation_invest_view_user_result_data_path"), 'wr')
        # self.fr = open("/Users/litongyang/Desktop/test.txt", "r")  # 本地测试
        # self.fw_bid = open("result.txt", 'wr')  # 本地测试
        # self.fw_user = open("result_invest.txt", 'wr')  # 本地测试
        self.user_id = []
        self.user_id_view_no_invest = []  # 只浏览不投资的用户id
        self.deadline_type = []  # 标的期限分类
        self.rate_tye = []  # 标的收益率分类
        self.view_bid_cnt = []  # 浏览标的次数
        self.buy_cnt = []   # 购买次数
        self.train_set = {}  # 浏览训练集
        self.train_set_invest_view = {}  # 投资训练集
        self.train_set_invest_invest = {}  # 投资训练集
        self.train_set_view = {}  # 只浏览不投资训练集
        self.user_id_view_invest = []  # 浏览和投资的user
        self.recommend_bid_list = []  # 推荐的bid的list
        self.recommend_near_user_list = []  # 推荐相关度最大的user的list
        self.is_success = []
        self.error_cnt = 0
        self.error_cnt_threshold = 10000

    def get_train_data(self, is_success):
        logger = logging.getLogger('personas.get_train_data')
        try:
            fr = open(read_conf.ReadConf().get_options("path_user_relation_invest_view","user_relation_invest_view_train_path"), 'r')
            # fr = open("/Users/litongyang/Desktop/test.txt", "r")  # 本地测试
            for line in fr:
                lines = line.strip().split('\t')
                # lines = line.strip().split('\x01')
                if lines[0] not in self.train_set:
                    self.train_set[lines[0]] = {}
                if lines[len(lines) - 1] == '1':
                    self.user_id_view_invest.append(str(lines[0]))
                if lines[len(lines) - 1] == '0':
                    self.user_id_view_no_invest.append(str(lines[0]))
                if lines[0] not in self.train_set_invest_view and lines[len(lines) - 1] == '1':
                    self.train_set_invest_view[lines[0]] = {}
                    self.train_set_invest_invest[lines[0]] = {}
                if lines[0] not in self.train_set_view and lines[len(lines) - 1] == '0':
                    self.train_set_view[lines[0]] = {}
                key = ''
                for i in range(1, 3):
                    key += str(lines[i]) + '-'
                key = key[:len(key) - 1]
                self.train_set[lines[0]][key] = (int(lines[len(lines) - 3]))
                if lines[len(lines) - 1] == '0':
                    self.train_set_view[lines[0]][key] = (int(lines[3]))
                if lines[len(lines) - 1] == '1':
                    self.train_set_invest_view[lines[0]][key] = (int(lines[3]))
                    self.train_set_invest_invest[lines[0]][key] = (int(lines[4]))
            self.user_id_view_invest = list(set(self.user_id_view_invest))  # 去重
            self.user_id_view_no_invest = list(set(self.user_id_view_no_invest))  # 去重
            # for k, v in self.train_set.items():
            #     print k, v
            is_success.append(1)
            logger.info("get_train_data is success !")
            # print self.train_set_invest
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
                    # self.user_id_result_list.append(user_id)
                    if user_id in self.user_id_view_invest:
                        flag = 'invest'
                        cf_model = cf.Cf(self.train_set, self.train_set, self.train_set, self.user_id_view_invest)
                    else:
                        flag = 'view'
                        cf_model = cf.Cf(self.train_set_view, self.train_set_invest_view, self.train_set_invest_invest,
                                                                    self.user_id_view_invest)
                    recommend_bid, self.recommend_near_user_list = cf_model.recommend("%s" % user_id)
                    self.recommend_near_user_list = self.recommend_near_user_list[:3]
                    recommend_bid = recommend_bid[:3]
                    # print "recommend_bid", recommend_bid
                    # print "recommend_near_user_list", self.recommend_near_user_list
                    # print "==========================="
                    for i in range(len(recommend_bid)):
                        self.fw_bid.write(str(user_id))
                        self.fw_bid.write('\t')
                        self.fw_bid.write(str(flag))
                        self.fw_bid.write('\t')
                        self.fw_bid.write(str(recommend_bid[i][0]))
                        self.fw_bid.write('\t')
                        self.fw_bid.write(str(recommend_bid[i][1]))
                        self.fw_bid.write('\n')
                    for j in range(len(self.recommend_near_user_list)):
                        self.fw_user.write(str(user_id))
                        self.fw_user.write('\t')
                        self.fw_user.write(str(flag))
                        self.fw_user.write('\t')
                        self.fw_user.write(str(self.recommend_near_user_list[j][0]))
                        self.fw_user.write('\t')
                        self.fw_user.write(str(self.recommend_near_user_list[j][1]))
                        self.fw_user.write('\n')
                except Exception, e:
                    print traceback.print_exc()
                    exception = Exception, e
                    error_info = str(exception) + "--------->>" + str(user_id) + " is Exception !"
                    logger.error(error_info)
                    self.error_cnt += 1
            if self.error_cnt < self.error_cnt_threshold:
                is_success.append(1)
            else:
                is_success.append(0)
            logger.info("compute_model_save_result_data is success !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "compute_model_save_result_data is Exception !"
            logger.error(error_info)
            is_success.append(0)
        self.fw_bid.close()
        self.fw_user.close()

if __name__ == '__main__':
    test = UserRelationInvestViewModelTraining()
    test.get_train_data(test.is_success)
    # test.compute_model_save_result_data(test.is_success)

