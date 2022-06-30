# __author__ = 'lty'
# -*- coding: utf-8 -*-

import datetime
import logging
import logging.config
import hive_command_method


class SaveResultData:
    def __init__(self):
        self.yesterday = datetime.date.today() - datetime.timedelta(days=1)

    def get_result_data(self, input_result_sql_path, is_success):
        logger = logging.getLogger('intelligence_info.get_result_data')
        try:
            param = '-d' + ' ' + 'dt=' + '\'' + str(self.yesterday) + '\'' + ' ' + '-f'
            os_v = hive_command_method.hive_command(str(param), input_result_sql_path)
            if os_v == 0:
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
    test = SaveResultData()
