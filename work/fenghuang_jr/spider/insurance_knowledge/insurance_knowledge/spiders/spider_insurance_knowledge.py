# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector


class SpiderInsuranceKnowledgeSpider(scrapy.Spider):
    name = "spider_insurance_knowledge"
    allowed_domains = ["spider_insurance_knowledge.com"]
    start_urls = (
        'http://www.xyz.cn/study/maibaoxian-news-2284046.html',
    )

    def parse(self, response):
        try:
            print response.url
            data_html = response.body_as_unicode()
            sel = Selector(text=data_html, type="html")
            nodes_sel_template = sel.xpath('//div[@id="coreText" and @class="fn-clear"]/p')
            context = ''
            for i in range(0, len(nodes_sel_template)):
                context += nodes_sel_template[i].extract()
            print context  # 保险知识内容
        except Exception, e:
            print Exception, e
