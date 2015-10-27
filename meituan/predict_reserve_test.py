#__author__ = 'litongyang'
# -*- coding: utf-8 -*-

from __future__ import division
import matplotlib.pyplot as plt
import numpy as numpy

class PredictReserve():
    def __init__(self):
        self.week = []
        self.poiid = []
        self.orderid_cnt = []
        self.orderid_common_cnt = []
        self.orderid_week_cnt = []
        self.refundid_cnt = []
        self.refundid_common_cnt = []
        self.refundid_week_cnt = []
        self.sale_cnt = []
        self.sale_common_cnt = []
        self.sale_week_cnt = []


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
            lineone4 = int(linone[4])
            if lineone0 == 1487525:
                self.week.append(lineone1)
                self.orderid_cnt.append(lineone2)
                self.refundid_cnt.append(lineone3)
                self.sale_cnt.append(lineone4)

    def get_ordercnt_refundcnt(self):
        try:

            print self.week
            print self.orderid_cnt
            print self.refundid_cnt

            for i in range(0, len(self.week)):
                if (self.week[i] == 5 or self.week[i] == 6):
                    self.orderid_week_cnt.append(self.orderid_cnt[i])
                    self.refundid_week_cnt.append(self.refundid_cnt[i])
                    self.sale_week_cnt.append(self.sale_cnt[i])
                else:
                    self.orderid_common_cnt.append(self.orderid_cnt[i])
                    self.refundid_common_cnt.append(self.refundid_cnt[i])
                    self.sale_common_cnt.append(self.sale_cnt[i])

            #print numpy.average(self.orderid_common_cnt)+1
            print int(numpy.average(self.orderid_common_cnt)/90+1)
            print int(numpy.average(self.refundid_common_cnt)/90+1)
            print int(numpy.average(self.sale_common_cnt)/90+1)
            print "\n"
            print int(numpy.average(self.orderid_week_cnt)/90+1)
            print int(numpy.average(self.refundid_week_cnt)/90+1)
            print int(numpy.average(self.sale_week_cnt)/90+1)
            #print max(self.orderid_cnt)
            #print max(self.paycnt)
            #print numpy.average(self.refund2order_ratio)
            #print min(self.refund2order_ratio)
            #print max(self.refund2order_ratio)

        except:
           pass


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