# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-


import logging
import logging.config
import work.fenghuang_jr.crm.crm_beta.base_method.file_dir_process as file_dir_process
import create_log
import work.fenghuang_jr.crm.crm_beta.base_method.time_moniter as time_moniter
import work.fenghuang_jr.crm.crm_beta.base_method.read_conf as read_conf
import error_log
import work.fenghuang_jr.crm.crm_beta.base_method.sqoop_function as sqoop_function
import work.fenghuang_jr.crm.crm_beta.input_data_toHive.start_data_input as start_data_input
import start_full_data
import drop_table


class Start:
    def __init__(self):
        self.log_path = ""
        self.file_dir_process = file_dir_process.FileProcess()
        self.create_log = create_log.CreateLogs()
        self.error_log = error_log.ErrorLog()
        self.time_moniter = time_moniter.TimeMoniter()
        self.read_conf = read_conf.ReadConf()
        self.sqoop_function = sqoop_function.SqoopFunction()
        self.start_data_input = start_data_input.StartDataInput()
        self.start_full_data = start_full_data.StartFullData()

    def fun(self):
        logging.config.fileConfig('logger.conf')
        root_logger = logging.getLogger('root')
        root_logger.debug('test start logger...')
        logger = logging.getLogger('start')
        try:
            logger.info("start............")
            drop_table.drop_table()
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
            self.time_moniter.get_diff(self.read_conf, self.file_dir_process, self.create_log.log_path_file)
            self.time_moniter.is_all_fun(self.read_conf, self.file_dir_process, self.create_log.log_path_file)
            self.time_moniter.write_cycle_all(self.read_conf, self.file_dir_process, self.create_log.log_path_file)
            #
            # # 判断全量还是增量并执行相关代码
            if str(self.read_conf.get_options('cycle_all', 'content')) == "all":
                # 从mysql数据源获得基础数据
                self.start_data_input.input_tb_counpon_record_fun(self.error_log, self.file_dir_process, self.create_log.log_path_file)
                self.start_data_input.input_tb_invite_reward_trace_fun(self.error_log, self.file_dir_process, self.create_log.log_path_file)
                self.start_data_input.input_tb_invest_fun(self.error_log, self.file_dir_process, self.create_log.log_path_file)
                # self.start_full_data.get_base_data(self.file_dir_process, self.create_log.log_path_file)

                # 获得fund的结果数据
                self.start_full_data.get_fund_parallel_data(self.read_conf, self.sqoop_function, self.error_log, self.file_dir_process, self.create_log.log_path_file)
                # self.start_full_data.get_coupon_parallel_data(self.error_log, self.file_dir_process, self.create_log.log_path_file)
                # self.start_full_data.get_activity_parallel_data(self.read_conf, self.sqoop_function, self.error_log, self.file_dir_process, self.create_log.log_path_file)
                # self.start_full_data.crm_end(self.error_log, self.file_dir_process, self.create_log.log_path_file)
                # self.start_full_data.implement_es(self.error_log)
                # self.read_conf.set_options("before_all_cycle_time", "content", self.time_moniter.this_time)  # 调整本次运行时间设置

            if str(self.read_conf.get_options('cycle_all', 'content')) == 'append':
                print "append"
        except Exception, e:
            print Exception, e

if __name__ == '__main__':
    test = Start()
    test.fun()
