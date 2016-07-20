# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.utils.project import get_project_settings  # 调用settings.py 文件方法
from scrapy import log
from scrapy.mail import MailSender
from spiders.spider_basic import SpiderBasic
from spiders.spider_preference import SpiderPreference
from spiders.spider_archives import SpiderArchives
import json
import time
import codecs
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi


class JsonWriterPipeline(object):
    def __init__(self):
        self.file_basic = codecs.open('basic.json', 'w', encoding='utf-8')
        self.file_archives = codecs.open('archives.json', 'w', encoding='utf-8')
        self.file_preference = codecs.open('preference.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(spider, SpiderPreference):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file_preference.write(line)
            return item
        if isinstance(spider, SpiderBasic):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file_basic.write(line)
            return item
        if isinstance(spider, SpiderArchives):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file_archives.write(line)
            return item
        else:
            return

    def spider_closed(self):
        self.file_basic.close()
        self.file_archives.close()
        self.file_preference.close()


class WdzjPipelineMysql(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool
        self.time_stamp_tmp = time.time()
        self.time_array = time.localtime(self.time_stamp_tmp)
        self.date = time.strftime("%Y-%m-%d", self.time_array)
        self.mailer = MailSender.from_settings(get_project_settings())

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        try:
            if isinstance(spider, SpiderPreference):
                query = self.dbpool.runInteraction(self._conditional_insert_preference, item)
                query.addErrback(self.handle_error)
                return item
            if isinstance(spider, SpiderBasic):
                query = self.dbpool.runInteraction(self._conditional_insert_basic, item)
                query.addErrback(self.handle_error)
                return item
            if isinstance(spider, SpiderArchives):
                query = self.dbpool.runInteraction(self._conditional_insert_archives, item)
                query.addErrback(self.handle_error)
                return item
        except Exception, e:
            error_info = "process_item: ", Exception, e
            print error_info
            self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-process_item", body=str(error_info), mimetype='text/plain')

    def _conditional_insert_preference(self, cur, item):
        try:
            for i in range(0, len(item['core_index_name'])):
                try:
                    cur.execute("insert into wdzj_preference_info values(%s,%s,%s,%s,%s,%s,%s)"
                                % (
                                    '\'' + str(item['item_type']) + '\'',
                                    '\'' + str(item['company_name']) + '\'',
                                    '\'' + str(item['core_index_name'][i]) + '\'',
                                    '\'' + str(item['core_index_data'][i]) + '\'',
                                    '\'' + str(item['index_preference_data'][i]) + '\'',
                                    '\'' + str(item['url']) + '\'',
                                    '\'' + str(self.date) + '\''
                                )
                    )
                except Exception, e:
                    error_info = "_conditional_insert_preference: ", Exception, e
                    print error_info
                    self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-_conditional_insert_preference", body=str(error_info), mimetype='text/plain')
                    pass
        except Exception, e:
            error_info = "_conditional_insert_preference: ", Exception, e
            print error_info
            self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-_conditional_insert_preference", body=str(error_info), mimetype='text/plain')

    def _conditional_insert_basic(self, cur, item):
        try:
            for i in range(0, len(item['last_90day_type_name'])):
                try:
                    insert_sql = ''
                    insert_sql += '\'' + str(item['item_type']) + '\'' + ','
                    insert_sql += '\'' + str(item['company_name']) + '\'' + ','
                    insert_sql += '\'' + str(item['last_90day_type_name'][i]) + '\'' + ','
                    insert_sql += '\'' + str(item['last_90day_type_data'][i]) + '\'' + ','
                    insert_sql += '\'' + str(item['url']) + '\'' + ','
                    insert_sql += '\'' + str(self.date) + '\'' + ','
                    insert_sql = insert_sql[0:-1]  # 去除最后一个逗号
                    cur.execute("insert into wdzj_basic_info_last90_type values(%s)" % insert_sql)
                except Exception, e:
                    error_info = "_conditional_insert_basic: ", Exception, e
                    print error_info
                    self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-_conditional_insert_basic", body=str(error_info), mimetype='text/plain')
                    pass
            for i in range(0, len(item['last_90day_deadline_name'])):
                try:
                    insert_sql = ''
                    insert_sql += '\'' + str(item['item_type']) + '\'' + ','
                    insert_sql += '\'' + str(item['company_name']) + '\'' + ','
                    insert_sql += '\'' + str(item['last_90day_deadline_name'][i]) + '\'' + ','
                    insert_sql += '\'' + str(item['last_90day_deadline_data'][i]) + '\'' + ','
                    insert_sql += '\'' + str(item['url']) + '\'' + ','
                    insert_sql += '\'' + str(self.date) + '\'' + ','
                    insert_sql = insert_sql[0:-1]  # 去除最后一个逗号
                    cur.execute("insert into wdzj_basic_info_last90_deadline values(%s)" % insert_sql)
                except Exception, e:
                    error_info = "_conditional_insert_basic: ", Exception, e
                    print error_info
                    self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-_conditional_insert_basic", body=str(error_info), mimetype='text/plain')
                    pass
            for i in range(0, len(item['last_90day_amount_name'])):
                try:
                    insert_sql = ''
                    insert_sql += '\'' + str(item['item_type']) + '\'' + ','
                    insert_sql += '\'' + str(item['company_name']) + '\'' + ','
                    insert_sql += '\'' + str(item['last_90day_amount_name'][i]) + '\'' + ','
                    insert_sql += '\'' + str(item['last_90day_amount_data'][i]) + '\'' + ','
                    insert_sql += '\'' + str(item['url']) + '\'' + ','
                    insert_sql += '\'' + str(self.date) + '\'' + ','
                    insert_sql = insert_sql[0:-1]  # 去除最后一个逗号
                    cur.execute("insert into wdzj_basic_info_last90_amount values(%s)" % insert_sql)
                except Exception, e:
                    error_info = "_conditional_insert_basic: ", Exception, e
                    print error_info
                    self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-_conditional_insert_basic", body=str(error_info), mimetype='text/plain')
                    pass
        except Exception, e:
            error_info = "_conditional_insert_basic: ", Exception, e
            print error_info
            self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-_conditional_insert_basic", body=str(error_info), mimetype='text/plain')

    def _conditional_insert_archives(self, cur, item):
        try:
            for i in range(0, len(item['interest_rate_volume_date'])):
                try:
                    insert_sql = ''
                    insert_sql += '\'' + str(item['item_type']) + '\'' + ','
                    insert_sql += '\'' + str(item['company_name']) + '\'' + ','
                    insert_sql += '\'' + str(item['type']) + '\'' + ','
                    insert_sql += '\'' + str(item['status']) + '\'' + ','
                    insert_sql += '\'' + str(item['interest_rate_volume_date'][i]) + '\'' + ','
                    insert_sql += '\'' + str(item['interest_rate_day'][i]) + '\'' + ','
                    insert_sql += '\'' + str(item['volume_day'][i]) + '\'' + ','
                    insert_sql += '\'' + str(item['url']) + '\'' + ','
                    insert_sql += '\'' + str(self.date) + '\'' + ','
                    insert_sql = insert_sql[0:-1]  # 去除最后一个逗号
                    cur.execute("insert into wdzj_archives_interest_volume_daily values(%s)" % insert_sql)
                except Exception, e:
                    error_info = "_conditional_insert_archives: ", Exception, e
                    print error_info
                    self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-_conditional_insert_archives", body=str(error_info), mimetype='text/plain')
                    pass
            for i in range(0, len(item['pending_repayment_inflow_date'])):
                try:
                    insert_sql = ''
                    insert_sql += '\'' + str(item['item_type']) + '\'' + ','
                    insert_sql += '\'' + str(item['company_name']) + '\'' + ','
                    insert_sql += '\'' + str(item['type']) + '\'' + ','
                    insert_sql += '\'' + str(item['status']) + '\'' + ','
                    insert_sql += '\'' + str(item['pending_repayment_inflow_date'][i]) + '\'' + ','
                    insert_sql += '\'' + str(item['pending_repayment_history_day'][i]) + '\'' + ','
                    insert_sql += '\'' + str(item['net_inflow_day'][i]) + '\'' + ','
                    insert_sql += '\'' + str(item['url']) + '\'' + ','
                    insert_sql += '\'' + str(self.date) + '\'' + ','
                    insert_sql = insert_sql[0:-1]  # 去除最后一个逗号
                    cur.execute("insert into wdzj_archives_repayment_inflow_daily values(%s)" % insert_sql)
                except Exception, e:
                    error_info = "_conditional_insert_archives: ", Exception, e
                    print error_info
                    self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-_conditional_insert_archives", body=str(error_info), mimetype='text/plain')
                    pass
            for i in range(0, len(item['invest_loan_user_date'])):
                try:
                    insert_sql = ''
                    insert_sql += '\'' + str(item['item_type']) + '\'' + ','
                    insert_sql += '\'' + str(item['company_name']) + '\'' + ','
                    insert_sql += '\'' + str(item['type']) + '\'' + ','
                    insert_sql += '\'' + str(item['status']) + '\'' + ','
                    insert_sql += '\'' + str(item['invest_loan_user_date'][i]) + '\'' + ','
                    insert_sql += '\'' + str(item['invest_user_day'][i]) + '\'' + ','
                    insert_sql += '\'' + str(item['loan_user_day'][i]) + '\'' + ','
                    insert_sql += '\'' + str(item['url']) + '\'' + ','
                    insert_sql += '\'' + str(self.date) + '\'' + ','
                    insert_sql = insert_sql[0:-1]  # 去除最后一个逗号
                    cur.execute("insert into wdzj_archives_invest_loan_daily values(%s)" % insert_sql)
                except Exception, e:
                    error_info = "_conditional_insert_archives: ", Exception, e
                    print error_info
                    self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-_conditional_insert_archives", body=str(error_info), mimetype='text/plain')
                    pass
        except Exception, e:
            error_info = "_conditional_insert_archives: ", Exception, e
            print error_info
            self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-_conditional_insert_archives", body=str(error_info), mimetype='text/plain')

    @staticmethod
    def handle_error(e):
        log.err(e)
