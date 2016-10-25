# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
基于用户投资行为的用户关系模型和产品推荐模型
"""
import get_user_relation_invest_train


class UserRelationInvest:
    def __init__(self):
        self.get_train_set = get_user_relation_invest_train.GetRelationInvestTrain()
        self.is_success = []

    def implement_process(self):
        """ 得到训练集 """
        self.get_train_set.get_train_set(self.is_success)


if __name__ == '__main__':
    test = UserRelationInvest()
    test.implement_process()