# __author__ = 'lty'
# -*- coding: utf-8 -*-

fr = open('/Users/litongyang/Desktop/test.txt', 'r')
profit = []
profit_basic = []  # 每股收益增长
profit_ying = []  # 营业利润同比
profit_all = []  # 利润总额同比
v_pre_3 = []
v_pre_7 = []
v_pre_15 = []
v_after_3 = []
v_after_7 = []
v_after_15 = []
date = []
cnt = 0
cnt1 = 0
for line in fr:
    line_one = line.split()
    for i in range(0, len(line_one)):
        if line_one[i] == 'NULL':
            line_one[i] = '0'
    date.append(str(line_one[1]))
    profit.append(float(line_one[2]))
    profit_basic.append(float(line_one[3]))
    profit_ying.append(float(line_one[4]))
    profit_all.append(float(line_one[5]))
    v_pre_3.append(float(line_one[6]))
    v_after_3.append(float(line_one[7]))
    v_pre_7.append(float(line_one[8]))
    v_after_7.append(float(line_one[9]))
    v_pre_15.append(float(line_one[10]))
    v_after_15.append(float(line_one[11]))
for i in range(0, len(profit)):
    if profit[i] > 100 and date[i][0:4] == '2017':
        cnt1 += 1
    if profit[i] > 1000 and v_after_3[i] > 0:
        cnt += 1
print cnt1