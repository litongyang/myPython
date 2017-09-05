# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
获取周黑鸭商品列表页的url
"""
import socket
import sys
import os

# from spider.get_zhouheiya_data.get_zhouheiya_data.items import GetZhouheiyaDataItem

parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.spiders import BaseSpider
import json
from scrapy.selector import HtmlXPathSelector
from lxml import etree
from scrapy.utils.project import get_project_settings  # 调用settings.py 文件方法
from scrapy.mail import MailSender
from get_zhouheiya_data.items import *
import urllib2


class SpiderGetZhouheiyaData(BaseSpider):
    def __init__(self):
        self.col_num = 6
    name = "get_zhouheiya_data"
    allowed_domains = ["get_zhouheiya_data.org"]
    start_urls = ['https://www.zhouheiya.cn/index.php/index-show-tid-5.html?id=0-5-0-2']

    # @staticmethod
    def parse(self, response):
        print "assadasda", socket.getaddrinfo('', 0)
        try:
            item = GetZhouheiyaDataItem()
            x = response.body_as_unicode()
            print x
            root = etree.HTML(x)
            print root
            #nodes = root.xpath('//*[@id="J_ShopSearchResult"]/div/div[3]/div[16]/dl[1]/dd/div')
            # print len(nodes)
            company_code_list = []
            company_name_list = []
            notice_title_list = []
            notice_type_list = []
            notice_title_link_list = []
            notice_date_list = []
            # nodes = root.xpath('//table[@id="dt" and @class="tableCont"]/tbody/tr')
            # for row_info in nodes:
            #     for i in range(0, self.col_num):
            #         if i == 0:
            #             company_code_list.append(str(row_info[i].getchildren()[0].text))
            #         if i == 1:
            #             company_name_list.append(str(row_info[i].getchildren()[0].text))
            #         if i == 3:
            #             notice_title_list.append(str(row_info[i].getchildren()[0].text))
            #             notice_title_link_list.append(str("http://data.eastmoney.com") + str(row_info[i][0].attrib['href']))
            #         if i == 4:
            #             notice_type_list.append(str(row_info[i].text))
            #         if i == 5:
            #             notice_date_list.append(str(row_info[i].text))
            # item['company_code'] = company_code_list
            # item['company_name'] = company_name_list
            # item['notice_title'] = notice_title_list
            # item['notice_type'] = notice_type_list
            # item['notice_title_link'] = notice_title_link_list
            # item['notice_date'] = notice_date_list
            item['html'] = x
            # print item['html']
            yield item
        except Exception, e:
            print Exception, e
