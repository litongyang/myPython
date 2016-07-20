# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


#  公司公告 item
class NoticeItem(scrapy.Item):
    company_code = Field()  # 公司编码
    company_name = Field()  # 公司名称
    notice_title = Field()  # 公告标题
    notice_type = Field()   # 公告类型
    notice_title_link = Field()   # 公告标题链接
    notice_date = Field()  # 公告日期


# 公司研报 item
class ResearchItem(scrapy.Item):
    company_code = Field()  # 公司编码
    company_name = Field()  # 公司名称
    research_title = Field()  # 研报标题
    research_date = Field()  # 研报日期
    ins_name = Field()  # 机构名称
    ins_star = Field()  # 机构等级
    rating_name = Field()  # 评级名称
    rating_change = Field()  # 评级改变
    author = Field()  # 作者
    profit_year = Field()  # 收益起始年份
    pe_list = Field()  # 预测市盈率
    per_share_list = Field()  # 预测每股收益
    net_profit_list = Field()  # 预测净利润
    research_url = Field()  # 研报url



