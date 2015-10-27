#__author__ = 'litongyang'
# -*- coding: utf-8 -*-

from __future__ import division
import matplotlib.pyplot as plt
import numpy as numpy

class PredictReserve():
    def __init__(self):
        self.datekey = []
        self.poiid = []
        self.orderid_cnt = []
        self.refundid_cnt = []
        self.orderid_cnt_one = []
        self.refundid_cnt_one = []
        self.paycnt = []
        self.refund2order_ratio = []

    def read_data(self):
        for line in open("/Users/litongyang/Desktop/预测库存/poiid_orderid_refund1.txt"):
            linone = line.split()
            lineone0 = int(linone[0])
            lineone1 = int(linone[1])
            lineone2 = int(linone[2])
            lineone3 = int(linone[3])
            if lineone1 == 4703936:
                self.datekey.append(lineone0)
                self.orderid_cnt.append(lineone2)
                self.refundid_cnt.append(lineone3)

    def get_ordercnt_refundcnt(self):
        for i in  range(0, len(self.orderid_cnt)):
            self.refund2order_ratio.append(self.refundid_cnt[i]/self.orderid_cnt[i])
            self.paycnt.append(self.orderid_cnt[i]-self.refundid_cnt[i])
            if (self.refundid_cnt[i]/self.orderid_cnt[i]) > 0.25:
                print "datekey:%d" %self.datekey[i]
                print "orderid_cnt:%d" %self.orderid_cnt[i]
                print "refundid_cnt:%d" %self.refundid_cnt[i]
                print '\n'
        print self.orderid_cnt
        print self.refundid_cnt
        print max(self.orderid_cnt)
        print max(self.paycnt)
        print numpy.average(self.refund2order_ratio)
        print min(self.refund2order_ratio)
        print max(self.refund2order_ratio)


    def drawing(self):
        refund2order = [float(self.refundid_cnt[i]/self.orderid_cnt[i]) for i in range(0, len(self.orderid_cnt))]
        date = [i for i in range(0, 31, 1)]
        plt.plot(date, refund2order, 'o-', linewidth=2)
        plt.grid()
        #---设置x轴刻度----#
        plt.xticks(range(min(date), max(date)+1, 1))
        plt.show()



if __name__ == '__main__':
    PredictReserve = PredictReserve()
    PredictReserve.read_data()
    PredictReserve.get_ordercnt_refundcnt()
    #PredictReserve.drawing()