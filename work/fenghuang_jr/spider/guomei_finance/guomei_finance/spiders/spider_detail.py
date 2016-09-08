# -*- coding: utf-8 -*-
import scrapy
from lxml import etree


class SpiderDetailSpider(scrapy.Spider):
    name = "spider_detail"
    allowed_domains = ["spider_detail.com"]
    start_urls = (
        'https://www.gomefinance.com.cn/loan/75BB4E5F-D4DF-4ED2-98F2-FA5E8807B815',
    )

    def parse(self, response):
        try:
            data_html = response.body_as_unicode()
            root = etree.HTML(data_html)

            x = root.xpath('//*[@id="pro_detail"]/div/div[4]/text()')
            y = x[0].split('公司')
            z = y[0] + '公司'
            print z
        except Exception, e:
            error_info = Exception, e
            print error_info
