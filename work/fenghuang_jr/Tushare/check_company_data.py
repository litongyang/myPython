# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
核对复权表和不复权表数据,如果有问题重跑
"""

import logging
import logging.config
import MySQLdb
import datetime
import get_trade_data_method as get_trade_data_method
import application_method as application_method
import create_table.create_table as mysqldb
import read_conf as read_conf
import send_mail as send_mail


class CreateTable:
    def __init__(self):
        self.mail_tolist = read_conf.ReadConf().get_options("mail_send", "mail_tolist")
        self.mail_host = read_conf.ReadConf().get_options("mail_send", "mail_host")
        self.mail_user = read_conf.ReadConf().get_options("mail_send", "mail_user")
        self.mail_password = read_conf.ReadConf().get_options("mail_send", "mail_password")
        self.mail_postfix = read_conf.ReadConf().get_options("mail_send", "mail_postfix")
        self.today = datetime.date.today()
        self.begin_date = str(self.today - datetime.timedelta(days=1))
        self.end_date = str(self.today - datetime.timedelta(days=1))
        self.week_day = (self.today - datetime.timedelta(days=1)).weekday()
        # self.begin_date = '2016-12-29'  # test
        # self.end_date = '2016-12-29'  # test
        self.get_trade_data_method_class = get_trade_data_method.GetDataTradeHistroy()
        self.mysqldb = mysqldb.CreateTable()
        self.company_cnt = 2800  # 每日非停牌的上市公司数量约数

    def check_fun(self):
        logging.config.fileConfig('logger.conf')
        logger = logging.getLogger('tradedata.test')
        if self.week_day == 5 or self.week_day == 6:
            pass
        else:
            count_no = self.mysqldb.cur.execute(
                "SELECT * FROM %s where date='%s'" % (self.mysqldb.table_trade_history_data_no, self.begin_date))
            results_no = self.mysqldb.cur.fetchmany(count_no)
            # 不复权表数据严重缺失,重跑
            if len(results_no) < self.company_cnt:
                logger.error("trade_history_data_cn_no数据严重缺失,重跑!")
                send_mail.send_mail(self.mail_tolist, self.mail_host, self.mail_user, self.mail_password, self.mail_postfix, "trade_history_data_cn_no严重缺失,重跑!", "trade_history_data_cn_no严重缺失,重跑!   明细:该表已入库:%s条数据" % len(results_no))
                self.get_trade_data_method_class.get_company_code()
                self.get_trade_data_method_class.get_trade_data(self.get_trade_data_method_class.company_code_list, self.begin_date, self.end_date, None, self.mysqldb.table_trade_history_data_no)
                logger.info("trade_history_data_cn_no全量重跑成功!")
                logger.info("================")

            count = self.mysqldb.cur.execute("SELECT * FROM %s where date='%s'" % (self.mysqldb.table_trade_history_data, self.begin_date))
            results = self.mysqldb.cur.fetchmany(count)
            # 后复权表数据严重缺失,重跑
            if len(results) < self.company_cnt:
                logger.error("trade_history_data_cn严重缺失,重跑!")
                send_mail.send_mail(self.mail_tolist, self.mail_host, self.mail_user, self.mail_password, self.mail_postfix, "trade_history_data_cn严重缺失,重跑!", "trade_history_data_cn严重缺失,重跑!   明细:该表已入库: %s 条数据" % len(results) )
                self.get_trade_data_method_class.get_company_code()
                self.get_trade_data_method_class.get_trade_data(self.get_trade_data_method_class.company_code_list, self.begin_date, self.end_date, 'hfq',
                                                                self.mysqldb.table_trade_history_data)
                logger.info("trade_history_data_cn全量重跑成功!")
                logger.info("================")

            # 相对于不复权数据,复权缺失数据补全
            diff = self.mysqldb.cur.execute(
                "select a.company_code from ( select company_code from trade_history_data_cn_no where date = '%s')a left outer join (select company_code from trade_history_data_cn where date = '%s')b on a.company_code = b.company_code where b.company_code is null" % (self.begin_date, self.begin_date))
            results_diff = self.mysqldb.cur.fetchmany(diff)
            company_diff_list = []
            if len(results_diff) == 0:
                pass
            else:
                logger.error("trade_history_data_cn缺失部分数据,重跑!")
                for i in range(0, len(results_diff)):
                    company_diff_list.append(str(results_diff[i][0]))
                send_mail.send_mail(self.mail_tolist, self.mail_host, self.mail_user, self.mail_password, self.mail_postfix, "trade_history_data_cn缺失部分数据,重跑!", "trade_history_data_cn缺失部分数据,重跑!   明细:该表缺失的公司代码: %s " % ";".join(company_diff_list))
                self.get_trade_data_method_class.get_trade_data(company_diff_list, self.begin_date, self.end_date, 'hfq', self.mysqldb.table_trade_history_data)
                logger.info("trade_history_data_cn缺失数据补全成功!")
                logger.info("================")

            # 相对于复权数据,不复权缺失数据补全
            diff_no = self.mysqldb.cur.execute(
                "select a.company_code from ( select company_code from trade_history_data_cn where date = '%s')a left outer join (select company_code from trade_history_data_cn_no where date = '%s')b on a.company_code = b.company_code where b.company_code is null" % (self.begin_date, self.begin_date))
            results_diff_no = self.mysqldb.cur.fetchmany(diff_no)
            company_diff_no_list = []
            if len(results_diff_no) == 0:
                pass
            else:
                logger.error("trade_history_data_cn_no缺失部分数据,重跑!")
                for i in range(0, len(results_diff_no)):
                    company_diff_no_list.append(str(results_diff_no[i][0]))
                self.get_trade_data_method_class.get_trade_data(company_diff_no_list, self.begin_date, self.end_date, None, self.mysqldb.table_trade_history_data_no)
                send_mail.send_mail(self.mail_tolist, self.mail_host, self.mail_user, self.mail_password, self.mail_postfix, "trade_history_data_cn_no缺失部分数据,重跑!", "trade_history_data_cn_no缺失部分数据,重跑!   明细:该表缺失的公司代码: %s " % ";".join(company_diff_no_list) )
                logger.info("trade_history_data_cn_no缺失数据补全成功!")
                logger.info("================")
        application_method.move_log_file("logs.log")


if __name__ == '__main__':
    test = CreateTable()
    test.check_fun()
    # test.create_table_archives_interest_volume_daily()
