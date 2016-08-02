# -*- coding: utf-8 -*-
import scrapy
import scrapy
import sys
import os

parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
reload(sys)
sys.setdefaultencoding('utf-8')
from lxml import etree
from scrapy import Selector
from sina_stock_news_us.items import *


class SpiderNewsSpider(scrapy.Spider):
    name = "spider_news"
    allowed_domains = ["spider_news.com"]
    start_urls = ['http://tech.sina.com.cn/i/2016-07-29/doc-ifxunyxy6002895.shtml']

    def parse(self, response):
        try:
            item = SinaStockNewsUsItem()
            data_html = response.body_as_unicode()
            sel = Selector(text=data_html, type="html")
            nodes_sel = sel.xpath("//p[@class='p1']")
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
            item['news_html'] = content_html
            return item
        except Exception, e:
            error_info = Exception, e
            print error_info
