# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import time
from scrapy import log
import codecs
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi
from spiders.spider_detail import SpiderDetailSpider


class GuomeiFinancePipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool
        self.detail = codecs.open('detail.json', 'w', encoding='utf-8')
        self.time_stamp_tmp = time.time()
        self.time_array = time.localtime(self.time_stamp_tmp)
        self.date = time.strftime("%Y-%m-%d", self.time_array)

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
        # if isinstance(spider, SpiderDetailSpider):
        #     line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #     self.detail.write(line)
        #     return item
        try:
            if isinstance(spider, SpiderDetailSpider):
                # query = self.dbpool.runInteraction(self._conditional_insert_guomei_bid_info, item)
                # query.addErrback(self.handle_error)
                return item

        except Exception, e:
            error_info = "process_item: ", Exception, e
            print error_info

    def _conditional_insert_guomei_bid_info(self, cur, item):
        try:
            insert_sql = ''
            insert_sql += '\'' + str(item['id']) + '\'' + ','
            insert_sql += '\'' + str(item['title']) + '\'' + ','
            insert_sql += '\'' + str(item['repay_method']) + '\'' + ','
            insert_sql += '\'' + str(item['amount']) + '\'' + ','
            insert_sql += '\'' + str(item['rate']) + '\'' + ','
            insert_sql += '\'' + str(item['days']) + '\'' + ','
            insert_sql += '\'' + str(item['min_amount']) + '\'' + ','
            insert_sql += '\'' + str(item['max_amount']) + '\'' + ','
            insert_sql += '\'' + str(item['step_amount']) + '\'' + ','
            insert_sql += '\'' + str(item['time_open']) + '\'' + ','
            insert_sql += '\'' + str(item['date_open']) + '\'' + ','
            insert_sql += '\'' + str(item['time_finished']) + '\'' + ','
            insert_sql += '\'' + str(item['bid_number']) + '\'' + ','
            insert_sql += '\'' + str(item['invest_amount']) + '\'' + ','
            insert_sql += '\'' + str(item['status']) + '\'' + ','
            insert_sql += '\'' + str(item['invest_percent']) + '\'' + ','
            insert_sql += '\'' + str(item['available']) + '\'' + ','
            insert_sql += '\'' + str(self.date) + '\'' + ','
            insert_sql = insert_sql[0:-1]  # 去除最后一个逗号
            # print insert_sql
            cur.execute("insert into guomei_bid_info values(%s)" % insert_sql)
        except Exception, e:
            error_info = "_conditional_insert_archives: ", Exception, e
            print error_info

    @staticmethod
    def handle_error(e):
        log.err(e)
