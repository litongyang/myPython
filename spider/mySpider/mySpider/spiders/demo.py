# -*- coding: utf-8 -*-
import sys
# sys.path.append("C:\\Users\\Administrator\\PycharmProjects\\myPython\\spider\\mySpider\\mySpider")
import scrapy
from lxml import etree
from ..items import MyspiderItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['demo.cn']
    start_urls = ['https://www.lexico.com/list/0/2?locale=en']

    def parse(self, response):
        item = MyspiderItem()
        data_html = response.body_as_unicode()
        root = etree.HTML(data_html)
        items = []
        iitems = root.xpath('//*[@id="content"]/div[1]/div[2]/div/div/div/div[2]/ul/li/a/text()')
        print "#################################"
        # print type(iitems)
        item['title']= iitems
        print item['title']
        # for i in iitems:
        #     item['title']= i
        #     items.append(item['title'])
        # print"%%%%%%%%%%%%%%%%%"
        # for i in items:
        #     print i
        # print item['title']
        # yield item
