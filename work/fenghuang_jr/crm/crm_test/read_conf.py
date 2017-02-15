# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-


import ConfigParser
import error_log


class ReadConf:
    def __init__(self):
        self.error_log = error_log.ErrorLog()
        self.cf = ConfigParser.RawConfigParser()
        self.conf_name = "crm.conf"
        self.is_overdue_days = ""

    def get_options(self, section_name, var_name):
        # type: (object, object) -> object
        try:
            self.cf.read(self.conf_name)
            return self.cf.get(section_name, var_name)
        except Exception, e:
            error_info = Exception, ": ", e
            # self.error_log.handle_error_log_file()
            self.error_log.write_log(error_info)

    def set_options(self, section_name, var_name, value):
        try:
            self.cf.set(section_name, var_name, value)
            self.cf.write(open(self.conf_name, 'w'))
        except Exception, e:
            error_info = Exception, ": ", e
            # self.error_log.handle_error_log_file()
            self.error_log.write_log(error_info)

if __name__ == '__main__':
    test = ReadConf()
    test.get_options("is_all", "is_overdue_days")
    test.set_options("cycle_all", "content", "2")
