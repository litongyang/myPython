#__author__ = 'litongyang'
# -*- coding: utf-8 -*-

#import urllib
import MySQLdb
import numpy

class POI_REFUND:
    def __init__(self):
        self.new1 = []
        self.old = []
        self.last = []

    def link_mysql_newresult(self):
        for city in range(1, 600):
            try:
                conn = MySQLdb.connect(host='localhost', user='root', passwd='123', db='test', port=3306)
                cur = conn.cursor()
                count = cur.execute('SELECT cityid,AVG(refund_ratio) FROM ( SELECT  r.poiid as poiid, r.cityid as cityid,temp.sorce as sorce,r.refund_ratio as refund_ratio FROM ( SELECT * FROM refund_poi_city_20141109  WHERE cityid =%d)r JOIN ( SELECT * FROM poi_decline_07_20141109 o )temp ON temp.poiid = r.poiid ORDER BY temp.sorce DESC  LIMIT 10 )t GROUP BY cityid'%city)#行数
                results = cur.fetchmany(count)
                for i in range(len(results)):
                    self.new1.append(results[i][1])
                cur.close()
                conn.close()
            except MySQLdb.Error,e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def link_mysql_oldresult(self):
        for city in range(1,600):
            try:
                conn = MySQLdb.connect(host='localhost', user='root', passwd='123', db='test', port=3306)
                cur = conn.cursor()
                count = cur.execute('SELECT cityid,AVG(refund_ratio) FROM ( SELECT  r.poiid as poiid, r.cityid as cityid,temp.sorce as sorce,r.refund_ratio as refund_ratio FROM ( SELECT * FROM refund_poi_city_20141109  WHERE cityid =%d)r JOIN ( SELECT * FROM poi_decline_20141109 o )temp ON temp.poiid = r.poiid ORDER BY temp.sorce DESC  LIMIT 10 )t GROUP BY cityid'%city)#行数
                results1 = cur.fetchmany(count)
                for i in range(len(results1)):
                    self.old.append(results1[i][1])
                cur.close()
                conn.close()
            except MySQLdb.Error, e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def result_last(self):
        for i in range(len(self.new1)):
            self.last.append(self.new1[i]-self.old[i])
        refund_city_avg = numpy.average(self.last)
        print refund_city_avg

if __name__ == '__main__':
    poi_refund = POI_REFUND()
    poi_refund.link_mysql_newresult()
    poi_refund.link_mysql_oldresult()
    poi_refund.result_last()
