# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class Qihu360FinanceUrlItem(scrapy.Item):
    url = Field()
    status = Field()


class Qihu360FinanceDetailItem(scrapy.Item):
    url = Field()  # 产品详情url
    title = Field()  # 产品标题
    ratio = Field()  # 预期收益率
    days = Field()  # 期限
    repay_method = Field()  # 收益方式
    start_date = Field()  # 起息日期
    end_date = Field()  # 到期日期
    profit_date = Field()  # 发放日
    available = Field()  # 当前可投资金额
    amount = Field()  # 募集金额
    min_amount_info = Field()  # 起投金额信息

