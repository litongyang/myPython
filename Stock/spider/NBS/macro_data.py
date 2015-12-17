# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# 宏观数据

import MySQLdb
import urllib2
import json
import time
import Stock.spider.NBS.data_init as dataInit


class MacroData:
    def __init__(self):
        self.month_now = time.strftime('%m',time.localtime(time.time()))  # 当前月份
        self.year_now = time.strftime('%Y',time.localtime(time.time()))  # 当前年
        self.datekey= time.strftime('%Y%m%d',time.localtime(time.time()))  # 当日
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
                           # 'Cookie': 'gscu_1771678062=480079816mgye972; acmrAutoLoginUser=""; acmrAutoSessionId=""; _gscs_1771678062=50141303hvyoqs19|pv:1; _gscbrs_1771678062=1; JSESSIONID=0B035D5C2CCA3A90F8CF8C2006E40973; u=2',
                           'Cookie': '	_gscu_1771678062=480079816mgye972; _gscs_1771678062=50314679d7beon19|pv:1; _gscbrs_1771678062=1; JSESSIONID=E7FAF8B4A9E97C6548538BA5096FAA7C; u=5',
                           'Host': 'data.stats.gov.cn'}

        self.db_name = 'STOCK_INFO_2014'  # 数据库名,如果与现有数据库冲突，可改为其他名字
        self.db_host = 'localhost'  # 主机名
        self.db_port = 3306  # 端口号
        self.username = 'root'  # 用户名
        self.password = '123'  # 密码
        self.macro_info_fileName = 'log_macro_economic_information'  # 宏观数据表

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
                index_name = []
                # if indexCode == "A010A":
                # if indexCode == "A030A":
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
                            elif key2 == "wdnodes":
                                for key3,value3 in datanodes[0].items():
                                    if key3 == "nodes":
                                        for i in range(0, len(self.data_init_class.data_dict[indexCode])):
                                            for key4, value4 in value3[i].items():
                                                if key4 == "name":
                                                    index_name.append(value4)
                # for i in range(0, len(index_name)):
                #     print index_name[i]
                for i in range(0, len(self.data_init_class.data_dict[indexCode])):
                    # print index_name[i]
                    # print self.data_init_class.data_dict[indexCode][i]
                    self.data_init_class.data_dict[indexCode][i].insert(0, index_name[i])
                    # print self.data_init_class.data_dict[indexCode][i]
                print "######################################"
            except:
                pass

    # 创建宏观数据表
    def create_table(self):
        month = []  # 200512-至今所有的月份
        for m in range(int(self.month_now) -1,0,-1):
            month.append(str(self.year_now) + str("%02d" % m))
        for year in range(int(self.year_now) -1,2005,-1):
            for mon in range(12,0,-1):
                month.append(str(year) + str("%02d" % mon))
        month.append(str(200512))
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            try:
                cur.execute("DROP TABLE IF EXISTS %s" % self.macro_info_fileName)
            except:
                pass
            try:
                col_name = ""
                for i in range(0, len(month)):
                    temp = '`' + str(month[i]) + '`' + " DECIMAL(20,2)" + ","
                    col_name += temp
                # col_name = col_name[0:len(col_name) - 1]  # 去除最后的','
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS %s "
                    "(datekey INT(8),"
                    "index_name VARCHAR(200),"
                    "%s"
                    "PRIMARY KEY (`datekey`,`index_name`) )ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8"
                    % (self.macro_info_fileName, col_name))
                print self.macro_info_fileName + " is created successful"
            except:
                pass
        except:
            pass

    #  向数据表插入数据
    def insert_data(self):
        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.username, passwd=self.password, db=self.db_name,
                                   port=self.db_port)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
            for k, v in self.data_init_class.data_dict.items():
                # if k == 'A030A':
                print k
                for i in range(0, len(v)):
                    print len(v[i])
                    insert_info = ""
                    insert_info += '\'' + self.datekey + '\'' + ','
                    for j in range(0, len(v[i])):
                        insert_info += '\'' + v[i][j].encode('utf8') + '\'' + ','
                    insert_info = insert_info[0:len(insert_info) -1]
                    insert_sql = "insert into %s values(%s)" % (self.macro_info_fileName, insert_info)
                    print insert_info
                    print insert_sql
                    try:
                        cur.execute(insert_sql)
                    except Exception,ex:
                        print Exception,":",ex
        except:
            pass


if __name__ == '__main__':
    macroData = MacroData()
    macroData.get_url()
    # macroData.get_data()
    # macroData.create_table()
    # macroData.insert_data()
