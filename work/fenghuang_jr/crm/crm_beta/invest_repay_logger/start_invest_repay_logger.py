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
import start_invest_repay_logger_parallel
import work.fenghuang_jr.crm.crm_beta.schedule.invoke_schedule as invoke_schedule


class StartFund:
    def __init__(self):
        self.log_path = ""
        self.is_success = []
        self.drop_table_sql_path = "../query_sql/invest_repay/drop_table_invest_repay.sql"
        self.invoke_schedule = invoke_schedule.InvokeSchedule()
        self.time_moniter = time_moniter.TimeMoniter()
        self.read_conf = read_conf.ReadConf()
        self.sqoop_function = sqoop_function.SqoopFunction()
        self.start_data_input = start_data_input.StartDataInput()
        self.start_invest_repay_logger_parallel = start_invest_repay_logger_parallel.StartInvestRepayLoggerParallel()

    def fun(self):
        logging.config.fileConfig('../logger.conf')
        root_logger = logging.getLogger('root')
        root_logger.debug('test start logger...')
        logger = logging.getLogger('crm.start_invest_repay_logger')
        self.invoke_schedule.invoke_first_fun(32, 'start_invest_repay_logger', 'start running......')
        try:
            logger.info("start............")
            drop_table.drop_table(self.drop_table_sql_path, self.is_success)

            # # 判断全量还是增量并执行相关代码
            if str(self.read_conf.get_options('cycle_all', 'content')) == "all":
                # 从mysql数据源获得基础数据
                self.start_data_input.input_invest_repay_logger(self.is_success)

                # 获得fund的结果数据
                self.start_invest_repay_logger_parallel.crm_end_invest_repay_logger(self.is_success)
                self.start_invest_repay_logger_parallel.implement_es_invest_repay_logger(self.is_success)

            if str(self.read_conf.get_options('cycle_all', 'content')) == 'append':
                print "append"
            logger.info(" value of is_success is %s :" % self.is_success)
            flag = 1
            for v in self.is_success:
                if v == 0:
                    self.invoke_schedule.invoke_update_fun(0, 1, "start_invest_repay_logger is failed !", -1)
                    flag = 0
                    break
            if flag == 1:
                self.invoke_schedule.invoke_update_fun(0, 0, "start_invest_repay_logger is successed !", -1)
            application_method.move_log_file("logs.log")
        except Exception, e:
            print Exception, e

if __name__ == '__main__':
    test = StartFund()
    test.fun()

