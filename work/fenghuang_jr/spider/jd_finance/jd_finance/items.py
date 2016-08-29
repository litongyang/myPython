# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class JdFinanceDetailItem(scrapy.Item):
    id = Field()  # id
    title = Field()  # 产品名称
    amount = Field()  # 募集金额
    buy_amount = Field()  # 当前募集总额
    merchant_id = Field()  # 购买方ID
    merchant_name = Field()  # 购买方名称
    insurance_code = Field()  # 担保方id
    insurance_name = Field()  # 担保方名称
    insurance_type = Field()  # 保险类型
    insurance_type_name = Field()  # 保险类型名称
    min_amount = Field()  # 最低投资金额
    max_amount = Field()  # 最高投资金额
    max_num = Field()  # 最多购买数量
    days = Field()  # 期限
    sale_begin_date = Field()  # 售卖开始时间
    sale_end_date = Field()  # 售卖截止时间
    rate = Field()  # 历史收益率
    refund_info = Field()  # 退款说明
    is_support_part_refund = Field()  # 是否支持持有期之前退款
    is_support_ins_append = Field()  # 是否支持追加
    status = Field()  # 标的状态

