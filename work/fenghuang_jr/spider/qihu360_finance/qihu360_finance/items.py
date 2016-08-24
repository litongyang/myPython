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
    url = Field()

