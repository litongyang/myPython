# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class MyspiderItem(scrapy.Item):
    title = Field()
    # define the fields for your item here like:

