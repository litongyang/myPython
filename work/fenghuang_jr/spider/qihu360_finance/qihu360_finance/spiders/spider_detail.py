# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from qihu360_finance.items import *
import time


class SpiderDetailSpider(scrapy.Spider):
    def __init__(self):
        self.time_stamp_tmp = time.time()
        self.time_array = time.localtime(self.time_stamp_tmp)
        self.date = time.strftime("%Y-%m-%d", self.time_array)
    name = "qihu360_finance_spider_detail"
    allowed_domains = ["spider_detail.com"]
    start_urls = [
        'https://www.nicaifu.com/dq/detail?code=DDF3H6RXQLwubcJNgfSICYYWK9A4KkI2',
        'https://www.nicaifu.com/dq/detail?code=DDF3H6RXQLx-0FYvUn2WOrHUNxwMsonO',
        'https://www.nicaifu.com/qilu/detail?code=SF2886',
        'https://www.nicaifu.com/qilu/detail?code=SF2883',
        # 'https://www.nicaifu.com/dc/detail?code=DC2803',
        # 'https://www.nicaifu.com/ins/detail?product_code=BULY',
    ]

    def parse(self, response):
        try:
            item = Qihu360FinanceDetailItem()
            data_html = response.body_as_unicode()
            root = etree.HTML(data_html)
            title_nodes = root.xpath('//h3/text()')
            ratio_days_method_noeds = root.xpath('//div[@class="rgl-top"]/ul/li/div')
            open_date_template1 = root.xpath('//div[@class="rgl-date rgb-date-2"]/ul/li[@class="sp1"]/p/text()[2]')
            open_date_template2 = root.xpath('//div[@class="rgl-date rgb-date-1"]/ul/li[@class="sp1"]/p/text()[2]')
            open_date_template3 = root.xpath('//div[@class="rgl-date rgb-date-4"]/ul/li[@class="sp1"]/p/em/text()')
            interest_start_template1 = root.xpath('//div[@class="rgl-date rgb-date-2"]/ul/li[@class="sp2"]/p/text()[2]')
            interest_start_template2 = root.xpath('//div[@class="rgl-date rgb-date-1"]/ul/li[@class="sp2"]/p/text()[2]')
            interest_start_template3 = root.xpath('//div[@class="rgl-date rgb-date-4"]/ul/li[@class="sp2"]/p/em/text()')
            interest_end_template1 = root.xpath('//div[@class="rgl-date rgb-date-2"]/ul/li[@class="sp3"]/p/text()[2]')
            interest_end_template2 = root.xpath('//div[@class="rgl-date rgb-date-1"]/ul/li[@class="sp3"]/p/text()[2]')
            interest_end_template3 = root.xpath('//div[@class="rgl-date rgb-date-4"]/ul/li[@class="sp3"]/p/em[2]/text()')
            profit_date_template1 = root.xpath('//li[@class="sp4"]/p/text()[2]')
            profit_date_template2 = root.xpath('//li[@class="sp4"]/p/em[1]/text()')
            remainder_template1 = root.xpath('//div[@class="invest"]/p/span[1]/em/text()')
            total_teplate1 = root.xpath('//div[@class="limit clearfix"]/p/span/text()')
            start_amount_info_teplate1 = root.xpath('//div[@style="margin:16px 0 0;"]/text()')

            if len(open_date_template1) > 0:
                open_date_nodes = open_date_template1
            elif len(open_date_template2) > 0:
                open_date_nodes = open_date_template2
            elif len(open_date_template3) > 0:
                open_date_nodes = open_date_template3

            if len(interest_start_template1) > 0:
                interest_start_nodes = interest_start_template1
            elif len(interest_start_template2) > 0:
                interest_start_nodes = interest_start_template2
            elif len(interest_start_template3) > 0:
                interest_start_nodes = interest_start_template3

            if len(interest_end_template1) > 0:
                interest_end_nodes = interest_end_template1
            elif len(interest_end_template2) > 0:
                interest_end_nodes = interest_end_template2
            elif len(interest_end_template3) > 0:
                interest_end_nodes = interest_end_template3

            if len(profit_date_template1) > 0:
                profit_date_nodes = profit_date_template1
            elif len(profit_date_template2) > 0:
                profit_date_nodes = profit_date_template2

            if len(remainder_template1) > 0:
                remainder_node = remainder_template1
            else:
                remainder_node = [0]

            if len(total_teplate1) > 0:
                total_node = total_teplate1
            else:
                total_node = ['null']

            if len(start_amount_info_teplate1):
                start_amount_info_node = start_amount_info_teplate1
            else:
                start_amount_info_node = ['null']
            open_date = open_date_nodes[0][0:10].replace('/', '').replace('-', '')
            today = self.date.replace('-', '')
            print open_date  # 开标时间
            print title_nodes[0]  # 产品名称
            print ratio_days_method_noeds[0].text.replace(' ', '').replace('\n', '')  # 预期年化收益率
            print ratio_days_method_noeds[1].text.replace(' ', '')  # 期限
            print ratio_days_method_noeds[2].text.replace(' ', '')  # 收益方式
            print interest_start_nodes[0]  # 起息日
            print interest_end_nodes[0]  # 到期日
            print profit_date_nodes[0]  # 发放日期
            print remainder_node[0]  # 剩余金额
            print total_node[0]  # 总的募集金额
            print start_amount_info_node[0]  # 起投金额信息
            print "================="
            item['url'] = open_date  # 产品详情url
            item['title'] = title_nodes[0]  # 产品标题
            item['ratio'] = ratio_days_method_noeds[0].text.replace(' ', '').replace('\n', '')  # 预期收益率
            item['days'] = ratio_days_method_noeds[1].text.replace(' ', '')  # 期限
            item['repay_method'] = ratio_days_method_noeds[2].text.replace(' ', '')  # 收益方式
            item['start_date'] = interest_start_nodes[0]  # 起息日期
            item['end_date'] = interest_end_nodes[0]  # 到期日期
            item['profit_date'] = profit_date_nodes[0]  # 发放日
            item['available'] = remainder_node[0]  # 当前可投资金额
            item['amount'] = total_node[0]  # 募集金额
            item['min_amount_info'] = start_amount_info_node[0]  # 起投金额信息

        except Exception, e:
            error_info = Exception, e
            print error_info
