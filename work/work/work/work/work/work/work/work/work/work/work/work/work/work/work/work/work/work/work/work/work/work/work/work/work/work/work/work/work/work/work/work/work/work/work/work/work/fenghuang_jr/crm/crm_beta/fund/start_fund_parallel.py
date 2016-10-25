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


class StartFundParallel:
    def __init__(self):
        self.logger = logging.getLogger('../start.start_coupon_parallel')
        self.crm_fund_statistics_sql_path = "../query_sql/fund/crm_fund_statistics.sql"
        self.crm_fund_logger_sql_path = "../query_sql/fund/crm_fund_logger.sql"
        self.crm_end_fund_statistics_sql_path = "../query_sql/fund/crm_end_fund_statistics.sql"
        self.crm_end_fund_logger_sql_path = "../query_sql/fund/crm_end_fund_logger.sql"
        self.crm_error_sql_path = "../query_sql/crm_error.sql"
        self.invoke_schedule = invoke_schedule.InvokeSchedule()

    def get_crm_fund_statistics(self, is_success):
        logger = logging.getLogger('crm.start_fund.get_crm_fund_statistics')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(3, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            os_v = hive_command_method.hive_command("-f", self.crm_fund_statistics_sql_path)
            push_schedule_result_method.push_schedule_result(os_v, 3, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

    def get_crm_fund_logger(self, is_success):
        logger = logging.getLogger('crm.start_fund.get_crm_fund_logger')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(3, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            os_v = hive_command_method.hive_command("-f", self.crm_fund_logger_sql_path)
            push_schedule_result_method.push_schedule_result(os_v, 3, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

    def get_fund_statistics_data(self, is_success):
        logger = logging.getLogger('crm.start_fund.get_fund_statistics_data')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(3, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            os_v = hive_command_method.hive_command("-f", self.crm_end_fund_statistics_sql_path)
            push_schedule_result_method.push_schedule_result(os_v, 3, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

    def get_fund_logger_data(self, is_success):
        logger = logging.getLogger('crm.start_fund.get_fund_logger_data')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(3, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            os_v = hive_command_method.hive_command("-f", self.crm_end_fund_logger_sql_path)
            if os_v == 0:
                logger.info("run function of get_fund_logger_data is successed !")
                self.invoke_schedule.invoke_update_fun(3, 0, "run function of get_fund_logger_data is successed !", -1)
                is_success.append(1)
            else:
                logger.error("run function of get_fund_logger_data failed !")
                self.invoke_schedule.invoke_update_fun(3, 1, "run function of get_fund_logger_data is failed !", -1)
                is_success.append(0)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

    def implement_es_fund(self, is_success):
        logger = logging.getLogger('crm.start_coupon.implement_es_fund')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(4, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            fund_statistics_path = read_conf.ReadConf().get_options("path", "crm_fund_statistic_data_path")
            fund_logger_path = read_conf.ReadConf().get_options("path", "crm_fund_logger_data_path")
            os_v, rank_cnt = start_es.implement_es(fund_statistics_path, "fund_account")
            push_schedule_result_method.push_schedule_result_es(os_v, 4, is_success, (str(fun_name) + "-fund_account"), rank_cnt)
            os_v1, rank_cnt = start_es.implement_es(fund_logger_path, "fund_account.logger")
            push_schedule_result_method.push_schedule_result_es(os_v1, 4, is_success, (str(fun_name) + "-fund_account.logger"), rank_cnt)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)


if __name__ == '__main__':
    test = StartFundParallel()
