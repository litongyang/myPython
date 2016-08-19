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
import start_invest_parallel
import work.fenghuang_jr.crm.crm_beta.schedule.invoke_schedule as invoke_schedule


class StartFund:
    def __init__(self):
        self.log_path = ""
        self.is_success = []
        self.drop_table_sql_path = "../query_sql/invest/drop_table_invest.sql"
        self.invoke_schedule = invoke_schedule.InvokeSchedule()
        self.time_moniter = time_moniter.TimeMoniter()
        self.read_conf = read_conf.ReadConf()
        self.sqoop_function = sqoop_function.SqoopFunction()
        self.start_data_input = start_data_input.StartDataInput()
        self.start_invest_parallel = start_invest_parallel.StartInvestParallel()

    def fun(self):
        logging.config.fileConfig('../logger.conf')
        root_logger = logging.getLogger('root')
        root_logger.debug('test start logger...')
        logger = logging.getLogger('crm.start_invest')
        self.invoke_schedule.invoke_first_fun(29, 'start invest', 'start running......')
        try:
            logger.info("start............")
            drop_table.drop_table(self.drop_table_sql_path, self.is_success)

            # # 时间监控
            # self.time_moniter.get_diff(self.read_conf)
            # self.time_moniter.is_all_fun(self.read_conf)
            # self.time_moniter.write_cycle_all(self.read_conf)
            #
            # # 判断全量还是增量并执行相关代码
            if str(self.read_conf.get_options('cycle_all', 'content')) == "all":
                # 从mysql数据源获得基础数据
                self.start_data_input.input_tb_user_fun(self.is_success)
                self.start_data_input.input_tb_fund_record_fun(self.is_success)
                self.start_data_input.input_tb_loanrequest_privilege_fun(self.is_success)
                self.start_data_input.input_tb_loan_fun(self.is_success)
                self.start_data_input.input_tb_invite_reward_trace_fun(self.is_success)
                self.start_data_input.input_tb_invest_fun(self.is_success)
                self.start_data_input.input_invest_desc_trans(self.is_success)
                # self.start_data_input.input_invest_trans(self.is_success)
                self.start_data_input.input_invest_one_trans(self.is_success)

                # 获得fund的结果数据
                self.start_invest_parallel.get_crm_invest_status(self.is_success)
                # self.start_invest_parallel.get_crm_desc_json_new(self.is_success)
                self.start_invest_parallel.crm_end_invest(self.is_success)
                self.start_invest_parallel.crm_end_invest_logger(self.is_success)
                self.start_invest_parallel.implement_es_invest(self.is_success)
                # self.read_conf.set_options("before_all_cycle_time", "content", self.time_moniter.this_time)  # 调整本次运行时间设置

            if str(self.read_conf.get_options('cycle_all', 'content')) == 'append':
                print "append"
            logger.info(" value of is_success is %s :" % self.is_success)
            flag = 1
            for v in self.is_success:
                if v == 0:
                    self.invoke_schedule.invoke_update_fun(0, 1, "start_invest is failed !", -1)
                    flag = 0
                    break
            if flag == 1:
                self.invoke_schedule.invoke_update_fun(0, 0, "start_invest is successed !", -1)
            application_method.move_log_file("logs.log")
        except Exception, e:
            print Exception, e

if __name__ == '__main__':
    test = StartFund()
    test.fun()
