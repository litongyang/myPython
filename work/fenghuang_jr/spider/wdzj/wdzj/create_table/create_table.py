# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import MySQLdb


class CreateTable:
    def __init__(self):
        """
        self.db_name = 'spider'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = '10.10.202.16'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '1234abcd'  # 密码
        """
        self.db_name = 'test'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.file_name = 'test1'
        self.table_archives_interest_volume_daily = 'wdzj_archives_interest_volume_daily'
        self.table_archives_repayment_inflow_daily = 'wdzj_archives_repayment_inflow_daily'
        self.table_archives_invest_loan_daily = 'wdzj_archives_invest_loan_daily'
        self.table_preference = 'wdzj_preference_info'
        self.table_basic_last90_type = 'wdzj_basic_info_last90_type'
        self.table_basic_last90_deadline = 'wdzj_basic_info_last90_deadline'
        self.table_basic_last90_amount = 'wdzj_basic_info_last90_amount'
        self.conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                    port=self.db_port)
        self.cur = self.conn.cursor()

    # 利率和成交量的每日数据
    def create_table_archives_interest_volume_daily(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.table_archives_interest_volume_daily)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "source_type varchar(20) comment '数据源类型',"
                "company_name varchar(100) comment '公司名称',"
                "index_type varchar(20) comment '指标类型:0:利率和成交量 1:历史待还和净流入 3:投资人数和借款人数',"
                "time_slot varchar(20) comment '时间段类型:0:每日 1:周 3:月',"
                "interest_rate_volume_date varchar(50) comment '日期',"
                "interest_rate_day varchar(100) comment '每日的利率数据',"
                "volume_day varchar(100) comment '每日的成交量数据',"
                "url varchar(2000) comment 'url',"
                "date varchar(20) comment '抓取日期date',"
                "PRIMARY KEY (`company_name`,`interest_rate_volume_date`,`date`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.table_archives_interest_volume_daily)
        except Exception, e:
            print Exception, e

    # 历史待还和净流入的每日数据
    def create_table_archives_repayment_inflow_daily(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.table_archives_repayment_inflow_daily)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "source_type varchar(20) comment '数据源类型',"
                "company_name varchar(100) comment '公司名称',"
                "index_type varchar(20) comment '指标类型:0:利率和成交量 1:历史待还和净流入 3:投资人数和借款人数',"
                "time_slot varchar(20) comment '时间段类型:0:每日 1:周 3:月',"
                "pending_repayment_inflow_date varchar(50) comment '日期',"
                "pending_repayment_history_day varchar(100) comment '每日的历史待还数据',"
                "net_inflow_day varchar(100) comment '每日的净流入数据',"
                "url varchar(2000) comment 'url',"
                "date varchar(20) comment '抓取日期date',"
                "PRIMARY KEY (`company_name`,`pending_repayment_inflow_date`,`date`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.table_archives_repayment_inflow_daily)
        except Exception, e:
            print Exception, e

    # 投资人数和借款人数的每日数据
    def create_table_archives_invest_loan_daily(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.table_archives_invest_loan_daily)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "source_type varchar(20) comment '数据源类型',"
                "company_name varchar(100) comment '公司名称',"
                "index_type varchar(20) comment '指标类型:0:利率和成交量 1:历史待还和净流入 3:投资人数和借款人数',"
                "time_slot varchar(20) comment '时间段类型:0:每日 1:周 3:月',"
                "invest_loan_user_date varchar(50) comment '日期',"
                "invest_user_day varchar(100) comment '每日的投资人数的数据',"
                "loan_user_day varchar(100) comment '每日的借款人数的数据',"
                "url varchar(2000) comment 'url',"
                "date varchar(20) comment '抓取日期date',"
                "PRIMARY KEY (`company_name`,`invest_loan_user_date`,`date`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.table_archives_invest_loan_daily)
        except Exception, e:
            print Exception, e

    # 近90日标的类型数据
    def create_table_basic_last90_type(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.table_basic_last90_type)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "source_type varchar(20) comment '数据源类型',"
                "company_name varchar(100) comment '公司名称',"
                "last_90day_type_name varchar(100) comment '近90日标的类型名称',"
                "last_90day_type_data varchar(100) comment '近90日标的类型数据',"
                "url varchar(2000) comment 'url',"
                "date varchar(20) comment '抓取日期date',"
                "PRIMARY KEY (`company_name`,`last_90day_type_name`,`date`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.table_basic_last90_type)
        except Exception, e:
            print Exception, e

    #  近90日标的到期数据
    def create_table_basic_last90_deadline(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.table_basic_last90_deadline)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "source_type varchar(20) comment '数据源类型',"
                "company_name varchar(100) comment '公司名称',"
                "last_90day_deadline_name varchar(100) comment '近90日标的到期名称',"
                "last_90day_deadline_data varchar(100) comment '近90日标的到期数据',"
                "url varchar(2000) comment 'url',"
                "date varchar(20) comment '抓取日期date',"
                "PRIMARY KEY (`company_name`,`last_90day_deadline_name`,`date`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.table_basic_last90_deadline)
        except Exception, e:
            print Exception, e

    # 近90日标的金额数据
    def create_table_basic_last90_amount(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.table_basic_last90_amount)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "source_type varchar(20) comment '数据源类型',"
                "company_name varchar(100) comment '公司名称',"
                "last_90day_amount_name varchar(100) comment '近90日标的金额名称',"
                "last_90day_amount_data varchar(100) comment '近90日标的金额数据',"
                "url varchar(2000) comment 'url',"
                "date varchar(20) comment '抓取日期date',"
                "PRIMARY KEY (`company_name`,`last_90day_amount_name`,`date`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.table_basic_last90_amount)
        except Exception, e:
            print Exception, e

    # 公司核心和投资偏好数据
    def create_table_preference(self):
        try:
            self.cur.execute('set names \'utf8\'')
            self.cur.execute("drop table if exists %s" % self.table_preference)
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS %s "
                "("
                "source_type varchar(20) comment '数据源类型',"
                "company_name varchar(100) comment '公司名称',"
                "core_index_name varchar(50) comment '核心指标名称',"
                "core_index_data varchar(100) comment '核心指标数据',"
                "index_preference_data varchar(100) comment '投资偏好数据',"
                "url varchar(2000) comment 'url',"
                "date varchar(20) comment '抓取日期date',"
                "PRIMARY KEY (`company_name`,`core_index_name`,`date`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                % self.table_preference)
        except Exception, e:
            print Exception, e

    # def create_table(self):
    #     try:
    #         self.cur.execute('set names \'utf8\'')
    #         self.cur.execute("drop table if exists %s" % self.file_name)
    #         self.cur.execute(
    #             "CREATE TABLE IF NOT EXISTS %s "
    #             "("
    #             "url varchar(20) comment '产品id',"
    #             "x varchar(200) comment '产品名称',"
    #             "y varchar(2000) comment '产品全称',"
    #             "PRIMARY KEY (`url`,`x`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
    #             % self.file_name)
    #     except Exception, e:
    #         print Exception, e


if __name__ == '__main__':
    test = CreateTable()
    test.create_table_archives_invest_loan_daily()
    test.create_table_archives_repayment_inflow_daily()
    test.create_table_archives_interest_volume_daily()
    test.create_table_basic_last90_amount()
    test.create_table_basic_last90_deadline()
    test.create_table_basic_last90_type()
    test.create_table_preference()
    # test.create_table()
