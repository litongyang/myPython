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
from lxml import etree
from hexun_stock_news_us.items import *
import random
from scrapy.http import Request,FormRequest


class SpiderUrlSpider(scrapy.Spider):

    name = "spider_url"
    allowed_domains = ["spider_url.com"]
    # start_urls = ['http://stockdata.stock.hexun.com/us/Nlist.aspx?code=JD&p=2']
    start_urls = ['http://stockdata.stock.hexun.com/us/news/CXDC.shtml',
                  'http://stockdata.stock.hexun.com/us/news/JD.shtml',
                  'http://hkdata.stock.hexun.com/company/news/00941.shtml'
                  ]
    # start_urls = ['http://hkdata.stock.hexun.com/company/news/00941.shtml']

    def parse(self, response):
        try:
            r = redis.Redis(host='127.0.0.1', port=6379, db=0)
            news_title_list = []
            news_time_list = []
            item = HexunStockUrlUsItem()
            data_html = response.body_as_unicode()
            root = etree.HTML(data_html)

            """ 获取公司字典 """
            get_company_dict_class = get_company_dict.GetCompanyDict()
            company_code_dict = get_company_dict_class.get_code_name_hsymbol_dict()
            us_position = response.url.find('us/news/')
            company_code = ''
            if us_position >= 0:  # 美股资讯
                us_position_tail = response.url.find('.shtml')
                company_code = response.url[int(us_position) + 8:us_position_tail]
                """ 从redis获取公司上一次最近爬取的发布标题 """
                company_news_lately_title_key = str('hexun_spider_url_lately_title_') + str(company_code)
                last_title = r.get(str(company_news_lately_title_key))
                if last_title is None:
                    last_title = ''
                title_url_us_nodes = root.xpath('//ul[@class="news-list"]/li/a')
                time_us_nodes = root.xpath('//ul[@class="news-list"]/li/span[@class="fr"]')
                for i in range(0, len(title_url_us_nodes)):
                    if str(title_url_us_nodes[0].text) != str(last_title):
                        item['company_code'] = company_code
                        item['company_code_other'] = ''
                        item['news_title'] = title_url_us_nodes[i].text
                        item['news_url'] = title_url_us_nodes[i].attrib['href']
                        item['news_time'] = time_us_nodes[i].text
                        news_title_list.append(title_url_us_nodes[i].text)
                    else:
                        break
                if len(news_title_list) > 0:
                    company_news_lately_title = news_title_list[0]
                    r.set(str(company_news_lately_title_key), str(company_news_lately_title))

            else:  # 港股资讯
                hk_position_hk = response.url.find('company/news/')
                if hk_position_hk >= 0:
                    hk_position_tail = response.url.find('.shtml')
                    company_code_hk = response.url[int(hk_position_hk) + 13:hk_position_tail]
                    for k, v in company_code_dict.items():
                        if v[1] == company_code_hk:
                            company_code = k
                    """ 从redis获取公司上一次最近爬取的发布时间 """
                    company_news_lately_time_key = str('hexun_spider_url_lately_time_') + str(company_code)
                    last_time = r.get(str(company_news_lately_time_key))
                    if last_time is None:
                        last_time = ''
                    title_url_hk_nodes = root.xpath('//tr/td[@height="30" and @colspan="2"]/a')
                    time_hk_nodes = root.xpath('//tr/td[@colspan="2"]')  # 存在None
                    time_list = []
                    for j in range(0, len(time_hk_nodes)):
                        if time_hk_nodes[j].text is not None:
                            time_list.append(time_hk_nodes[j].text)
                    for i in range(0, len(title_url_hk_nodes)):
                        if str(time_list[0]) > str(last_time):
                            item['company_code'] = company_code
                            item['company_code_other'] = company_code_hk
                            item['news_title'] = title_url_hk_nodes[i].text
                            item['news_url'] = title_url_hk_nodes[i].attrib['href']
                            item['news_time'] = time_list[i]
                            print item['news_url']
                            news_time_list.append(time_list[i])
                        else:
                            break
                    if len(news_time_list) > 0:
                        company_news_lately_time = news_time_list[0]
                        r.set(str(company_news_lately_time_key), str(company_news_lately_time))

        except Exception, e:
            error_info = Exception, e
            print error_info
