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


def str_add_marks(myStr, word):
    myStr_result = myStr
    for i in range(0, len(word)):
        if myStr_result.find(str(word[i])) != -1:
            temp = "\"" + word[i] + "\""
            myStr_result = myStr_result.replace(word[i], temp)
    return myStr_result


class ZuoTi51:
    def __init__(self):
        self.try_cnt = 3
        # self.book = [358]
        self.book = [140]
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
        self.info_chapter = []  # 章节信息
        self.subject_info = {}  # 答案信息

        self.db_name = 'test'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.companyData_oneDay_fileName = 'zuoti_51'


    # # 字符加引号
    # # noinspection PyPep8Naming
    # @staticmethod
    # def str_add_marks(myStr, word):
    #     if myStr.find(word) != -1:
    #         temp = "'" + word + "'"
    #         myStr = myStr.replace(word, temp)
    #         return myStr

    # 数据处理
    def data_process_chapter(self):
        for bookid in self.book:
            part = []
            # subject_cnt = 0
            try:
                url_chapter_list = "http://www.51zuoti.com/chapter_list.php?book=%s" % bookid
                req_chapter_list = urllib2.Request(url_chapter_list, headers=self.req_header)
                resp_chapter_list= urllib2.urlopen(req_chapter_list, timeout=10)
                chapter_list = resp_chapter_list.read()
                words = ['index','href','total','did','finish','process','review','uiProvider','cls','leaf','children','true','false']
                # print chapter_list
                temp = str_add_marks(chapter_list, words)
                data_json = eval(temp)
                # print type(data_json[0])

                for i in range(0, len(data_json)):
                    info_chapter = {
                       "bookid": [],
                       "chapter": [],
                       "section": [],
                       "code_list_chapter": [],
                       "code_list_section": [],
                       "chapter_subject_cnt": [],
                       "subject_cnt": []
                    }  # 一条信息
                    for k, v in data_json[i].items():
                        # info_chapter['bookid'].append(bookid)
                        if k == 'index':  # 第一层index
                            x = v
                            # print v
                            info_chapter['bookid'].append(bookid)
                            info_chapter['chapter'].append(v)
                        if k == 'href':
                            regex_code = ur"\((.*?)\)"
                            reobj_code = re.compile(regex_code)
                            match_code = reobj_code.search(v)
                            if match_code:
                                code = match_code.group(1)
                                code_list = code.split(',')
                                info_chapter['code_list_chapter'].append(code_list)
                                # print code_list
                                # if int(code_list[2]) == 0:
                                #     part.append()
                        if k == 'total':
                            # print v1
                            regex_cnt = ur"[0-9]*"
                            reobj_cnt = re.compile(regex_cnt)
                            match_cnt = reobj_cnt.search(v)
                            if match_cnt:
                                chapter_subject_cnt = int(match_cnt.group(0))
                                info_chapter['chapter_subject_cnt'].append(chapter_subject_cnt)
                                # print subject_cnt
                        elif k == 'children':
                            # print v
                            for j in range(0, len(v)):
                                for k1, v1 in v[j].items():
                                    if k1 == 'index':  # 第二层index
                                        # print x,v1
                                        info_chapter['section'].append(v1)
                                    if k1 == 'href':
                                        regex_code_section = ur"\((.*?)\)"
                                        reobj_code_section = re.compile(regex_code_section)
                                        match_code_section = reobj_code_section.search(v1)
                                        if match_code_section:
                                            code = match_code_section.group(1)
                                            code_list_section = code.split(',')
                                            # print code_list_section
                                            info_chapter['code_list_section'].append(code_list_section)
                                    if k1 == 'total':
                                        # print v1
                                        regex_cnt = ur"[0-9]*"
                                        reobj_cnt = re.compile(regex_cnt)
                                        match_cnt = reobj_cnt.search(v1)
                                        if match_cnt:
                                            subject_cnt = int(match_cnt.group(0))
                                            info_chapter['subject_cnt'].append(subject_cnt)
                                            # print subject_cnt

                    # for k,v in info_chapter.items():
                    #     # print k,v
                    #     for i in range(0, len(v)):
                    #         print k , v[i]
                    # print "*****"
                    self.info_chapter.append(info_chapter)
                # print chapter_list
            except:
                pass

    # 获取所有url
    def get_url(self):
        for info_chapter_one in self.info_chapter:
            for k,v in info_chapter_one.items():
                # print k,v
                if k == 'section':
                    if len(v):  # 有section部分
                        for i in range(0, len(info_chapter_one['code_list_section'])):
                            # print info_chapter_one['subject_cnt'][i]
                            for cnt in range(0, int(info_chapter_one['subject_cnt'][i])):
                                url = "http://www.51zuoti.com/get_subject.php?book=%s&part=%s&chapter=%s&section=%s&category=1257a&review_type=1&try_count=%s" \
                                    "&Number=1450831519888" % (info_chapter_one['code_list_section'][i][0],
                                                               info_chapter_one['code_list_section'][i][1],
                                                               info_chapter_one['code_list_section'][i][2],
                                                               info_chapter_one['code_list_section'][i][3],
                                                               str(cnt))
                                url_id = str(info_chapter_one['code_list_section'][i][0]) + "-"\
                                         + str(info_chapter_one['code_list_section'][i][1]) + "-"\
                                         + str(info_chapter_one['code_list_section'][i][2]) + "-"\
                                         + str(info_chapter_one['code_list_section'][i][3]) + "-"\
                                         + str(cnt)
                                self.url_set[url_id] = url
                    else:  # 没有section部分
                        for i in range(0, len(info_chapter_one['code_list_chapter'])):
                            for cnt in range(0, int(info_chapter_one['chapter_subject_cnt'][i])):
                                url = "http://www.51zuoti.com/get_subject.php?book=%s&part=%s&chapter=%s&section=%s&category=1257a&review_type=1&try_count=%s" \
                                    "&Number=1450831519888" % (info_chapter_one['code_list_chapter'][i][0],
                                                               info_chapter_one['code_list_chapter'][i][1],
                                                               info_chapter_one['code_list_chapter'][i][2],
                                                               info_chapter_one['code_list_chapter'][i][3],
                                                               str(cnt))
                                url_id = str(info_chapter_one['code_list_chapter'][i][0]) + "-"\
                                         + str(info_chapter_one['code_list_chapter'][i][1]) + "-"\
                                         + str(info_chapter_one['code_list_chapter'][i][2]) + "-"\
                                         + str(info_chapter_one['code_list_chapter'][i][3]) + "-"\
                                         + str(cnt)
                                # print url_id
                                self.url_set[url_id] = url
                        # print info_chapter_one['code_list_section']
        for i,k in self.url_set.items():
            print i,k

    # 获取所有url
    # def get_url(self):
        # # url_chapter = "http://www.51zuoti.com/chapter_list.php?book=140"
        # # url_chapter = "http://www.51zuoti.com/bookStructures/index/140"
        # html_book = ""
        # book_name = ""
        # for bookid in self.book:
        #     try:
        #         url_book = "http://www.51zuoti.com/bookStructures/index/%s" % bookid
        #         req_book = urllib2.Request(url_book, headers=self.req_header)
        #         resp_book = urllib2.urlopen(req_book, timeout=10)
        #         html_book = resp_book.read()
        #         regex_book = ur"<title>(.*?)</title>"
        #         reobj_book = re.compile(regex_book)
        #         match_book = reobj_book.search(html_book)
        #         if match_book:
        #             book_name = match_book.group(1)
        #             print book_name
        #     except:
        #         pass
        #     for partid in self.part:
        #         for chapterid in self.chapter:
        #             for sectionid in self.section:
        #                 regex_part = ur"<h3>(.*?)</h3><ul><li><a href=\'/subjects/content/%s_%s_1_0\'>" %(bookid,partid)
        #                 # print regex_part
        #                 # regex_part = ur"<h3>(.*?)</h3><ul><li><a href='/subjects/content/(\d+)_(\d)_(\d)_(\d)'>"
        #                 reobj_part = re.compile(regex_part)
        #                 match_part = reobj_part.search(html_book)
        #                 if match_part:
        #                     part_name = match_part.group(1)
        #                     print part_name
        #                     print "\n"
        #                 url = "http://www.51zuoti.com/get_subject.php?book=%s&part=%s&chapter=%s&section=%s&category=1257a&review_type=1&try_count=4&Number=1450782297127"\
        #                       %(bookid,partid,chapterid,sectionid)
        #                 # print url
        #                 self.url_set[book_name] = url
        # # url = "http://www.51zuoti.com/get_subject.php?book=140&part=0&chapter=2&section=0&category=1257a&review_type=1&try_count=4&Number=1450782297127"
        # # self.url_chapter_set["u"] = url_chapter
        # # self.url_set["u"] = url
        # for k, v in self.url_set.items():
        #     print k, v

    # def get_data_test(self):
    #     url = "http://www.51zuoti.com/bookStructures/index/358"
    #     req = urllib2.Request(url, headers=self.req_header)
    #     resp = urllib2.urlopen(req, timeout=10)
    #     html = resp.read()
    #     print html
    #     # regex_s_a = ur"index\:(.*?),href\:"
    #     # reobj_s_a = re.compile(regex_s_a)
    #     # match_s_a = reobj_s_a.search(html)
    #     # if match_s_a:
    #     #     print match_s_a.group(1)

    # 获取题库数据
    # noinspection PyBroadException
    def get_data(self):
        for url_id, url in self.url_set.items():
            if url_id == '140-0-12-2-69':
                subject_info = {}
                req = urllib2.Request(url, headers=self.req_header)
                resp = urllib2.urlopen(req, timeout=10)
                html = resp.read()
                # print html
                # 题型
                temp = html.split("<br>")
                question_type = temp[0]
                subject_info['type'] = question_type
                print question_type
                # 答案
                regex_a = ur"<h1>(.*?)</h1>"
                reobj_a = re.compile(regex_a)
                match_a = reobj_a.search(html)
                if match_a:
                    data_a = match_a.group(1)
                    subject_info['answer'] = data_a
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
                        subject_info['theme'] = data_s
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
                    regex_o = ur"<a href=\"javascript\:[A-Za-z]_select\(\'%s\'\)\">(.*?)</a>" % i
                    # print regex_o
                    reobj_o = re.compile(regex_o)
                    match_o = reobj_o.search(html)
                    if match_o:
                        # print match_o.group(1)
                        # print alphabet_match[str(i)]
                        choice_one += alphabet_match[str(i)]
                        choice_one += ":"
                        choice_one += match_o.group(1)
                        data_o.append(choice_one)
                subject_info['chioce'] = data_o
                print data_o
                # 解析
                regex_an = ur"<h2>(.*?)</h2>"
                reobj_an = re.compile(regex_an)
                match_an = reobj_an.search(html)
                if match_an:
                    data_an = match_an.group(1)
                    subject_info['analysis'] = data_an
                    print data_an
                self.subject_info[url_id] = subject_info

                print "***************************"
                for k,v in self.subject_info.items():
                    print k,v
                print "******"

    # 创建公司每日数据表
    def create_table(self):
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            try:
                cur.execute("DROP TABLE IF EXISTS %s" % self.companyData_oneDay_fileName)
            except Exception,e:
                error_info = Exception,":",e
                print "Do not drop table"
            try:
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS %s "
                    "("
                    # "datekey INT(8),"
                    "subject_id VARCHAR(20),"
                    "bookid VARCHAR(20),"
                    "part_name VARCHAR(20),"
                    "chapter_name VARCHAR(20),"
                    "type VARCHAR(20),"
                    "theme VARCHAR(20),"
                    "chioce VARCHAR(20),"
                    "answer VARCHAR(20),"
                    "analysis VARCHAR(20),"
                    "PRIMARY KEY (`subject_id`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                    % self.companyData_oneDay_fileName)
                print self.companyData_oneDay_fileName + " is created successful"
            except Exception,e:
                error_info = Exception,":",e
                print error_info
        except Exception,e:
            error_info = Exception,":",e
            print error_info

    #  导入数据库
    def insert_data(self):
        for url_id, info in self.subject_info.items():
            id_list = url_id.split('-')
            print id_list
            id_c = id_list[0] + id_list[1] + id_list[2]+ id_list[3]
            # print id_c
            if id_list[3] != '0':  # 有section部分
                for i in range(0, len(self.info_chapter)):
                    for j in range(0, len(self.info_chapter[i]['code_list_section'])):
                        id_cx = ""
                        for k in range(0, len(self.info_chapter[i]['code_list_section'][j])):
                            id_cx += str(self.info_chapter[i]['code_list_section'][j][k])
                        if id_c == id_cx:
                            print self.info_chapter[i]['bookid'][0]
                            print self.info_chapter[i]['chapter'][0]
                            print self.info_chapter[i]['section'][j]
                            print id_cx
                        # if id_list == self.info_chapter[i]['code_list_section'][j]:
                            # print self.info_chapter[i]['code_list_section'][j]
                            # print id_list
                    # if str(id_c) ==

if __name__ == '__main__':
    source = ZuoTi51()
    source.data_process_chapter()
    source.get_url()
    source.get_data()
    source.insert_data()
