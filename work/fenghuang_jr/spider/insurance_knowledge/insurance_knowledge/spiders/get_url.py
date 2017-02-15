# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
获去保险列表页所以url
"""


class GetUrl:
    def __init__(self):
        self.num = 800
        self.url_head = 'http://www.xyz.cn/study/list-76-'
        self.url_tail = '.html'
        self.url_list = []

    def get_url(self):
        try:
            for i in range(1, self.num + 1):
                url = str(self.url_head) + str(i) + str(self.url_tail)
                self.url_list.append(url)
            return self.url_list
        except Exception, e:
            print Exception, e

if __name__ == '__main__':
    test = GetUrl()
    test.get_url()
