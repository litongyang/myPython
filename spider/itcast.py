# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast']
    start_urls = ['http://itcast/']

    def parse(self, response):
        pass
