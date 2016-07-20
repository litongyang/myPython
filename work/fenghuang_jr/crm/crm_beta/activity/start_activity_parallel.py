# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import sys
import logging
import logging.config
import work.fenghuang_jr.crm.crm_beta.base_method.hive_command_method as hive_command_method
import work.fenghuang_jr.crm.crm_beta.base_method.start_es as start_es
import work.fenghuang_jr.crm.crm_beta.base_method.read_conf as read_conf
import work.fenghuang_jr.crm.crm_beta.schedule.invoke_schedule as invoke_schedule
import work.fenghuang_jr.crm.crm_beta.base_method.push_schedule_result_method as push_schedule_result_method

logger = logging.getLogger('start.start_activity_parallel')


class StartActivityParallel:
    def __init__(self):
        self.crm_end_activity_statistics_sql_path = "../query_sql/activity/crm_end_activity_statistics.sql"
        self.crm_end_activity_logger_sql_path = "../query_sql/activity/crm_end_activity_logger.sql"
        self.crm_error_sql_path = "../query_sql/crm_error.sql"
        self.invoke_schedule = invoke_schedule.InvokeSchedule()

    def get_activity_statistics_data(self, is_success):
        logger = logging.getLogger('crm.start_coupon.get_coupon_statistics_data')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(3, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            os_v = hive_command_method.hive_command("-f", self.crm_end_activity_statistics_sql_path)
            push_schedule_result_method.push_schedule_result(os_v, 3, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

    def get_activity_logger_data(self, is_success):
        logger = logging.getLogger('crm.start_coupon.get_coupon_logger_data')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(3, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            os_v = hive_command_method.hive_command("-f", self.crm_end_activity_logger_sql_path)
            push_schedule_result_method.push_schedule_result(os_v, 3, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

    def implement_es_activity(self, is_success):
        # logger = logging.getLogger('crm.start_coupon.implement_es_coupon')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(4, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            activity_statistics_path = read_conf.ReadConf().get_options("path", "crm_activity_statistic_data_path")
            activity_logger_path = read_conf.ReadConf().get_options("path", "crm_activity_logger_data_path")
            os_v, rank_cnt = start_es.implement_es(activity_statistics_path, "activity")
            push_schedule_result_method.push_schedule_result_es(os_v, 4, is_success, (str(fun_name) + "-activity"), rank_cnt)
            os_v1, rank_cnt = start_es.implement_es(activity_logger_path, "activity.logger")
            push_schedule_result_method.push_schedule_result_es(os_v1, 4, is_success, (str(fun_name) + "-activity.logger"), rank_cnt)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 4, is_success, fun_name)

if __name__ == '__main__':
    test = StartActivityParallel()
