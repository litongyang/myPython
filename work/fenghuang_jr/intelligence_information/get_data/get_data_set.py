# __author__ = 'lty'
# -*- coding: utf-8 -*-

import sys
sys.path.append("/root/intelligence_info/")
import logging
import logging.config
import intelligence_information.base_method.hive_command_method as hive_command_method
import intelligence_information.base_method.read_conf as read_conf
import intelligence_information.base_method.get_loading_data as get_loading_data


class GetDataSet:
    def __init__(self):
        self.load_finance_prices_sql_path = read_conf.ReadConf().get_options('finance_sql_path', 'load_finance_prices_sql_path')
        self.load_company_code_sql_path = read_conf.ReadConf().get_options('finance_sql_path', 'load_company_code_sql_path')

    def load_data(self, is_success):
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('intelligence_info.load_data')
        param = '-f'
        try:
            os_v_1 = hive_command_method.hive_command(param, self.load_finance_prices_sql_path)
            os_v_2 = hive_command_method.hive_command(param, self.load_finance_prices_sql_path)
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
    def get_data_set(predict_file_path, predict_set_path, is_success):
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('intelligence_info.get_data_set')
        param = '-f'
        try:
            get_loading_data.GetLoadingData().get_loading_data(predict_file_path, predict_set_path)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_predict_set is Exception !"
            logger.error(error_info)
            is_success.append(0)


if __name__ == '__main__':
    test = GetDataSet()
    # test.get_predict_set('', '')
