# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
得到历史投资标的利率的list
"""

import sys
sys.path.append("/data/ml/tongyang/test/")

import personas.version_1.base_method.hive_command_method as hive_command_method
import personas.version_1.base_method.get_train_set as get_train_set
import personas.version_1.base_method.read_conf as read_conf


class GetInvestRateTrainSet:
    def __init__(self):
        self.next_invest_ratio_train_sql_path = read_conf.ReadConf().get_options("path_next_invest_bid",
                                                                               "next_invest_ratio_train_sql_path")
        self.next_invest_ratio_hive_path = read_conf.ReadConf().get_options("path_next_invest_bid",
                                                                          "next_invest_ratio_hive_path")
        self.next_invest_ratio_train_path = read_conf.ReadConf().get_options("path_next_invest_bid",
                                                                           "next_invest_ratio_train_path")

    def get_train_set(self, is_success):
        try:
            os_v = hive_command_method.hive_command('-f', self.next_invest_ratio_train_sql_path)
            get_train_set.GetTrainSet().get_train_set(self.next_invest_ratio_hive_path, self.next_invest_ratio_train_path)
            if os_v == 0:
                is_success.append(1)
            else:
                is_success.append(0)
        except Exception, e:
            print Exception, e
            is_success.append(0)


if __name__ == '__main__':
    test = GetInvestRateTrainSet()
