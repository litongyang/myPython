# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import redis
from qihu360_finance.items import *



class SpiderUrlSpider(scrapy.Spider):
    name = "qihu360_finacne_spider_url"
    allowed_domains = ["spider_url.com"]
    start_urls = [
        'https://www.nicaifu.com/dq',
    ]

    def parse(self, response):
        try:
            item = Qihu360FinanceUrlItem()
            data_html = response.body_as_unicode()
            root = etree.HTML(data_html)
            name_noeds = root.xpath('//td[@colspan="4"]/div/div/span')  # 产品名称node
            # transfer_info_noeds = root.xpath('//td[@colspan="4"]/div/div/i')  # 转让信息node
            url_status_noeds = root.xpath('//div[@class="listTop"]/a')  # 产品状态node
            print 'https://www.nicaifu.com' + url_status_noeds[0].attrib['href']
            print url_status_noeds[0].text
            print name_noeds[0].text
            for i in range(0, len(url_status_noeds)):
                item['url'] = 'https://www.nicaifu.com' + url_status_noeds[i].attrib['href']
                item['status'] = url_status_noeds[i].text
                yield item
        except Exception, e:
            error_info = Exception, e
            print error_info
