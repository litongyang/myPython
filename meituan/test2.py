#!/usr/bin/env python
#coding=utf-8

import sys
import os
import urllib
sys.path.append(os.getcwd())


class POIREFUND:
    
    def __init__(self):
        self.cityid_pos = [[1, '40.007529%2C116.489209'], [10, '31.233397%2C121.486592'], [30, '22.01667%2C114.06667'], [182, '32.2%2C119.15']]
        self.rank_sort = ['smart', 'distance']
        self.firstPoi = 0
        self.lastPoi = 9
        self.datekey = 0
        self.cityid = 0
        self.poiid_temp = []
        self.cityid_temp = []
        self.refund_ratio_temp = []
        self.poiid_result = []
        self.cityid_result = []
        self.refund_ratio_result = []
        self.poiid_topk = []

    def get_refund_ratio(self, line):
        try:
            features = line.strip('\n').split('\t')
            self.datekey = features[0].split(',')[0]
            self.poiid_temp = features[1].split(',')
            self.cityid_temp = features[2].split(',')
            self.refund_ratio_temp = features[3].split(',')
        except:
            pass

    def reptile_topk_poiid(self, k, j):
        try:
            url ="http://api.mobile.meituan.com/group/v1/poi/select/hotel?cityId=%d&sort=%s&mypos=%s&cateId=20&offset=%d&limit=%d&startendday=%s~%s&client=android&utm_source=undefined&utm_medium=android&utm_term=180&version_name=4.8&utm_content=869323001086103&utm_campaign=AgroupBgroupC0E0&ci=1&uuid=0CA5AA54C17A56B5521E3D8CEBFDED1943718C8DD55572BD128DC38CA93C4CDF&msid=8693230010861031408015315260"% (int(self.cityid_pos[k][0]), self.rank_sort[j], self.cityid_pos[k][1],  self.firstPoi, self.lastPoi, self.datekey, self.datekey)
            content = urllib.urlopen(url).read()
            content = content.replace('true', 'True').replace('false', 'False').replace('null', 'None')
            test = eval(content)
            myContent_ctpois = test['ct_pois']
            for one in myContent_ctpois:
                self.poiid_topk.append(one['poiid'])
        except:
            pass

    def result(self):
        try:
            poiid_last_len = self.poiid_temp.__len__()
            for i in range(0, poiid_last_len):
                if int(self.poiid_temp[i]) in self.poiid_topk:
                    self.poiid_result.append(self.poiid_temp[i])
                    self.cityid_result.append(self.cityid_temp[i])
                    self.refund_ratio_result.append(self.refund_ratio_temp[i])
        except:
            pass

if __name__ == '__main__':

    for line in sys.stdin:
        poi_refund = POIREFUND()
        poi_refund.get_refund_ratio(line)
        for city_count in range(0, len(poi_refund.cityid_pos)):
            for sort_count in range(0, len(poi_refund.rank_sort)):
                poi_refund.reptile_topk_poiid(city_count, sort_count)
                poi_refund.result()
                if len(poi_refund.poiid_topk) > 0:
                    for i in range(0, len(poi_refund.poiid_topk)):
                        print '\t'.join([str(0), str(poi_refund.cityid_result[i]), str(poi_refund.poiid_result[i]), str(poi_refund.refund_ratio_result[i])])
                    poi_refund.cityid_result = []
                    poi_refund.poiid_result = []
                    poi_refund.refund_ratio_result = []
                    poi_refund.poiid_topk = []