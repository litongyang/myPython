# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class GuomeiFinanceDetailItem(scrapy.Item):
    id = Field()  # 产品id
    title = Field()  # 产品名称
    repay_method = Field()  # 偿还方式:BulletRepayment(一次性偿还)
    amount = Field()  # 产品募集金额
    rate = Field()  # 产品预期收益率
    days = Field()  # 产品期限天数
    min_amount = Field()  # 最小投资金额
    max_amount = Field()  # 最大投资金额
    step_amount = Field()  # 每笔投资单位金额
    time_open = Field()  # 开标时间
    date_open = Field()  # 开标日期
    time_finished = Field()  # 关标时间
    bid_number = Field()  # 投资人数
    invest_amount = Field()  # 投资金额
    status = Field()  # 标的状态
    invest_percent = Field()  # 当前进度
    available = Field()  # 当前可投资金额
    ts = Field()  # 爬取时间
