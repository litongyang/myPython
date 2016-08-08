# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# -----在51做题网抓取题库和答案-----------------------------
#
# ----------------------------------------------------------

import re
import urllib2
import MySQLdb
import warnings

warnings.filterwarnings("ignore")


# noinspection PyPep8Naming
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
        # self.book = [i for i in range(26)]  # id：0到620
        # self.book = [194,226,231,230,199,409,410,411,412,413,482,483,484,485,486,487,488,489,502,589,539,505,506,590]
        self.book = [199, 194]  # test
        self.url_set = {}
        self.req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/43.0',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
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
        self.companyData_oneDay_fileName = 'zuoti_51_test'

        # self.threads =[]  # 5个线程
        self.error_log = open("error_log.txt", 'w')  # 错误日志


    # 数据处理
    # noinspection PyAssignmentToLoopOrWithParameter
    def data_process_chapter(self, bookid):
        # for bookid in self.book:
        try_cnt = 3
        while try_cnt > 0:
            try:
                url_chapter_list = "http://www.51zuoti.com/chapter_list.php?book=%s" % bookid
                req_chapter_list = urllib2.Request(url_chapter_list, headers=self.req_header)
                resp_chapter_list= urllib2.urlopen(req_chapter_list, timeout=10)
                chapter_list = resp_chapter_list.read()
                words = ['index', 'href','total','did','finish','process','review','uiProvider','cls','leaf','children','true','false']
                temp = str_add_marks(chapter_list, words)
                data_json = eval(temp)
                if len(data_json) ==0:
                    self.error_log.write(str("book%s is not exit"% bookid))
                    self.error_log.write('\n')
                for i in range(0, len(data_json)):
                    info_chapter = {
                       "bookid": [],
                       "part": [],
                       "chapter": [],
                       "section": [],
                       "code_list_part": [],
                       "code_list_chapter": [],
                       "code_list_section": [],
                       "chapter_subject_cnt": [],
                       "subject_cnt": []
                    }  # 一条信息
                    if str(data_json[i]).count("children") <2:  # 2层
                        code_list = [] *4
                        regex_code = ur"\((.*?)\)"
                        reobj_code = re.compile(regex_code)
                        match_code = reobj_code.search(data_json[i]['href'])
                        if match_code:
                            code = match_code.group(1)
                            code_list = code.split(',')
                        if code_list[1] == '0':  # 没有part部分
                            for kp,vp in data_json[i].items():
                                info_chapter['part'].append("null")
                                if kp == 'index':  # 第一层index
                                    info_chapter['bookid'].append(bookid)
                                    info_chapter['chapter'].append(vp)
                                    info_chapter['code_list_chapter'].append(code_list)
                                if kp == 'total':
                                    regex_cnt = ur"[0-9]*"
                                    reobj_cnt = re.compile(regex_cnt)
                                    match_cnt = reobj_cnt.search(vp)
                                    if match_cnt:
                                        chapter_subject_cnt = int(match_cnt.group(0))
                                        info_chapter['chapter_subject_cnt'].append(chapter_subject_cnt)
                                elif kp == 'children':
                                    for j in range(0, len(vp)):
                                        for k1, v1 in vp[j].items():
                                            if k1 == 'index':  # 第二层index
                                                info_chapter['section'].append(v1)
                                            if k1 == 'href':
                                                regex_code_section = ur"\((.*?)\)"
                                                reobj_code_section = re.compile(regex_code_section)
                                                match_code_section = reobj_code_section.search(v1)
                                                if match_code_section:
                                                    code = match_code_section.group(1)
                                                    code_list_section = code.split(',')
                                                    info_chapter['code_list_section'].append(code_list_section)
                                            if k1 == 'total':
                                                regex_cnt = ur"[0-9]*"
                                                reobj_cnt = re.compile(regex_cnt)
                                                match_cnt = reobj_cnt.search(v1)
                                                if match_cnt:
                                                    subject_cnt = int(match_cnt.group(0))
                                                    info_chapter['subject_cnt'].append(subject_cnt)
                        else:  # 有part部分
                            for kp,vp in data_json[i].items():
                                if kp == 'index':  # 第一层index
                                    info_chapter['bookid'].append(bookid)
                                    info_chapter['part'].append(vp)
                                    info_chapter['code_list_part'].append(code_list)
                                if kp == 'children':
                                    for j in range(0, len(vp)):
                                        for k1, v1 in vp[j].items():
                                            if k1 == 'index':  # 第二层index
                                                info_chapter['chapter'].append(v1)
                                            if k1 == 'href':
                                                regex_code_section = ur"\((.*?)\)"
                                                reobj_code_section = re.compile(regex_code_section)
                                                match_code_section = reobj_code_section.search(v1)
                                                if match_code_section:
                                                    code = match_code_section.group(1)
                                                    code_list_section = code.split(',')
                                                    info_chapter['code_list_chapter'].append(code_list_section)
                                            if k1 == 'total':
                                                # print v1
                                                regex_cnt = ur"[0-9]*"
                                                reobj_cnt = re.compile(regex_cnt)
                                                match_cnt = reobj_cnt.search(v1)
                                                if match_cnt:
                                                    chapter_subject_cnt = int(match_cnt.group(0))
                                                    info_chapter['chapter_subject_cnt'].append(chapter_subject_cnt)

                    else:  # 有part部分
                        for k,v in data_json[i].items():
                            if k == 'index':  # 第一层index
                                info_chapter['bookid'].append(bookid)
                                info_chapter['part'].append(v)
                            if k == 'href':
                                regex_code = ur"\((.*?)\)"
                                reobj_code = re.compile(regex_code)
                                match_code = reobj_code.search(v)
                                if match_code:
                                    code = match_code.group(1)
                                    code_list = code.split(',')
                                    info_chapter['code_list_part'].append(code_list)
                            elif k == 'children':
                                for j in range(0, len(v)):
                                    for k1, v1 in v[j].items():
                                        if k1 == 'index':  # 第二层index
                                            info_chapter['chapter'].append(v1)
                                        if k1 == 'href':
                                            regex_code_chapter = ur"\((.*?)\)"
                                            reobj_code_chapter = re.compile(regex_code_chapter)
                                            match_code_chapter = reobj_code_chapter.search(v1)
                                            if match_code_chapter:
                                                code = match_code_chapter.group(1)
                                                code_list_chapter = code.split(',')
                                                info_chapter['code_list_chapter'].append(code_list_chapter)
                                        if k1 == 'total':
                                            regex_cnt = ur"[0-9]*"
                                            reobj_cnt = re.compile(regex_cnt)
                                            match_cnt = reobj_cnt.search(v1)
                                            if match_cnt:
                                                subject_cnt = int(match_cnt.group(0))
                                                info_chapter['chapter_subject_cnt'].append(subject_cnt)
                                        if k1 == 'children':
                                            for j in range(0, len(v1)):
                                                for k2, v2 in v1[j].items():
                                                    if k2 == 'index':  # 第三层index
                                                        info_chapter['section'].append(v2)
                                                    if k2 == 'href':
                                                        regex_code_section = ur"\((.*?)\)"
                                                        reobj_code_section = re.compile(regex_code_section)
                                                        match_code_section = reobj_code_section.search(v2)
                                                        if match_code_section:
                                                            code = match_code_section.group(1)
                                                            code_list_section = code.split(',')
                                                            info_chapter['code_list_section'].append(code_list_section)
                                                    if k2 == 'total':
                                                        regex_cnt = ur"[0-9]*"
                                                        reobj_cnt = re.compile(regex_cnt)
                                                        match_cnt = reobj_cnt.search(v2)
                                                        if match_cnt:
                                                            subject_cnt = int(match_cnt.group(0))
                                                            info_chapter['subject_cnt'].append(subject_cnt)
                    # for k,v in info_chapter.items():
                    #     # print k,v
                    #     for i in range(0, len(v)):
                    #         print k , v[i]
                    # print "*****"
                    self.info_chapter.append(info_chapter)
                break
            except Exception,e:
                try_cnt -= 1
                error_info = bookid,try_cnt,Exception,":",e
                self.error_log.write(str(error_info))
                self.error_log.write('\n')
                print error_info

    # 获取所有url
    def get_url(self):
        for info_chapter_one in self.info_chapter:
            for k,v in info_chapter_one.items():
                if k == 'section':
                    if len(v):  # 有section部分
                        for i in range(0, len(info_chapter_one['code_list_section'])):
                            for cnt in range(0, int(info_chapter_one['subject_cnt'][i])):
                                url = "http://www.51zuoti.com/get_subject.php?book=%s&part=%s&chapter=%s&section=%s&category=0123456789abcdefghijklmnopqrstuvwxyz&review_type=1&try_count=%s" \
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
                                url = "http://www.51zuoti.com/get_subject.php?book=%s&part=%s&chapter=%s&section=%s&category=0123456789abcdefghijklmnopqrstuvwxyz&review_type=1&try_count=%s" \
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
                                self.url_set[url_id] = url

    # 获取题库数据
    # noinspection PyBroadException
    def get_data(self):
        for url_id, url in self.url_set.items():
            # --------Test--------------
            # if url_id == '385-2-1-4-25':
            # if url_id == '358-2-1-0-25':
            # if url_id == '140-0-2-0-37':
            # if url_id == '413-0-16-1-4':
            # if url_id == '505-26-1-7-13' or url_id == '506-2-2-0-5' or url_id == '194-0-2-0-42' :
            try_cnt = 3
            while try_cnt > 0:
                try:
                    subject_info = {}
                    req = urllib2.Request(url, headers=self.req_header)
                    resp = urllib2.urlopen(req, timeout=5)
                    html = resp.read()
                    if html == "<input type='hidden' name='review_times' value=0 />":
                        break
                    # 题型
                    temp = html.split("<br>")
                    question_type = temp[0]
                    regex_t = ur"[\[（][\s\S]*[\]）]"
                    reobj_t = re.compile(regex_t)
                    match_t = reobj_t.search(question_type)
                    if match_t:
                        question_type = match_t.group(0)
                        subject_info['type'] = question_type
                    else:
                        subject_info['type'] = ""
                    # 答案
                    regex_a = ur"<h1>(.*?)</h1>"
                    reobj_a = re.compile(regex_a)
                    match_a = reobj_a.search(html)
                    data_a = ""
                    if match_a:
                        data_a = match_a.group(1)
                        subject_info['answer'] = data_a
                    else:
                        subject_info['answer'] = "null"
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
                        else:
                            subject_info['theme'] = data_s_a
                    else:
                        subject_info['theme'] = "null"
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
                        reobj_o = re.compile(regex_o)
                        match_o = reobj_o.search(html)
                        if match_o:
                            choice_one += alphabet_match[str(i)]
                            choice_one += ":"
                            choice_one += match_o.group(1)
                            data_o.append(choice_one)
                    subject_info['chioce'] = data_o
                    # 解析
                    regex_an = ur"<h2>(.*?)</h2>"
                    reobj_an = re.compile(regex_an)
                    match_an = reobj_an.search(html)
                    if match_an:
                        data_an = match_an.group(1)
                        subject_info['analysis'] = data_an
                    else:
                        subject_info['analysis'] = "null"
                    self.subject_info[url_id] = subject_info
                    print url_id,":",self.subject_info[url_id]
                    break
                except Exception,e:
                    try_cnt -= 1
                    error_info = url_id,try_cnt,Exception,":",e
                    self.error_log.write(str(error_info))
                    self.error_log.write('\n')
                    print error_info
            # print "***************************"
            # for k,v in self.subject_info.items():
            #     print k,v
            # print "******"

    # 创建公司每日数据表
    def create_table(self):
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            # --------删除数据表------
            # try:
            #     cur.execute("DROP TABLE IF EXISTS %s" % self.companyData_oneDay_fileName)
            # except Exception,e:
            #     error_info = Exception,":",e
            #     print "Do not drop table"
            try:
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS %s "
                    "("
                    "subject_id VARCHAR(100),"  # 题目id
                    "bookid VARCHAR(20),"  # 书的id
                    "part_name VARCHAR(100),"  # 部分名称
                    "chapter_name VARCHAR(100),"  # 章节名称
                    "section_name VARCHAR(100),"  # 章节部分名称
                    "type VARCHAR(100),"  # 题型
                    "theme VARCHAR(255),"  # 题目
                    "chioce_A VARCHAR(255),"  # 选项A内容
                    "chioce_B VARCHAR(255),"  # 选项B内容
                    "chioce_C VARCHAR(255),"  # 选项C内容
                    "chioce_D VARCHAR(255),"  # 选项D内容
                    "chioce_E VARCHAR(255),"  # 选项E内容
                    "answer VARCHAR(255),"    # 答案内容
                    "analysis VARCHAR(255),"  # 解析内容
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
    # noinspection PyBroadException,PyUnusedLocal
    def insert_data(self):
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                       port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            for url_id, info in self.subject_info.items():
                try:
                    insert_list = ['null'] *14
                    url_id_temp = url_id.split('-')
                    id_t = ""
                    for i in url_id_temp:
                        id_t += str("%04d" % int(i)) + "-"
                    id = id_t[0:len(id_t) -1]
                    insert_list[0] = id
                    for k,sub_info in self.subject_info.items():
                        if k == url_id:
                            insert_list[5] = sub_info['type'].replace("'","")
                            insert_list[6] = sub_info['theme'].replace("&nbsp;","").replace('<br>',"").replace("'","")
                            for i in range(7, 12):
                                if (i -7)< len(sub_info['chioce']):
                                    insert_list[i] = sub_info['chioce'][i -7].replace("&nbsp;","").replace("'","")
                            insert_list[12] = sub_info['answer'].replace("'","")
                            insert_list[13] = sub_info['analysis'].replace("&nbsp;","").replace('<br>',"").replace("'","")

                    id_list = url_id.split('-')
                    id_c = id_list[0] + id_list[1] + id_list[2]+ id_list[3]
                    if id_list[3] != '0':  # 有section部分
                        for i in range(0, len(self.info_chapter)):
                            for k1 in range(0, len(self.info_chapter[i]['code_list_chapter'])):
                                for j in range(0, len(self.info_chapter[i]['code_list_section'])):
                                    if self.info_chapter[i]['code_list_section'][j][2] == self.info_chapter[i]['code_list_chapter'][k1][2] \
                                            and self.info_chapter[i]['code_list_section'][j][1] == self.info_chapter[i]['code_list_chapter'][k1][1]:
                                        id_cx = ""
                                        for k in range(0, len(self.info_chapter[i]['code_list_section'][j])):
                                            id_cx += str(self.info_chapter[i]['code_list_section'][j][k])
                                        if id_c == id_cx :
                                            insert_list[1] = self.info_chapter[i]['bookid'][0]
                                            insert_list[2] = self.info_chapter[i]['part'][0].replace("'","")
                                            regex = ur"\s+"
                                            reobj = re.compile(regex)
                                            match_chapter = reobj.search(self.info_chapter[i]['chapter'][k1])
                                            if match_chapter:
                                                t = match_chapter.group(0)
                                                insert_list[3] = self.info_chapter[i]['chapter'][k1].replace(t,"")\
                                                    .replace("<fontcolor=\"#FF0000\">(免费试用)</font","").replace("'","")
                                            else:
                                                insert_list[3] = self.info_chapter[i]['chapter'][k1].replace("<fontcolor=\"#FF0000\">(免费试用)</font","")\
                                                    .replace("'","")
                                            match_section = reobj.search(self.info_chapter[i]['section'][0])
                                            if match_section:
                                                t = match_section.group(0)
                                                insert_list[4] = self.info_chapter[i]['section'][j].replace(t,"").replace("'","")
                                            else:
                                                insert_list[4] = self.info_chapter[i]['section'][j].replace("'","")
                    else:  # 没有section部分
                        for i in range(0, len(self.info_chapter)):
                            for j in range(0, len(self.info_chapter[i]['code_list_chapter'])):
                                id_cx = ""
                                for k in range(0, len(self.info_chapter[i]['code_list_chapter'][j])):
                                    id_cx += str(self.info_chapter[i]['code_list_chapter'][j][k])
                                if id_c == id_cx:
                                    insert_list[1] = self.info_chapter[i]['bookid'][0]
                                    insert_list[2] = self.info_chapter[i]['part'][0].replace("'","")
                                    regex = ur"\s+"
                                    reobj = re.compile(regex)
                                    match_chapter = reobj.search(self.info_chapter[i]['chapter'][j])
                                    if match_chapter:
                                        t = match_chapter.group(0)
                                        insert_list[3] = self.info_chapter[i]['chapter'][j].replace(t,"")\
                                            .replace("<fontcolor=\"#FF0000\">(免费试用)</font","").replace("'","")
                                    else:
                                        insert_list[3] = self.info_chapter[i]['chapter'][j].replace("<fontcolor=\"#FF0000\">(免费试用)</font","").replace("'","")
                    print "*******************"
                    insert_info = ""
                    for i in insert_list:
                        # print i
                        insert_info += '\'' + str(i) + '\'' + ','
                    insert_info = insert_info[0:len(insert_info) -1]
                    insert_sql = "insert into %s values(%s)" % (self.companyData_oneDay_fileName, insert_info)
                    print insert_sql
                    cur.execute(insert_sql)
                except Exception,e:
                    error_info = url_id,Exception,":",e
                    self.error_log.write(str(error_info))
                    self.error_log.write('\n')
                    print error_info
        except Exception,e:
            pass

    #  test
    def test(self):
        url = "http://www.51zuoti.com/bookStructures/index/358"
        # url = "http://www.51zuoti.com/chapter_list.php?book=358"
        req_chapter_list = urllib2.Request(url, headers=self.req_header)
        resp_chapter_list= urllib2.urlopen(req_chapter_list, timeout=10)
        html = resp_chapter_list.read()
        print html


if __name__ == '__main__':
    source = ZuoTi51()
    source.create_table()
    for bookid in source.book:
        source.url_set = {}
        source.info_chapter = []  # 章节信息
        source.subject_info = {}  # 答案信息
        source.data_process_chapter(bookid)
        source.get_url()
        source.get_data()
        source.insert_data()
