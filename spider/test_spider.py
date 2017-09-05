# __author__ = 'lty'
# -*- coding: utf-8 -*-

import re
import urllib2
import MySQLdb
import warnings
import gzip
from StringIO import StringIO


def gzip1(data):
    buf = StringIO(data)
    f = gzip.GzipFile(fileobj=buf)
    return f.read()


class Test:
    def __init__(self):
        self.try_cnt = 3
        self.url_set = {}
        self.req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/43.0',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate, br',
                           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                           'Connection': 'keep-alive',
                           'upgrade - insecure - requests': 1,
                           'Cache - Control':'max - age = 0',
                           'Cookie':'d413cee3f267af25e4f2; _tb_token_=fed567e3eb9ce; cna=bgszEPsGwUgCAWomMOJtJnry; pnm_cku822=059UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5Ockp3S3JGe057RHFPdSM%3D%7CU2xMHDJ7G2AHYg8hAS8XIw0tA0QtRmg%2BaA%3D%3D%7CVGhXd1llXWBcZVFsWWxTZlhiVWhKf0B7Rn9Lckl9RntCdkh2T2E3%7CVWldfS0TMwczDi4bOxVkK3Bbe0VlWXchdw%3D%3D%7CVmhIGCYdPQE8AiIeIRQpCTcCNwkpFSwVKAg8ATwcIBkgHT0IMgxaDA%3D%3D%7CV25Tbk5zU2xMcEl1VWtTaUlwJg%3D%3D; cq=ccp%3D1; isg=And3GmuX4jD7hWa8fK77jZz7Bm3Lwjeqp-2768kkt8ateJe60Qzb7jXaLO7d',
                           'Referer':'https://zhouheiya.tmall.com/category.htm?spm=a1z10.3-b-s.w5001-14819609427.5.1ded7572LsgwAk&search=y&scene=taobao_shop',
                           'Host': 'zhouheiya.tmall.com'}

    def test(self):
        print "wwww"
        url_chapter_list = "https://www.zhouheiya.cn/index.php/index-show-tid-5.html?id=0-9-1-3"
        req_chapter_list = urllib2.Request(url_chapter_list)
        resp_chapter_list = urllib2.urlopen(req_chapter_list, timeout=10)
        x = resp_chapter_list.read()
        print x
        # encoding = resp_chapter_list.info().get('Content-Encoding')
        # print encoding
        # y = gzip1(x)
        # print y
        print "sssss"



if __name__ == '__main__':
    test1 = Test()
    test1.test()