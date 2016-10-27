# __author__ = 'lty'
# -*- coding: utf-8 -*-

import sys
sys.path.append("/data/ml/tongyang/test")
import personas.version_1.base_method.hive_command_method as hive_command_method
import personas.version_1.base_method.read_conf as read_conf


class SaveUserAgeResultData:
    def __init__(self):
        self.input_invest_var_result_sql_path = read_conf.ReadConf().get_options("path_user_age", "input_user_age_result_sql_path")

    def get_result_data(self, is_success):
        try:
            os_v = hive_command_method.hive_command('-f', self.input_invest_var_result_sql_path)
            if os_v == 0:
                is_success.append(1)
            else:
                is_success.append(0)
        except Exception, e:
            print Exception, e
            is_success.append(0)

if __name__ == '__main__':
    test = SaveUserAgeResultData()
