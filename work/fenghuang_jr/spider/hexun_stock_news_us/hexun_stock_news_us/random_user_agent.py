# __author__ = 'lty'
# -*- coding: utf-8 -*-
import random


class RandomUserAgentMiddleware(object):

    def process_request(self, request, spider):
        ua = ['Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0']
        request.headers.setdefault('User-Agent', ua)
