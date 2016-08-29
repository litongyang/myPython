# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import codecs
import json
from spiders.spider_detail import SpiderUrlSpider


class JdFinancePipeline(object):
    def __init__(self):
        self.detail = codecs.open('detail.json', 'w', encoding='utf-8')
        self.time_stamp_tmp = time.time()
        self.time_array = time.localtime(self.time_stamp_tmp)
        self.date = time.strftime("%Y-%m-%d", self.time_array)

    def process_item(self, item, spider):
        if isinstance(spider, SpiderUrlSpider):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.detail.write(line)
            return item

    def spider_closed(self):
        self.detail.close()
