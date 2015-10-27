#__author__ = 'litongyang'
# -*- coding: utf-8 -*-
#对离线数据进行评估
pay_now = [] #今天消费
pay_mean = [] #历史平均值
for line in open("/Users/litongyang/Desktop/c1.txt"):
     content = line.replace("\n", "").split("\t")
     pay_now.append(float(content[1]))
     pay_mean.append(float(content[2]))

len = pay_now.__len__()
k = 0
k1 = 0
k3 = 0
count_02 = 0
count_05 = 0
count_10 = 0
count_12 = 0
count_15 = 0

for i in range(0,len):
    if pay_mean[i] !=0 :
        if pay_now[i] !=0:
            if round(float((pay_mean[i] - pay_now[i])/ pay_now[i]),2)>0.5:
                k = k+1
            if round(float((pay_mean[i] - pay_now[i])/ pay_now[i]),2)<-0.5:
                k1 = k1+1
            if float(pay_now[i]) > float(pay_mean[i] *2):
                k3 = k3+1
        if  round(float(pay_now[i]/pay_mean[i]),2) <0.2 :
            count_02 = count_02 +1
        if round(float(pay_now[i]/pay_mean[i]),2) <0.5:
            count_05 = count_05 +1
        if round(float(pay_now[i]/pay_mean[i]),2) <1.0:
            count_10 = count_10 +1
        if round(float(pay_now[i]/pay_mean[i]),2) <1.2:
            count_12 = count_12+1
        if round(float(pay_now[i]/pay_mean[i]),2) >=1.2:
            count_15 = count_15 +1
print "(pay_today/pay_mean)<0.2 %d"%count_02
print "(pay_today/pay_mean)<0.5 %d"%count_05
print "(pay_today/pay_mean)<1.0 %d"%count_10
print "(pay_today/pay_mean)<1.2 %d"%count_12
print "(pay_today/pay_mean)>=1.2 %d"%count_15
print k
print k3