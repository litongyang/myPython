# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import redis
import json
from jd_finance.items import *


class SpiderUrlSpider(scrapy.Spider):
    name = "jd_finance_spider_url"
    allowed_domains = ["spider_url.com"]
    start_urls = [
        'http://dq.jd.com/getItemPage.action?pageIndex=1',
        'http://dq.jd.com/getItemPage.action?pageIndex=2',
    ]

    def parse(self, response):
        try:
            item = JdFinanceUrlItem()
            json_data = json.loads(response.body_as_unicode())
            for k, v in json_data.items():
                if k == 'result':
                    for k1, v1 in v.items():
                        if k1 == 'items':
                            for i in range(0, len(v1)):
                                for key, value in v1[i].items():
                                    if key == 'totalAmount':  # 产品募集总额
                                        print value
                                    elif key == 'canBuyAmount':  # 当前募集总额
                                        print value
                                    elif key == 'skuId':  # ID
                                        print value
                                    elif key == 'itemName':  # 产品名称
                                        print value
                                    elif key == 'merchantId':  # 购买方ID
                                        print value
                                    elif key == 'merchantName':  # 购买方名称
                                        print value
                                    elif key == 'insuranceCode':  # 担保方ID
                                        print value
                                    elif key == 'insuranceName':  # 担保方名称
                                        print value
                                    elif key == 'insuranceType':  # 保险类型ID
                                        print value
                                    elif key == 'insuranceTypeName':  # 保险类型名称
                                        print value
                                    elif key == 'minAmount':  # 最低投资金额
                                        print value
                                    elif key == 'maxAmount':  # 最高投资金额
                                        print value
                                    elif key == 'maxNum':  # 最多购买数量
                                        print value
                                    elif key == 'period':  # 期限
                                        print value
                                    elif key == 'saleBeginDate':  # 售卖开始时间
                                        print value
                                    elif key == 'saleEndDate':  # 售卖截止时间
                                        print value
                                    elif key == 'historyBenefit':  # 收益率
                                        print value
                                    elif key == 'refundFeeIntro':  # 退款说明
                                        print value
                                    elif key == 'isSupportPartRefund':  # 是否支持持有期之前退款
                                        print value
                                    elif key == 'isSupportInsAppend':  # 是否支持持有期期间退款
                                        print value
                                    elif key == 'itemStatus':  # 标的状态
                                        print value
                                print "======"
        except Exception, e:
            error_info = Exception, e
            print error_info
