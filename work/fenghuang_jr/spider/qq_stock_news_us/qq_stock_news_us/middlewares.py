# # __author__ = 'tongyang.li'
# # -*- coding: utf-8 -*-
#
# from urllib import urlencode
# import urllib2
# import random
# import base64
# from settings import PROXIES
# import sys
# sys.setdefaultencoding('gbk')
#
#
# class ProxyMiddleware(object):
#
#     def process_request(self, request, spider):
#         proxy = random.choice(PROXIES)
#         # if proxy['user_pass'] is not None:
#         #     x = "http://%s" % proxy['ip_port']
#         #     request.meta['proxy'] = "http://%s:%s" % (proxy['ip_port'], proxy['port'])
#         #     # request.meta['proxy'] = urllib2.ProxyHandler({'http': '122.96.59.104:80'})
#         #     y = request.meta['proxy']
#         #     encoded_user_pass = base64.encodestring(proxy['user_pass'])
#         #     # request.headers.setdefault('proxy', x)
#         #     request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
#         #     print "**************ProxyMiddleware have pass************" + proxy['ip_port']
#         # else:
#         print "**************ProxyMiddleware no pass************" + proxy['ip']
#         x = 'http://%s:%d' % (proxy['ip'], proxy['port'])
#         request.meta['proxy'] = x
#
#
