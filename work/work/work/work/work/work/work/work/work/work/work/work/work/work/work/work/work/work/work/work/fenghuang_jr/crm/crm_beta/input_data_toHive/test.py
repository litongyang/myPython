# __author__ = 'lty'
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
import work.fenghuang_jr.crm.crm_beta.activity.start_activity_parallel


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
        os_v = self.sqoop_function.sqoop_all(host, username, password, self.crm_activity_contact_awards_sql, table_name,
                                             target_dir, hive_table)
        # push_schedule_result_method.push_schedule_result(os_v, 2, is_success, fun_name)
    except Exception, e:
        print Exception, e
        # push_schedule_result_method.push_schedule_exception

input_activity_contact_awards(1)