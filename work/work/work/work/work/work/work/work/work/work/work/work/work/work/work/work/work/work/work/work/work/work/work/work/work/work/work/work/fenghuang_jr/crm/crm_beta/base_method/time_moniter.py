# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import logging
import logging.config
import time
import datetime
# import error_log
import file_dir_process


class TimeMoniter:
    def __init__(self):
        self.logger = logging.getLogger('start.time_moniter')
        # self.read_conf = read_conf.ReadConf()
        # self.error_log = error_log.ErrorLog()
        self.date = datetime.date.today()
        self.before_all_cycle_time = ""
        self.before_time = ''
        self.ys_time = 0.0  # 上一次运行时间
        self.this_time = time.time()  # 本次运行时间
        self.diff = 1  # 上次运行日期距离本次运行间隔天数
        self.is_all = 0  # 全量标示(1:全量;0:增量)

    def get_diff(self, read_conf_class):
        try:
            self.before_time = read_conf_class.get_options("before_all_cycle_time", "content")
            if self.before_time == '':
                self.before_time = 0
                # self.before_time = '1971-01-01 00:00:00'
            # self.ys_time = time.mktime(time.strptime(self.before_time, '%Y-%m-%d %H:%M:%S'))
            self.ys_time = self.before_time
            self.diff = (float(self.this_time) - float(self.ys_time)) / 86400
            # print self.diff
            self.logger.info("Runing time difference : %f" % self.diff)
        except Exception, e:

            exception = Exception, e
            error_info = str(exception) + "--------->>" + "run  function of get_diff is failed !"
            self.logger.error(error_info)

    def is_all_fun(self, read_conf_class):
        read_conf_class.get_options("is_all", "is_overdue_days")
        try:
            if self.diff < int(read_conf_class.get_options('is_all', 'is_overdue_days')):
                print "%s process is append input" % self.date
            else:
                self.is_all = 1
                self.logger.info("%s process is  all  input" % self.date)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "run  function of is_all_fun failed !"
            self.logger.error(error_info)

    def write_cycle_all(self, read_conf_class):
        try:
            if self.is_all == 1:
                read_conf_class.set_options("cycle_all", "content", "all")
                self.logger.info("Refresh Type : all")
            else:
                read_conf_class.set_options("cycle_all", "content", "append")
                self.logger.info("Refresh Type : append")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "run  function of write_cycle_all is failed !"
            self.logger.error(error_info)

if __name__ == '__main__':
    time_moniter = TimeMoniter()
    # time_moniter.get_diff()
    # time_moniter.is_all_fun()
    # time_moniter.write_cycle_all()
