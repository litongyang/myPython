# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-
"""
log文件处理
"""

import os
import application_method


class LogProcess:
    def __init__(self):
        self.log_path = '../log/logs.log'
        self.log_name = 'logs.log'
        self.preference_log = 'preference_log.log'
        self.is_finished = 'Spider closed (finished)'

    def log_process(self):
        application_method.move_log_file(self.log_name, self.log_path)


if __name__ == '__main__':
    log = LogProcess()
    log.log_process()