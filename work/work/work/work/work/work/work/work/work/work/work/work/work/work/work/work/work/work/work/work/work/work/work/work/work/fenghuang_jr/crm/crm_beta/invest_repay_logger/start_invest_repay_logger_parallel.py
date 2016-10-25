# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import sys
import work.fenghuang_jr.crm.crm_beta.input_data_toHive.start_data_input as start_data_input
import work.fenghuang_jr.crm.crm_beta.base_method.hive_command_method as hive_command_method
import work.fenghuang_jr.crm.crm_beta.base_method.start_es as start_es
import work.fenghuang_jr.crm.crm_beta.base_method.read_conf as read_conf
import work.fenghuang_jr.crm.crm_beta.schedule.invoke_schedule as invoke_schedule
import work.fenghuang_jr.crm.crm_beta.base_method.push_schedule_result_method as push_schedule_result_method


class StartInvestRepayLoggerParallel:
    def __init__(self):
        self.crm_end_invest_repay_sql_path = "../query_sql/invest_repay/crm_end_invest_repay.sql"
        self.crm_error_sql_path = "../query_sql/crm_error.sql"
        self.start_data_input = start_data_input.StartDataInput()
        self.invoke_schedule = invoke_schedule.InvokeSchedule()

    def crm_end_invest_repay_logger(self, is_success):
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(3, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            os_v = hive_command_method.hive_command("-f", self.crm_end_invest_repay_sql_path)
            push_schedule_result_method.push_schedule_result(os_v, 3, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

    # 执行es
    def implement_es_invest_repay_logger(self, is_success):
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(4, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            invest_repay_logger_path = read_conf.ReadConf().get_options("path", "crm_invest_repay_logger_path")
            os_v1, rank_cnt = start_es.implement_es(invest_repay_logger_path, "invest_repay_logger")
            push_schedule_result_method.push_schedule_result_es(os_v1, 4, is_success, (str(fun_name) + "-invest_repay_logger"), rank_cnt)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 4, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

if __name__ == '__main__':
    test = StartInvestRepayLoggerParallel()
