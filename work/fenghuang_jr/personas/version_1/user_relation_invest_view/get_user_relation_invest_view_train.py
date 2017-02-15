# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
得到训练集: 通过用户投资行为
feature:
"""
import sys
sys.path.append("/root/personas_fengjr/")
import datetime
import logging
import logging.config
import personas.version_1.base_method.hive_command_method as hive_command_method
import personas.version_1.base_method.get_train_set as get_train_set
import personas.version_1.base_method.read_conf as read_conf


class GetRelationInvestViewTrain:
    def __init__(self):
        self.before = datetime.date.today() - datetime.timedelta(days=90)  # 90天前
        self.yesterday = datetime.date.today() - datetime.timedelta(days=1)
        self.user_relation_invest_view_train_sql_path = read_conf.ReadConf().get_options("path_user_relation_invest_view",
                                                                                    "user_relation_invest_view_train_sql_path")
        self.user_relation_invest_view_hive_path = read_conf.ReadConf().get_options("path_user_relation_invest_view",
                                                                               "user_relation_invest_view_hive_path")
        self.user_relation_invest_view_train_path = read_conf.ReadConf().get_options("path_user_relation_invest_view",
                                                                                "user_relation_invest_view_train_path")

    def get_train_set(self, is_success):
        logger = logging.getLogger('personas.get_train_set')
        try:
            param = '-d' + ' ' + 'before=' + '\'' + str(self.before) + '\'' + ' ' + '-d' + ' ' + 'dt=' + '\'' + str(self.yesterday) + '\'' + ' ' + '-f'
            os_v = hive_command_method.hive_command(str(param), self.user_relation_invest_view_train_sql_path)
            get_train_set.GetTrainSet().get_train_set(self.user_relation_invest_view_hive_path, self.user_relation_invest_view_train_path)
            if os_v == 0:
                is_success.append(1)
                logger.info("get_train_set is successed !")
            else:
                is_success.append(0)
                logger.error("get_train_set is failed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_train_set is Exception !"
            logger.error(error_info)
            is_success.append(0)


if __name__ == '__main__':
    test = GetRelationInvestViewTrain()
