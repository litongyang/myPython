# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-
"""
爬取偏好数据
"""
from scrapy.crawler import CrawlerProcess
import sys
import os
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
reload(sys)
sys.setdefaultencoding('utf-8')
import json
from scrapy.spiders import BaseSpider
from scrapy.utils.project import get_project_settings  # 调用settings.py 文件方法
from scrapy.mail import MailSender
import get_url as get_url_class
from wdzj.items import *


class SpiderPreference(BaseSpider):
    def __init__(self):
        self.get_url = get_url_class.GetUrl()
        self.mailer = MailSender.from_settings(get_project_settings())
    get_url = get_url_class.GetUrl()
    name = "preference"
    allowed_domains = ["preference.org"]
    start_urls = get_url_class.GetUrl().get_preference_url()

    # @staticmethod
    def parse(self, response):
        try:
            self.get_url.get_preference_url()
            item = PreferenceItem()
            sites = json.loads(response.body_as_unicode())
            for key, value in self.get_url.preference_url_dict.items():
                if str(value) == str(response.url):
                    company_name = str(key)
                    core_index_name_list = []
                    core_index_data_list = []
                    index_preference_data_list = []
                    for k, v in sites.items():
                        if k == 'data':
                            for k1, v1 in v.items():
                                if str(k1) == "x":
                                    core_index_name_list = v1
                                if str(k1) == 'y1':
                                    core_index_data_list = v1
                                if str(k1) == 'y2':
                                    index_preference_data_list = v1
                            item['item_type'] = 'preference'
                            item['company_name'] = str(company_name).encode("utf-8")
                            item['url'] = str(response.url)
                            item['core_index_name'] = core_index_name_list
                            item['core_index_data'] = core_index_data_list
                            item['index_preference_data'] = index_preference_data_list
                            yield item
        except Exception, e:
            error_info = "SpiderPreference: ", Exception, e
            print error_info
            self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-SpiderPreference", body=str(error_info), mimetype='text/plain')

    @staticmethod
    def _process_request(request):
        return request


