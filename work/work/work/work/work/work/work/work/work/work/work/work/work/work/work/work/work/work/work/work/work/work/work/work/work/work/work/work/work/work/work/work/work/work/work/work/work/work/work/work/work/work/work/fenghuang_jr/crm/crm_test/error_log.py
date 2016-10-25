# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import os
import datetime


class ErrorLog:
    def __init__(self):
        self.date = datetime.date.today()
        self.error_log_path = "./error_logs/%s" % self.date
        self.error_log_path_file = "%s/error_log.log" % self.error_log_path

    @staticmethod
    def handle_error_log_file(file_dir_process_class, error_log_path):
        file_dir_process_class.is_exist_mkdir(error_log_path)

    @staticmethod
    def handle_error_log_file(file_dir_process_class, error_log_path):
        file_dir_process_class.is_exist_mkdir(error_log_path)

    # 写错误日志到errorlog文件
    def write_log(self, content):
        try:
            fl = open(self.error_log_path_file, 'w')
            fl.write(str(content))
            fl.close()
        except Exception, e:
            print Exception, e

if __name__ == '__main__':
    test = ErrorLog()
    # test.handle_error_log_file()
    test.write_log("error!")

