# -*- coding: utf-8 -*-
from tabulate import tabulate
# x= [1,2,3,4,5,1,3,3]
# myset = set(x)
# print myset
# for item in myset:
#     print x.count(item), " of ", item, " in list"

# ----正则----
# 1975/09/9(\d{4})
# import re
# x = '1975/09/9'
# regex = ur"\d{4}"
# match = re.match(r'\d{4}', x)
# print match.group(0)


# from sklearn import linear_model
# X = [[0., 0.], [1., 1.], [2., 2.], [3., 3.]]
# Y = [0., 1., 2., 3.]
# clf = linear_model.BayesianRidge()
# clf.fit(X, Y)

import numpy as np
# import random
# import matplotlib.pylab as plt
#
# x = [1, 2, 3, 6, 101, 100]
# n = int(float(len(x))*0.5)
# print n
# y = random.sample(x, n)
# print y
# plt.hist(y)
# plt.show()

# list 转置
a = [ [1,2,3], [4,5,6], [7,8,9]]
print a
print map(list, zip(*a))