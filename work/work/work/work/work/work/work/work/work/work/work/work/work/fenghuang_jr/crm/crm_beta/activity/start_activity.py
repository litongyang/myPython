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
import work.fenghuang_jr.crm.crm_beta.schedule.invoke_schedule as invoke_schedule
import start_activity_parallel


class StartActivity:
    def __init__(self):
        self.log_path = ""
        self.is_success = []
        self.drop_table_sql_path = "../query_sql/activity/drop_table_activity.sql"
        self.invoke_schedule = invoke_schedule.InvokeSchedule()
        self.time_moniter = time_moniter.TimeMoniter()
        self.read_conf = read_conf.ReadConf()
        self.sqoop_function = sqoop_function.SqoopFunction()
        self.start_data_input = start_data_input.StartDataInput()
        self.start_activity_parallel = start_activity_parallel.StartActivityParallel()

    def fun(self):
        logging.config.fileConfig('../logger.conf')
        root_logger = logging.getLogger('root')
        root_logger.debug('test start logger...')
        logger = logging.getLogger('crm.start_activity')
        self.invoke_schedule.invoke_first_fun(31, 'start activity', 'start running......')
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
                self.start_data_input.input_activity_contact_awards(self.is_success)
                # 获得points的结果数据
                self.start_activity_parallel.get_activity_statistics_data(self.is_success)
                self.start_activity_parallel.get_activity_logger_data(self.is_success)
                self.start_activity_parallel.implement_es_activity(self.is_success)
            if str(self.read_conf.get_options('cycle_all', 'content')) == 'append':
                print "append"
            logger.info(" value of is_success is %s :" % self.is_success)
            flag = 1
            for v in self.is_success:
                if v == 0:
                    self.invoke_schedule.invoke_update_fun(0, 1, "start_points is failed !", -1)
                    flag = 0
                    break
            if flag == 1:
                self.invoke_schedule.invoke_update_fun(0, 0, "start_points is successed !", -1)
            application_method.move_log_file("logs.log")

        except Exception, e:
            print "==========",Exception, e

if __name__ == '__main__':
    test = StartActivity()
    test.fun()
