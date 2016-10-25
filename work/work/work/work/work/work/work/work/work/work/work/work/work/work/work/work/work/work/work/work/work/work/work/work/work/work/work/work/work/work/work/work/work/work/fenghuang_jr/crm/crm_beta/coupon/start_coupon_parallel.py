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


class StartCouponParallel:
    def __init__(self):
        self.crm_coupon_json_new_sql_path = "../query_sql/coupon/crm_coupon_json_new.sql"
        self.crm_end_coupon_statistics_sql_path = "../query_sql/coupon/crm_end_coupon_statistics.sql"
        self.crm_end_coupon_logger_sql_path = "../query_sql/coupon/crm_end_coupon_logger.sql"
        self.crm_error_sql_path = "../query_sql/crm_error.sql"
        self.invoke_schedule = invoke_schedule.InvokeSchedule()

    def get_crm_coupon_json_new(self, is_success):
        logger = logging.getLogger('crm.start_coupon.get_crm_coupon_josn_new')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(3, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            os_v = hive_command_method.hive_command("-f", self.crm_coupon_json_new_sql_path)
            push_schedule_result_method.push_schedule_result(os_v, 3, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

    def get_coupon_statistics_data(self, is_success):
        logger = logging.getLogger('crm.start_coupon.get_coupon_statistics_data')
        # self.invoke_schedule.invoke_level_fun(3, "get_coupon_statistics_data", " get_crm_coupon_josn_new is starting !")
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(3, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            os_v = hive_command_method.hive_command("-f", self.crm_end_coupon_statistics_sql_path)
            push_schedule_result_method.push_schedule_result(os_v, 3, is_success, fun_name)
            # if os_v == 0:
            #     logger.info("run function of get_coupon_statistics_data is successed !")
            #     self.invoke_schedule.invoke_update_fun(3, 0, "run function of get_coupon_statistics_data is successed !", -1)
            #     is_success.append(1)
            # else:
            #     logger.error("run function of get_coupon_statistics_data failed !")
            #     self.invoke_schedule.invoke_update_fun(3, 1, "run function of get_coupon_statistics_data is failed !", -1)
            #     is_success.append(0)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)
            # exception = Exception, e
            # error_info = str(exception) + "--------->>" + "run  function of coupon_parallel failed !"
            # logger.error(error_info)
            # hive_command_method.hive_command("-f", self.crm_error_sql_path)
            # self.invoke_schedule.invoke_update_fun(3, 2, error_info, -1)
            # is_success.append(0)

    def get_coupon_logger_data(self, is_success):
        logger = logging.getLogger('crm.start_coupon.get_coupon_logger_data')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(3, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            os_v = hive_command_method.hive_command("-f", self.crm_end_coupon_logger_sql_path)
            push_schedule_result_method.push_schedule_result(os_v, 3, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 3, is_success, fun_name)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

    def implement_es_coupon(self, is_success):
        logger = logging.getLogger('crm.start_coupon.implement_es_coupon')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(4, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            coupon_statistics_path = read_conf.ReadConf().get_options("path", "crm_coupon_statistic_data_path")
            coupon_logger_path = read_conf.ReadConf().get_options("path", "crm_coupon_logger_data_path")
            os_v, rank_cnt = start_es.implement_es(coupon_statistics_path, "coupon")
            push_schedule_result_method.push_schedule_result_es(os_v, 4, is_success, (str(fun_name) + "-coupon"), rank_cnt)
            os_v1, rank_cnt = start_es.implement_es(coupon_logger_path, "coupon.logger")
            push_schedule_result_method.push_schedule_result_es(os_v1, 4, is_success, (str(fun_name) + "-coupon.logger"), rank_cnt)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 4, is_success, fun_name)


if __name__ == '__main__':
    test = StartCouponParallel()
