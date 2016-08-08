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
from wangyi_stock_news_us.items import *


class SpiderUrlSpider(scrapy.Spider):
    name = "spider_url"
    allowed_domains = ["spider_url.com"]
    start_urls = ['http://quotes.money.163.com/usstock/JD_news.html?page=0']

    def parse(self, response):
        try:
            print "sdasdadsadasdas"
            item = WangyiStockNewsUsItem()
            data_html = response.body_as_unicode()
            print data_html
            root = etree.HTML(data_html)
            nodes = root.xpath('//div[@class="news_pills"]/dl/dt/a')
            time_nodes = root.xpath('//div[@class="time icon_news_pills_time"]/span')
            print nodes[0].text
            print nodes[0].attrib['href']
            print time_nodes[0].text
        except Exception, e:
            error_info = Exception, e
            print error_info
