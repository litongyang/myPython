# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.utils.project import get_project_settings  # 调用settings.py 文件方法
from scrapy import log
from scrapy.mail import MailSender
from spiders.spider_news import SpiderNewsSpider
from spiders.spider_url import SpiderUrlSpider
import json
import codecs


class QqStockNewsUsPipelineJson(object):
    def __init__(self):
        self.file_test = codecs.open('test.json', 'w', encoding='utf-8')
        self.news_url = codecs.open('news_url.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(spider, SpiderNewsSpider):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file_test.write(line)
            return item
        if isinstance(spider, SpiderUrlSpider):
            line = json.dumps(dict(item), ensure_ascii=False, encoding='utf-8') + "\n"
            self.news_url.write(line)
            return item

    def spider_closed(self):
        self.file_test.close()
        self.news_url.close()
