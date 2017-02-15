# -*- coding: utf-8 -*-
import scrapy
from get_url import *
from lxml import etree


class SpiderInsuranceUrlSpider(scrapy.Spider):
    name = "spider_insurance_url"
    allowed_domains = ["spider_insurance_knowledge.com"]
    # start_urls = (
    #     'http://www.xyz.cn/study/list-76-1.html',
    # )
    start_urls = GetUrl().get_url()

    def parse(self, response):
        try:
            print response.url   # 保险列表页url
            data_html = response.body_as_unicode()
            root = etree.HTML(data_html)
            nodes_url = root.xpath('//div[@class="news-list-cont"]/dl/dt/a')
            for i in range(0, len(nodes_url)):
                print "http://www.xyz.cn" + nodes_url[i].attrib['href']  # 保险详情页url
                print nodes_url[i].text  # 保险知识标题
                print "============="
        except Exception, e:
            print Exception, e
