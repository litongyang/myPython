# __author__ = 'lty'
# -*- coding: utf-8 -*-

import LWR
import numpy as np
import matplotlib.pyplot as plt
lwlr = LWR.Locally_Weighted_Linear_Regression()
rate_list = []
fl = open('train.txt', 'r')
for line in fl:
    line_one = line.split()
    rate_tmp = line_one[1].split(',')
    # rate_list.append(rate_tmp)
X = []
# X= range(1, len(rate_tmp)+1)
# print X
# print X
# x = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13]])
for i in range(1, len(rate_tmp)+1):
    x_tmp = []
    x_tmp.append(i)
    X.append(x_tmp)
print X
x=np.array(X)
print x

for i in rate_tmp:
    rate_list.append(int(i))
y = np.array(rate_list)
print y
# print rate_list
taus = [1, 0.01, 25]
plt.scatter(x, y)  # Plot train data
color = ["r", "g", "b"]
for i, tau in enumerate(taus):
    thetas, estimation = lwlr.fit(x, y, x, tau=tau)
    print thetas
    print estimation
    plt.plot(x, estimation, c=color[i])  # Plot prediction
    print "========="

plt.show()
