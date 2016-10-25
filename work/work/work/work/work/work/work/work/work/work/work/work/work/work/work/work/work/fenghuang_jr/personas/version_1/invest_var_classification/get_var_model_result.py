# __author__ = 'lty'
# -*- coding: utf-8 -*-


import work.fenghuang_jr.personas.version_1.base_method.hive_command_method as hive_command_method
import work.fenghuang_jr.personas.version_1.base_method.get_train_set as get_train_set


class GetVarModelResult:
    def __init__(self):
        self.user_invest_var_train_sql_path = "../query_sql/uer_invest_var_train.sql"
        self.user_invest_var_hive_path = "/data/ml/tongyang/test/data"
        self.user_invest_var_train_path = "/data/ml/tongyang/test/train_set/user_invest_var_train"

    def get_train_set(self):
        try:
            os_v = hive_command_method.hive_command('-f', self.user_invest_var_train_sql_path)
            get_train_set.GetTrainSet().get_train_set(self.user_invest_var_hive_path, self.user_invest_var_train_path)

        except Exception, e:
            print Exception, e

if __name__ == '__main__':
    test = GetVarModelResult()
    test.get_train_set()