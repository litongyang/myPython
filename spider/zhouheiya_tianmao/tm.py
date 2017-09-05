# -*- coding:utf-8 -*-
from selenium import webdriver
import sys
import os, time
import create_table
from lxml import etree
from bs4 import BeautifulSoup
import re

reload(sys)
sys.setdefaultencoding('utf-8')

# 也可以用chrome或者PhantomJS，这两个要装驱动
# chromedriver = "D:\WorkSpace\cefpython\chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver
# browser = webdriver.Chrome(chromedriver)
# OSX上我没试过，Windows和linux，版本正确的好，Firefox不需要装驱动
create_tables = create_table.CreateTable()
browser = webdriver.Firefox()
# time.sleep(5)
url_bid = [
    'https://zhouheiya.tmall.com/category.htm?spm=a1z10.3-b-s.w5001-14819609427.5.46f16db06oFhe0&search=y&scene=taobao_shop',
    'https://zhouheiya.tmall.com/category.htm?spm=a1z10.3-b-s.w4011-14819609434.245.46f16db0F7didM&search=y&scene=taobao_shop&pageNo=2#anchor',
]
url_list = []
names_list = []
count_all_list = []
evaluate_list = []
for bid in url_bid:
    browser.get(str(bid))
    time.sleep(5)
    html = browser.page_source
    html = html.decode('utf-8')
    selector = etree.HTML(html.decode('utf-8'))
    urls = selector.xpath('//div[@class="item5line1"]/dl/dt/a/@href')
    names = selector.xpath('//div[@class="item5line1"]/dl/dd[@class="detail"]/a')
    count_all = selector.xpath('//div[@class="item5line1"]/dl/dd[@class="detail"]/div[1]/div[2]/span')
    evaluates_cnt = selector.xpath('//div[@class="item5line1"]/dl/dd[@class="rates"]/div[1]/h4/a/span')

    # print "sssss", len(urls)
    for i in range(0, len(evaluates_cnt)):
        try:
            url = 'https:' + urls[i]
            url_list.append(url)
            names_list.append(names[i].text)
            count_all_list.append(count_all[i].text)
            evaluate_cnt = str(evaluates_cnt[i].text).replace('评价: ', '')
            evaluate_list.append(evaluate_cnt)
        except:
            pass

for j in range(0, len(evaluate_list)):
    insert_sql = ''
    insert_sql += '\'' + str(names_list[j]) + '\'' + ','
    insert_sql += '\'' + str(url_list[j]) + '\'' + ','
    insert_sql += '\'' + str(count_all_list[j]) + '\'' + ','
    insert_sql += '\'' + str(evaluate_list[j]) + '\'' + ','
    insert_sql = insert_sql[0:-1]
    create_tables.insert_sql('zhouheiya_tianmao_url', insert_sql)

