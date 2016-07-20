# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

"""
东方财富网：上市公司公告
"""

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
from scrapy.mail import MailSender
from dongfang_finance.items import *
import time
import datetime


class SpiderResearch(BaseSpider):
    def __init__(self):
        self.get_url = get_url_class.GetUrl()
    get_url = get_url_class.GetUrl()
    name = "research"
    allowed_domains = ["research.org"]
    start_urls = get_url_class.GetUrl().get_research_url()

    # @staticmethod
    def parse(self, response):
        try:
            # self.get_url.get_research_url()
            item = ResearchItem()
            print type(item)
            company_code_list = []
            company_name_list = []
            research_title_list = []
            research_code_list = []  # 研报的ID,可以通过该id和日期拼接研报的url
            research_url_list = []
            research_date_list = []
            ins_name_list = []
            rating_name_list = []
            rating_change_list = []
            ins_star_list = []
            author_list = []
            profit_year_list = []
            pe_list_list = []
            per_share_list_list = []
            net_profit_list_list = []
            load_data = str(response.body_as_unicode())
            load_data = load_data.replace('var lty=', '')
            data_dict = json.loads(load_data)
            for k, v in data_dict.items():
                if k == 'data':  # 列表数据部分 v:list
                    for i in range(0, len(v)):  # table中每一行的数据:dict
                        for k_row, v_row in v[i].items():
                            # print k_row, v_row
                            if k_row == 'secuFullCode':
                                company_code_list.append(str(v_row))
                            if k_row == 'secuName':
                                company_name_list.append(str(v_row))
                            if k_row == 'title':
                                research_title_list.append(str(v_row))
                            if k_row == 'infoCode':
                                research_code_list.append(str(v_row))
                            if k_row == 'datetime':
                                research_date_list.append(str((datetime.datetime(*time.strptime(str(v_row), "%Y-%m-%dT%H:%M:%S")[:6])).date()))
                            if k_row == 'insName':
                                ins_name_list.append(str(v_row))
                            if k_row == 'sratingName':
                                rating_name_list.append(str(v_row))
                            if k_row == 'change':
                                rating_change_list.append(str(v_row))
                            if k_row == 'insStar':
                                ins_star_list.append(str(v_row))
                            if k_row == 'author':
                                author_list.append(str(v_row))
                            if k_row == 'profitYear':
                                profit_year_list.append(str(v_row))
                            if k_row == 'syls':  # 需要将list拼接成string
                                tmp = ''
                                for value in v_row:
                                    tmp += str(value) + '-'
                                tmp = tmp[0:-1]  # 去除最后一个逗号
                                pe_list_list.append(str(tmp))
                            if k_row == 'sys':
                                tmp = ''
                                for value in v_row:
                                    tmp += str(value) + '-'
                                tmp = tmp[0:-1]  # 去除最后一个逗号
                                per_share_list_list.append(str(tmp))
                            if k_row == 'jlrs':
                                tmp = ''
                                for value in v_row:
                                    tmp += str(value) + '-'
                                tmp = tmp[0:-1]  # 去除最后一个逗号
                                net_profit_list_list.append(str(tmp))
            for i in range(0, len(research_code_list)):  # 拼接研报url
                url = 'http://data.eastmoney.com/report/' + str(research_date_list[i]).replace('-', '') + '/' + str(research_code_list[i]) + '.html'
                research_url_list.append(url)
            # print research_url_list
            item['company_code'] = company_code_list
            item['company_name'] = company_name_list
            item['research_title'] = research_title_list
            item['research_date'] = research_date_list
            item['ins_name'] = ins_name_list
            item['rating_name'] = rating_name_list
            item['rating_change'] = rating_change_list
            item['ins_star'] = ins_star_list
            item['author'] = author_list
            item['profit_year'] = profit_year_list
            item['pe_list'] = pe_list_list
            item['per_share_list'] = per_share_list_list
            item['net_profit_list'] = net_profit_list_list
            item['research_url'] = research_url_list
            # print item['company_name']
            yield item
        except Exception, e:
            print Exception, e