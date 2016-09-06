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
    # start_urls = [
    #     'http://dq.jd.com/getItemPage.action?pageIndex=1',
    #     'http://dq.jd.com/getItemPage.action?pageIndex=2',
    # ]
    start_urls = ['http://jdd.jr.jd.com/product/listTableRemote.html?callback=&pageNo=1']

    def parse(self, response):
        try:
            item = JdFinanceDetailItem()
            json_data = json.loads(response.body_as_unicode()[1:len(response.body_as_unicode())-1])
            # print json_data
            # "itemTypeName":"月月盈",
            # "totalAmount":"500000000",
            # "canBuyAmount":"439184000",
            # "nextOpenDate":"2016-10-06",
            # "itemExtends":[
            #
            #               ],
            # "itemType":3,
            # "id":37049,
            # "skuId":"11003000107",
            # "itemCode":"gzgqjyzx809625",
            # "itemName":"京穗月月盈44号理财计划",
            # "merchantId":"11003",
            # "merchantName":"广州金融资产交易中心有限公司",
            # "assetCode":"1100320160902001",
            # "assetName":"京穗月月盈44号理财计划",
            # "skuType":"305",
            # "bizType":"1",
            # "amount":1000,
            # "minAmount":1000,
            # "maxAmount":300000,
            # "waterLevelLine":0,
            # "saleBeginDate":"2016-09-04 23:30:00",
            # "saleEndDate":"2016-09-05 23:30:00",
            # "beginDate":"2016-09-06 00:00:00",
            # "endDate":"2019-09-06 00:00:00",
            # "benefit":4.5,
            # "periodType":"年",
            # "periodValue":"3",
            #
            # "itemStatus":2,
            # "createTime":"2016-09-02 18:13:45",
            # "updateTime":"2016-09-03 22:31:42",
            # "operator":"lxyll",
            # "label":"可预约赎回",
            # "repaymentType":"1",
            # "interestType":"2",
            # "bookRedemption":"1",
            # "bookRedemptionRule":"{"}",
            # "versionId":3

            for k, v in json_data.items():

                if k == 'items':
                    for k1, v1 in v.items():
                        if k1 == 'values':
                            for i in range(0, len(v1)):
                                id = ''  # id
                                sku_id = ''  # skuid
                                title = ''  # 产品名称
                                amount = ''  # 募集金额
                                available = ''  # 当前可投资金额
                                next_open_date = ''  # 下一次开标日期
                                item_type = ''  # 产品类型id
                                type_name = ''  # 产品类型名称
                                merchant_id = ''  # 交易中心id
                                merchant_name = ''  # 交易中心id
                                step_amount = ''  # 每笔投资单位金额
                                min_amount = ''  # 最小投资金额
                                max_amount = ''  # 最大投资金额
                                sale_begin_date = ''  # 起售时间
                                sale_end_date = ''  # 截止时间
                                begin_date = ''  # 计息时间
                                end_date = ''  # 到期时间
                                rate = ''  # 收益率
                                period_type = ''  # 期限类型
                                period_value = ''  # 期限值
                                status = ''  # 产品状态
                                create_time = ''  # 创建时间
                                update_time = ''  # 更新时间
                                label_info = ''  # 赎回说明
                                repayment_type = ''  # 偿还类型
                                interest_type = ''  # 利息类型
                                version_id = ''  # 版本id
                                for k2, v2 in v1[i].items():
                                    if k2 == 'id':
                                        id = v2
                                    elif k2 == 'skuId':
                                        sku_id = v2
                                    elif k2 == 'itemTypeName':
                                        type_name = v2
                                    elif k2 == 'totalAmount':
                                        amount = v2
                                    elif k2 == 'canBuyAmount':
                                        available = v2
                                    elif k2 == 'nextOpenDate':
                                        next_open_date = v2
                                    elif k2 == 'itemType':
                                        item_type = v2
                                    elif k2 == 'itemName':
                                        title = v2
                                    elif k2 == 'merchantId':
                                        merchant_id = v2
                                    elif k2 == 'merchantName':
                                        merchant_name = v2
                                    elif k2 == 'amount':
                                        step_amount = v2
                                    elif k2 == 'minAmount':
                                        min_amount = v2
                                    elif k2 == 'maxAmount':
                                        max_amount = v2
                                    elif k2 == 'saleBeginDate':
                                        sale_begin_date = v2
                                    elif k2 == 'saleEndDate':
                                        sale_end_date = v2
                                    elif k2 == 'beginDate':
                                        begin_date = v2
                                    elif k2 == 'endDate':
                                        end_date = v2
                                    elif k2 == 'benefit':
                                        rate = v2
                                    elif k2 == 'periodType':
                                        period_type = v2
                                    elif k2 == 'periodValue':
                                        period_value = v2
                                    elif k2 == 'itemStatus':
                                        status = v2
                                    elif k2 == 'createTime':
                                        create_time = v2
                                    elif k2 == 'updateTime':
                                        update_time = v2
                                    elif k2 == 'label':
                                        label_info = v2
                                    elif k2 == 'repaymentType':
                                        repayment_type = v2
                                    elif k2 == 'interestType':
                                        interest_type = v2
                                    elif k2 == 'versionId':
                                        version_id = v2
                                item['id'] = id
                                item['sku_id'] = sku_id
                                item['type_name'] = type_name
                                item['amount'] = amount
                                item['available'] = available
                                item['next_open_date'] = next_open_date
                                item['item_type'] = item_type
                                item['title'] = title
                                item['merchant_id'] = merchant_id
                                item['merchant_name'] = merchant_name
                                item['step_amount'] = step_amount
                                item['min_amount'] = min_amount
                                item['max_amount'] = max_amount
                                item['sale_begin_date'] = sale_begin_date
                                item['sale_end_date'] = sale_end_date
                                item['begin_date'] = begin_date
                                item['end_date'] = end_date
                                item['rate'] = rate
                                item['period_type'] = period_type
                                item['period_value'] = period_value
                                item['status'] = status
                                item['create_time'] = create_time
                                item['update_time'] = update_time
                                item['label_info'] = label_info
                                item['repayment_type'] = repayment_type
                                item['interest_type'] = interest_type
                                item['version_id'] = version_id
                                yield item


            # json_data = json.loads(response.body_as_unicode())


            # for k, v in json_data.items():
            #     id = ''  # id
            #     title = ''  # 产品名称
            #     amount = ''  # 募集金额
            #     buy_amount = ''  # 当前募集总额
            #     merchant_id = ''  # 购买方ID
            #     merchant_name = ''  # 购买方名称
            #     insurance_code = ''  # 担保方id
            #     insurance_name = ''  # 担保方名称
            #     insurance_type = ''  # 保险类型
            #     insurance_type_name = ''  # 保险类型名称
            #     min_amount = ''  # 最低投资金额
            #     max_amount = ''  # 最高投资金额
            #     max_num = ''  # 最多购买数量
            #     days = ''  # 期限
            #     sale_begin_date = ''  # 售卖开始时间
            #     sale_end_date = ''  # 售卖截止时间
            #     rate = ''  # 历史收益率
            #     refund_info = ''  # 退款说明
            #     is_support_part_refund = ''  # 是否支持持有期之前退款
            #     is_support_ins_append = ''  # 是否支持追加
            #     status = ''  # 标的状态
            #     if k == 'result':
            #         for k1, v1 in v.items():
            #             if k1 == 'items':
            #                 for i in range(0, len(v1)):
            #                     for key, value in v1[i].items():
            #                         if key == 'totalAmount':  # 产品募集总额
            #                             amount = value
            #                         elif key == 'canBuyAmount':  # 当前募集总额
            #                             buy_amount = value
            #                         elif key == 'skuId':  # ID
            #                             id = value
            #                         elif key == 'itemName':  # 产品名称
            #                             title = value
            #                         elif key == 'merchantId':  # 购买方ID
            #                             merchant_id = value
            #                         elif key == 'merchantName':  # 购买方名称
            #                             merchant_name = value
            #                         elif key == 'insuranceCode':  # 担保方ID
            #                             insurance_code = value
            #                         elif key == 'insuranceName':  # 担保方名称
            #                             insurance_name = value
            #                         elif key == 'insuranceType':  # 保险类型ID
            #                             insurance_type = value
            #                         elif key == 'insuranceTypeName':  # 保险类型名称
            #                             insurance_type_name = value
            #                         elif key == 'minAmount':  # 最低投资金额
            #                             min_amount = value
            #                         elif key == 'maxAmount':  # 最高投资金额
            #                             max_amount = value
            #                         elif key == 'maxNum':  # 最多购买数量
            #                             max_num = value
            #                         elif key == 'period':  # 期限
            #                             days = value
            #                         elif key == 'saleBeginDate':  # 售卖开始时间
            #                             sale_begin_date = value
            #                         elif key == 'saleEndDate':  # 售卖截止时间
            #                             sale_end_date = value
            #                         elif key == 'historyBenefit':  # 收益率
            #                             rate = value
            #                         elif key == 'refundFeeIntro':  # 退款说明
            #                             refund_info = value
            #                         elif key == 'isSupportPartRefund':  # 是否支持持有期之前退款
            #                             is_support_part_refund = value
            #                         elif key == 'isSupportInsAppend':  # 是否支持持有期期间退款
            #                             is_support_ins_append = value
            #                         elif key == 'itemStatus':  # 标的状态
            #                             status = value
            #                     item['id'] = id
            #                     item['title'] = title
            #                     item['amount'] = amount
            #                     item['buy_amount'] = buy_amount
            #                     item['merchant_id'] = merchant_id
            #                     item['merchant_name'] = merchant_name
            #                     item['insurance_code'] = insurance_code
            #                     item['insurance_name'] = insurance_name
            #                     item['insurance_type'] = insurance_type
            #                     item['insurance_type_name'] = insurance_type_name
            #                     item['min_amount'] = min_amount
            #                     item['max_amount'] = max_amount
            #                     item['max_num'] = max_num
            #                     item['days'] = days
            #                     item['sale_begin_date'] = sale_begin_date
            #                     item['sale_end_date'] = sale_end_date
            #                     item['rate'] = rate
            #                     item['refund_info'] = refund_info
            #                     item['is_support_part_refund'] = is_support_part_refund
            #                     item['is_support_ins_append'] = is_support_ins_append
            #                     item['status'] = status
            #                     yield item
        except Exception, e:
            error_info = Exception, e
            print error_info
