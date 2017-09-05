# -*- coding:utf-8 -*-
from selenium import webdriver
import sys
import os, time
from lxml import etree
import create_table
from bs4 import BeautifulSoup
import re
reload(sys)
sys.setdefaultencoding('utf-8')
create_tables = create_table.CreateTable()
browser = webdriver.Firefox()
urls = []
price_list = []
sale_cnt = []
sales = []
# urls = ['https://detail.tmall.com/item.htm?id=45055385354&rn=7232d9e0497a989c604c3ef339433c47&abbucket=0']


def get_url():
    url = []
    create_tables.cur.execute('set names \'utf8\'')
    sql = create_tables.cur.execute('select url from zhouheiya_tianmao_url')
    results = create_tables.cur.fetchmany(sql)
    for i in range(0, len(results)):
        url.append(results[i][0])
    return url

url_list = get_url()
for i in range(80, 110):
    print url_list[i]
    urls.append(url_list[i])
    browser.get(str(url_list[i]))
    time.sleep(5)
    html = browser.page_source
    html = html.decode('utf-8')
    selector = etree.HTML(html.decode('utf-8'))
    cnt = selector.xpath('//div[@class="tm-indcon"]/span[@class="tm-count"]')
    price = selector.xpath('//div[@class="tm-promo-price"]/span[@class="tm-price"]')
    if len(price) == 0:
        price = selector.xpath('//dd/span[@class="tm-price"]')
    print cnt[0].text, price[0].text
    print "======================"
    for j in range(0, len(price)):
        try:
            price_list.append(price[j].text)
            sale_cnt.append(cnt[j].text)
        except:
            pass
for k in range(0, len(price_list)):
    sales.append(float(price_list[k]) * int(sale_cnt[k]))
# print len(urls)
# print len(sale_cnt)
# print len(sales)
# print price_list
for i in range(0, len(urls)):
    insert_sql = ''
    insert_sql += '\'' + str(urls[i]) + '\'' + ','
    insert_sql += '\'' + str(price_list[i]) + '\'' + ','
    insert_sql += '\'' + str(sale_cnt[i]) + '\'' + ','
    insert_sql += '\'' + str(sales[i]) + '\'' + ','
    insert_sql = insert_sql[0:-1]
    create_tables.insert_sql('zhouheiya_tianmao_bid', insert_sql)


