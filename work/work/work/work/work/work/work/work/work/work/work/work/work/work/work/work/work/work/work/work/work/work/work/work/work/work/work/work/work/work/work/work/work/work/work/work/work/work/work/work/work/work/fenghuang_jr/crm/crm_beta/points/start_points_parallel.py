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


class StartPointsParallel:
    def __init__(self):
        self.logger = logging.getLogger('../start.start_coupon_parallel')
        self.crm_points_statistics_sql_path = "../query_sql/points/crm_points_statistics.sql"
        self.crm_end_points_statistics_sql_path = "../query_sql/points/crm_end_points_statistics.sql"
        self.crm_error_sql_path = "../query_sql/crm_error.sql"
        self.invoke_schedule = invoke_schedule.InvokeSchedule()

    def get_points_statistics_mid_data(self, is_success):
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(3, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            os_v = hive_command_method.hive_command("-f", self.crm_points_statistics_sql_path)
            push_schedule_result_method.push_schedule_result(os_v, 3, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

    def get_points_statistics_data(self, is_success):
        logger = logging.getLogger('crm.start_points.get_points_statistics_data')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(3, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            os_v = hive_command_method.hive_command("-f", self.crm_end_points_statistics_sql_path)
            push_schedule_result_method.push_schedule_result(os_v, 3, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

    def implement_es_points(self, is_success):
        logger = logging.getLogger('crm.start_points.implement_es_points')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(4, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            points_statistics_path = read_conf.ReadConf().get_options("path", "crm_points_statistic_data_path")
            os_v, rank_cnt = start_es.implement_es(points_statistics_path, "points")
            push_schedule_result_method.push_schedule_result_es(os_v, 4, is_success, (str(fun_name) + "-points"), rank_cnt)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 4, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)


if __name__ == '__main__':
    test = StartPointsParallel()
