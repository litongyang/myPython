# -*- coding: utf-8 -*-
import scrapy
import redis
import json
from guomei_finance.items import *


class SpiderDetailSpider(scrapy.Spider):
    name = "guomei_finance_spider_detail"
    allowed_domains = ["spider_detail.com"]
    start_urls = [
        'https://www.gomefinance.com.cn/api/v2/loans/getLoanWithPage?&pageSize=100&status=SCHEDULED&minDuration=0&maxDuration=100&currentPage=1',
    ]

    def parse(self, response):
        try:
            item = GuomeiFinanceDetailItem()
            json_data = json.loads(response.body_as_unicode())
            for k, v in json_data.items():
                if k == 'results':
                    for i in range(0, len(v)):
                        for k1, v1 in v[i].items():
                            if k1 == 'id':  # 产品id
                                print v1
                            elif k1 == 'title':  # 产品名称
                                print v1
                            elif k1 == 'method':  # 偿还方式:BulletRepayment(一次性偿还)
                                print v1
                            elif k1 == 'amount':  # 产品募集金额
                                print v1
                            elif k1 == 'rate':  # 产品预期收益率
                                print v1
                            elif k1 == 'duration':  # 产品期限天数
                                for k2, v2 in v1.items():
                                    if k2 == 'totalDays':
                                        print v2
                            elif k1 == 'loanRequest':
                                for k2, v2 in v1.items():
                                    if k2 == 'investRule':
                                        for k3, v3 in v2.items():
                                            if k3 == 'minAmount':
                                                print v3  # 最小投资金额
                                            if k3 == 'maxAmount':
                                                print v3  # 最大投资金额
                                            if k3 == 'stepAmount':
                                                print v3  # 每笔投资单位金额
                            elif k1 == 'timeOpen':  # 开标时间
                                print v1
                            elif k1 == 'timeFinished':  # 关标时间
                                print v1
                            elif k1 == 'bidNumber':  # 投资人数
                                print v1
                            elif k1 == 'bidAmount':  # 投资金额
                                print v1
                            elif k1 == 'status':  # 标的状态
                                print v1
                            elif k1 == 'investPercent':  # 当前进度
                                print v1
                            elif k1 == 'available':  # 当前可投资金额
                                print v1
                        print "========="
        except Exception, e:
            error_info = Exception, e
            print error_info
