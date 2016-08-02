# -*- coding: utf-8 -*-
import scrapy
import sys
import os
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
reload(sys)
sys.setdefaultencoding('utf-8')
from lxml import etree
from sina_stock_news_us.items import *


class SpiderUrlSpider(scrapy.Spider):
    name = "spider_url"
    allowed_domains = ["spider_url.com"]
    start_urls = (
        'http://biz.finance.sina.com.cn/usstock/usstock_news.php?pageIndex=1&symbol=BIDU&type=1',
    )

    def parse(self, response):
        try:
            item = SinaStockUrlUsItem()
            data_html = response.body_as_unicode()
            root = etree.HTML(data_html)
            nodes = root.xpath('//div[@class="xb_news"]')
            news_url_title_nodes = nodes[0][5].xpath('./li/a')
            news_time_nodes = nodes[0][5].xpath('./li/span')
            news_url_list = []
            news_title_list = []
            news_time_list = []
            for i in range(0, len(news_url_title_nodes)):
                news_url_list.append(news_url_title_nodes[i].attrib['href'])
                news_title_list.append(news_url_title_nodes[i].text)
            for j in range(0, len(news_time_nodes)):  # 所有成员,一个为时间标签,一个不是时间标签
                if news_time_nodes[j].text is not None:  # 为空时,说明不是时间标签
                    news_time_list.append(news_time_nodes[j].text)
            item['news_url'] = news_url_list
            item['news_title'] = news_title_list
            item['news_time'] = news_time_list
            return item
            # print news_url_title_nodes[0].attrib['href']  # url
            # print news_time_nodes[0].text  # time
            # print news_url_title_nodes[0].text  # title

        except Exception, e:
            error_info = Exception, e
            print error_info
