# __author__ = 'lty'
# -*- coding: utf-8 -*-
import work.fenghuang_jr.user_value_predict_project.base_method.get_loading_data as get_loading_data
import work.fenghuang_jr.user_value_predict_project.base_method.hive_command_method as hive_command_method
import work.fenghuang_jr.user_value_predict_project.base_method.read_conf as read_conf
import sys
sys.path.append("/root/user_value_predict")
import logging
import logging.config
# import user_value_predict_project.base_method.get_train_set as get_train_set
# import user_value_predict_project.base_method.hive_command_method as hive_command_method
# import user_value_predict_project.base_method.read_conf as read_conf


class GetTrainSet:
    def __init__(self):
        self.first_invest_predict_label_sql_path = read_conf.ReadConf().get_options('first_invest_training', 'first_invest_predict_label_sql_path')
        self.user_predict_base_feature_sql_path = read_conf.ReadConf().get_options('first_invest_training', 'user_predict_base_feature_sql_path')
        self.first_invest_account_feature_sql_path = read_conf.ReadConf().get_options('first_invest_training', 'first_invest_account_feature_sql_path')
        self.first_invest_train_set_from_30_sql_path = read_conf.ReadConf().get_options('first_invest_training', 'first_invest_train_set_from_30_sql_path')
        self.first_invest_load_train_set_from_30_sql_path = read_conf.ReadConf().get_options('first_invest_training', 'first_invest_load_train_set_from_30_sql_path')

    def get_train_set(self, file_path, trans_path):
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('user_predict.get_train_set')
        param = '-f'
        os_v_1 = hive_command_method.hive_command(param, self.first_invest_predict_label_sql_path)
        os_v_2 = hive_command_method.hive_command(param, self.user_predict_base_feature_sql_path)
        os_v_3 = hive_command_method.hive_command(param, self.first_invest_account_feature_sql_path)
        os_v_4 = hive_command_method.hive_command(param, self.first_invest_train_set_from_30_sql_path)
        os_v_5 = hive_command_method.hive_command(param, self.first_invest_load_train_set_from_30_sql_path)
        # get_loading_data.GetLoadingData().get_loading_data(file_path, trans_path)


if __name__ == '__main__':
    test = GetTrainSet()
    test.get_train_set('', '')
