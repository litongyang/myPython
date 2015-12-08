# -*- coding: utf-8 -*-
from tabulate import tabulate
# x= [1,2,3,4,5,1,3,3]
# myset = set(x)
# print myset
# for item in myset:
#     print x.count(item), " of ", item, " in list"

# ----正则----
# 1975/09/9(\d{4})
# import re
# x = '1975/09/9'
# regex = ur"\d{4}"
# match = re.match(r'\d{4}', x)
# print match.group(0)


# from sklearn import linear_model
# X = [[0., 0.], [1., 1.], [2., 2.], [3., 3.]]
# Y = [0., 1., 2., 3.]
# clf = linear_model.BayesianRidge()
# clf.fit(X, Y)

# import numpy as np
# import random
# import matplotlib.pylab as plt
#
# x = [1, 2, 3, 6, 101, 100]
# n = int(float(len(x))*0.5)
# print n
# y = random.sample(x, n)
# print y
# plt.hist(y)
# plt.show()

# list 转置
# a = [ [1,2,3], [4,5,6], [7,8,9]]
# print a
# print map(list, zip(*a))




# import scipy
# import sklearn

#
# from sklearn import datasets
# from sklearn import decomposition
# import matplotlib.pyplot as plt
# iris = datasets.load_iris()
# print iris.data
# pca = decomposition.PCA(n_components=2)
# pca_result = pca.fit_transform(iris.data)
# print pca_result
# plt.show()

# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )
# import json
# import re
# import urllib2
# import requests
# import types
# import urllib
# from urllib import urlencode
# from urllib import quote
# fl = open("C:\\Users\\\Thinkpad\\Desktop\\test.txt", 'w')
# # url = "http://data.stats.gov.cn/easyquery.htm?cn=A01"
# url = "http://data.stats.gov.cn/easyquery.htm?cn=B01"
# response = urllib2.urlopen(url)
# print response
# # html = response.read()
# html = requests.get(url)
#
# data = html.text
# # print data
# link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", data)
# for url1 in link_list:
#     print url1
# # match = re.match(r'<li><a href="/search.htm?s=农村居民家庭人均纯收入">农村居民家庭人均纯收入</a></li>', data)
# # print match.group(0)
# # print type(html)
# # print html
# fl.write(data)



# ! /usr/bin/env python
# -*- coding=utf-8 -*-
# @Author pythontab.comn
# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )
# import urllib2
# fl = open("C:\\Users\\\Thinkpad\\Desktop\\test.txt", 'w')
# url="http://data.stats.gov.cn/easyquery.htm?cn=A01"
# req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
# 'Accept':'text/html;q=0.9,*/*;q=0.8',
# 'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
# 'Accept-Encoding':'gzip',
# 'Connection':'close',
# 'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
# }
# req_timeout = 5
# req = urllib2.Request(url,None,req_header)
# resp = urllib2.urlopen(req,None,req_timeout)
# html = resp.read()
# print html
# fl.write(html)

import urllib2
import chardet
import json
import requests
import StringIO
import gzip

try:
    print int(None)
except:
    print 2
# url = "http://xueqiu.com/S/SZ000003"
# req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0',
#                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#                            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#                            'Accept-Encoding': 'gzip, deflate',
#                            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
#                            'Connection': 'keep-alive',
#                            'Cookie': 's=vnw12f2ga9; __utma=1.117406079.1444787307.1448854251.1448867323.98; __utmz=1.1448854251.97.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_1db88642e346389874251b5a1eded6e3=1448602155,1448792074,1448850399,1448854252; bid=a6f34af86ba79e86c2f9b2f0ef1b8e54_ifq4xlp9; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1448867332; __utmc=1; last_account=lty369963%40sina.com; xq_a_token=077324eba92f407349bb2ae35e87af7eb6c71cb9; xq_r_token=ac9129a23277d00eb85f86889f2a27ab65173144; u=1062948460; xq_token_expire=Fri%20Dec%2025%202015%2015%3A08%3A17%20GMT%2B0800%20(CST); xq_is_login=1; xqat=077324eba92f407349bb2ae35e87af7eb6c71cb9; __utmb=1.2.10.1448867323; __utmt=1',
#                            'Host': 'xueqiu.com'}
# req = urllib2.Request(url, headers=req_header)
# resp = urllib2.urlopen(req)
# html = resp.read()
# compressedstream = StringIO.StringIO(html)
# gziper = gzip.GzipFile(fileobj=compressedstream)
# jsondata = gziper.read()
# print jsondata

# import StringIO, gzip
# url = "http://www.sina.com.cn/"
# req = urllib2.Request(url)
# html = urllib2.urlopen(req).read()
# compressedstream = StringIO.StringIO(html)
# gziper = gzip.GzipFile(fileobj=compressedstream)
# data = gziper.read()
# print data

