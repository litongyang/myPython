# -*- coding: utf-8 -*-
import scrapy
import sys
import os
from lxml import etree
import redis
from wangyi_finance.items import *
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
reload(sys)
sys.setdefaultencoding('utf-8')


class WangyiFinanceSpiderDetailSpider(scrapy.Spider):
    name = "wangyi_finance_spider_detail"
    allowed_domains = ["wangyi_finance_spider_detail.com"]
    start_urls = [
        'https://8.163.com/dqlcProductDetail.htm?productId=2016081711DQ197990819',
    ]

    def parse(self, response):
        try:
            item = WangyiFinanceDetailItem()
            data_html = response.body_as_unicode()
            root = etree.HTML(data_html)
            """ 收益率和期限节点 """
            ratio_days_nodes = root.xpath('//div[@class="p2p-params p2p-detail-params f-clr"]/div/p')
            """ 募集状态节点 """
            status_nodes = root.xpath('//h2')
            """ 产品详情节点 """
            detail_nodes = root.xpath('//table[@class="pro-detail-table"]/tbody/tr/td')
            print ratio_days_nodes[0].text
            print ratio_days_nodes[1].text
            print status_nodes[0].text
            print len(ratio_days_nodes)
            for i in range(0, len(detail_nodes)):
                print detail_nodes[i].text
        except Exception, e:
            error_info = Exception, e
            print error_info

