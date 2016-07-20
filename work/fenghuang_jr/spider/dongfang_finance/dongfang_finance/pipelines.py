# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.utils.project import get_project_settings  # 调用settings.py 文件方法
from scrapy import log
from scrapy.mail import MailSender
from spiders.spider_notice import SpiderNotice
from spiders.spider_research import SpiderResearch
import json
import time
import codecs
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi


class DongfangFinancePipelineJson(object):
    def __init__(self):
        self.file_notice = codecs.open('notice.json', 'w', encoding='utf-8')
        self.file_research = codecs.open('research.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(spider, SpiderNotice):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file_notice.write(line)
            return item
        if isinstance(spider, SpiderResearch):
            # print type(item)
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file_research.write(line)
            return item

    def spider_closed(self):
        self.file_notice.close()
        self.file_research.close()


class DongfangPipelineMysql(object):
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
            if isinstance(spider, SpiderNotice):
                query = self.dbpool.runInteraction(self._conditional_insert_notice, item)
                query.addErrback(self.handle_error)
                return item
            if isinstance(spider, SpiderResearch):
                query = self.dbpool.runInteraction(self._conditional_insert_research, item)
                query.addErrback(self.handle_error)
                return item

        except Exception, e:
            error_info = "process_item: ", Exception, e
            print error_info
            self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-process_item", body=str(error_info), mimetype='text/plain')

    def _conditional_insert_notice(self, cur, item):
        try:
            for i in range(0, len(item['company_code'])):
                try:
                    cur.execute("insert into dongfang_test values(%s,%s,%s,%s,%s,%s,%s)"
                                % (
                                    '\'' + str(item['company_code'][i]) + '\'',
                                    '\'' + str(item['company_name'][i]) + '\'',
                                    '\'' + str(item['notice_title'][i]) + '\'',
                                    '\'' + str(item['notice_type'][i]) + '\'',
                                    '\'' + str(item['notice_date'][i]) + '\'',
                                    '\'' + str(item['notice_title_link'][i]) + '\'',
                                    '\'' + str(self.date) + '\''
                                )
                    )
                except Exception, e:
                    error_info = "_conditional_insert_archives: ", Exception, e
                    print error_info
                    self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-_conditional_insert_archives", body=str(error_info), mimetype='text/plain')
                    pass
        except Exception, e:
            print Exception, e

    def _conditional_insert_research(self, cur, item):
        try:
            for i in range(0, len(item['company_code'])):
                try:
                    cur.execute("insert into dongfang_research_test values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                % (
                                    '\'' + str(item['company_code'][i]) + '\'',
                                    '\'' + str(item['company_name'][i]) + '\'',
                                    '\'' + str(item['research_title'][i]) + '\'',
                                    '\'' + str(item['research_date'][i]) + '\'',
                                    '\'' + str(item['ins_name'][i]) + '\'',
                                    '\'' + str(item['ins_star'][i]) + '\'',
                                    '\'' + str(item['rating_name'][i]) + '\'',
                                    '\'' + str(item['rating_change'][i]) + '\'',
                                    '\'' + str(item['author'][i]) + '\'',
                                    '\'' + str(item['profit_year'][i]) + '\'',
                                    '\'' + str(item['pe_list'][i]) + '\'',
                                    '\'' + str(item['per_share_list'][i]) + '\'',
                                    '\'' + str(item['net_profit_list'][i]) + '\'',
                                    '\'' + str(item['research_url'][i]) + '\'',
                                    '\'' + str(self.date) + '\''
                                )
                    )
                except Exception, e:
                    error_info = "_conditional_insert_archives: ", Exception, e
                    print error_info
                    self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-_conditional_insert_archives", body=str(error_info), mimetype='text/plain')
                    pass
        except Exception, e:
            print Exception, e

    @staticmethod
    def handle_error(e):
        log.err(e)
