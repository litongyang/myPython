#__author__ = 'litongyang'
# -*- coding: utf-8 -*-

pay_now = [] #最近一个月最大支付
pay_max = [] #三个月支付
for line in open("/Users/litongyang/Desktop/c2.txt"):
    content = line.replace("\n", "").split("\t")
    pay_now.append(float(content[2]))
    pay_max.append(float(content[6]))
len = pay_now.__len__()

count_02 = 0
count_05 = 0
count_10 = 0
count_12 = 0
count_15 = 0

for i in range(0,len):
    if pay_now[i] !=0:
        if round(float((pay_max[i] - pay_now[i])/ pay_now[i]),2)< -0.2:
            count_02 = count_02 + 1
        if round(float((pay_max[i] - pay_now[i])/ pay_now[i]),2)> 0:
            count_05 = count_05 + 1
        if round(float((pay_max[i] - pay_now[i])/ pay_now[i]),2)> -0.2 and round(float((pay_max[i] - pay_now[i])/ pay_now[i]),2)< 0:
            print pay_max[i]
            print pay_now[i]
            print "\n"
            count_12 = count_12 +1
print count_05