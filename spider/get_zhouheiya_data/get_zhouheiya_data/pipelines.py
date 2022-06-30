# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import codecs
import json
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from spiders.spider_store_list import SpiderGetStoreList
from spiders.spider_area_dict import SpiderAreaDictSpider


class GetZhouheiyaDataPipeline(object):
    def __init__(self, dbpool):
        self.file_notice = codecs.open('html.json', 'w', encoding='utf-8')
        self.dbpool = dbpool

    def process_item(self, item, spider):
        if isinstance(spider, SpiderGetStoreList):
            query = self.dbpool.runInteraction(self._conditional_insert_zhouheiya_store_info, item)
            query.addErrback(self.handle_error)
            return item
        if isinstance(spider, SpiderAreaDictSpider):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file_notice.write(line)
            query = self.dbpool.runInteraction(self._conditional_insert_zhouheiya_dict_info, item)
            query.addErrback(self.handle_error)
            return item

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

    def _conditional_insert_zhouheiya_store_info(self, cur, item):
        try:
            insert_sql = ''
            insert_sql += '\'' + str(item['id']) + '\'' + ','
            insert_sql += '\'' + str(item['name']) + '\'' + ','
            insert_sql += '\'' + str(item['address']) + '\'' + ','
            insert_sql += '\'' + str(item['latitude']) + '\'' + ','
            insert_sql += '\'' + str(item['longitude']) + '\'' + ','
            insert_sql += '\'' + str(item['address_id']) + '\'' + ','
            insert_sql = insert_sql[0:-1]  # 去除最后一个逗号
            cur.execute("insert into zhouheiya values(%s)" % insert_sql)
        except Exception, e:
            error_info = "_conditional_insert_archives: ", Exception, e
            print error_info

    def _conditional_insert_zhouheiya_dict_info(self, cur, item):
        try:
            insert_sql = item['content']
            cur.execute("insert into zhouheiya_area_dict values(%s)" % insert_sql)
        except Exception, e:
            error_info = "_conditional_insert_archives: ", Exception, e
            print error_info

    @staticmethod
    def handle_error(e):
        pass

