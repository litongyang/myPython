# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import sys
import time
import urllib2
from lxml import etree
import create_table
reload(sys)
sys.setdefaultencoding('utf-8')


class XiaoYingLicai:
    def __init__(self):
        self.error_log = open('error.log', 'w')
        self.create_table = create_table.CreateTable()
        self.page_cnt = 3
        self.url = 'https://www.xiaoying.com/invest/list?p1='
        self.url_list = []
        self.req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Charset': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                           'Accept-Encoding': 'gzip, deflate, br',
                           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                           'Connection': 'keep-alive',
                           'Cookie': 'source=10008; Hm_lvt_6a5064ae576aec13acf46a38ed77e29d=1465022778; Hm_lpvt_6a5064ae576aec13acf46a38ed77e29d=1465026831; uuid=68151228967682049; captchaKey=9906125752793a3bd58',
                           'Host': 'www.xiaoying.com'}

    def get_url(self):
        try:
            for page_num in range(1, self.page_cnt):
                url = self.url + str(page_num)
                self.url_list.append(url)
            for v in self.url_list:
                print v
        except Exception, e:
            print Exception, e

    def get_data(self):
        try:
            for url in self.url_list:
                insert_sql = ''
                data = urllib2.urlopen(url, timeout=10).read()
                root = etree.HTML(data)
                nodes = root.xpath("//div[@class='card-in']")  # 产品区域层

                for node in nodes:
                    # print node.tag
                    for node_child in node.getchildren():   # card-divider 产品明细层
                        for divider in node_child.getchildren():
                            if str(divider.attrib) == "{'class': 'card-hd'}":
                                time_stamp_tmp = time.time()
                                time_array = time.localtime(time_stamp_tmp)
                                time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
                                insert_sql += '\'' + time_stamp + '\'' + ','
                                print divider.getchildren()[0].text  # 产品名称
                                insert_sql += '\'' + str(divider.getchildren()[0].text).encode("utf-8") + '\'' + ','
                                if len(divider.getchildren()) > 1:
                                    print divider.getchildren()[1].text  # 产品标识区分
                                    insert_sql += '\'' + str(divider.getchildren()[1].text).encode("utf-8") + '\'' + ','
                                    if len(divider.getchildren()) > 2:
                                        print divider.getchildren()[2].text  # 投资上限
                                        insert_sql += '\'' + str(divider.getchildren()[2].text).encode("utf-8") + '\'' + ','
                                    else:  # 没有投资上限
                                        insert_sql += '\'' + 'null' + '\'' + ','
                                else:
                                    insert_sql += '\'' + 'null' + '\'' + ','
                                    insert_sql += '\'' + 'null' + '\'' + ','
                            if str(divider.attrib) == "{'class': 'card-bd'}":  # 年化收益区域，起投金额区域
                                for divider_db in divider.getchildren():
                                    if str(divider_db.attrib) == "{'class': 'card-info mb10'}":
                                        print divider_db[0].getchildren()[1].text  # 投资收益率
                                        insert_sql += '\'' + str(divider_db[0].getchildren()[1].text).encode("utf-8") + '\'' + ','
                                        print divider_db[1].getchildren()[1].text  # 投资周期
                                        insert_sql += '\'' + str(divider_db[1].getchildren()[1].text).encode("utf-8") + '\'' + ','
                                        print divider_db[2].getchildren()[1].text  # 还款方式
                                        insert_sql += '\'' + str(divider_db[2].getchildren()[1].text).encode("utf-8") + '\'' + ','
                                    if str(divider_db.attrib) == "{'class': 'card-info'}":
                                        print divider_db[0].getchildren()[1].text  # 起投金额
                                        insert_sql += '\'' + str(divider_db[0].getchildren()[1].text).encode("utf-8") + '\'' + ','
                                        print divider_db[1].getchildren()[1].text  # 融资总额
                                        insert_sql += '\'' + str(divider_db[1].getchildren()[1].text).encode("utf-8") + '\'' + ','
                                        print divider_db[2].getchildren()[1].text  # 起息时间
                                        insert_sql += '\'' + str(divider_db[2].getchildren()[1].text).encode("utf-8") + '\'' + ','
                                        insert_sql += '\'' + '众安保险提供全额保单' + '\'' + ','

                            # if str(divider.attrib) == "{'class': 'card-bb'}":  # 保障方式区域
                            #     print divider.getchildren()[0].getchildren()[1][0].text  #  保障方式有问题
                            if str(divider.attrib) == "{'class': 'cr-in'}":
                                for divider_cr_in in divider.getchildren():
                                    if str(divider_cr_in.attrib) == "{'class': 'cr-top'}":
                                        print divider_cr_in[0].getchildren()[0].text   # 已投笔数
                                        insert_sql += '\'' + str(divider_cr_in[0].getchildren()[0].text).encode("utf-8") + '\'' + ','
                                        print divider_cr_in[1].getchildren()[1].text   # 剩余金额
                                        insert_sql += '\'' + str(divider_cr_in[1].getchildren()[1].text).encode("utf-8") + '\'' + ','
                                    if str(divider_cr_in.attrib) == "{'class': 'cr-mid'}":
                                        print divider_cr_in[0].text  # 投资占比
                                        insert_sql += '\'' + str(divider_cr_in[0].text).encode("utf-8") + '\'' + ','
                                    if str(divider_cr_in.attrib) == "{'class': 'cr-btm'}":
                                        print divider_cr_in[0].text  # 可否投资的状态
                                        insert_sql += '\'' + str(divider_cr_in[0].text).encode("utf-8") + '\'' + ','
                    insert_sql = insert_sql[0:-1]  # 去除最后一个逗号
                    # print "insert into %s values(%s)" % (self.create_table.file_name, insert_sql)
                    self.create_table.cur.execute('set names \'utf8\'')
                    self.create_table.cur.execute("insert into %s values(%s)" % (self.create_table.table_name_product, insert_sql))
                    insert_sql = ''

                    print "**********"

        except Exception, e:
            print Exception, e
            error_log = Exception, e
            self.error_log.write(str(error_log))
            self.error_log.write('\n')
                # for i in node_child:
                #     print i.attrib
                #     for j in i:
                #         print j.text
            # for
        # regex_s_a = ur"<div class=\"prjl-item \">(.*?)<div class=\"prjl-item \">"
        # regex_s_a = ur"<p>(.*?)</p>"
        # reobj_s_a = re.compile(regex_s_a)
        # match_s_a = reobj_s_a.search(data)
        # data_s_a = match_s_a.group(1)
        # print data_s_a
        # HTMLParser.feed(str(data))
        # HTMLParser.handle_starttag(tag,attrs)

if __name__ == '__main__':
    test = XiaoYingLicai()
    test.get_url()
    test.get_data()
