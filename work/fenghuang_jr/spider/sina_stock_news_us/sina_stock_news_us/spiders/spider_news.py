# -*- coding: utf-8 -*-
import scrapy
import scrapy
import sys
import os
import time
from get_url import *

parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
reload(sys)
sys.setdefaultencoding('utf-8')
from lxml import etree
from scrapy import Selector
from sina_stock_news_us.items import *


class SpiderNewsSpider(scrapy.Spider):
    def __init__(self):
        self.time_stamp_tmp = time.time()
        self.time_array = time.localtime(self.time_stamp_tmp)
        self.time_satmp = time.strftime("%Y-%m-%d %H:%M:%S", self.time_array)
    name = "spider_news"
    allowed_domains = ["spider_news.com"]
    start_urls = [
                    # 'http://tech.sina.com.cn/i/2016-07-29/doc-ifxunyxy6002895.shtml',
                    # 'http://finance.sina.com.cn/stock/s/2016-06-20/doc-ifxtfrrf0653412.shtml',
                    # 'http://finance.sina.com.cn/stock/hkstock/ggscyd/2016-08-08/doc-ifxutfpc4736724.shtml',
                    # 'http://finance.sina.com.cn/world/20131202/154217501832.shtml',
                    'http://finance.yahoo.com/news/ehi-car-services-report-first-120000802.html'
                  ]
    # start_urls = GetUrl().get_news_url()

    def parse(self, response):
        # global nodes_source, nodes_time, nodes_sel
        try:
            item = SinaStockNewsUsItem()
            data_html = response.body_as_unicode()
            root = etree.HTML(data_html)
            company_code = ''  # 公司代码
            company_name = ''  # 公司名称
            source_name = ''  # 新闻来源
            news_time = ''  # 新闻创建时间
            """ 新闻url """
            new_url = response._url
            """ 新闻标题 """
            nodes_title = root.xpath('//h1')
            if nodes_title[0].text is not None:
                news_title = nodes_title[0].text
            else:
                news_title = nodes_title[1].text
            print news_title
            """ 新闻来源 """
            source_template1 = root.xpath('//span[@id="media_name" and @class=""]/a')
            source_template2 = root.xpath('//span[@data-sudaclick="media_name"]/a')
            source_template3 = root.xpath('//span[@id="media_name"]/a')
            source_template4 = root.xpath('//span[@class="time-source"]')
            source_template5 = root.xpath('//span[@id="media_name"]')
            if len(source_template1) != 0:
                nodes_source = source_template1
            elif len(source_template2) != 0:
                nodes_source = source_template2
            elif len(source_template3) != 0:
                nodes_source = source_template3
            elif len(source_template4) != 0:
                nodes_source = source_template4
            elif len(source_template5) != 0:
                nodes_source = source_template5
            source_name = nodes_source[0].text
            print source_name
            """ 新闻创建时间 """
            time_template1 = root.xpath('//span[@class="titer"]')
            time_template2 = root.xpath('//span[@class="time-source"]')
            time_template3 = root.xpath('//span[@id="pub_date"]')
            if len(time_template1) != 0:
                nodes_time = time_template1
            elif len(time_template2) != 0:
                nodes_time = time_template2
            elif len(time_template3) != 0:
                nodes_time = time_template3
            news_time = nodes_time[0].text
            print news_time
            print "*************"
            """ 新闻内容 """
            sel = Selector(text=data_html, type="html")
            nodes_sel_template1 = sel.xpath('//div[@id="artibody" and @class="content" and @data-sudaclick="blk_content"]/p')
            nodes_sel_template2 = sel.xpath('//div[@id="artibody" and @class="article article_16"]/p')
            nodes_sel_template3 = sel.xpath('//div[@class="blkContainerSblk"]/div/p')
            if len(nodes_sel_template1) > 0:
                nodes_sel = nodes_sel_template1
            elif len(nodes_sel_template2) > 0:
                nodes_sel = nodes_sel_template2
            elif len(nodes_sel_template3) > 0:
                nodes_sel = nodes_sel_template3
            context = nodes_sel.extract()  # 获取新闻内容的整段html:list结构
            content_html = ''  # 将新闻html拼接成整段html
            for i in range(0, len(context)):
                start_index = context[i].find('<span')
                if start_index >= 0:  # 存在这个样式,会导致后面的文字全部是链接状态,所以删除
                    start_index += len('<span')
                    end_index = context[i].index('</span>')
                    del_str = '<span' + context[i][start_index:end_index] + '</span>'
                    content_html += context[i].replace(del_str, '')
                else:  # 不存在<span>样式
                    content_html += context[i]
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
            """ 过滤新浪从yahoo和capitalcube爬取的新闻url """
            if str(response.url).find('yahoo') > 0 or str(response.url).find('capitalcube') > 0:
                pass
            else:
                print "==========="
                print response.url
                error_info = Exception, e
                print error_info
                print "==========="
