# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# 宏观数据

import urllib2
import json
import Stock.spider.NBS.data_init as dataInit


class MacroData:
    def __init__(self):
        self.month_count = 120
        self.url_set = {}
        self.data_init_class = dataInit.DataInit()

        self.monthNum = "LAST120"
        # self.endTime = "201512"
        self.ur_history = "http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgyd&rowcode=zb&colcode=sj&wds=[]&dfwds=[{%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%222005%2C2015%22}]&k1=1449710776640"
        self.req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0',
                           'Accept': 'application/json, text/javascript, */*; q=0.01',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                           'Accept-Encoding': 'gzip, deflate',
                           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                           'Connection': 'keep-alive',
                           'Cookie': 'gscu_1771678062=480079816mgye972; acmrAutoLoginUser=""; acmrAutoSessionId=""; _gscs_1771678062=50141303hvyoqs19|pv:1; _gscbrs_1771678062=1; JSESSIONID=0B035D5C2CCA3A90F8CF8C2006E40973; u=2',
                           'Host': 'data.stats.gov.cn'}

    # 获取所以url
    def get_url(self):
        # for i in range(0, len(self.indexCode)):
        for i in range(0, len(self.data_init_class.indexCode)):
            url = "http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgyd&rowcode=zb&colcode=sj&wds=[]&dfwds=[{%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22"
            url += self.data_init_class.indexCode[i]
            url += "%22%22"
            url += self.monthNum
            url += "%22}]"
            self.url_set[self.data_init_class.indexCode[i]] = url
        for k, v in self.url_set.items():
            print k, v

    # 获取数据
    def get_data(self):
        for indexCode, url in self.url_set.items():
            try:
                # if indexCode == "A0B01":
                if indexCode == "A010A":
                    req = urllib2.Request(url, headers=self.req_header)
                    resp = urllib2.urlopen(req)
                    jsondata = resp.read()
                    data = json.loads(jsondata)
                    for key1, value1 in data.items():
                        if key1 == "returndata":
                            for key2, datanodes in value1.items():
                                if key2 == "datanodes":
                                    # print len(datanodes)
                                    # print datanodes
                                    count = 0
                                    # for km, vm in self.industry1.items():
                                    for k in range(0, len(self.data_init_class.data_dict[indexCode])):
                                        for i in range(0, self.month_count):
                                            for key3, value3 in datanodes[count].items():
                                                if key3 == "data":
                                                    for key, value in value3.items():
                                                        if key == "strdata" and count < len(datanodes):
                                                            self.data_init_class.data_dict[indexCode][k].append(value)
                                                            count += 1
                                    print indexCode
                                    for i in range(0, len(self.data_init_class.data_dict[indexCode])):
                                        print self.data_init_class.data_dict[indexCode][i]
                                    print "*********************"
                                # elif key2 == "wdnodes":
                                #     # print datanodes[0]
                                #     for k1,v1 in datanodes[0].items():
                                #         if k1 == "nodes":
                                #             print v1
                                #             for k2, v2 in v1[41].items():
                                #                 if k2 == "name":
                                #                     print v2

                # print self.money_supply1
                # print "*****************************"
            except:
                pass
        # for k, v in self.data_init_class.data_dict.items():
        #     print "*************"
        #     print k
        #     for i in range(0, len(v)):
        #         print v[i]

                # def data_process(self):


if __name__ == '__main__':
    macroData = MacroData()
    macroData.get_url()
    macroData.get_data()
