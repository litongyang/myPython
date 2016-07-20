# __author__ = 'tongyang.li'
# coding=utf-8

"""
模拟post 请求
(以网贷之家为例)
"""
import urllib
import urllib2


body = {'custom': '0,3,4,8', 'endTime': '2016-06-22', 'startTime': '2016-06-16', 'status': '1'}
url = 'http://shuju.wdzj.com/platdata-custom.html'
post_data = urllib.urlencode(body)
req = urllib2.urlopen(url, post_data)
content = req.read()
print content

