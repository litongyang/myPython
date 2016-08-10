# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class SinaStockUrlUsItem(scrapy.Item):
    company_code = Field()  # 新闻所属公司代码
    company_code_other = Field()  # 新闻所属公司港股代码
    news_time = Field()  # 新闻的发布时间
    news_title = Field()  # 新闻标题
    news_url = Field()  # 新闻的url


class SinaStockNewsUsItem(scrapy.Item):
    company_code = Field()  # 公司代码
    company_code_other = Field()  # 公司在其他市场的交易代码
    company_name = Field()  # 公司名称
    issue_time = Field()  # 发布时间
    content_html = Field()  # 新闻内容html
    abstract = Field()  # 新闻摘要
    news_title = Field()  # 新闻标题
    source_name = Field()  # 新闻来源
    news_time = Field()  # 新闻创建时间
    author = Field()  # 新闻作者
    news_url = Field()  # 新闻的url
    crawl_time = Field()  # 新闻抓取时间
