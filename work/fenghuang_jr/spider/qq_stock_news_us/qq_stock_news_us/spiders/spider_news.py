# -*- coding: utf-8 -*-
import scrapy
import sys
import os
import re
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
reload(sys)
sys.setdefaultencoding('utf-8')
import get_url as get_url_class
from scrapy import Selector
from scrapy.spiders import BaseSpider
from scrapy.utils.project import get_project_settings  # 调用settings.py 文件方法
from scrapy.mail import MailSender
from lxml import etree
from qq_stock_news_us.items import *


class SpiderNewsSpider(scrapy.Spider):
    name = "spider_news"
    allowed_domains = ["spider_news.com"]
    # start_urls = ["http://finance.qq.com/a/20160719/008840.htm?stockcode=usSOHU&version=1#highlight=%E6%90%9C%E7%8B%90"]
    # start_urls = ["http://finance.qq.com/a/20160714/040261.htm#highlight=京东"]
    # start_urls = ["http://tech.qq.com/a/20160720/042094.htm#highlight=京东"]
    start_urls = get_url_class.GetUrl().get_news_url()

    def parse(self, response):
        try:
            item = QqStockNewsUsItem()
            html = response.body_as_unicode()
            root = etree.HTML(html)
            """ 新闻url """
            new_url = response._url
            news_time_url_dict = get_url_class.GetUrl().get_news_time_url_dict()
            # get_url.get_news_url()
            for url, time in news_time_url_dict.items():
                if str(new_url) in str(url):
                    print url
                    regex_cnt = ur"us(.*?)&"
                    reobj_cnt = re.compile(regex_cnt)
                    match_cnt = reobj_cnt.search(url)
                    company_code = ''
                    if match_cnt:
                        subject_cnt = match_cnt.group(0)
                        subject_cnt = subject_cnt.replace('us', '')
                        company_code = subject_cnt.replace('&', '')
                    # if new_url == str('http://stock.qq.com/a/20160707/007248.htm'):
                    """ 新闻标题 """
                    nodes_title = root.xpath('//h1')
                    new_title = nodes_title[0].text
                    print new_title

                    """ 新闻来源 """
                    source_template1 = root.xpath('//span[@class="where color-a-1" and @bosszone="jgname"]')
                    source_template1_1 = root.xpath('//span[@class="where color-a-1" and @bosszone="jgname"]/a')
                    source_template2 = root.xpath('//span[@class="where" and @bosszone="jgname"]')
                    source_template2_1 = root.xpath('//span[@class="where" and @bosszone="jgname"]/a')
                    source_template3 = root.xpath('//span[@class="a_source" and @bosszone="jgname"]')
                    source_template3_1 = root.xpath('//span[@class="a_source" and @bosszone="jgname"]/a')
                    source_template4 = root.xpath('//span[@class="where"]')
                    source_template4_1 = root.xpath('//span[@class="where"]/a')
                    if len(source_template1) != 0:
                        if len(source_template1_1) != 0:
                            nodes_source = source_template1_1
                        else:
                            nodes_source = source_template1
                    elif len(source_template2) != 0:
                        if len(source_template2_1) != 0:
                            nodes_source = source_template2_1
                        else:
                            nodes_source = source_template2
                    elif len(source_template3) != 0:
                        if len(source_template3_1) != 0:
                            nodes_source = source_template3_1
                        else:
                            nodes_source = source_template3
                    else:
                        if len(source_template4_1) != 0:
                            nodes_source = source_template3_1
                        else:
                            nodes_source = source_template4

                    #     nodes_source = source_template5
                    source_name = str(nodes_source[0].text)
                    print source_name

                    """ 新闻创建时间 """
                    time_template1 = root.xpath('//span[@class="pubTime article-time"]')
                    time_template2 = root.xpath('//span[@class="pubTime"]')
                    time_template3 = root.xpath('//span[@class="a_time"]')
                    if len(time_template1) != 0:
                        nodes_time = time_template1
                    elif len(time_template2) != 0:
                        nodes_time = time_template2
                    else:
                        nodes_time = time_template3
                    # nodes_time = root.xpath('//span[@class="pubTime article-time"]')
                    news_time = str(nodes_time[0].text)
                    print news_time

                    """ 新闻内容的html """
                    sel = Selector(text=html, type="html")
                    nodes_sel = sel.xpath("//p[@style='TEXT-INDENT: 2em']")
                    context = nodes_sel.extract()  # 获取新闻内容的整段html:list结构
                    content_html = ''  # 将新闻html拼接成整段html
                    for i in range(0, len(context)):
                        content_html += str(context[i])
                    item['company_code'] = company_code
                    item['issue_time'] = time
                    item['source_name'] = source_name
                    item['news_time'] = news_time
                    item['news_title'] = new_title
                    item['content_html'] = str(content_html)
                    item['news_url'] = str(new_url)
                    yield item
        except Exception, e:
            error_info = Exception, e
            print error_info
