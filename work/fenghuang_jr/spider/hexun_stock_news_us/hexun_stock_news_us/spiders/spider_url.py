# -*- coding: utf-8 -*-
import scrapy
import sys
import os
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
reload(sys)
sys.setdefaultencoding('utf-8')
from lxml import etree
from hexun_stock_news_us.items import *
import random
from scrapy.http import Request,FormRequest


class SpiderUrlSpider(scrapy.Spider):

    name = "spider_url"
    allowed_domains = ["spider_url.com"]
    # start_urls = ['http://stockdata.stock.hexun.com/us/Nlist.aspx?code=JD&p=2']
    start_urls = ['http://stockdata.stock.hexun.com/us/news/CXDC.shtml']

    def parse(self, response):
        try:
            item = HexunStockNewsUsItem()
            data_html = response.body_as_unicode()

            root = etree.HTML(data_html)
            nodes = root.xpath('//ul[@class="news-list"]/li/a')
            print nodes[0].text
            print nodes[0].attrib['href']
            return item
        except Exception, e:
            error_info = Exception, e
            print error_info
