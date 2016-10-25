# __author__ = 'tongyang.li'

import sys
import work.fenghuang_jr.crm.crm_beta.base_method.drop_table as drop_table
import work.fenghuang_jr.crm.crm_beta.base_method.time_moniter as time_moniter
import work.fenghuang_jr.crm.crm_beta.base_method.read_conf as read_conf
import work.fenghuang_jr.crm.crm_beta.base_method.sqoop_function as sqoop_function
import work.fenghuang_jr.crm.crm_beta.base_method.application_method as application_method
import work.fenghuang_jr.crm.crm_beta.input_data_toHive.start_data_input as start_data_input
import work.fenghuang_jr.crm.crm_beta.schedule.invoke_schedule as invoke_schedule

if __name__ == '__main__':
    start_data_input_class = start_data_input.StartDataInput()
    drop_table_sql_path = ""
    is_success = []
    print "Program name:", sys.argv[1]
    if sys.argv[1] == 'input_crm_points_statistics_fun':
         drop_table.drop_table(drop_table_sql_path, is_success)
    if sys.argv[1] == 'input_crm_points_statistics_fun':
        start_data_input_class.input_crm_points_statistics_fun(is_success)
