# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
from spiders.spider_url import SpiderUrlSpider
from spiders.spider_news import SpiderNewsSpider

class HexunStockNewsUsPipeline(object):
    def __init__(self):
        self.news_url = codecs.open('news_url.json', 'w', encoding='utf-8')
        self.news_content = codecs.open('news_content.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(spider, SpiderUrlSpider):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.news_url.write(line)
            return item
        if isinstance(spider, SpiderNewsSpider):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.news_content.write(line)
            return item

    def spider_closed(self):
        self.news_url.close()
        self.news_content.close()
