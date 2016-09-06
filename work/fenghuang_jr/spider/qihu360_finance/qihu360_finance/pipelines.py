# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from spiders.spider_url import SpiderUrlSpider
from spiders.spider_detail import SpiderDetailSpider


class Qihu360FinancePipeline(object):
    def __init__(self):
        self.file_url = codecs.open('360_url.json', 'w', encoding='utf-8')
        self.file_detail = codecs.open('detail.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(spider, SpiderUrlSpider):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file_url.write(line)
            return item

        if isinstance(spider, SpiderDetailSpider):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file_detail.write(line)
            return item
