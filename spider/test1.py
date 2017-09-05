
# -*- coding:utf-8 -*-
from selenium import webdriver
import sys
import os, time
from lxml import etree
from bs4 import BeautifulSoup
import re

# help(webdriver.Firefox)
# dr = webdriver.Chrome()
# os.environ["webdriver.chrome.driver"] = '/Applications/Firefox.app/Contents/MacOS/geckodriver'
dr = webdriver.Firefox(executable_path='/Applications/Firefox.app/Contents/MacOS/geckodriver')
time.sleep(5)
print 'Browser will close.'
dr.quit()

# time.sleep(5)
# browser.get(
#     'https://list.tmall.com/search_product.htm?spm=875.7931836/B.subpannel2016052.17.10c849dapHmBDu&pos=1&cat=50918004&vmarket=97602&theme=699&acm=2016031451.1003.2.720492&scm=1003.2.2016031451.OTHER_1463390981979_720492')
#
# URLS = []
#
# time.sleep(5)
# html = browser.page_source
# # print html
#
#
# html = html.decode('utf-8')
# selector = etree.HTML(html.decode('utf-8'))
#
# urls = selector.xpath('//div[@class="productTitle productTitle-spu"]/a/@href')
# for url in urls:
#     url = 'https:' + url
#     print url
#     # print urls