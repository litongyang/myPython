# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import logging
import logging.config
import datetime
import error_log
import work.fenghuang_jr.crm.crm_beta.base_method.file_dir_process as file_dir_process


class CreateLogs:
    def __init__(self):
        self.date = datetime.date.today()
        self.error_log = error_log.ErrorLog()
        self.file_dir_process = file_dir_process.FileProcess()
        self.log_path = "../logs/%s" % self.date
        self.log_path_file = "%s/log.log" % self.log_path
        self.error_log_path_file = "%s/error_log.log" % self.log_path
        self.fund_log_path_file = "%s/fund_log.log" % self.log_path
        self.coupon_log_path_file = "%s/coupon_log.log" % self.log_path
        self.logger = logging.getLogger('start.create_log')

    # 处理log文件
    # @staticmethod
    def handle_log_file(self, file_dir_process_class, log_path):
        try:
            file_dir_process_class.is_exist_mkdir(log_path)
            self.logger.info("create dir of log is success !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "create dir of log is failed !"
            self.logger.error(error_info)

    # @staticmethod
    def create_log_file(self, file_dir_process_class, file_path):
        try:
            file_dir_process_class.create_file(file_path)
            self.logger.info("create log is success !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "create log is failed !"
            self.logger.error(error_info)

    # 写日志到log文件
    def write_log(self, content):
        try:
            print content
            fl = open(self.log_path_file, 'w')
            fl.write(str(content))
            fl.close()
        except Exception, e:
            error_info = Exception, ": ", e
            # self.error_log.handle_error_log_file()
            self.error_log.write_log(error_info)


if __name__ == '__main__':
    # ---test----
    test = CreateLogs()
    # test.handle_log_file()
    test.write_log("lty")
