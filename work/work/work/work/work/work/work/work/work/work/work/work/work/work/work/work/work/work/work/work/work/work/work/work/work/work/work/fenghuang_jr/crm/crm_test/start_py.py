# __author__ = 'tongyang.li'

import file_dir_process
import create_log
import error_log
import read_conf
import application_method as method
import sqoop_function
import datetime


class StartPy:
    def __init__(self):
        self.file_dir_process = file_dir_process.FileProcess()
        self.create_log = create_log.CreateLogs()
        self.error_log = error_log.ErrorLog()
        self.read_conf = read_conf.ReadConf()
        self.sqoop = sqoop_function.SqoopFunction()
        self.date = datetime.date.today()

    def invoke_fun(self):
        self.create_log.handle_log_file(self.file_dir_process, self.create_log.log_path)
        self.error_log.handle_error_log_file(self.file_dir_process, self.error_log.error_log_path)
        self.sqoop.sqoop_table(self.error_log, 'host', 'user_name', 'password', 'table_name', 'target_dir', 'hive_table')
        self.sqoop.sqoop_dt(self.error_log, 'd', self.date, 'host', 'user_name', 'password', 'sql', 'table_name', 'target_dir', 'hive_table')


if __name__ == '__main__':
    start_py = StartPy()
    start_py.invoke_fun()
