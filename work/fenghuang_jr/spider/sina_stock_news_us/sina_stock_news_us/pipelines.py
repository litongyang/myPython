# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from spiders.spider_url import SpiderUrlSpider
from spiders.spider_news import SpiderNewsSpider
import codecs
import json


class SinaStockNewsUsPipelineJson(object):
    def __init__(self):
        self.file_url = codecs.open('url.json', 'w', encoding='utf-8')
        self.file_news = codecs.open('news.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(spider, SpiderUrlSpider):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file_url.write(line)
            return item
        if isinstance(spider, SpiderNewsSpider):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file_news.write(line)
            return item

    def spider_closed(self):
        self.file_url.close()
        self.file_news.close()
