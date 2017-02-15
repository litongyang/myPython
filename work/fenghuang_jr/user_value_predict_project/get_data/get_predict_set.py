# __author__ = 'lty'
# -*- coding: utf-8 -*-
# import work.fenghuang_jr.user_value_predict_project.base_method.get_loading_data as get_loading_data
# import work.fenghuang_jr.user_value_predict_project.base_method.hive_command_method as hive_command_method
# import work.fenghuang_jr.user_value_predict_project.base_method.read_conf as read_conf
import sys
sys.path.append("/root/user_value_predict")
import logging
import logging.config
import user_value_predict_project.base_method.hive_command_method as hive_command_method
import user_value_predict_project.base_method.read_conf as read_conf
import user_value_predict_project.base_method.get_loading_data as get_loading_data


class GetPredictSet:
    def __init__(self):
        self.user_predict_base_feature_2017_sql_path = read_conf.ReadConf().get_options('first_invest_predict', 'user_predict_base_feature_2017_sql_path')
        self.first_invest_predict_set_from_1_sql_path = read_conf.ReadConf().get_options('first_invest_predict', 'first_invest_predict_from_1_sql_path')
        self.first_invest_load_predict_from_1_sql_path = read_conf.ReadConf().get_options('first_invest_predict', 'first_invest_load_predict_from_1_sql_path')
        self.first_invest_predict_set_from_30_sql_path = read_conf.ReadConf().get_options('first_invest_predict', 'first_invest_predict_from_30_sql_path')
        self.first_invest_load_predict_from_30_sql_path = read_conf.ReadConf().get_options('first_invest_predict', 'first_invest_load_predict_from_30_sql_path')
        self.first_invest_load_predict_from_60_sql_path = read_conf.ReadConf().get_options('first_invest_predict', 'first_invest_load_predict_from_60_sql_path')

    def load_data(self, is_success):
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('user_predict.load_data')
        param = '-f'
        try:
            # os_v_3 = hive_command_method.hive_command(param, self.user_predict_base_feature_2017_sql_path)
            # os_v_4 = hive_command_method.hive_command(param, self.first_invest_predict_set_from_1_sql_path)
            # os_v_5 = hive_command_method.hive_command(param, self.first_invest_predict_set_from_30_sql_path)
            os_v_1 = hive_command_method.hive_command(param, self.first_invest_load_predict_from_1_sql_path)
            os_v_2 = hive_command_method.hive_command(param, self.first_invest_load_predict_from_30_sql_path)
            os_v_3 = hive_command_method.hive_command(param, self.first_invest_load_predict_from_60_sql_path)
            if os_v_1 == 0 and os_v_2 == 0:
                is_success.append(1)
                logger.info("load_data is successed !")
            else:
                logger.error("load_data is failed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "load_data is Exception !"
            logger.error(error_info)
            is_success.append(0)

    @staticmethod
    def get_predict_set(predict_file_path, predict_set_path, is_success):
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('user_predict.get_predict_set')
        param = '-f'
        try:
            get_loading_data.GetLoadingData().get_loading_data(predict_file_path, predict_set_path)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_predict_set is Exception !"
            logger.error(error_info)
            is_success.append(0)


if __name__ == '__main__':
    test = GetPredictSet()
    # test.get_predict_set('', '')
