# -*- coding: utf-8 -*-
import scrapy
import scrapy
import sys
import os
import time
from get_url import *
from scrapy import Selector
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
reload(sys)
sys.setdefaultencoding('utf-8')
from lxml import etree
from hexun_stock_news_us.items import *


class SpiderNewsSpider(scrapy.Spider):
    def __init__(self):
        self.time_stamp_tmp = time.time()
        self.time_array = time.localtime(self.time_stamp_tmp)
        self.time_satmp = time.strftime("%Y-%m-%d %H:%M:%S", self.time_array)
    name = "spider_news"
    allowed_domains = ["spider_news.com"]
    # start_urls = ['http://news.hexun.com/2016-08-09/185412895.html',
    #               'http://bschool.hexun.com/2016-08-09/185410268.html'
    #               ]
    start_urls = ['http://stock.hexun.com/2015-08-19/178456338.html']
    # start_urls = GetUrl().get_news_url()

    def parse(self, response):
        try:
            item = HexunStockNewsUsItem()
            html = response.body_as_unicode()
            root = etree.HTML(html)
            """ 新闻url """
            new_url = response._url
            """ 新闻标题 """
            nodes_title = root.xpath('//h1')
            news_title = nodes_title[0].text
            print news_title
            """ 新闻来源 """
            source_template1 = root.xpath('//div[@class="tip fl"]/a')
            source_template2 = root.xpath('//span[@id="source_baidu" and @class="gray"]/a')
            source_template3 = root.xpath('//span[@id="artibodyDesc"]/a')
            source_template4 = root.xpath('//span[@class="blue"]/a')  # 来源是图片
            source_template5 = root.xpath('//div[@class="tip fl"]')
            source_template6 = root.xpath('//span[@id="source_baidu" and @class="gray"]')
            source_template7 = root.xpath('//span[@id="artibodyDesc"]')
            source_template8 = root.xpath('//div[@id="artInfo" and @class="from"]/span/a')
            if len(source_template1) > 0:
                nodes_source = source_template1
            elif len(source_template2) > 0:
                nodes_source = source_template2
            elif len(source_template3) > 0:
                nodes_source = source_template3
            elif len(source_template4) > 0:
                nodes_source = source_template4
            elif len(source_template5) > 0:
                nodes_source = source_template5
            elif len(source_template6) > 0:
                nodes_source = source_template6
            elif len(source_template7) > 0:
                nodes_source = source_template7
            elif len(source_template8) > 0:
                nodes_source = source_template8
            source_name = nodes_source[0].text
            print source_name
            """ 新闻创建时间 """
            time_template1 = root.xpath('//div[@class="tip fl"]/span')
            time_template2 = root.xpath('//span[@id="pubtime_baidu" and @class="gray"]')
            time_template3 = root.xpath('//span[@class="gray"]')
            time_template4 = root.xpath('//div[@id="artInfo" and @class="from"]/span')
            if len(time_template1) > 0:
                nodes_time = time_template1
            elif len(time_template2) > 0:
                nodes_time = time_template2
            elif len(time_template3) > 0:
                nodes_time = time_template3
            elif len(time_template4) > 0:
                nodes_time = time_template4
            news_time = nodes_time[0].text
            print news_time
            """ 新闻内容的html """
            sel = Selector(text=html, type="html")
            nodes_sel_template1 = sel.xpath('//div[@id="artibody" and @class="art_context"]/p')
            nodes_sel_template2 = sel.xpath('//div[@class="art_context"]/div/p')
            nodes_sel_template3 = sel.xpath('//div[@id="artibody" and @class="concent"]/p')
            nodes_sel_template4 = sel.xpath('//div[@id="artibody" and @class="art_context"]')
            nodes_sel_template5 = sel.xpath('//div[@class="art_context"]/div/div/p')
            nodes_sel_template6 = sel.xpath('//div[@class="art_context"]/div')
            nodes_sel_template7 = sel.xpath('//div[@id="artibody" and @class="concent"]')
            nodes_sel_template8 = sel.xpath('//div[@class="text_panel"]/p')
            nodes_sel_template9 = sel.xpath('//div[@id="artibody" and @class="txtcont"]/p')
            if len(nodes_sel_template1) > 0:
                nodes_sel = nodes_sel_template1
            elif len(nodes_sel_template2) > 0:
                nodes_sel = nodes_sel_template2
            elif len(nodes_sel_template3) > 0:
                nodes_sel = nodes_sel_template3
            elif len(nodes_sel_template4) > 0:
                nodes_sel = nodes_sel_template4
            elif len(nodes_sel_template5) > 0:
                nodes_sel = nodes_sel_template5
            elif len(nodes_sel_template6) > 0:
                nodes_sel = nodes_sel_template6
            elif len(nodes_sel_template7) > 0:
                nodes_sel = nodes_sel_template7
            elif len(nodes_sel_template8) > 0:
                nodes_sel = nodes_sel_template8
            elif len(nodes_sel_template9) > 0:
                nodes_sel = nodes_sel_template9
            context = nodes_sel.extract()  # 获取新闻内容的整段html:list结构
            content_html = ''  # 将新闻html拼接成整段html
            for i in range(0, len(context)):
                content_html += str(context[i])
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
            if response.url.find('baidu') > 0 or response.url.find('error') > 0:
                pass
            else:
                error_file = open('error.txt', 'aw')
                print "==========="
                print response.url
                error_info = response.url, Exception, e
                print error_info
                error_file.write(str(error_info))
                error_file.write('\n')
