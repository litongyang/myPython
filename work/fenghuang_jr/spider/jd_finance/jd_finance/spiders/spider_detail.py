# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import redis
import json
from jd_finance.items import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class SpiderUrlSpider(scrapy.Spider):
    name = "jd_finance_spider_detail"
    allowed_domains = ["spider_detail.com"]
    start_urls = [
        'http://dq.jd.com/getItemPage.action?pageIndex=1',
        'http://dq.jd.com/getItemPage.action?pageIndex=2',
    ]

    def parse(self, response):
        try:
            item = JdFinanceDetailItem()
            json_data = json.loads(response.body_as_unicode())
            # for k, v in item.items():
            #     print "ssssss", k

            for k, v in json_data.items():
                id = ''  # id
                title = ''  # 产品名称
                amount = ''  # 募集金额
                buy_amount = ''  # 当前募集总额
                merchant_id = ''  # 购买方ID
                merchant_name = ''  # 购买方名称
                insurance_code = ''  # 担保方id
                insurance_name = ''  # 担保方名称
                insurance_type = ''  # 保险类型
                insurance_type_name = ''  # 保险类型名称
                min_amount = ''  # 最低投资金额
                max_amount = ''  # 最高投资金额
                max_num = ''  # 最多购买数量
                days = ''  # 期限
                sale_begin_date = ''  # 售卖开始时间
                sale_end_date = ''  # 售卖截止时间
                rate = ''  # 历史收益率
                refund_info = ''  # 退款说明
                is_support_part_refund = ''  # 是否支持持有期之前退款
                is_support_ins_append = ''  # 是否支持追加
                status = ''  # 标的状态
                if k == 'result':
                    for k1, v1 in v.items():
                        if k1 == 'items':
                            for i in range(0, len(v1)):
                                for key, value in v1[i].items():
                                    if key == 'totalAmount':  # 产品募集总额
                                        amount = value
                                    elif key == 'canBuyAmount':  # 当前募集总额
                                        buy_amount = value
                                    elif key == 'skuId':  # ID
                                        id = value
                                    elif key == 'itemName':  # 产品名称
                                        title = value
                                    elif key == 'merchantId':  # 购买方ID
                                        merchant_id = value
                                    elif key == 'merchantName':  # 购买方名称
                                        merchant_name = value
                                    elif key == 'insuranceCode':  # 担保方ID
                                        insurance_code = value
                                    elif key == 'insuranceName':  # 担保方名称
                                        insurance_name = value
                                    elif key == 'insuranceType':  # 保险类型ID
                                        insurance_type = value
                                    elif key == 'insuranceTypeName':  # 保险类型名称
                                        insurance_type_name = value
                                    elif key == 'minAmount':  # 最低投资金额
                                        min_amount = value
                                    elif key == 'maxAmount':  # 最高投资金额
                                        max_amount = value
                                    elif key == 'maxNum':  # 最多购买数量
                                        max_num = value
                                    elif key == 'period':  # 期限
                                        days = value
                                    elif key == 'saleBeginDate':  # 售卖开始时间
                                        sale_begin_date = value
                                    elif key == 'saleEndDate':  # 售卖截止时间
                                        sale_end_date = value
                                    elif key == 'historyBenefit':  # 收益率
                                        rate = value
                                    elif key == 'refundFeeIntro':  # 退款说明
                                        refund_info = value
                                    elif key == 'isSupportPartRefund':  # 是否支持持有期之前退款
                                        is_support_part_refund = value
                                    elif key == 'isSupportInsAppend':  # 是否支持持有期期间退款
                                        is_support_ins_append = value
                                    elif key == 'itemStatus':  # 标的状态
                                        status = value
                                item['id'] = id
                                item['title'] = title
                                item['amount'] = amount
                                item['buy_amount'] = buy_amount
                                item['merchant_id'] = merchant_id
                                item['merchant_name'] = merchant_name
                                item['insurance_code'] = insurance_code
                                item['insurance_name'] = insurance_name
                                item['insurance_type'] = insurance_type
                                item['insurance_type_name'] = insurance_type_name
                                item['min_amount'] = min_amount
                                item['max_amount'] = max_amount
                                item['max_num'] = max_num
                                item['days'] = days
                                item['sale_begin_date'] = sale_begin_date
                                item['sale_end_date'] = sale_end_date
                                item['rate'] = rate
                                item['refund_info'] = refund_info
                                item['is_support_part_refund'] = is_support_part_refund
                                item['is_support_ins_append'] = is_support_ins_append
                                item['status'] = status
                                yield item
        except Exception, e:
            error_info = Exception, e
            print error_info
