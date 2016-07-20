# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

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
from scrapy.utils.project import get_project_settings  # 调用settings.py 文件方法
from scrapy.mail import MailSender
from wdzj.items import *


class SpiderBasic(BaseSpider):
    def __init__(self):
        self.get_url = get_url_class.GetUrl()
        self.mailer = MailSender.from_settings(get_project_settings())
    get_url = get_url_class.GetUrl()
    name = "basic"
    allowed_domains = ["basic.org"]
    start_urls = get_url_class.GetUrl().get_basic_url()

    def parse(self, response):
        try:
            # get_url = get_url_class.GetUrl()
            self.get_url.get_basic_url()
            item = BasicItem()
            sites = json.loads(response.body_as_unicode())
            for key, value in self.get_url.basic_url_dict.items():
                if str(value) == str(response.url):
                    company_name = str(key)
                    last_90day_type_name_list = []
                    last_90day_type_data_list = []
                    last_90day_deadline_name_list = []
                    last_90day_deadline_data_list = []
                    last_90day_amount_name_list = []
                    last_90day_amount_data_list = []
                    for k, v in sites.items():
                        if str(k) == 'pie1':  # 近90日标的类型
                            for i in range(0, len(v)):
                                for pie1_k, v1 in v[i].items():
                                    if pie1_k == 'key':
                                        last_90day_type_name_list.append(str(v1))
                                    if pie1_k == 'value':
                                        last_90day_type_data_list.append(str(v1))
                        if str(k) == 'pie2':  # 近90日标的期限
                            for i in range(0, len(v)):
                                for pie1_k, v1 in v[i].items():
                                    if pie1_k == 'key':
                                        last_90day_deadline_name_list.append(str(v1))
                                    if pie1_k == 'value':
                                        last_90day_deadline_data_list.append(str(v1))
                        if str(k) == 'pie3':  # 近90日标的金额
                            for i in range(0, len(v)):
                                for pie1_k, v1 in v[i].items():
                                    if pie1_k == 'key':
                                        last_90day_amount_name_list.append(str(v1))
                                    if pie1_k == 'value':
                                        last_90day_amount_data_list.append(str(v1))
                    item['item_type'] = 'basic'
                    item['company_name'] = str(company_name).encode("utf-8")
                    item['url'] = str(response.url)
                    item['last_90day_type_name'] = last_90day_type_name_list
                    item['last_90day_type_data'] = last_90day_type_data_list
                    item['last_90day_deadline_name'] = last_90day_deadline_name_list
                    item['last_90day_deadline_data'] = last_90day_deadline_data_list
                    item['last_90day_amount_name'] = last_90day_amount_name_list
                    item['last_90day_amount_data'] = last_90day_amount_data_list
                    yield item
        except Exception, e:
            error_info = "SpiderPreference: ", Exception, e
            print error_info
            self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-SpiderPreference", body=str(error_info), mimetype='text/plain')

    @staticmethod
    def _process_request(request):
        return request
