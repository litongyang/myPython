# -*- coding: utf-8 -*-

import scrapy
import sys
import os
import redis
import get_company_dict


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
    start_urls = ['http://news.gtimg.cn/bodynews.php?name=body_news&n=10&q=usJD',
                  'http://news.gtimg.cn/bodynews.php?name=body_news&n=10&q=usBABA',
                  'http://news.gtimg.cn/bodynews.php?name=body_news&n=10&q=hk00165',
                  # 'http://news.gtimg.cn/bodynews.php?name=body_news&n=10&q=usBIDU',
                  # 'http://news.gtimg.cn/bodynews.php?name=body_news&n=10&q=usDUKS',
                  # 'http://news.gtimg.cn/bodynews.php?name=body_news&n=10&q=usEDU',
                  ]
    # start_urls = get_url_class.GetUrl().get_company_news_url()

    def parse(self, response):
        try:
            """ 获取公司字典 """
            get_company_dict_class = get_company_dict.GetCompanyDict()
            company_code_dict = get_company_dict_class.get_code_name_hsymbol_dict()
            r = redis.Redis(host='127.0.0.1', port=6379, db=0)
            print "url", response.url
            us_position = response.url.find('us')
            """ 从url中截取公司代码 """
            company_code = ''
            if us_position >= 0:
                company_code = response.url[int(us_position)+2:len(response.url)]
            else:
                us_position_hk = response.url.find('hk')
                if us_position_hk >= 0:
                    company_code_hk = response.url[int(us_position_hk)+2:len(response.url)]
                    for k, v in company_code_dict.items():
                        if v[1] == company_code_hk:
                            print v[1]
                            company_code = k

            """ 从redis获取公司上一次最近爬取的发布时间 """
            company_news_lately_time_key = str('spider_url_lately_time_') + str(company_code)
            last_time = r.get(str(company_news_lately_time_key))
            company_news_lately_time = ''  # 公司相关新闻最近的抓取的发布时间
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
                """ 抓取的最新新闻的发布时间要大于上一次时间,否则剩余的url过滤掉 """
                if str(load_data[i][0]) < str(r.get(last_time)):
                    news_time_list.append(load_data[i][0])
                    news_url_list.append(load_data[i][2])
                else:
                    break
            if len(news_time_list) > 0:
                company_news_lately_time = news_time_list[0]
            print company_news_lately_time
            item['company_code'] = company_code
            item['news_time'] = news_time_list
            item['news_url'] = news_url_list
            company_news_lately_time_key = str('spider_url_lately_time_') + str(item['company_code'])
            r.set(str(company_news_lately_time_key), str(company_news_lately_time))
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
