# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
基于用户投资行为的用户关系模型和产品推荐模型
"""
import get_user_relation_invest_train
import user_relation_invest_model_training
import save_user_relation_invest_result_data


class UserRelationInvest:
    def __init__(self):
        self.get_train_set = get_user_relation_invest_train.GetRelationInvestTrain()
        self.model_training = user_relation_invest_model_training.UserRelationInvestModelTraining()
        self.save_hive = save_user_relation_invest_result_data.SaveUserRelationInvestResultData()
        self.is_success = []

    def implement_process(self):
        """ 得到训练集 """
        self.get_train_set.get_train_set(self.is_success)
        """ 模型训练 """
        self.model_training.get_train_data(self.is_success)
        self.model_training.compute_model_save_result_data(self.is_success)
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
    test = UserRelationInvest()
    test.implement_process()