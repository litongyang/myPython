# -*- coding: utf-8 -*-
"""
证券之星-股票知识详情页抓取
"""
import scrapy
from scrapy import Selector
from stock_star.items import *


class SpiderStockKnowledgeSpider(scrapy.Spider):
    name = "stock_knowledge"
    allowed_domains = ["stock_knowledge.com"]
    start_urls = (
        'http://school.stockstar.com/SS2016022200001938.shtml',
        'http://school.stockstar.com/SS2008062630134703.shtml',
        'http://school.stockstar.com/SS2016021800002149.shtml',
    )

    def parse(self, response):
        try:
            # print response.url  # 股票知识的url
            data_html = response.body_as_unicode()
            sel = Selector(text=data_html, type="html")
            #  知识模板
            nodes_sel_template = sel.xpath('//div[@class="viewInfo" and @style="overflow:hidden"]/p')
            context = ''
            for i in range(0, len(nodes_sel_template)):
                context += nodes_sel_template[i].extract()
            print context  # 股票知识内容
        except Exception, e:
            print Exception, e
