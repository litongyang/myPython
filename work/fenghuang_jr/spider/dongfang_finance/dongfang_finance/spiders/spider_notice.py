# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

"""
东方财富网：上市公司公告
"""
import socket
import sys
import os
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.spiders import BaseSpider
import json
import get_url as get_url_class
from scrapy.selector import HtmlXPathSelector
from lxml import etree
from scrapy.utils.project import get_project_settings  # 调用settings.py 文件方法
from scrapy.mail import MailSender
from dongfang_finance.items import *
import urllib2


class SpiderNotice(BaseSpider):
    def __init__(self):
        self.col_num = 6
    get_url = get_url_class.GetUrl()
    name = "notice"
    allowed_domains = ["notice.org"]
    start_urls = get_url_class.GetUrl().get_notice_url()

    # @staticmethod
    def parse(self, response):
        print "assadasda", socket.getaddrinfo('',0)
        try:
            # self.get_url.get_notice_url()
            item = NoticeItem()
            x = response.body_as_unicode()
            root = etree.HTML(x)
            company_code_list = []
            company_name_list = []
            notice_title_list = []
            notice_type_list = []
            notice_title_link_list = []
            notice_date_list = []
            nodes = root.xpath('//table[@id="dt" and @class="tableCont"]/tbody/tr')
            for row_info in nodes:
                for i in range(0, self.col_num):
                    if i == 0:
                        company_code_list.append(str(row_info[i].getchildren()[0].text))
                    if i == 1:
                        company_name_list.append(str(row_info[i].getchildren()[0].text))
                    if i == 3:
                        notice_title_list.append(str(row_info[i].getchildren()[0].text))
                        notice_title_link_list.append(str("http://data.eastmoney.com") + str(row_info[i][0].attrib['href']))
                    if i == 4:
                        notice_type_list.append(str(row_info[i].text))
                    if i == 5:
                        notice_date_list.append(str(row_info[i].text))
            item['company_code'] = company_code_list
            item['company_name'] = company_name_list
            item['notice_title'] = notice_title_list
            item['notice_type'] = notice_type_list
            item['notice_title_link'] = notice_title_link_list
            item['notice_date'] = notice_date_list
            yield item
        except Exception, e:
            print Exception, e
