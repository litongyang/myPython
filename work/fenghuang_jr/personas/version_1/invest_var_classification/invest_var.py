# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
用户投资稳定性分类模型
"""
import save_invest_var_result_data
import invset_var_model_training
import get_invest_var_train_set


class InvestVar:
    def __init__(self):
        self.get_train_set = get_invest_var_train_set.GetInvestVarTrainSet()
        self.model_training = invset_var_model_training.InvestVarModelTraining()
        self.save_hive = save_invest_var_result_data.SaveInvestVarResultData()
        self.is_success = []  # 每一步运行成功或者失败的标记

    def implement_process(self):
        """ 得到训练集 """
        self.get_train_set.get_train_set(self.is_success)

        """ 模型训练 """
        self.model_training.get_train_data(self.is_success)
        self.model_training.kmeans_var(self.is_success)
        self.model_training.get_classification_result(self.is_success)
        self.model_training.get_result(self.is_success)

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
    test = InvestVar()
    test.implement_process()
