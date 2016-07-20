# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import HTMLParser
import urllib2


class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        # 这里重新定义了处理开始标签的函数
        if tag == 'a':
            # 判断标签<a>的属性
            for name,value in attrs:
                if name == 'href':
                    print value
    # def handle_endtag(self, tag):

if __name__ == '__main__':
    # a = '<html><head><title>test</title><body><a href="http://www.163.com">链接到163</a></body></html>'
    # a = '<a href="/invest/detail?id=68152367134654464">企业贷68152367134654464</a>'
    data = urllib2.urlopen('https://www.xiaoying.com/invest/list?p1=2').read()
    my = MyParser()
    # 传入要分析的数据，是html的。
    my.feed(data)