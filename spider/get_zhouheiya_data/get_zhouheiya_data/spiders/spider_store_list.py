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
from get_store_url import GetStoreUrl

class SpiderGetStoreList(BaseSpider):
    def __init__(self):
        self.col_num = 6
    name = "spider_store_list"
    allowed_domains = ["spider_store_list.com"]
    # start_urls = ['https://www.zhouheiya.cn/wcs/Tpl/home/default/storejson/0-5-0-1.json']
    start_urls = GetStoreUrl().get_url()

    def parse(self, response):
        try:
            url = response.url
            address_id = url.replace('https://www.zhouheiya.cn/wcs/Tpl/home/default/storejson/', '').replace('.json', '')
            print address_id
            item = GetZhouheiyaDataItem()
            store_json_list = json.loads(response.body_as_unicode())
            for i in range(0, len(store_json_list)):
                item['longitude'] = store_json_list[i][0]
                item['latitude'] = store_json_list[i][1]
                item['name'] = store_json_list[i][2]
                item['address'] = store_json_list[i][3]
                item['id'] = store_json_list[i][4]
                item['address_id'] = address_id
                yield item
        except Exception, e:
            print Exception, e
