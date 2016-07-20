#__author__ = 'litongyang'
# -*- coding: utf-8 -*-
'''
##---------- 离线数据------------
pay_max_daily = 0 #poi每日最大支付数量
pay_deal_max_daliy = 0 #poi中销量最好的deal最大支付数量
poi_pay_usually = 0 #poi平日支付数量
poi_pay_week = 0 #poi周末支付数量
poi_refund_usually = 0 #poi平日退款数量
poi_refund_week = 0 #poi周末退款数量
week_type = 0 #0:周日~周四 1：周五、周六

#-------------实时数据---------------
pay_cnt_realtime = 0 #poi支付的实时数据
refund_realtime = 0 #实时退款数

#--------------得分-----------------
poi_payCnt_score = 0 #poi支付能力得分
poi_payDealCnt_score = 0#poi销量最大deal的支付能力得分
pay_score = 0 #poi总支付能力得分
poi_refundRatio_score = 0 #poi退款率得分
reserve_score = 0 #库存总得分


if pay_cnt_realtime < pay_max_daily * 0.8:
    poi_payCnt_score = 0
    if pay_cnt_realtime <= pay_deal_max_daliy * 0.6:
        poi_payDealCnt_score = 2
    elif pay_cnt_realtime > pay_deal_max_daliy * 0.6 and pay_cnt_realtime <= pay_deal_max_daliy * 0.8:
        poi_payDealCnt_score = 1
    elif pay_cnt_realtime > pay_deal_max_daliy * 0.8 and pay_cnt_realtime <= pay_deal_max_daliy:
        poi_payDealCnt_score = 0.5
    else:
        poi_payDealCnt_score = -1
elif pay_cnt_realtime >= pay_max_daily * 0.8 and pay_cnt_realtime <= pay_max_daily:
    poi_payDealCnt_score = 0
    poi_payCnt_score = 0
else:
    poi_payDealCnt_score = 0
    poi_payCnt_score = -1

pay_score = poi_payDealCnt_score + poi_payCnt_score #总支付能力得分


if week_type == 0:
    if (refund_realtime/pay_cnt_realtime)< (poi_refund_usually/poi_pay_usually) * 0.6:
        poi_refundRatio_score = 3
    elif (refund_realtime/pay_cnt_realtime)>= (poi_refund_usually/poi_pay_usually) * 0.6 and  (refund_realtime/pay_cnt_realtime)< (poi_refund_usually/poi_pay_usually)*0.8:
        poi_refundRatio_score = 2
    elif (refund_realtime/pay_cnt_realtime)>= (poi_refund_usually/poi_pay_usually) * 0.8 and  (refund_realtime/pay_cnt_realtime)<= (poi_refund_usually/poi_pay_usually):
        poi_refundRatio_score = 1
    else:
        poi_refundRatio_score = ((poi_refund_usually/poi_pay_usually)-(refund_realtime/pay_cnt_realtime))*10

reserve_score = pay_score + poi_refundRatio_score #库存总得分
'''

'''
poi = []
for line in open("/Users/litongyang/Desktop/poi.txt"):
     content = line.replace("\n", "").split("\t")
     poi.append(round(float(content[7]),2))
print poi

deal = []
for line in open("/Users/litongyang/Desktop/deal.txt"):
     content = line.replace("\n", "").split("\t")
     deal.append(round(float(content[7]),2))
print deal

for i in range(0,len(poi)):
    if poi[i] >= deal[i]:
        continue
    else:
        print "false!"
print "true!"
'''

poi_pay = []

for line in open("/Users/litongyang/Desktop/re1.txt"):

     content = line.replace("\n", "").split("\t")

     poi_pay.append(round(float(content[1]),10))



print len(poi_pay)

for j in range(1, 11):
    k=0
    print j
    for i in range(0,len(poi_pay)):
        if poi_pay[i] >j:
            k = k+1
    print k