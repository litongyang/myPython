# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
证券之星-股票知识列表页抓取
"""
import scrapy
import sys
from lxml import etree
from stock_star.items import *
import stock_classified_dict
# sys.setdefaultencoding('utf-8')


class SpiderStockUrl(scrapy.Spider):
    name = "stock_url"
    allowed_domains = ["stock_knowledge.com"]
    start_urls = (
        "http://school.stockstar.com/list/4067.shtml",
        "http://school.stockstar.com/list/4073.shtml",
        "http://school.stockstar.com/list/2329.shtml",
        "http://school.stockstar.com/list/4091.shtml",
        "http://school.stockstar.com/list/4093.shtml",
        "http://school.stockstar.com/list/4095.shtml",
        "http://school.stockstar.com/list/4097.shtml",
        "http://school.stockstar.com/list/4127.shtml",
        "http://school.stockstar.com/list/4183.shtml",
        "http://school.stockstar.com/list/4175.shtml",
        "http://school.stockstar.com/list/4131.shtml",
        "http://school.stockstar.com/list/4171.shtml",
        "http://school.stockstar.com/list/4169.shtml",
        "http://school.stockstar.com/list/4173.shtml",
        "http://school.stockstar.com/list/4179.shtml",
        "http://school.stockstar.com/list/1205.shtml",
        "http://school.stockstar.com/list/1213.shtml",
        "http://school.stockstar.com/list/1209.shtml"
    )

    def parse(self, response):
        try:
            # item = StockStarStockUrlItem()
            print response.url  # 股票知识分类列表url
            for k, v in stock_classified_dict.stock_classified_dict.items():
                if response.url == k:
                    print v  # 股票知识分类
            data_html = response.body_as_unicode()
            root = etree.HTML(data_html)
            x = root.xpath('//div[@id="listPageContent"]/div/a[2]')
            for i in range(0, len(x)):
                print 'http://school.stockstar.com' + x[i].attrib['href']  # 知识详情的url
            print "=========="
        except Exception, e:
            print Exception, e