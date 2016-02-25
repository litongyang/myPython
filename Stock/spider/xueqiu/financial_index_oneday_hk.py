#  __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# -----在雪球抓取H股股票当日财务指标数据,并找出存在的公司代码--
# 不定期要更换cookie
# ------------------------------------------------------------

import re
import urllib2
import socket
import json
import StringIO
import gzip
import datetime
import MySQLdb
import threading
import warnings
warnings.filterwarnings("ignore")


class XueQiuHk:
    def __init__(self):
        self.try_cnt = 3
        self.yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y%m%d')
        self.url_set = {}
        self.threads = []  # 线程池
        self.req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                           'Accept-Encoding': 'gzip, deflate',
                           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                           'Connection': 'keep-alive',
                           'Cookie':'Hm_lvt_1db88642e346389874251b5a1eded6e3=1455842467,1455856824,1455969805,1456101489; s=10hh12edmw; __utma=1.676762656.1451027781.1456101489.1456104260.123; __utmz=1.1451027781.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); bid=a6f34af86ba79e86c2f9b2f0ef1b8e54_iiwheq86; webp=0; xq_a_token=18949a168da31eb80aa1b692da066ba7d9ede76a; xq_r_token=952569eaa89fa41d44a73bd7692f429f17161ace; u=1062948460; xq_token_expire=Thu%20Mar%2010%202016%2009%3A50%3A10%20GMT%2B0800%20(CST); xq_is_login=1; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1456104350; __utmc=1; __utmb=1.2.10.1456104260; __utmt=1',
                           'Host': 'xueqiu.com'}
        self.company_info_oneday = {}

        #  每个线程的起始点和终点
        self.begin_threads1 = 0
        self.end_threads1 = 1000
        self.begin_threads2 = 1000
        self.end_threads2 = 2000
        self.begin_threads3 = 2000
        self.end_threads3 = 4000
        self.begin_threads4 = 6000
        self.end_threads4 = 7500
        self.begin_threads5 = 7500
        self.end_threads5 = 9000

        self.db_name = 'STOCK_INFO_2014'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.companyData_oneDay_fileName = 'company_hk_data_oneday'

    # 获取所有url
    def get_url(self):
        for code in range(1, 9000):
        # for code in range(1988, 1989):
            if 4100 < code < 6000:
                continue
            else :
                url = "http://xueqiu.com/S/"
                company_code = str("%05d" % code)
                url += company_code
                self.url_set[company_code] = url
        # for k,v in self.url_set.items():
        #     print k,v

    # 获取每个已存在的上市公司的当日数据
    # 记录所有存在的公司
    # noinspection PyBroadException
    def get_data(self, begin, end):
        for company_code, url in self.url_set.items():
            if begin < int(company_code) <= end:
                while self.try_cnt > 0:
                    try:
                        req = urllib2.Request(url, headers=self.req_header)
                        resp = urllib2.urlopen(req, timeout=10)
                        html = resp.read()
                        compressedstream = StringIO.StringIO(html)
                        gziper = gzip.GzipFile(fileobj=compressedstream)
                        html_data = gziper.read()
                        info_company = [-1] * 10
                        regex = ur"SNB.data.quote =(.*?);"
                        reobj = re.compile(regex)
                        match = reobj.search(html_data)
                        if match:
                            company_data = match.group(1)
                            # print company_data
                            company_data = json.loads(company_data)
                            for k,value in company_data.items():
                                # print k,value
                                info_company[0] = self.yesterday
                                if k == "code":
                                    info_company[1] = value
                                elif k == "name":
                                    if value.find("'") == -1:
                                        info_company[2] = value
                                    else:
                                        info_company[2] = value.replace("'","")
                                elif k == "close":
                                    try:
                                        info_company[3] = float(value)
                                    except:
                                        info_company[3] = -1
                                elif k == "pe_ttm":
                                    try:
                                        info_company[4] = float(value)
                                    except:
                                        info_company[4] = -1
                                elif k == "pb":
                                    try:
                                        info_company[5] = float(value)
                                    except:
                                        info_company[5] = -1
                                elif k == "psr":
                                    try:
                                        info_company[6] = float(value)
                                    except:
                                        info_company[6] = -1
                                elif k == "dividend":
                                    try:
                                        info_company[7] = float(value)
                                    except:
                                        info_company[7] = -1
                                elif k == "marketCapital":
                                    value = value.encode('utf8')
                                    if value.find("亿") != -1:
                                        info_company[8] = float(value.replace("亿","")) * 100000000
                                    elif value.find("万") != -1:
                                        info_company[8] = float(value.replace("万","")) * 10000
                                    else:
                                        info_company[8] = -1
                                elif k == "issue_type":
                                    try:
                                        value = value.encode('utf8')
                                        info_company[9] = value
                                    except:
                                        info_company[9] = '-'
                                # elif k == "last_close":
                                #     info_company[8] = value
                        else:
                            print "%s : Data is empty" % company_code
                        self.company_info_oneday[company_code] = info_company
                        print company_code, self.company_info_oneday[company_code]
                        break

                    except socket.timeout,e:
                        error_info = company_code,self.try_cnt,Exception,":",e
                        print error_info
                        # self.error_log.write(str(error_info))
                        # self.error_log.write('\n')
                        self.try_cnt -= 1
                    # except AttributeError,atrr:
                    #     error_info = company_code,Exception,":",atrr
                    #     # self.error_log.write(str(error_info))
                    #     # self.error_log.write('\n')
                    #     # self.companyCode_nexistence.append(company_code)
                    #     print company_code + " " + "is not exit"
                    #     break
                    except urllib2.HTTPError,e:
                        error_info = company_code,Exception,":",e
                        print company_code + " " + "is not exit"
                        break
                self.try_cnt = 3

    # 多线程并发执行
    # noinspection PyShadowingNames
    def threads_exe(self, fun):
        try:
            threads1 = threading.Thread(target=fun, args=(self.begin_threads1, self.end_threads1))
            threads2 = threading.Thread(target=fun, args=(self.begin_threads2, self.end_threads2))
            threads3 = threading.Thread(target=fun, args=(self.begin_threads3, self.end_threads3))
            threads4 = threading.Thread(target=fun, args=(self.begin_threads4, self.end_threads4))
            threads5 = threading.Thread(target=fun, args=(self.begin_threads5, self.end_threads5))
            self.threads.append(threads1)
            self.threads.append(threads2)
            self.threads.append(threads3)
            self.threads.append(threads4)
            self.threads.append(threads5)
            for t in self.threads:
                t.start()
            for t in self.threads:
                t.join()
        except Exception,e:
            print Exception,":",e

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
                    "datekey INT(8),"
                    "company_code VARCHAR(20),"
                    "company_name VARCHAR(20),"
                    "price DECIMAL(20,4),"
                    "pe DECIMAL(20,4), "
                    "pb DECIMAL(20,4),"
                    "ps DECIMAL(20,4),"
                    "dividend DECIMAL(20,4), "
                    "market_value DECIMAL(20,2), "
                    "is_HK VARCHAR(20), "
                    "PRIMARY KEY (`datekey`,`company_code`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                    % self.companyData_oneDay_fileName)
                print self.companyData_oneDay_fileName + " is created successful"
            except Exception,e:
                error_info = Exception,":",e
                print error_info
        except Exception,e:
            error_info = Exception,":",e
            print error_info

    # 插入上市公司的当日数据
    # noinspection PyBroadException
    def insert_data(self):
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            for code,info in self.company_info_oneday.items():
                # print code,info
                try:
                    insert_info = '\'' + str(info[0]) + '\'' + ',' + '\'' + code + '\'' + ','\
                                  + '\''+ str(info[2].encode('utf8')) + '\''+ ',' + '\'' + str(info[3]) + '\''+ ','\
                                  + '\'' + str(info[4]) + '\''+ ',' + '\'' + str(info[5]) + '\''+ ','\
                                  + '\'' + str(info[6]) + '\''+ ',' + '\'' + str(info[7]) + '\''+ ','+ '\'' + str(info[8]) + '\''\
                                  + ','+ '\'' + str(info[9]) + '\''

                    # print insert_info
                    insert_sql = "insert into %s values(%s)" % (self.companyData_oneDay_fileName, insert_info)
                    print insert_sql
                    cur.execute(insert_sql)
                except Exception,e:
                    error_info = Exception,":",e
                    print error_info
        except Exception,e:
            error_info = Exception,":",e
            print error_info
            pass

if __name__ == '__main__':
    source = XueQiuHk()
    source.get_url()
    source.threads_exe(source.get_data)
    source.create_table()
    source.insert_data()