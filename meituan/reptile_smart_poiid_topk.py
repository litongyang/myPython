#__author__ = 'litongyang'
# -*- coding: utf-8 -*-

import urllib
import MySQLdb
import numpy

class POIREFUND:

    def __init__(self):
        self.cityid_pos = [[1, '40.007529%2C116.489209'], [10, '31.233397%2C121.486592'], [30, '22.01667%2C114.06667'], [182, '32.2%2C119.15']]
        self.rank_sort = ['smart', 'distance']
        self.firstPoi = 0
        self.lastPoi = 9
        self.beginDatekey = 20141109
        self.endDatekey = 20141109
        self.poiid_topk = []

    def reptile_topk_poiid(self, k):
        url ="http://api.mobile.meituan.com/group/v1/poi/select/hotel?cityId=%d&sort=%s&mypos=%s&" \
             "cateId=20&offset=%d&limit=%d&" \
             "startendday=%d~%d&client=android&utm_source=undefined&utm_medium=android&utm_term=180&version_name=4.8" \
             "&utm_content=869323001086103&utm_" \
             "campaign=AgroupBgroupC0E0&ci=1&uuid=0CA5AA54C17A56B5521E3D8CEBFDED1943718C8DD55572BD128DC38CA93C4CDF&msid=8693230010861031408015315260"\
             % (int(self.cityid_pos[k][0]), self.rank_sort[1], self.cityid_pos[k][1],  self.firstPoi, self.lastPoi, self.beginDatekey, self.endDatekey)
        print url
        self.poiid_topk = []
        content = urllib.urlopen(url).read()
        content = content.replace('true', 'True').replace('false', 'False').replace('null', 'None')
        test = eval(content)
        myContent_ctpois = test['ct_pois']
        for one in myContent_ctpois:
            self.poiid_topk.append(one['poiid'])
        print self.poiid_topk

    def link_mysql_result(self):
        try:
            conn = MySQLdb.connect(host='localhost', user='root', passwd='123', db='test', port=3306)
            cur = conn.cursor()
            count = cur.execute('select * from `refund_poi_city_20141109`')#行数
            results = cur.fetchmany(count)
            cur.close()
            conn.close()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        refund_ratio = []

        for i in range(len(results)):
            if results[i][0] in self.poiid_topk:
                refund_ratio.append(results[i][2])
        if len(refund_ratio) == 0:
            refund_ratio_avg = -1
        else:
            print refund_ratio
            refund_ratio_avg = numpy.average(refund_ratio)
        print refund_ratio_avg

if __name__ == '__main__':
    poi_refund = POIREFUND()
    for w in range(0, 4):
        poi_refund.reptile_topk_poiid(w)
        poi_refund.link_mysql_result()
