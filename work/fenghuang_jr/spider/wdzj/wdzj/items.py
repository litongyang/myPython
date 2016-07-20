# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class PreferenceItem(scrapy.Item):
    item_type = Field()  # item的类型：判别来源那个网址
    company_name = Field()  # 公司名称
    url = Field()  # url
    core_index_name = Field()  # 核心指标名称
    core_index_data = Field()  # 核心指标数据
    index_preference_data = Field()  # 投资偏好数据


class BasicItem(scrapy.Item):
    item_type = Field()  # item的类型：判别来源那个网址
    company_name = Field()  # 公司名称
    url = Field()  # url
    last_90day_type_name = Field()  # 近90日标的类型名称
    last_90day_type_data = Field()  # 近90日标的类型数据
    last_90day_deadline_name = Field()  # 近90日标的期限名称
    last_90day_deadline_data = Field()  # 近90日标的期限数据
    last_90day_amount_name = Field()  # 近90日标的金额数据
    last_90day_amount_data = Field()  # 近90日标的金额数据


class ArchivesItem(scrapy.Item):
    item_type = Field()
    company_name = Field()  # 公司名称
    type = Field()
    status = Field()
    url = Field()  # url
    interest_rate_volume_date = Field()  # 利率和成交量的日期
    interest_rate_day = Field()  # 利率每日信息
    volume_day = Field()  # 成交量每日信息
    pending_repayment_inflow_date = Field()  # 历史待还和净流入的日期
    pending_repayment_history_day = Field()  # 历史待还每日信息
    net_inflow_day = Field()  # 净流入每日信息
    invest_loan_user_date = Field()  # 投资人数和借款人数的日期
    invest_user_day = Field()  # 投资人数每日信息
    loan_user_day = Field()  # 借款人数每日信息


