# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import sys
import urllib2
import json
import create_table
import ColNameDict
import time


reload(sys)
sys.setdefaultencoding('utf-8')


class DemoGetData:
    def __init__(self):
        self.ur_head = "http://caifu.baidu.com/wealth/ajax?pageSize=10&pageNum="
        self.ur_tail = "&module=Finance&category=wealth&serverTime=1464256652806&pvid=1464256652802624939&resourceid=1800181&subqid=1464256652802624939&sid=ui%3A0%26bsInsurance%3A1%26bsInvest%3A3%26bsLoan%3A1%26loanCardBbd%3A0%26bsCreditCard%3A3&pssid=0&tn=NONE&signTime=82&qid=1464249266929912097&wd=&zt=fc&fr=fc&f=sug&baiduid=849E8F172893D03D03247DC8E478996B&amount=&cycle=&profit=&risk=&productType=0"
        self.url_list = []
        self.data_file = open("data_file.txt", 'w')
        self.req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Charset': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                           'Accept-Encoding': 'gzip, deflate',
                           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                           'Connection': 'keep-alive',
                           'Cookie': 'BAIDUID=849E8F172893D03D03247DC8E478996B:FG=1; BIDUPSID=849E8F172893D03D03247DC8E478996B; PSTM=1458713879 \
; BDUSS=FNmdnZQc2hudmgwUk1NUmtEV0pEc0hVdEdIdDdxSjNTU1Y0aTNDWGFzNlV4QmxYQVFBQUFBJCQAAAAAAAAAAAEAAAC9QJIsc3VucXdlMzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJQ38laUN \
~JWW; __cfduid=d971bcd6c590421c53c425a66d9e1176d1463047663; H_PS_PSSID=20145_1443_20079_19721_19568_19861_15217_11855_19360 \
; BDSFRCVID=IKPsJeCCYr3pLwRROuoi5TLXReKK0gOTJfV3nvURVLBInsnYg5aYEG0PJx8gywkboFI8ogKK0gOTH65P; H_BDCLCKID_SF \
=tR-t_I-XtKK3fP36qR6Shn3H-UIst6Jt-2Q-5hOw-DO28-3-0xnhBUr03-vvQtQiWbRM2MbF5fL5e-boMlOH-6FZQUTkK5QKymT \
xoUJFMInJJt3c-4nPyjkebPRiJPb9Qg-q_xtLtCPhMK-wDT_35bD_-gT024oHbDTQW-5bHJO_bUo9QbbkbftdWqKebU7fLHr9Lx7 \
lJxbdoMoNyU42bU47yxjpJ-6qQGrp2poYatO_oJ0G-qrpQT8rylAOKbcf2KryKqIyab3vOIJTXpO1j6LreGLOt60JfRAtV-35b5r \
0Db7mq4b_en8rBpbZKxJmy6ueQpR5Lfocff7_jqOdWhD8yP4jKMRnWDcpobb2WbcxHJ_w3xJ_Wtb0-Jr405OTWj-O0-T52booslI \
9hPJvyT8sXnO7tjQTfJCO_C-2fC8hbPb4-t-_Mtu_Klj-2PRt--o2WDvmMIJ5OR5JLprKDn8T5n5NWbQdQJTn2Un45lvvhb3O3M6 \
t36tH5RoNLf7GWCoeWfTjJRjZsq0x0M6We---5URa2M5AfIOMahkM5h7xOKLG05Cae5Q3jauet6nfb5kXXJRObTrjDCvGbT35y4L \
dLnrHJbOrbarN2-570K5x8Mn-bfRvD--g3-6hLjJbbg3B-njtfxQnDxTTjtQZQfbQ0-6OqPb8bK3aWhQYfn7JOpkxbUnxy5500aC \
DJTFJJnCH_Kv5b-0_DtczhPTq2DCShUFs24-J-2Q-5hOw0R8KhJ3v0xnhBPJ03-vvQtQiWbRM2MbF5fL5JJvOD-6GhU5ybNjJttC \
DKeTxoUJFBCnJJt3cqtJPKxPebPRiJPb9Qg-q_xtLtCPhMK-wDT_35bD_-gT024oHbDTQW-5bHJO_bpTo0bbkbftdWqKebU7fLHr \
9LR7VJxbdoMoNyU42bU47yxjpJ-6qQGrp2poYatO_oJ0G-qrpQT8rylAOKbcf2KryKqIyab3vOIJTXpO1j6LrexbH55utJnkJ_MK \
; Hm_lvt_2724d98690b9b21595bd86c07591b6a3=1464249270; Hm_lpvt_2724d98690b9b21595bd86c07591b6a3=1464256656 \
; BD_TOPAD_ENDTIME=4590921600000; BCLID=658289246985240945',
                           'Host': 'caifu.baidu.com'}
        self.page_len = 400  # 页数
        self.temp_data = {}
        self.col_name_dict = ColNameDict.col_name_dict
        self.create_table = create_table.CreateTable()

    def delete_data(self):
        try:
            self.create_table.cur.execute("delete from %s" % self.create_table.file_name)
        except Exception, e:
            print Exception, e

    def get_url(self):
        try:
            for page in range(1, self.page_len):
                url = self.ur_head + str(page) + self.ur_tail
                self.url_list.append(url)
        except:
            pass

    def process_data(self):
        try:
            for i in range(1, len(self.url_list)):
                print self.url_list[i]
                req = urllib2.Request(self.url_list[i], headers=self.req_header)
                resp = urllib2.urlopen(req)
                jsondata = resp.read().encode('utf8')
                # self.data_file.write(jsondata)
                # self.data_file.write("\n")
                data = json.loads(jsondata)
                for k, v in data.items():
                    if k == 'data':
                        for k1, v1 in v.items():  # list 层
                            if k1 == 'list':
                                for value in v1:
                                    for k2, v2 in value.items():  # 字段层
                                        if k2 == 'profitDesc':
                                            for k3, v3 in v2[0].items():
                                                # print k3, v3
                                                k3_tmp = 'profitDesc_' + str(k3)
                                                self.temp_data[k3_tmp] = v3
                                        if k2 == 'extraFields':
                                            for k3_1, v3_1 in v2[0][0].items():
                                                # print k3_1, v3_1
                                                k3_1_tmp = 'extraFields_' + str(k3_1)
                                                self.temp_data[k3_1_tmp] = v3_1
                                        if k2 != 'profitDesc' and k2 != 'extraFields':
                                            # print k2, v2
                                            self.temp_data[k2] = v2
                                    # print "**************"
                                    # for k, v in self.temp_data.items():
                                    #     print k, v
                                    # insert data to DB
                                    intsert_sql = ''
                                    cnt = 0
                                    for i in range(0, len(self.col_name_dict)):
                                        flag = 0
                                        for k, v in self.temp_data.items():
                                            if k == self.col_name_dict[i]:
                                                flag = 1
                                                cnt += 1
                                                v = str(v)
                                                v = v.encode("utf-8")
                                                intsert_sql += '\'' + v + '\'' + ','
                                        if flag == 0:  # 没有匹配的字段
                                            intsert_sql += '\'' + '' + '\'' + ','
                                    time_stamp_tmp = time.time()
                                    time_array = time.localtime(time_stamp_tmp)
                                    time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
                                    intsert_sql += '\'' + time_stamp + '\'' + ','
                                    intsert_sql = intsert_sql[0:-1]  # 去除最后一个逗号
                                    # print intsert_sql
                                    try:
                                        self.create_table.cur.execute('set names \'utf8\'')
                                        self.create_table.cur.execute("insert into %s values(%s)" % (self.create_table.file_name, intsert_sql))
                                        self.temp_data = {}
                                        # print "====================================="
                                    except Exception, e:
                                        print Exception, e
        except Exception, e:
            print Exception, e

if __name__ == '__main__':
    demo = DemoGetData()
    demo.delete_data()
    demo.get_url()
    demo.process_data()
