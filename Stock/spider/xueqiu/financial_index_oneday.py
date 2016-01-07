# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# -----在雪球抓取A股股票当日财务指标数据,并找出存在的公司代码--
#  不定期要更换cookie
# ------------------------------------------------------------

import urllib2
import socket
import json
import StringIO
import gzip
import MySQLdb
import threading


class XueQiu:
    def __init__(self):
        self.url_set = {}
        self.req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                           'Accept-Encoding': 'gzip, deflate',
                           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                           'Connection': 'keep-alive',
                           'Cookie': 'Hm_lvt_1db88642e346389874251b5a1eded6e3=1450919388,1451008674,1451452629,1451701055; s=10hh12edmw; xq_a_token=a76c8ff2718de0ee5888263f70bb99c6273a6add; xq_r_token=1087f50e54dc71bae2c45ad9be5ab352edb63bb2; u=1062948460; xq_token_expire=Tue%20Jan%2019%202016%2015%3A15%3A48%20GMT%2B0800%20(CST); xq_is_login=1; __utma=1.676762656.1451027781.1451459879.1451701056.4; __utmz=1.1451027781.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lpvt_1db88642e346389874251b5a1eded6e3=1451701055; __utmb=1.1.10.1451701056; __utmc=1; __utmt=1',
                           'Host': 'xueqiu.com'}
        self.company_info_onday = {}
        self.companyCode_nexistence = []  # 不存在公司
        self.companyCode_existence = []  # 存在公司

        self.db_name = 'STOCK_INFO_2014'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.companyData_oneDay_fileName = 'company_data_oneday'

        self.error_log = open("error_log.txt", 'w')
        self.try_cnt = 3  # 超时后尝试次数
        self.threads = []  # 线程池
        #  每个线程的起始点和终点
        self.begin_threads1 = 0
        self.end_threads1 = 2000
        self.begin_threads2 = 2000
        self.end_threads2 = 3000
        self.begin_threads3 = 3000
        self.end_threads3 = 600000
        self.begin_threads4 = 600000
        self.end_threads4 = 601500
        self.begin_threads5 = 601500
        self.end_threads5 = 603000


    # 获取所有url
    def get_url(self):
        for code in range(1, 604000):
            url = "http://xueqiu.com/stock/f10/dailypriceextend.json?symbol="
            company_code = str("%06d" % code)
            if not (not (1100 <= code < 1600) and not (3000 < code <= 300000)) or (301000 < code <= 599999) or (
                            code > 602000 <= 602999):
                continue
            elif code < 600000:
                url += "SZ" + company_code
                self.url_set[company_code] = url
            else:
                url += "SH" + company_code
                self.url_set[company_code] = url
                # for key, value in self.url_set.items():
                #     print key, value

    # 获取每个以存在的上市公司的当日数据
    # 记录所有存在的公司
    # noinspection PyBroadException
    def get_data(self, begin, end):
        for company_code, url in self.url_set.items():
            if begin < int(company_code) <= end:
                while self.try_cnt > 0:
                    try:
                        # if self.try_cnt > 1:
                        req = urllib2.Request(url, headers=self.req_header)
                        resp = urllib2.urlopen(req, timeout=10)
                        html = resp.read()
                        compressedstream = StringIO.StringIO(html)
                        gziper = gzip.GzipFile(fileobj=compressedstream)
                        jsondata = gziper.read()
                        data = json.loads(jsondata)
                        info_company = [-1] * 9
                        for key1, value1 in data.items():
                            for key2, value2 in value1.items():
                                for key, value in value2.items():
                                    if key == 'tradedate':  # 交易日期
                                        try:
                                            info_company[0] = int(value)
                                        except:
                                            info_company[0] = -1
                                            # info_company.append(int(value))
                                    if key == 'tclose':  # 收盘价
                                        try:
                                            info_company[1] = float(value)
                                        except:
                                            info_company[1] = float(-1)
                                    if key == 'pettm':
                                        try:
                                            info_company[2] = float(value)
                                        except:
                                            info_company[3] = float(-1)
                                    if key == 'pb':
                                        try:
                                            info_company[3] = float(value)
                                        except:
                                            info_company[3] = float(-1)
                                    if key == 'pcttm':  # 市销率
                                        try:
                                            info_company[4] = float(value)
                                        except:
                                            info_company[4] = float(-1)
                                    if key == 'dy':  # 股息率
                                        try:
                                            info_company[5] = float(value)
                                        except:
                                            info_company[5] = float(-1)
                                    if key == 'totmktcap':  # 总市值
                                        try:
                                            info_company[6] = float(value)
                                        except:
                                            info_company[6] = float(-1)
                                    if key == 'negotiablemv':  # 流通市值
                                        try:
                                            info_company[7] = float(value)
                                        except:
                                            info_company[7] = float(-1)
                                    if key == 'lclose':  # 前一日收盘价
                                        try:
                                            info_company[8] = float(value)
                                        except:
                                            info_company[8] = float(-1)
                        self.companyCode_existence.append(company_code)  # 存在的公司
                        self.company_info_onday[company_code] = info_company
                        print company_code, self.company_info_onday[company_code]
                        break
                    except socket.timeout,e:
                        error_info = company_code,self.try_cnt,Exception,":",e
                        print error_info
                        self.error_log.write(str(error_info))
                        self.error_log.write('\n')
                        self.try_cnt -= 1
                    except AttributeError,atrr:
                        error_info = company_code,Exception,":",atrr
                        self.error_log.write(str(error_info))
                        self.error_log.write('\n')
                        self.companyCode_nexistence.append(company_code)
                        print company_code + " " + "is not exit"
                        break
                    except Exception,e:
                        error_info = company_code,self.try_cnt,Exception,":",e
                        print error_info
                        self.error_log.write(str(error_info))
                        self.error_log.write('\n')
                        self.try_cnt -= 1
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
                print error_info
            try:
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS %s "
                    "(datekey INT(8),"
                    "company_code VARCHAR(20),"
                    "price DECIMAL(20,4),"
                    "pe DECIMAL(20,4), "
                    "pb DECIMAL(20,4),"
                    "ps DECIMAL(20,4),"
                    "dividend_rate DECIMAL(20,4), "
                    "market_value DECIMAL(20,2), "
                    "circulation_market_value DECIMAL(20,2),"
                    "price_yesterday DECIMAL(20,2),"
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
    def insert_data(self):
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            for code,info in self.company_info_onday.items():
                print code,info
                insert_info = '\'' + str(info[0]) + '\'' + ',' + '\'' + code + '\'' + ',' + '\'' + str(info[1]) + '\'' + ',' \
                              + '\'' + str(info[2]) + '\''+ ',' + '\'' + str(info[3]) + '\''+ ','\
                              + '\'' + str(info[4]) + '\''+ ',' + '\'' + str(info[5]) + '\''+ ','\
                              + '\'' + str(info[6]) + '\''+ ',' + '\'' + str(info[7]) + '\''+ ','+ '\'' + str(info[8]) + '\''

                # print insert_info
                insert_sql = "insert into %s values(%s)" % (self.companyData_oneDay_fileName, insert_info)
                print insert_sql
                cur.execute(insert_sql)
        except Exception,e:
            error_info = Exception,":",e
            print error_info

if __name__ == '__main__':
    source = XueQiu()
    source.get_url()
    # source.get_data()
    source.threads_exe(source.get_data)
    source.create_table()
    source.insert_data()
