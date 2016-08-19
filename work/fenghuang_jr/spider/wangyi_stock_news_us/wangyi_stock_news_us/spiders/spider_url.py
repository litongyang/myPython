# -*- coding: utf-8 -*-
import scrapy
import sys
import os
import get_company_dict
from lxml import etree
import redis
from get_url import *
from wangyi_stock_news_us.items import *
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
reload(sys)
sys.setdefaultencoding('utf-8')


class SpiderUrlSpider(scrapy.Spider):
    name = "spider_url"
    allowed_domains = ["spider_url.com"]
    # start_urls = ['http://quotes.money.163.com/usstock/JD_news.html?page=0',
    #               'http://quotes.money.163.com/hkstock/00323.html'
    #               ]
    start_urls = GetUrl().get_company_news_url()

    def parse(self, response):
        try:
            r = redis.Redis(host='127.0.0.1', port=6379, db=0)
            news_time_list = []
            # company_news_lately_time = ''  # 公司相关新闻最近的抓取的发布时间
            item = WangyiStockUrlUsItem()
            data_html = response.body_as_unicode()
            root = etree.HTML(data_html)
            """ 获取公司字典 """
            get_company_dict_class = get_company_dict.GetCompanyDict()
            company_code_dict = get_company_dict_class.get_code_name_hsymbol_dict()
            us_position = response.url.find('usstock')
            company_code = ''
            if us_position >= 0:  # 美股资讯
                us_position_tail = response.url.find('_news')
                company_code = response.url[int(us_position)+8:us_position_tail]
                """ 从redis获取公司上一次最近爬取的发布时间 """
                company_news_lately_time_key = str('wanyi_spider_url_lately_time_') + str(company_code)
                last_time = r.get(str(company_news_lately_time_key))
                if last_time is None:
                    last_time = ''
                title_url_us_nodes = root.xpath('//div[@class="news_pills"]/dl/dt/a')
                time_us_nodes = root.xpath('//div[@class="time icon_news_pills_time"]/span')
                for i in range(0, len(title_url_us_nodes)):
                    if str(time_us_nodes[0].text) > str(last_time):
                        item['company_code'] = company_code
                        item['news_title'] = title_url_us_nodes[i].text
                        item['news_url'] = title_url_us_nodes[i].attrib['href']
                        item['news_time'] = time_us_nodes[i].text
                        news_time_list.append(time_us_nodes[i].text)
                        yield item
                    else:
                        break
                if len(news_time_list) > 0:
                    company_news_lately_time = news_time_list[0]
                    # print company_news_lately_time
                    # r.set(str(company_news_lately_time_key), str(company_news_lately_time))

            else:  # 港股资讯
                hk_position_hk = response.url.find('hkstock')
                if hk_position_hk >= 0:
                    hk_position_tail = response.url.find('.html')
                    company_code_hk = response.url[int(hk_position_hk) + 8:hk_position_tail]
                    for k, v in company_code_dict.items():
                        if v[1] == company_code_hk:
                            company_code = k
                    """ 从redis获取公司上一次最近爬取的发布时间 """
                    company_news_lately_time_key = str('wanyi_spider_url_lately_time_') + str(company_code)
                    last_time = r.get(str(company_news_lately_time_key))
                    if last_time is None:
                        last_time = ''
                    title_url_hk_nodes = root.xpath('//ul[@class="new-list"]/li//a')
                    time_hk_nodes = root.xpath('//ul[@class="new-list"]/li//span')
                    for i in range(0, len(title_url_hk_nodes)):
                        if str(time_hk_nodes[0].text) > str(last_time):
                            item['company_code'] = company_code
                            item['news_title'] = title_url_hk_nodes[i].text
                            item['news_url'] = title_url_hk_nodes[i].attrib['href']
                            item['news_time'] = time_hk_nodes[i].text
                            news_time_list.append(time_hk_nodes[i].text)
                            yield item
                        else:
                            break
                    if len(news_time_list) > 0:
                        company_news_lately_time = news_time_list[0]
                        # print company_news_lately_time
                        # r.set(str(company_news_lately_time_key), str(company_news_lately_time))

        except Exception, e:
            error_info = Exception, e
            print error_info
