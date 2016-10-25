# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import sys
sys.path.append("/data/ml/tongyang/python")

import logging
import logging.config
import work.fenghuang_jr.crm.crm_beta.base_method.drop_table as drop_table
import work.fenghuang_jr.crm.crm_beta.base_method.time_moniter as time_moniter
import work.fenghuang_jr.crm.crm_beta.base_method.read_conf as read_conf
import work.fenghuang_jr.crm.crm_beta.base_method.sqoop_function as sqoop_function
import work.fenghuang_jr.crm.crm_beta.base_method.application_method as application_method
import work.fenghuang_jr.crm.crm_beta.input_data_toHive.start_data_input as start_data_input
import start_coupon_parallel
import work.fenghuang_jr.crm.crm_beta.schedule.invoke_schedule as invoke_schedule


class StartCoupon:
    def __init__(self):
        self.log_path = ""
        self.is_success = []
        self.drop_table_sql_path = "../query_sql/coupon/drop_table_coupon.sql"
        self.invoke_schedule = invoke_schedule.InvokeSchedule()
        self.time_moniter = time_moniter.TimeMoniter()
        self.read_conf = read_conf.ReadConf()
        self.sqoop_function = sqoop_function.SqoopFunction()
        self.start_data_input = start_data_input.StartDataInput()
        self.start_coupon_parallel = start_coupon_parallel.StartCouponParallel()

    def fun(self):
        logging.config.fileConfig('../logger.conf')
        root_logger = logging.getLogger('root')
        root_logger.debug('start logger...')
        logger = logging.getLogger('crm.start_coupon')
        self.invoke_schedule.invoke_first_fun(28, 'start coupon', 'start running......')
        try:
            logger.info("start............")
            drop_table.drop_table(self.drop_table_sql_path, self.is_success)
            # #  判断 log日志是否存在 并创建log文件
            # self.create_log.handle_log_file(self.file_dir_process, self.create_log.log_path)
            # self.create_log.create_log_file(self.file_dir_process, self.create_log.log_path_file)
            # self.create_log.create_log_file(self.file_dir_process, self.create_log.error_log_path_file)
            # self.create_log.create_log_file(self.file_dir_process, self.create_log.fund_log_path_file)
            # self.create_log.create_log_file(self.file_dir_process, self.create_log.coupon_log_path_file)
            # self.error_log.handle_error_log_file(self.file_dir_process, self.error_log.error_log_path)
            # self.error_log.create_error_log_file(self.file_dir_process, self.error_log.error_log_path_file)
            #
            # # 时间监控
            # self.time_moniter.get_diff(self.read_conf)
            # self.time_moniter.is_all_fun(self.read_conf)
            # self.time_moniter.write_cycle_all(self.read_conf)
            #
            # # 判断全量还是增量并执行相关代码
            if str(self.read_conf.get_options('cycle_all', 'content')) == "all":
                # 从mysql数据源获得基础数据
                self.start_data_input.input_tb_coupon_record_fun(self.is_success)
                self.start_data_input.input_tb_invite_reward_trace_fun(self.is_success)
                self.start_data_input.input_tb_invest_fun(self.is_success)
                # 获得coupon的结果数据
                self.start_coupon_parallel.get_crm_coupon_json_new(self.is_success)
                self.start_coupon_parallel.get_coupon_statistics_data(self.is_success)
                self.start_coupon_parallel.get_coupon_logger_data(self.is_success)
                self.start_coupon_parallel.implement_es_coupon(self.is_success)

                # self.read_conf.set_options("before_all_cycle_time", "content", self.time_moniter.this_time)  # 调整本次运行时间设置

            if str(self.read_conf.get_options('cycle_all', 'content')) == 'append':
                print "append"
            logger.info(" value of is_success is %s :" % self.is_success)
            flag = 1
            for v in self.is_success:
                if v == 0:
                    self.invoke_schedule.invoke_update_fun(0, 1, "start_coupon is failed !", -1)
                    flag = 0
                    break
            if flag == 1:
                self.invoke_schedule.invoke_update_fun(0, 0, "start_coupon is successed !", -1)
            application_method.move_log_file("logs.log")

        except Exception, e:
            print Exception, e
            self.invoke_schedule.invoke_update_fun(0, 2, "start_coupon is Exception !", -1)

if __name__ == '__main__':
    test = StartCoupon()
    test.fun()
