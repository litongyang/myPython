# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# -----在雪51做题网抓取题库和答案-----------------------------
#
# ------------------------------------------------------------

import re
import urllib2
import socket
import json
import datetime
import MySQLdb
import threading
import warnings

warnings.filterwarnings("ignore")


class ZuoTi51:
    def __init__(self):
        self.try_cnt = 3
        self.book = [358]
        self.part = [i for i in range(0,5)]
        self.chapter = [i for i in range(0,30)]
        self.section = [i for i in range(0,10)]
        # self.url_book_set = {}
        # self.url_chapter_set = {}
        self.url_set = {}
        self.req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/43.0',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           # 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                           'Accept-Encoding': 'gzip, deflate',
                           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                           'Connection': 'keep-alive',
                           'Cookie': 'GM9C_lastvisit=1450769372; GM9C_sid=1jhXbj; GM9C_lastact=1450773695%09home.php%09misc; __utma=28681848.1095521665.1450773082.1450773082.1450782072.2; __utmz=28681848.1450773082.1.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); '
                                     'a7538_times=2; PHPSESSID=qiqq4itqvue3ep5ru1jlt1a381; a7538_pages=2; __utmb=28681848__utmc=28681848',
                           'Host': 'www.51zuoti.com'}

    # 获取所有url
    def get_url(self):
        # url_chapter = "http://www.51zuoti.com/chapter_list.php?book=140"
        # url_chapter = "http://www.51zuoti.com/bookStructures/index/140"
        book_name = ""
        for bookid in self.book:
            try:
                url_book = "http://www.51zuoti.com/bookStructures/index/%s" % bookid
                req_book = urllib2.Request(url_book, headers=self.req_header)
                resp_book = urllib2.urlopen(req_book, timeout=10)
                html_book = resp_book.read()
                regex_book = ur"<title>(.*?)</title>"
                reobj_book = re.compile(regex_book)
                match_book = reobj_book.search(html_book)
                if match_book:
                    book_name = match_book.group(1)
                    print book_name
            except:
                pass
            for partid in self.part:
                for chapterid in self.chapter:
                    for sectionid in self.section:
                        url = "http://www.51zuoti.com/get_subject.php?book=%s&part=%s&chapter=%s&section=%s&category=1257a&review_type=1&try_count=4&Number=1450782297127"\
                              %(bookid,partid,chapterid,sectionid)
                        print url
                        self.url_set[book_name] = url
        # url = "http://www.51zuoti.com/get_subject.php?book=140&part=0&chapter=2&section=0&category=1257a&review_type=1&try_count=4&Number=1450782297127"
        # self.url_chapter_set["u"] = url_chapter
        # self.url_set["u"] = url
        for k, v in self.url_set.items():
            print k, v

    def get_data_test(self):
        url = "http://www.51zuoti.com/bookStructures/index/140"
        req = urllib2.Request(url, headers=self.req_header)
        resp = urllib2.urlopen(req, timeout=10)
        html = resp.read()
        print html
        # regex_s_a = ur"index\:(.*?),href\:"
        # reobj_s_a = re.compile(regex_s_a)
        # match_s_a = reobj_s_a.search(html)
        # if match_s_a:
        #     print match_s_a.group(1)

    # 获取题库数据
    # noinspection PyBroadException
    def get_data(self):
        for company_code, url in self.url_set.items():
            req = urllib2.Request(url, headers=self.req_header)
            resp = urllib2.urlopen(req, timeout=10)
            html = resp.read()
            print html
            # 题型
            temp = html.split("<br>")
            question_type = temp[0]
            print question_type
            # 答案
            regex_a = ur"<h1>(.*?)</h1>"
            reobj_a = re.compile(regex_a)
            match_a = reobj_a.search(html)
            if match_a:
                data_a = match_a.group(1)
                print data_a
            # 题目
            regex_s_a = ur"<p>(.*?)</p>"
            reobj_s_a = re.compile(regex_s_a)
            match_s_a = reobj_s_a.search(html)
            if match_s_a:
                data_s_a = match_s_a.group(1)
                if data_s_a.find(data_a):
                    temp = "<h1>" + data_a + "</h1>"
                    data_s = data_s_a.replace(temp, "")
                    print data_s
            # 选项
            alphabet_match = {
                '0': "A",
                '1': "B",
                '2': "C",
                '3': "D",
                '4': "E",
                '5': "F",
            }
            data_o = []
            for i in range(0, 6):
                choice_one = ""
                regex_o = ur"<a href=\"javascript\:s_select\(\'%s\'\)\">(.*?)</a>" % i
                reobj_o = re.compile(regex_o)
                match_o = reobj_o.search(html)
                if match_o:
                    # print match_o.group(1)
                    # print alphabet_match[str(i)]
                    choice_one += alphabet_match[str(i)]
                    choice_one += ":"
                    choice_one += match_o.group(1)
                    data_o.append(choice_one)
            print data_o
            # 解析
            regex_an = ur"<h2>(.*?)</h2>"
            reobj_an = re.compile(regex_an)
            match_an = reobj_an.search(html)
            if match_an:
                data_an = match_an.group(1)
                print data_an


if __name__ == '__main__':
    source = ZuoTi51()
    source.get_url()
    source.get_data_test()
    # source.get_data_test()
    # source.get_data()
