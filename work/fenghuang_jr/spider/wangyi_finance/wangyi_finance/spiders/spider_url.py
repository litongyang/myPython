# -*- coding: utf-8 -*-
import scrapy
import sys
import re
import os
from lxml import etree
import redis
from wangyi_finance.items import *
sys.setdefaultencoding('utf-8')


class SpiderUrlSpider(scrapy.Spider):
    name = "wangyi_finacne_spider_url"
    allowed_domains = ["spider_url.com"]
    start_urls = [
        'https://8.163.com/dqlc/dqlcList.htm?lowestInvest=&productLimit=&productRateSort=&productDaysSort=&curpage=1#dqlc-list',
        ]

    def parse(self, response):
        try:
            item = WangyiFinanceUrlItem()
            data_html = response.body_as_unicode()
            root = etree.HTML(data_html)
            # product_nodes = root.xpath('//ul[@id="J-productLst" and class ="list"]')
            url_title_nodes = root.xpath('//div[@class="p2p-list"]/ul/li/h2/a')
            print url_title_nodes[0].text
            print 'https://8.163.com/' + url_title_nodes[0].attrib['href']
            print len(url_title_nodes)

        except Exception, e:
            error_info = Exception, e
            print error_info
