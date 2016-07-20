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
import sys
import json
import get_url as get_url_class
from scrapy.utils.project import get_project_settings  # 调用settings.py 文件方法
from scrapy.mail import MailSender
from wdzj.items import *


class SpiderArchives(BaseSpider):
    def __init__(self):
        self.get_url = get_url_class.GetUrl()
        self.mailer = MailSender.from_settings(get_project_settings())
    get_url = get_url_class.GetUrl()
    name = "archives"
    allowed_domains = ["archives.org"]
    start_urls = get_url.get_archives_url()

    def parse(self, response):
        try:
            # self.get_url.get_archives_url()
            item = ArchivesItem()
            sites = json.loads(response.body_as_unicode())
            for key, value in self.get_url.archives_url_dict.items():
                if str(value) == str(response.url):
                    company_name = str(key)
                    interest_rate_volume_date_list = []
                    interest_rate_day_list = []
                    volume_day_list = []
                    pending_repayment_inflow_date_list = []
                    pending_repayment_history_day_list = []
                    net_inflow_day_list = []
                    invest_loan_user_date_list = []
                    invest_user_day_list = []
                    loan_user_day_list = []
                    url_type = key.split('-')
                    if str(url_type[1]) == str(0) and str(url_type[2]) == str(0):
                        company_name = url_type[0]
                        for k, v in sites.items():
                            if k == 'x':
                                interest_rate_volume_date_list = v
                            if k == 'y1':
                                interest_rate_day_list = v
                            if k == 'y2':
                                volume_day_list = v
                    if str(url_type[1]) == str(1) and str(url_type[2]) == str(0):
                        company_name = url_type[0]
                        for k, v in sites.items():
                            if k == 'x':
                                pending_repayment_inflow_date_list = v
                            if k == 'y1':
                                pending_repayment_history_day_list = v
                            if k == 'y3':
                                net_inflow_day_list = v
                    if str(url_type[1]) == str(3) and str(url_type[2]) == str(0):
                        company_name = url_type[0]
                        for k, v in sites.items():
                            if k == 'x':
                                invest_loan_user_date_list = v
                            if k == 'y1':
                                invest_user_day_list = v
                            if k == 'y2':
                                loan_user_day_list = v
                    item['item_type'] = 'archives'
                    item['company_name'] = str(company_name).encode("utf-8")
                    item['type'] = str(url_type[1])
                    item['status'] = str(url_type[2])
                    item['url'] = str(response.url)
                    item['interest_rate_volume_date'] = interest_rate_volume_date_list
                    item['interest_rate_day'] = interest_rate_day_list
                    item['volume_day'] = volume_day_list
                    item['pending_repayment_inflow_date'] = pending_repayment_inflow_date_list
                    item['pending_repayment_history_day'] = pending_repayment_history_day_list
                    item['net_inflow_day'] = net_inflow_day_list
                    item['invest_loan_user_date'] = invest_loan_user_date_list
                    item['invest_user_day'] = invest_user_day_list
                    item['loan_user_day'] = loan_user_day_list
                    yield item
        except Exception, e:
            error_info = "SpiderArchives: ", Exception, e
            print error_info
            self.mailer.send(to=["tongyang.li@fengjr.com"], subject="wdjz-erro-fution-SpiderPreference", body=str(error_info), mimetype='text/plain')

    @staticmethod
    def _process_request(request):
        return request
