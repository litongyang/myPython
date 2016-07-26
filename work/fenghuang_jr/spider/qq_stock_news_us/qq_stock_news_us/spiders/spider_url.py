# -*- coding: utf-8 -*-

import scrapy
import sys
import os

parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
reload(sys)
sys.setdefaultencoding('utf-8')
import json
from qq_stock_news_us.items import *
from lxml import etree
import get_url as get_url_class


class SpiderUrlSpider(scrapy.Spider):
    name = "spider_url"
    allowed_domains = ["spider_url.com"]
    # start_urls = ['http://stockhtm.finance.qq.com/astock/quotpage/news.htm?c=usJD.OQ#']
    # start_urls = ['http://news.gtimg.cn/more.php?q=usJD&page=1']
    # start_urls = ['http://news.gtimg.cn/bodynews.php?name=body_news&n=10&q=usJD',
    #               'http://news.gtimg.cn/bodynews.php?name=body_news&n=10&q=usBABA',
    #               'http://news.gtimg.cn/bodynews.php?name=body_news&n=10&q=usBIDU',
    #               'http://news.gtimg.cn/bodynews.php?name=body_news&n=10&q=usDUKS',
    #               'http://news.gtimg.cn/bodynews.php?name=body_news&n=10&q=usEDU',
    #               ]
    start_urls = get_url_class.GetUrl().get_company_news_url()

    def parse(self, response):
        try:
            print response.url
            item = QqStockNewsUsUrlItem()
            load_data = response.body_as_unicode()
            # load_data = response.body.decode('gbk')
            load_data = load_data.replace('var body_news=', '')
            load_data = load_data.replace(';', '')
            load_data = eval(load_data)
            news_time_list = []
            news_url_list = []
            # print load_data[0]
            for i in range(0, len(load_data)):
                news_time_list.append(load_data[i][0])
                news_url_list.append(load_data[i][2])
            item['news_time'] = news_time_list
            item['news_url'] = news_url_list
            return item

        except Exception, e:
            error_info = Exception, e
            print error_info

    # """ 历史新闻:解析json """
    # def parse(self, response):
    #     try:
    #         item = QqStockNewsUsUrlItem()
    #         # load_data = response.body_as_unicode()
    #         load_data = response.body.decode('gbk')
    #         load_data = load_data.replace('var body_news =', '')
    #         load_data = load_data.replace(';', '')
    #         load_data = load_data.replace("'total'", '"total"')
    #         load_data = load_data.replace("'current'", '"current"')
    #         load_data = load_data.replace("'data'", '"data"')
    #         data_dict = json.loads(load_data)
    #         news_time_list = []
    #         news_title_list = []
    #         news_url_list = []
    #         for k, v in data_dict.items():
    #             if k == str('data'):  # v:url列表数据:二维数组
    #                 for i in range(0, len(v)):  # v[i]:一条新闻的列表
    #                     # my_char = chardet.detect(str(v[i][3]))
    #                     # print my_char
    #                     # print v[i][3].encode('ISO8859-1', 'ignore').decode('gbk')
    #                     # for j in range(0, len(v[i])):
    #                     """ 新闻发布时间 """
    #                     news_time_list.append(str(v[i][0]))
    #                     """ 新闻标题 """
    #                     news_title_list.append(str(v[i][2]))
    #                     """ 新闻url """
    #                     news_url_list.append(str(v[i][3]))
    #         print news_url_list
    #         item['news_time'] = news_time_list
    #         item['news_title'] = news_title_list
    #         item['news_url'] = news_url_list
    #         return item
    #     except Exception, e:
    #         error_info = Exception, e
    #         print error_info
