# __author__ = 'lty'
# -*- coding: utf-8 -*-
import sys
sys.path.append("/root/personas_fengjr/")
import datetime
import logging
import logging.config
import personas.version_1.base_method.hive_command_method as hive_command_method
import personas.version_1.base_method.read_conf as read_conf


class SaveNextInvetBidResultData:
    def __init__(self):
        self.yesterday = datetime.date.today() - datetime.timedelta(days=1)
        self.input_next_invest_rate_bid_result_sql_path = read_conf.ReadConf().get_options("path_next_invest_bid", "next_invest_ratio_result_sql_path")
        self.input_next_invest_dealine_bid_result_sql_path = read_conf.ReadConf().get_options("path_next_invest_bid", "next_invest_deadline_result_sql_path")

    def get_result_data(self, is_success):
        logger = logging.getLogger('personas.get_result_data')
        try:
            param = '-d' + ' ' + 'dt=' + '\'' + str(self.yesterday) + '\'' + ' ' + '-f'
            os_v = hive_command_method.hive_command(str(param), self.input_next_invest_rate_bid_result_sql_path)
            os_v_1 = hive_command_method.hive_command(str(param), self.input_next_invest_dealine_bid_result_sql_path)
            if os_v == 0 and os_v_1 == 0:
                is_success.append(1)
                logger.info("get_result_data is successed !")
            else:
                is_success.append(0)
                logger.error("get_result_data is failed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_result_data is Exception !"
            logger.error(error_info)
            is_success.append(0)

if __name__ == '__main__':
    test = SaveNextInvetBidResultData()
    # test.get_result_data()
