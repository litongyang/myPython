# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class SinaStockUrlUsItem(scrapy.Item):
    news_url = Field()
    news_title = Field()
    news_time = Field()

class SinaStockNewsUsItem(scrapy.Item):
    news_html = Field()
