# -*- coding: utf-8 -*-
import scrapy
import sys
import os
import time
import redis
import get_company_dict
from scrapy import Selector

parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
reload(sys)
sys.setdefaultencoding('utf-8')
from lxml import etree
from wangyi_stock_news_us.items import *
from get_url import *


class SpiderNewsSpider(scrapy.Spider):
    def __init__(self):
        self.time_stamp_tmp = time.time()
        self.time_array = time.localtime(self.time_stamp_tmp)
        self.time_satmp = time.strftime("%Y-%m-%d %H:%M:%S", self.time_array)

    name = "spider_news"
    allowed_domains = ["spider_news.com"]
    start_urls = [
        # 'http://money.163.com/16/0809/15/BU1M77D500254TI5.html',
        'http://money.163.com/12/0306/21/7RUN6QDD00254Q6L.html'
    ]
    # start_urls = GetUrl().get_news_url()

    def parse(self, response):
        # global nodes_source, time_nodes, nodes_sel
        try:
            item = WangyiStockNewsUsItem()
            html = response.body_as_unicode()
            root = etree.HTML(html)
            """ 新闻url """
            new_url = response._url
            print "=============="
            print new_url
            """ 新闻标题 """
            nodes_title = root.xpath('//h1')
            news_title = nodes_title[0].text
            print news_title
            """ 新闻来源 """
            source_template1 = root.xpath('//div[@class="post_time_source"]/a')
            source_template2 = root.xpath('//div[@class="left"]/a')
            source_template3 = root.xpath('//span[@class="info" and @style="display:block;"]/a')
            if len(source_template1) > 0:
                nodes_source = source_template1
            elif len(source_template2) > 0:
                nodes_source = source_template2
            elif len(source_template3) > 0:
                nodes_source = source_template3
            # nodes_source = root.xpath('//div[@class="post_time_source"]/a')
            source_name = nodes_source[0].text
            print source_name
            """ 新闻创建时间 """
            time_template1 = root.xpath('//div[@class="post_time_source"]')
            time_template2 = root.xpath('//span[@class="info" and @style="display:block;"]')
            if len(time_template1) > 0:
                time_nodes = time_template1
            elif len(time_template2) > 0:
                time_nodes = time_template2
            # time_nodes = root.xpath('//div[@class="post_time_source"]')
            news_time = time_nodes[0].text.replace('来源:', '').replace('\n', '')
            print news_time
            """ 新闻内容的html """
            sel = Selector(text=html, type="html")
            nodes_sel_template1 = sel.xpath('//div[@class="post_body"]/div/p')
            nodes_sel_template2 = sel.xpath('//div[@id="endText"]/p')
            if len(nodes_sel_template1) > 0:
                nodes_sel = nodes_sel_template1
            if len(nodes_sel_template2) > 0:
                nodes_sel = nodes_sel_template2
            context = nodes_sel.extract()  # 获取新闻内容的整段html:list结构
            content_html = ''  # 将新闻html拼接成整段html
            for i in range(0, len(context)):
                content_html += str(context[i])
            print content_html
            item['company_code'] = ''
            item['company_code_other'] = ''
            item['company_name'] = ''
            item['issue_time'] = ''
            item['source_name'] = source_name
            item['news_time'] = news_time
            item['author'] = ''
            item['news_title'] = news_title
            item['abstract'] = ''
            item['content_html'] = str(content_html)
            item['news_url'] = str(new_url)
            item['crawl_time'] = str(self.time_satmp)
            return item
        except Exception, e:
            error_info = Exception, e
            print error_info
