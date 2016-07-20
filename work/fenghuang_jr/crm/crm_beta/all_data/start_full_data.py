# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import logging
import logging.config
import work.fenghuang_jr.crm.crm_beta.input_data_toHive.start_data_input as start_data_input
import error_log
import work.fenghuang_jr.crm.crm_beta.fund.start_fund_parallel as start_fund_parallel
import work.fenghuang_jr.crm.crm_beta.coupon.start_coupon_parallel as start_coupon_parallel
import work.fenghuang_jr.crm.crm_beta.activity.start_activity_parallel as start_activity_parallel
import work.fenghuang_jr.crm.crm_beta.base_method.hive_command_method as hive_command_method
import start_es


class StartFullData:
    def __init__(self):
        self.logger = logging.getLogger('start.start_full_data')
        self.crm_end_sql_path = "../query_sql/crm_end.sql"
        self.crm_error_sql_path = "../query_sql/crm_error.sql"
        self.start_data_input = start_data_input.StartDataInput()
        self.error_log_class = error_log.ErrorLog()
        self.start_fund_parallel = start_fund_parallel.StartFundParallel()
        self.start_coupon_parallel = start_coupon_parallel.StartCouponParallel()
        self.start_activity_paarallel = start_activity_parallel.StartActivityParallel()
        self.start_es = start_es.StartEs()

    # 调用基础数据源
    # def get_base_data(self, file_dir_process_class, log_path):
    #     try:
    #         self.start_data_input.input_tb_counpon_record_fun(self.error_log_class, file_dir_process_class, log_path)
    #         self.start_data_input.input_tb_invite_reward_trace_fun(self.error_log_class, file_dir_process_class, log_path)
    #         self.start_data_input.input_tb_invest_fun(self.error_log_class, file_dir_process_class, log_path)
    #     except Exception, e:
    #         print Exception, e
        # self.start_data_input.input_tb_invest_fun(self.error_log_class)

    def get_fund_parallel_data(self, read_conf_class, sqoop_function_class, error_log_class, file_dir_process_class, log_path):
        try:
            self.start_fund_parallel.get_fund_desc_trans(self.start_fund_parallel.fund_desc_trans_sql, read_conf_class, sqoop_function_class, error_log_class, file_dir_process_class, log_path)
            self.start_fund_parallel.get_fund_trans(self.start_fund_parallel.fund_trans_sql, read_conf_class, sqoop_function_class, error_log_class, file_dir_process_class, log_path)
            self.start_fund_parallel.get_crm_desc_json_new(self.start_fund_parallel.fund_parallel_sql, error_log_class, file_dir_process_class, log_path)
            self.logger.info("run function of get_fund_parallel_data success !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "run  function of get_fund_parallel_data failed !"
            self.logger.error(error_info)

    def get_coupon_parallel_data(self, error_log_class, file_dir_process_class, log_path):
        try:
            self.start_coupon_parallel.coupon_parallel(error_log_class, file_dir_process_class, log_path)
            self.logger.info("run function of get_coupon_parallel_data success !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "run  function of get_coupon_parallel_data failed !"
            self.logger.error(error_info)

    def get_activity_parallel_data(self, start_activity_paarallel_sql, read_conf_class, sqoop_function_class, error_log_class, file_dir_process_class, log_path):
        try:
            self.start_activity_paarallel.get_crm_activity_contact_awards(start_activity_paarallel_sql, read_conf_class, sqoop_function_class, error_log_class, file_dir_process_class, log_path)
            self.logger.info("run function of get_activity_parallel_data success !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "run  function of get_activity_parallel_data failed !"
            self.logger.error(error_info)

    # 调用合并及最后程序 内部生成文件不做内部处理
    # @staticmethod
    def crm_end(self, error_log_class, file_dir_process_class, log_path):
        try:
            hive_command_method.hive_command("-f", self.crm_end_sql_path)
            file_dir_process_class.wirte_file(log_path, "data_json of file is successful saved !")
        except Exception, e:
            # error_info = Exception, ": ", e
            # error_log_class.write_log(error_info)
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "run  function of input_tb_invest_fun failed !"
            self.logger.error(error_info)
            hive_command_method.hive_command("-f", self.crm_error_sql_path)

    # 执行es
    def implement_es(self, error_log_class):
        try:
            self.start_es.implement_es("query_sql", error_log)
            self.logger.info("implement_es is successed!")
        except Exception, e:
            # error_info = Exception, ": ", e
            # error_log_class.write_log(error_info)
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "run  function of implement_es failed !"
            self.logger.error(error_info)


if __name__ == '__main__':
    test = StartFullData()
