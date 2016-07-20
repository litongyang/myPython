# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import sys
import logging
import logging.config
import work.fenghuang_jr.crm.crm_beta.base_method.application_method as application_method
import work.fenghuang_jr.crm.crm_beta.base_method.sqoop_function as sqoop_function
import work.fenghuang_jr.crm.crm_beta.base_method.read_conf as read_conf
import work.fenghuang_jr.crm.crm_beta.schedule.invoke_schedule as invoke_schedule
import work.fenghuang_jr.crm.crm_beta.base_method.push_schedule_result_method as push_schedule_result_method
logging.config.fileConfig('logger.conf')


class StartDataInput:
    def __init__(self):
        self.logger = logging.getLogger('start.start_data_input')
        self.tb_coupon_record_sql = application_method.read_file_content("../query_sql/coupon/tb_coupon_record.sql")
        self.crm_points_statistics_sql = application_method.read_file_content("../query_sql/points/crm_points_statistics.sql")
        self.invest_desc_trans_sql = application_method.read_file_content("../query_sql/invest/invest_desc_trans.sql")
        self.invest_trans_sql = application_method.read_file_content("../query_sql/invest/invest_trans.sql")
        self.invest_one_trans_sql = application_method.read_file_content("../query_sql/invest/invest_one_trans.sql")
        self.crm_activity_contact_awards_sql = application_method.read_file_content("../query_sql/activity/crm_activity_contact_awards.sql")
        self.invest_repay_logger_sql = application_method.read_file_content("../query_sql/invest_repay/invest_repay_logger.sql")
        self.sqoop_function = sqoop_function.SqoopFunction()
        self.read_conf = read_conf.ReadConf()
        self.invoke_schedule = invoke_schedule.InvokeSchedule()

    def input_tb_coupon_record_fun(self, is_success):
        logger = logging.getLogger('crm.input_data_hive.input_tb_counpon_record_fun')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(2, str(fun_name), (str(fun_name) + " is starting !"))
        # self.invoke_schedule.invoke_level_fun(2, "input_tb_counpon_record_fun", "input_tb_counpon_record_fun is starting !")
        try:
            host = self.read_conf.get_options("sqoop_params_tb_counpon_record", "host")
            username = self.read_conf.get_options("sqoop_params_tb_counpon_record", "username")
            password = self.read_conf.get_options("sqoop_params_tb_counpon_record", "password")
            table_name = self.read_conf.get_options("sqoop_params_tb_counpon_record", "table_name")
            target_dir = self.read_conf.get_options("sqoop_params_tb_counpon_record", "target_dir")
            hive_table = self.read_conf.get_options("sqoop_params_tb_counpon_record", "hive_table")
            os_v = self.sqoop_function.sqoop_all(host, username, password, self.tb_coupon_record_sql, table_name, target_dir, hive_table)
            push_schedule_result_method.push_schedule_result(os_v, 2, is_success, fun_name)
            # if os_v == 0:
            #     logger.info("run function of input_tb_counpon_record_fun is successed !")
            #     self.invoke_schedule.invoke_update_fun(2, 0, "input_tb_coupon_record_fun is successed !", -1)
            #     is_success.append(1)
            # else:
            #     logger.error("run function of input_tb_counpon_record_fun is failed !")
            #     self.invoke_schedule.invoke_update_fun(2, 1, "input_tb_coupon_record_fun is failed !", -1)
            #     is_success.append(0)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 2, is_success, fun_name)
            # exception = Exception, e
            # error_info = str(exception) + "--------->>" + "run  function of input_tb_counpon_record_fun Exception !"
            # self.logger.error(error_info)
            # self.invoke_schedule.invoke_update_fun(2, 2, error_info, -1)
            # is_success.append(0)

    def input_tb_invite_reward_trace_fun(self, is_success):
        logger = logging.getLogger('crm.input_data_hive.input_tb_invite_reward_trace_fun')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(2, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            host = self.read_conf.get_options("sqoop_params_tb_invite_reward_trace", "host")
            username = self.read_conf.get_options("sqoop_params_tb_invite_reward_trace", "username")
            password = self.read_conf.get_options("sqoop_params_tb_invite_reward_trace", "password")
            table = self.read_conf.get_options("sqoop_params_tb_invite_reward_trace", "table")
            table_name = self.read_conf.get_options("sqoop_params_tb_invite_reward_trace", "table_name")
            target_dir = self.read_conf.get_options("sqoop_params_tb_invite_reward_trace", "target_dir")
            hive_table = self.read_conf.get_options("sqoop_params_tb_invite_reward_trace", "hive_table")
            os_v = self.sqoop_function.sqoop_table(host, username, password, table, table_name, target_dir, hive_table)
            push_schedule_result_method.push_schedule_result(os_v, 2, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 2, is_success, fun_name)

    def input_tb_invest_fun(self, is_success):
        logger = logging.getLogger('crm.input_data_hive.input_tb_invest_fun')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(2, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            host = self.read_conf.get_options("sqoop_params_tb_invest", "host")
            username = self.read_conf.get_options("sqoop_params_tb_invest", "username")
            password = self.read_conf.get_options("sqoop_params_tb_invest", "password")
            table = self.read_conf.get_options("sqoop_params_tb_invest", "table")
            table_name = self.read_conf.get_options("sqoop_params_tb_invest", "table_name")
            target_dir = self.read_conf.get_options("sqoop_params_tb_invest", "target_dir")
            hive_table = self.read_conf.get_options("sqoop_params_tb_invest", "hive_table")
            os_v = self.sqoop_function.sqoop_table(host, username, password, table, table_name, target_dir, hive_table)
            push_schedule_result_method.push_schedule_result(os_v, 2, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 2, is_success, fun_name)

    def input_tb_user_fund_fun(self, is_success):
        logger = logging.getLogger('crm.input_data_hive.input_tb_user_fund_fun')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(2, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            host = self.read_conf.get_options("sqoop_params_tb_user_fund", "host")
            username = self.read_conf.get_options("sqoop_params_tb_user_fund", "username")
            password = self.read_conf.get_options("sqoop_params_tb_user_fund", "password")
            table = self.read_conf.get_options("sqoop_params_tb_user_fund", "table")
            table_name = self.read_conf.get_options("sqoop_params_tb_user_fund", "table_name")
            target_dir = self.read_conf.get_options("sqoop_params_tb_user_fund", "target_dir")
            hive_table = self.read_conf.get_options("sqoop_params_tb_user_fund", "hive_table")
            os_v = self.sqoop_function.sqoop_table(host, username, password, table, table_name, target_dir, hive_table)
            push_schedule_result_method.push_schedule_result(os_v, 2, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 2, is_success, fun_name)

    def input_tb_fund_record_fun(self, is_success):
        logger = logging.getLogger('crm.input_data_hive.input_tb_fund_record_fun')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(2, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            host = self.read_conf.get_options("sqoop_params_tb_fund_record", "host")
            username = self.read_conf.get_options("sqoop_params_tb_fund_record", "username")
            password = self.read_conf.get_options("sqoop_params_tb_fund_record", "password")
            table = self.read_conf.get_options("sqoop_params_tb_fund_record", "table")
            table_name = self.read_conf.get_options("sqoop_params_tb_fund_record", "table_name")
            target_dir = self.read_conf.get_options("sqoop_params_tb_fund_record", "target_dir")
            hive_table = self.read_conf.get_options("sqoop_params_tb_fund_record", "hive_table")
            os_v = self.sqoop_function.sqoop_table(host, username, password, table, table_name, target_dir, hive_table)
            push_schedule_result_method.push_schedule_result(os_v, 2, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 2, is_success, fun_name)

    def input_tb_invest_repayment_fun(self, is_success):
        logger = logging.getLogger('crm.input_data_hive.input_tb_invest_repayment_fun')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(2, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            host = self.read_conf.get_options("sqoop_params_tb_invest_repayment", "host")
            username = self.read_conf.get_options("sqoop_params_tb_invest_repayment", "username")
            password = self.read_conf.get_options("sqoop_params_tb_invest_repayment", "password")
            table = self.read_conf.get_options("sqoop_params_tb_invest_repayment", "table")
            table_name = self.read_conf.get_options("sqoop_params_tb_invest_repayment", "table_name")
            target_dir = self.read_conf.get_options("sqoop_params_tb_invest_repayment", "target_dir")
            hive_table = self.read_conf.get_options("sqoop_params_tb_invest_repayment", "hive_table")
            os_v = self.sqoop_function.sqoop_table(host, username, password, table, table_name, target_dir, hive_table)
            push_schedule_result_method.push_schedule_result(os_v, 2, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 2, is_success, fun_name)

    def input_crm_points_statistics_fun(self, is_success):
        logger = logging.getLogger('input_data_hive.input_crm_points_statistics_fun')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(2, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            host = self.read_conf.get_options("sqoop_params_crm_points_statistics", "host")
            username = self.read_conf.get_options("sqoop_params_crm_points_statistics", "username")
            password = self.read_conf.get_options("sqoop_params_crm_points_statistics", "password")
            table_name = self.read_conf.get_options("sqoop_params_crm_points_statistics", "table_name")
            target_dir = self.read_conf.get_options("sqoop_params_crm_points_statistics", "target_dir")
            hive_table = self.read_conf.get_options("sqoop_params_crm_points_statistics", "hive_table")
            os_v = self.sqoop_function.sqoop_all(host, username, password, self.crm_points_statistics_sql, table_name, target_dir, hive_table)
            push_schedule_result_method.push_schedule_result(os_v, 2, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 2, is_success, fun_name)

    def input_invest_desc_trans(self, is_success):
        logger = logging.getLogger('crm.input_data_hive.get_invest_desc_trans')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(2, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            host = self.read_conf.get_options("sqoop_params_invest_desc_trans", "host")
            username = self.read_conf.get_options("sqoop_params_invest_desc_trans", "username")
            password = self.read_conf.get_options("sqoop_params_invest_desc_trans", "password")
            table_name = self.read_conf.get_options("sqoop_params_invest_desc_trans", "table_name")
            target_dir = self.read_conf.get_options("sqoop_params_invest_desc_trans", "target_dir")
            hive_table = self.read_conf.get_options("sqoop_params_invest_desc_trans", "hive_table")
            os_v = self.sqoop_function.sqoop_all(host, username, password, self.invest_desc_trans_sql, table_name, target_dir, hive_table)
            push_schedule_result_method.push_schedule_result(os_v, 2, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 2, is_success, fun_name)

    def input_invest_trans(self, is_success):
        logger = logging.getLogger('crm.input_data_hive.get_invest_trans')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(2, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            host = self.read_conf.get_options("sqoop_params_invest_trans", "host")
            username = self.read_conf.get_options("sqoop_params_invest_trans", "username")
            password = self.read_conf.get_options("sqoop_params_invest_trans", "password")
            table_name = self.read_conf.get_options("sqoop_params_invest_trans", "table_name")
            target_dir = self.read_conf.get_options("sqoop_params_invest_trans", "target_dir")
            hive_table = self.read_conf.get_options("sqoop_params_invest_trans", "hive_table")
            os_v = self.sqoop_function.sqoop_all(host, username, password, self.invest_trans_sql, table_name, target_dir, hive_table)
            push_schedule_result_method.push_schedule_result(os_v, 2, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 2, is_success, fun_name)

    def input_invest_one_trans(self, is_success):
        logger = logging.getLogger('crm.input_data_hive.get_invest_trans')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(2, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            host = self.read_conf.get_options("sqoop_params_invest_one_trans", "host")
            username = self.read_conf.get_options("sqoop_params_invest_one_trans", "username")
            password = self.read_conf.get_options("sqoop_params_invest_one_trans", "password")
            table_name = self.read_conf.get_options("sqoop_params_invest_one_trans", "table_name")
            target_dir = self.read_conf.get_options("sqoop_params_invest_one_trans", "target_dir")
            hive_table = self.read_conf.get_options("sqoop_params_invest_one_trans", "hive_table")
            os_v = self.sqoop_function.sqoop_all(host, username, password, self.invest_one_trans_sql, table_name, target_dir, hive_table)
            push_schedule_result_method.push_schedule_result(os_v, 2, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 2, is_success, fun_name)

    def input_activity_contact_awards(self, is_success):
        # logger = logging.getLogger('crm.input_data_hive.input_activity_contact_awards')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(2, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            host = self.read_conf.get_options("sqoop_params_activity_contact_awards", "host")
            username = self.read_conf.get_options("sqoop_params_activity_contact_awards", "username")
            password = self.read_conf.get_options("sqoop_params_activity_contact_awards", "password")
            table_name = self.read_conf.get_options("sqoop_params_activity_contact_awards", "table_name")
            target_dir = self.read_conf.get_options("sqoop_params_activity_contact_awards", "target_dir")
            hive_table = self.read_conf.get_options("sqoop_params_activity_contact_awards", "hive_table")
            os_v = self.sqoop_function.sqoop_all(host, username, password, self.crm_activity_contact_awards_sql, table_name, target_dir, hive_table)
            push_schedule_result_method.push_schedule_result(os_v, 2, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 2, is_success, fun_name)

    def input_crm_contacts_cstm(self, is_success):
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(2, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            host = self.read_conf.get_options("sqoop_params_crm_contacts_cstm", "host")
            username = self.read_conf.get_options("sqoop_params_crm_contacts_cstm", "username")
            password = self.read_conf.get_options("sqoop_params_crm_contacts_cstm", "password")
            table = self.read_conf.get_options("sqoop_params_crm_contacts_cstm", "table")
            table_name = self.read_conf.get_options("sqoop_params_crm_contacts_cstm", "table_name")
            target_dir = self.read_conf.get_options("sqoop_params_crm_contacts_cstm", "target_dir")
            hive_table = self.read_conf.get_options("sqoop_params_crm_contacts_cstm", "hive_table")
            os_v = self.sqoop_function.sqoop_table(host, username, password, table, table_name, target_dir, hive_table)
            push_schedule_result_method.push_schedule_result(os_v, 2, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 2, is_success, fun_name)

    def input_crm_ptsts_points_transaction(self, is_success):
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(2, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            host = self.read_conf.get_options("sqoop_params_crm_ptsts_points_transaction", "host")
            username = self.read_conf.get_options("sqoop_params_crm_ptsts_points_transaction", "username")
            password = self.read_conf.get_options("sqoop_params_crm_ptsts_points_transaction", "password")
            table = self.read_conf.get_options("sqoop_params_crm_ptsts_points_transaction", "table")
            table_name = self.read_conf.get_options("sqoop_params_crm_ptsts_points_transaction", "table_name")
            target_dir = self.read_conf.get_options("sqoop_params_crm_ptsts_points_transaction", "target_dir")
            hive_table = self.read_conf.get_options("sqoop_params_crm_ptsts_points_transaction", "hive_table")
            os_v = self.sqoop_function.sqoop_table(host, username, password, table, table_name, target_dir, hive_table)
            push_schedule_result_method.push_schedule_result(os_v, 2, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 2, is_success, fun_name)

    def input_invest_repay_logger(self, is_success):
        # logger = logging.getLogger('crm.input_data_hive.input_activity_contact_awards')
        fun_name = (lambda: sys._getframe(1).f_code.co_name)()
        self.invoke_schedule.invoke_level_fun(2, str(fun_name), (str(fun_name) + " is starting !"))
        try:
            host = self.read_conf.get_options("sqoop_params_invest_repay_logger", "host")
            username = self.read_conf.get_options("sqoop_params_invest_repay_logger", "username")
            password = self.read_conf.get_options("sqoop_params_invest_repay_logger", "password")
            table_name = self.read_conf.get_options("sqoop_params_invest_repay_logger", "table_name")
            target_dir = self.read_conf.get_options("sqoop_params_invest_repay_logger", "target_dir")
            hive_table = self.read_conf.get_options("sqoop_params_invest_repay_logger", "hive_table")
            os_v = self.sqoop_function.sqoop_all(host, username, password, self.invest_repay_logger_sql, table_name, target_dir, hive_table)
            push_schedule_result_method.push_schedule_result(os_v, 2, is_success, fun_name)
        except Exception, e:
            push_schedule_result_method.push_schedule_exception((Exception, e), 2, is_success, fun_name)

if __name__ == '__main__':
    test = StartDataInput()
    # test.input_tb_counpon_record_fun()
