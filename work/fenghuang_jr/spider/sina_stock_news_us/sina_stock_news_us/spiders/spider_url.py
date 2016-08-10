# -*- coding: utf-8 -*-
import scrapy
import sys
import os
import redis
import get_company_dict
from lxml import etree
from get_url import *
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
reload(sys)
sys.setdefaultencoding('utf-8')
from sina_stock_news_us.items import *


class SpiderUrlSpider(scrapy.Spider):

    name = "spider_url"
    allowed_domains = ["spider_url.com"]
    # start_urls = [
    #     'http://biz.finance.sina.com.cn/usstock/usstock_news.php?pageIndex=1&symbol=BIDU&type=1',
    #     'http://biz.finance.sina.com.cn/usstock/usstock_news.php?pageIndex=1&symbol=DNFGY&type=1',
    #     'http://stock.finance.sina.com.cn/hkstock/news/01919.html'
    # ]
    start_urls = GetUrl().get_company_news_url()

    def parse(self, response):
        try:
            news_time_list = []
            r = redis.Redis(host='127.0.0.1', port=6379, db=0)
            item = SinaStockUrlUsItem()
            data_html = response.body_as_unicode()
            root = etree.HTML(data_html)
            nodes = root.xpath('//ul[@class="xb_list"]')
            """ 获取公司字典 """
            get_company_dict_class = get_company_dict.GetCompanyDict()
            company_code_dict = get_company_dict_class.get_code_name_hsymbol_dict()
            us_position = response.url.find('symbol=')
            company_code = ''
            if us_position >= 0:  # 美股资讯
                us_position_tail = response.url.find('&type=1')
                company_code = response.url[int(us_position) + 7:us_position_tail]
                company_news_lately_time_key = str('hexun_spider_url_lately_time_') + str(company_code)
                last_time = r.get(str(company_news_lately_time_key))
                if last_time is None:
                    last_time = ''
                news_url_title_nodes_us = nodes[len(nodes)-1].xpath('./li/a')
                news_time_nodes_us = nodes[len(nodes)-1].xpath('./li/span')
                time_list = []  # 存放新闻时间
                for j in range(0, len(news_time_nodes_us)):
                    if news_time_nodes_us[j].text is not None:
                        time_list.append(news_time_nodes_us[j].text.replace(" | ", ""))
                for i in range(0, len(news_url_title_nodes_us)):
                    if str(time_list[0]) > str(last_time):
                        item['company_code'] = company_code
                        item['company_code_other'] = ''
                        item['news_title'] = news_url_title_nodes_us[i].text
                        item['news_url'] = news_url_title_nodes_us[i].attrib['href']
                        item['news_time'] = time_list[i]
                        print company_code
                        news_time_list.append(time_list[i])
                        yield item
                if len(news_time_list) > 0:
                    company_news_lately_time = news_time_list[0]
                    # print company_news_lately_time
                    # r.set(str(company_news_lately_time_key), str(company_news_lately_time))
            else:  # 港股资讯
                hk_position_hk = response.url.find('news/')
                if hk_position_hk >= 0:
                    hk_position_tail = response.url.find('.html')
                    company_code_hk = response.url[int(hk_position_hk) + 5:hk_position_tail]
                    for k, v in company_code_dict.items():
                        if v[1] == company_code_hk:
                            company_code = k
                    """ 从redis获取公司上一次最近爬取的发布时间 """
                    company_news_lately_time_key = str('hexun_spider_url_lately_time_') + str(company_code)
                    last_time = r.get(str(company_news_lately_time_key))
                    if last_time is None:
                        last_time = ''
                    news_url_title_nodes_hk = root.xpath('//ul[@class="list01"]/li/a')
                    news_time_nodes_hk = root.xpath('//ul[@class="list01"]/li/span')  # 存在None
                    for i in range(0, len(news_url_title_nodes_hk)):
                        if str(news_time_nodes_hk[0].text) > last_time:
                            item['company_code'] = company_code
                            item['company_code_other'] = company_code_hk
                            item['news_title'] = news_url_title_nodes_hk[i].text
                            item['news_url'] = news_url_title_nodes_hk[i].attrib['href']
                            item['news_time'] = news_time_nodes_hk[i].text
                            news_time_list.append(news_time_nodes_hk[i].text)
                            print "hk", company_code
                            yield item
                    if len(news_time_list) > 0:
                        company_news_lately_time = news_time_list[0]
                        # print company_news_lately_time
                        # r.set(str(company_news_lately_time_key), str(company_news_lately_time))

        except Exception, e:
            print "=============="
            print response.url
            error_info = Exception, e
            print error_info
