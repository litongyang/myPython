# __author__ = 'lty'
# -*- coding: utf-8 -*-

"""
得到年龄划分的训练集
feature: user_id, age
"""

import personas.version_1.base_method.hive_command_method as hive_command_method
import personas.version_1.base_method.get_train_set as get_train_set
import personas.version_1.base_method.read_conf as read_conf


class GetAgeTransSet:
    def __init__(self):
        self.user_age_train_sql_path = read_conf.ReadConf().get_options("path_user_age",
                                                                               "user_age_train_sql_path")
        self.user_age_hive_path = read_conf.ReadConf().get_options("path_user_age",
                                                                          "user_age_hive_path")
        self.user_age_train_path = read_conf.ReadConf().get_options("path_user_age",
                                                                           "user_age_train_path")

    def get_train_set(self, is_success):
        try:
            os_v = hive_command_method.hive_command('-f', self.user_age_train_sql_path)
            get_train_set.GetTrainSet().get_train_set(self.user_age_hive_path, self.user_age_train_path)
            if os_v == 0:
                is_success.append(1)
            else:
                is_success.append(0)
        except Exception, e:
            print Exception, e
            is_success.append(0)


if __name__ == '__main__':
    test = GetAgeTransSet()
