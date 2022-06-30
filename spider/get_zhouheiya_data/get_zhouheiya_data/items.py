# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class GetZhouheiyaDataItem(scrapy.Item):
    longitude = Field()
    latitude = Field()
    name = Field()
    address = Field()
    id = Field()
    address_id = Field()


class GetDictItem(scrapy.Item):
    content = Field()