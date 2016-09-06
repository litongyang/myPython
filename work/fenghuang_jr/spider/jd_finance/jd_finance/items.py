# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class JdFinanceDetailItem(scrapy.Item):
    id = Field()  # id
    sku_id = Field()  # skuid
    title = Field()  # 产品名称
    amount = Field()  # 募集金额
    available = Field()  # 当前可投资金额
    next_open_date = Field()  # 下一次开标日期
    item_type = Field()  # 产品类型id
    type_name = Field()  # 产品类型名称
    merchant_id = Field()  # 交易中心id
    merchant_name = Field()  # 交易中心id
    step_amount = Field()  # 每笔投资单位金额
    min_amount = Field()  # 最小投资金额
    max_amount = Field()  # 最大投资金额
    sale_begin_date = Field()  # 起售时间
    sale_end_date = Field()  # 截止时间
    begin_date = Field()  # 计息时间
    end_date = Field()  # 到期时间
    rate = Field()  # 收益率
    period_type = Field()  # 期限类型
    period_value = Field()  # 期限值
    status = Field()  # 产品状态
    create_time = Field()  # 创建时间
    update_time = Field()  # 更新时间
    label_info = Field()  # 赎回说明
    repayment_type = Field()  # 偿还类型
    interest_type = Field()  # 利息类型
    version_id = Field()  # 版本id
    ts = Field()  # 爬取时间

