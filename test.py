# -*- coding: utf-8 -*-
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

# ----------多线程 ------------
# import threading
# from time import ctime,sleep
#
# class X:
#     def A(x):
#         print "A", x
#
#     def B(x):
#         print "B",x
#
#     def C(self,b, e):
#         for i in range(b, e):
#             print i
#
#     def T(self, fun):
#         threads = []
#         t1 = threading.Thread(target=fun, args=(0,2))
#         threads.append(t1)
#         t2 = threading.Thread(target=fun, args=(2,10))
#         threads.append(t2)
#         for t in threads:
#             # t.setDaemon(True)
#             t.start()
#         for t in threads:
#             t.join()
# if __name__ == '__main__':
#     w = X()
#     w.T(w.C)
#     # threads = []
#     # t1 = threading.Thread(target=w.C, args=(0,2))
#     # threads.append(t1)
#     # t2 = threading.Thread(target=w.C, args=(2,10))
#     # threads.append(t2)
#     # for t in threads:
#     #     # t.setDaemon(True)
#     #     t.start()
#
#     # print "all over %s" %ctime()

import re
# html = "企业在日常活动中形成的、会导致所有者权益增加的、与所有者投入资本无关的经济利益的总流入称为（<h1>D</h1>）"
# html1 = html.split("(")
# print html1[0]
# s= "[单选]"
# regex_t = ur"[(.*?)]<br>"
# reobj_t = re.compile(regex_t)
# match_t = reobj_t.search(html)
# if match_t:
#     data_t = match_t.group(0)
#     print data_t
# else:
#     print "lty"


import urllib2
import re
import chardet
import json
import StringIO
import gzip

# money_supply = [[0] * 131] * 1
# print money_supply[0]
# industry1 =[[]]*3
# industry1 = [[] for i in range(3)]
# for i in range(0,len(industry1)):
#     for j in range(0,2):
#         industry1[i].append(j)
# for k in range(0,len(industry1)):
#     print industry1[k]


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
# a = '13亿'
# if a.find("亿") != -1:
#     x = float(a.replace("亿","")) * 100000000
#     print x
# info =
# print float(a)
import re
# x = "<h3>第一部分  基础综合</h3><ul><li><a href='/subjects/content/358_1_1_0'>"
# i =1
# r= ur"<h3>(.*?)<a href=\'\/subjects\/content\/358_%s_1_0'>" % i
# reobj_book = re.compile(r)
# match_book = reobj_book.search(x)
# if match_book:
#     print "da"







# x = "    dsadas"
# r = ur"\s+"
# reobj = re.compile(r)
# m = reobj.search(x)
# if m:
#     t = m.group(0)
#     y = x.replace(t,"")
#     print y
# print x.replace(ur"\s+","")
# x = {A;}
# url_id = "472-0-2-0-234"
# url_id_temp = url_id.split('-')
# x = ""
# for i in url_id_temp:
#     x += str("%04d" % int(i)) + "-"
# print x[0: len(x)-1]
# book = [i for i in range(260)]
# print book
# x[0]["q"] =1
# print x[2]

from collections import Counter
# x = { 'apple': 1, 'banana': 2 }
# y = { 'banana': 10, 'pear': 11 }
# d = {key:value*2 for key,value in x.items()}
# print d
# import matplotlib.pylab as plt
# import seaborn as sns
# data1 = [1,1,1,2,2,2,3,4,4,5,6,6,6]
# sns.distplot(data1, kde=True, color="#FF0000", rug=True, hist=True)
# plt.show()
# X,Y = Counter(x), Counter(y )
# print X z = dict(2*X+Y)
#
# for k,v in z.items():
#     print k,v

from distutils.core import setup
# import py2exe
# x= 5
# if 0<x<=10:
#     print "lty"
# else:
#     print "wl"


import chardet

try:
    content = "新人红包"
    my_char = chardet.detect(content)
    print my_char
    bian_ma = my_char['encoding']
    content = content.decode(bian_ma, 'ignore').encode('ISO-8859-1')
    print content
    print content
except Exception, e:
    print Exception, e
