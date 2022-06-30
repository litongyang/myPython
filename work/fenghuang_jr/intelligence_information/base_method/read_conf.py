# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import logging
import logging.config
import ConfigParser
# import error_log


class ReadConf:
    def __init__(self):
        logging.config.fileConfig('../logger.conf')
        self.logger = logging.getLogger('start.read_conf')
        self.cf = ConfigParser.RawConfigParser()
        self.conf_name = "../info.conf"
        self.is_overdue_days = ""

    def get_options(self, section_name, var_name):
        try:
            self.cf.read(self.conf_name)
            return self.cf.get(section_name, var_name)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get options of crm_conf: %s %s is failed !" % (section_name, var_name)
            self.logger.error(error_info)

    def set_options(self, section_name, var_name, value):
        try:
            self.cf.set(section_name, var_name, value)
            self.cf.write(open(self.conf_name, 'w'))
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "set options of crm_conf: %s %s is failed !" % (section_name, var_name)
            self.logger.error(error_info)

if __name__ == '__main__':
    test = ReadConf()
    test.get_options("finance_sql_path", "load_finance_prices_sql_path")
    # test.set_options("cycle_all", "content", "2")
