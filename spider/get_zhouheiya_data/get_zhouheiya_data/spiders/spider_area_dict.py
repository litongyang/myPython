# -*- coding: utf-8 -*-
import scrapy
import json
from get_zhouheiya_data.items import *


class SpiderAreaDictSpider(scrapy.Spider):
    name = "spider_area_dict"
    allowed_domains = ["spider_area_dict.com"]
    start_urls = (
        'https://www.zhouheiya.cn/wcs/Tpl/home/default/storejson/store.json',
    )

    def parse(self, response):
        try:
            item = GetDictItem()
            dict_list = json.loads(response.body_as_unicode())
            for dict_json in dict_list:
                province = ''
                province_id = ''
                city = ''
                city_id = ''
                area = ''
                area_id = ''
                for k, v in dict_json.items():
                    if k == 'children':  # 省级
                        for i in range(0, len(v)):
                            province = v[i]['name']
                            province_id = v[i]['level']
                            for j in range(0, len(v[i]['children'])):
                                v1 = v[i]['children'][j]
                                city = v1['name']
                                city_id = v1['level']
                                for k1 in range(0, len(v1['children'])):  # 区级
                                    area = v1['children'][k1]['name']  # 区名称
                                    area_id = v1['children'][k1]['level']  # 区id
                                    tmp_string = ''
                                    tmp_string += '\'' + str(province) + '\'' + ','
                                    tmp_string += '\'' + str(province_id) + '\'' + ','
                                    tmp_string += '\'' + str(city) + '\'' + ','
                                    tmp_string += '\'' + str(city_id) + '\'' + ','
                                    tmp_string += '\'' + str(area) + '\'' + ','
                                    tmp_string += '\'' + str(area_id) + '\'' + ','
                                    tmp_string = tmp_string[0:-1]
                                    item['content'] = tmp_string
                                    print "i"
                                    # print item['content']
                                    yield item

        except Exception, e:
            print Exception, e


