#  __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# -----在雪球抓取A股股票当日财务指标数据,并找出存在的公司代码--
#
# ------------------------------------------------------------

import re
import urllib2
import socket
import json
import StringIO
import gzip
import MySQLdb


class XueQiuHk:
    def __init__(self):
        self.try_cnt = 3
        self.url_set = {}
        self.req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                           'Accept-Encoding': 'gzip, deflate',
                           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                           'Connection': 'keep-alive',
                           'Cookie': 's=vnw12f2ga9; __utma=1.117406079.1444787307.1448854251.1448867323.98; __utmz=1.1448854251.97.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_1db88642e346389874251b5a1eded6e3=1448602155,1448792074,1448850399,1448854252; bid=a6f34af86ba79e86c2f9b2f0ef1b8e54_ifq4xlp9; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1448867332; __utmc=1; last_account=lty369963%40sina.com; xq_a_token=077324eba92f407349bb2ae35e87af7eb6c71cb9; xq_r_token=ac9129a23277d00eb85f86889f2a27ab65173144; u=1062948460; xq_token_expire=Fri%20Dec%2025%202015%2015%3A08%3A17%20GMT%2B0800%20(CST); xq_is_login=1; xqat=077324eba92f407349bb2ae35e87af7eb6c71cb9; __utmb=1.2.10.1448867323; __utmt=1',
                           'Host': 'xueqiu.com'}
        self.company_info_oneday = {}

    # 获取所有url
    def get_url(self):
        for code in range(1988, 1989):
            url = "http://xueqiu.com/S/"
            company_code = str("%05d" % code)
            url += company_code
            self.url_set[company_code] = url
        for k,v in self.url_set.items():
            print k,v

    # 获取每个已存在的上市公司的当日数据
    # 记录所有存在的公司
    def get_data(self):
        for company_code, url in self.url_set.items():
            while self.try_cnt > 0:
                try:
                    req = urllib2.Request(url, headers=self.req_header)
                    resp = urllib2.urlopen(req, timeout=10)
                    html = resp.read()
                    compressedstream = StringIO.StringIO(html)
                    gziper = gzip.GzipFile(fileobj=compressedstream)
                    html_data = gziper.read()
                    info_company = [-1] * 8
                    regex = ur"SNB.data.quote =(.*?);"
                    reobj = re.compile(regex)
                    match = reobj.search(html_data)
                    if match:
                        company_data = match.group(1)
                        print company_data
                        company_data = json.loads(company_data)
                        for k,value in company_data.items():
                            print k,value
                            # info_company.append(v)
                            if k == "code":
                                info_company[0] = value
                            elif k == "name":
                                info_company[1] = value
                            elif k == "close":
                                info_company[2] = value
                            elif k == "pe_ttm":
                                info_company[3] = value
                            elif k == "pb":
                                info_company[4] = value
                            elif k == "psr":
                                info_company[5] = value
                            elif k == "dividend":
                                info_company[6] = value
                            elif k == "marketCapital":
                                info_company[7] = value
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
                except AttributeError,atrr:
                    error_info = company_code,Exception,":",atrr
                    # self.error_log.write(str(error_info))
                    # self.error_log.write('\n')
                    # self.companyCode_nexistence.append(company_code)
                    print company_code + " " + "is not exit"
                    break
            self.try_cnt = 3

if __name__ == '__main__':
    source = XueQiuHk()
    source.get_url()
    source.get_data()