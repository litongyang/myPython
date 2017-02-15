# __author__ = 'lty'
# -*- coding: utf-8 -*-

import datetime
import logging
import logging.config
import sys
sys.path.append("/root/personas_fengjr")
import personas.version_1.base_method.hive_command_method as hive_command_method
import personas.version_1.base_method.application_method as application_method
import personas.version_1.base_method.read_conf as read_conf
import personas.version_1.base_method.send_mail as send_mail


class GetAllLabel:
    def __init__(self):
        self.yesterday = datetime.date.today() - datetime.timedelta(days=1)
        self.before_day = datetime.date.today() - datetime.timedelta(days=2)
        self.all_label_sql_path = read_conf.ReadConf().get_options("path_get_label", "all_label_sql_path")
        self.show_label_sql_path = read_conf.ReadConf().get_options("path_get_label", "show_label_sql_path")
        self.is_success = []
        self.mail_tolist = read_conf.ReadConf().get_options("mail_send", "mail_tolist")
        self.mail_host = read_conf.ReadConf().get_options("mail_send", "mail_host")
        self.mail_user = read_conf.ReadConf().get_options("mail_send", "mail_user")
        self.mail_password = read_conf.ReadConf().get_options("mail_send", "mail_password")
        self.mail_postfix = read_conf.ReadConf().get_options("mail_send", "mail_postfix")

    """ 将标签汇总到一张表 """
    def get_label(self, is_success):
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('personas.get_label')
        try:
            param = '-d' + ' ' + 'dt=' + '\'' + str(self.yesterday) + '\'' + ' ' + '-f'
            os_v = hive_command_method.hive_command(str(param), self.all_label_sql_path)
            if os_v == 0:
                is_success.append(1)
                logger.info("get_label is successed !")
            else:
                is_success.append(0)
                logger.error("get_label is failed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_label is Exception !"
            logger.error(error_info)
            is_success.append(0)

    """ 展示标签 """
    def get_show_label(self, is_success):
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('personas.get_show_label')
        try:
            param = '-d' + ' ' + 'dt=' + '\'' + str(self.yesterday) + '\'' + ' ' + '-d' + ' ' + 'before=' + '\'' + str(self.before_day) + '\'' + ' ' + '-f'
            if self.is_success[0] == 1:
                os_v = hive_command_method.hive_command(str(param), self.show_label_sql_path)
            else:
                os_v = 2
            if os_v == 0:
                is_success.append(1)
                logger.info("get_show_label is successed !")
            else:
                is_success.append(0)
                logger.error("get_show_label is failed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_show_label is Exception !"
            logger.error(error_info)
            is_success.append(0)
        flag = 1
        for v in self.is_success:
            if v == 0:
                flag = 0
                break
        if flag == 1:
            logger.info("success!")
        else:
            logger.error("error!")
            send_mail.send_mail(self.mail_tolist, self.mail_host, self.mail_user, self.mail_password, self.mail_postfix, "GetAllLabel_error", "GetAllLabel is error！")
        application_method.move_log_file("logs.log")


if __name__ == '__main__':
    get_all_label = GetAllLabel()
    get_all_label.get_label(get_all_label.is_success)
    get_all_label.get_show_label(get_all_label.is_success)
