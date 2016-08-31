# -*- coding: utf-8 -*-
import scrapy
import redis
import os
import sys
import json
import time
from guomei_finance.items import *
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)

reload(sys)
sys.setdefaultencoding('utf-8')


# noinspection PyBroadException
class SpiderDetailSpider(scrapy.Spider):
    def __init__(self):
        self.time_stamp_tmp = time.time()
        self.time_array = time.localtime(self.time_stamp_tmp)
        self.date = time.strftime("%Y-%m-%d", self.time_array)
    name = "guomei_finance_spider_detail"
    allowed_domains = ["spider_detail.com"]
    start_urls = [
        'https://www.gomefinance.com.cn/api/v2/loans/getLoanWithPage?&pageSize=200&status=SCHEDULED&minDuration=0&maxDuration=100&currentPage=1',
    ]

    def parse(self, response):
        try:
            item = GuomeiFinanceDetailItem()
            json_data = json.loads(response.body_as_unicode())
            for k, v in json_data.items():
                if k == 'results':
                    for i in range(0, len(v)):
                        id = ''  # 产品id
                        title = ''  # 产品名称
                        repay_method = ''  # 偿还方式:BulletRepayment(一次性偿还)
                        amount = ''  # 产品募集金额
                        rate = ''  # 产品预期收益率
                        days = ''  # 产品期限天数
                        min_amount = ''  # 最小投资金额
                        max_amount = ''  # 最大投资金额
                        step_amount = ''  # 每笔投资单位金额
                        time_open = ''  # 开标时间
                        date_open = ''  # 开标日期
                        time_finished = ''  # 关标时间
                        bid_number = ''  # 投资人数
                        invest_amount = ''  # 投资金额
                        status = ''  # 标的状态
                        invest_percent = ''  # 当前进度
                        available = ''  # 当前可投资金额
                        for k1, v1 in v[i].items():
                            if k1 == 'id':  # 产品id
                                id = v1
                            elif k1 == 'title':  # 产品名称
                                title = v1
                            elif k1 == 'method':  # 偿还方式:BulletRepayment(一次性偿还)
                                repay_method = v1
                            elif k1 == 'amount':  # 产品募集金额
                                amount = v1
                            elif k1 == 'rate':  # 产品预期收益率
                                rate = v1
                            elif k1 == 'duration':  # 产品期限天数
                                for k2, v2 in v1.items():
                                    if k2 == 'totalDays':
                                        days = v2
                            elif k1 == 'loanRequest':
                                for k2, v2 in v1.items():
                                    if k2 == 'investRule':
                                        for k3, v3 in v2.items():
                                            if k3 == 'minAmount':
                                                min_amount = v3  # 最小投资金额
                                            if k3 == 'maxAmount':
                                                max_amount = v3  # 最大投资金额
                                            if k3 == 'stepAmount':
                                                step_amount = v3  # 每笔投资单位金额
                            elif k1 == 'timeOpen':  # 开标时间
                                try:
                                    time_open = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(v1)/1000))
                                    date_open = time.strftime("%Y-%m-%d", time.localtime(int(v1)/1000))
                                except:
                                    pass
                            elif k1 == 'timeFinished':  # 关标时间
                                try:
                                    time_finished = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(v1)/1000))
                                except:
                                    pass
                            elif k1 == 'bidNumber':  # 投资人数
                                bid_number = v1
                            elif k1 == 'bidAmount':  # 投资金额
                                invest_amount = v1
                            elif k1 == 'status':  # 标的状态
                                status = v1
                            elif k1 == 'investPercent':  # 当前进度
                                invest_percent = v1
                            elif k1 == 'available':  # 当前可投资金额
                                available = v1
                        if date_open == self.date:  # 取当天的标的信息
                            item['id'] = id
                            item['title'] = title
                            item['repay_method'] = repay_method
                            item['amount'] = amount
                            item['rate'] = rate
                            item['days'] = days
                            item['min_amount'] = min_amount
                            item['max_amount'] = max_amount
                            item['step_amount'] = step_amount
                            item['time_open'] = time_open
                            item['date_open'] = date_open
                            item['time_finished'] = time_finished
                            item['bid_number'] = bid_number
                            item['invest_amount'] = invest_amount
                            item['status'] = status
                            item['invest_percent'] = invest_percent
                            item['available'] = available
                            yield item

        except Exception, e:
            error_info = Exception, e
            print error_info
