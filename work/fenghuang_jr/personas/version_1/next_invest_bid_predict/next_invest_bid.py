# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
用户投资稳定性分类模型
"""
import get_invest_rate_train_set
import next_invest_bid_predict_model_training
import save_next_bid_rate_result_data


class NextInvestBid:
    def __init__(self):
        self.get_train_set = get_invest_rate_train_set.GetInvestRateTrainSet()
        self.model_training = next_invest_bid_predict_model_training.NextInvestBitPredictModelTraining()
        self.save_hive = save_next_bid_rate_result_data.SaveNextInvetBidResultData()
        self.is_success = []  # 每一步运行成功或者失败的标记

    def implement_process(self):
        """ 得到训练集 """
        self.get_train_set.get_train_set(self.is_success)

        """ 模型训练 """
        self.model_training.get_train_data(self.is_success)
        self.model_training.next_invest_deadline_predit_model_training(self.is_success)
        self.model_training.next_invest_rate_predit_model_training(self.is_success)

        """ 将训练好的数据存入hive表 """
        flag = 1
        for v in self.is_success:
            if v == 0:
                flag = 0
                break
        if flag == 1:
            self.save_hive.get_result_data(self.is_success)
        else:
            print "error"
        for v in self.is_success:
            if v == 0:
                flag = 0
                break
        if flag == 1:
            print "success"
        else:
            print "error"

if __name__ == '__main__':
    test = NextInvestBid()
    test.implement_process()
