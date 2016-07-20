# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import sys
import logging
import logging.config
import work.fenghuang_jr.crm.crm_beta.input_data_toHive.start_data_input as start_data_input
import work.fenghuang_jr.crm.crm_beta.base_method.hive_command_method as hive_command_method
import work.fenghuang_jr.crm.crm_beta.base_method.start_es as start_es
import work.fenghuang_jr.crm.crm_beta.base_method.read_conf as read_conf
import work.fenghuang_jr.crm.crm_beta.schedule.invoke_schedule as invoke_schedule
import work.fenghuang_jr.crm.crm_beta.base_method.push_schedule_result_method as push_schedule_result_method


class StartInvestParallel:
    def __init__(self):
        self.invest_parallel_sql_path = "../query_sql/invest/invest_parallel.sql"
        self.crm_end_invest_sql_path = "../query_sql/invest/crm_end_invest.sql"
        self.crm_end_invest_logger_sql_path = "../query_sql/invest/crm_end_invest_logger.sql"
        self.crm_error_sql_path = "../query_sql/crm_error.sql"
        self.start_data_input = start_data_input.StartDataInput()
        # self.start_invest_parallel = start_invest_parallel.StartInvestParallel()
        self.invoke_schedule = invoke_schedule.InvokeSchedule()

    def get_crm_desc_json_new(self, is_success):
        logger = logging.getLogger('crm.start_invest.get_crm_desc_json_new')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(3, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            os_v = hive_command_method.hive_command("-f", self.invest_parallel_sql_path)
            push_schedule_result_method.push_schedule_result(os_v, 3, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

    # def get_invest_parallel_data(self, read_conf_class, sqoop_function_class):
    #     try:
    #         self.start_invest_parallel.get_invest_desc_trans(self.start_invest_parallel.invest_desc_trans_sql, read_conf_class, sqoop_function_class)
    #         self.start_invest_parallel.get_invest_trans(self.start_invest_parallel.invest_trans_sql, read_conf_class, sqoop_function_class)
    #         self.start_invest_parallel.get_crm_desc_json_new(self.start_invest_parallel.invest_parallel_sql_path)
    #         self.logger.info("run function of get_fund_parallel_data success !")
    #     except Exception, e:
    #         exception = Exception, e
    #         error_info = str(exception) + "--------->>" + "run  function of get_fund_parallel_data failed !"
    #         self.logger.error(error_info)

    # 调用合并及最后程序 内部生成文件不做内部处理
    def crm_end_invest(self, is_success):
        logger = logging.getLogger('crm.start_invest.crm_end_invest')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(3, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            os_v = hive_command_method.hive_command("-f", self.crm_end_invest_sql_path)
            push_schedule_result_method.push_schedule_result(os_v, 3, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

    def crm_end_invest_logger(self, is_success):
        logger = logging.getLogger('crm.start_invest.crm_end_invest_logger')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(3, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            os_v = hive_command_method.hive_command("-f", self.crm_end_invest_logger_sql_path)
            push_schedule_result_method.push_schedule_result(os_v, 3, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

    # 执行es
    def implement_es_invest(self, is_success):
        logger = logging.getLogger('crm.start_invest.implement_es_invest')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(4, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            invest_statistics_path = read_conf.ReadConf().get_options("path", "crm_invest_statistic_data_path")
            invest_logger_path = read_conf.ReadConf().get_options("path", "crm_invest_logger_data_path")
            os_v, rank_cnt = start_es.implement_es(invest_statistics_path, "fund")
            push_schedule_result_method.push_schedule_result_es(os_v, 4, is_success, (str(fun_name) + "-fund"), rank_cnt)
            os_v1, rank_cnt = start_es.implement_es(invest_logger_path, "fund.logger")
            push_schedule_result_method.push_schedule_result_es(os_v1, 4, is_success, (str(fun_name) + "-fund.logger"), rank_cnt)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 4, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

if __name__ == '__main__':
    test = StartInvestParallel()
