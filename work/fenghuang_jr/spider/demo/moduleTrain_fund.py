# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


plt.figure(figsize=(12, 12))
random_state = 170
id = []
X = []
fi = open('pre_data_fund.txt', 'w')

for line in open('train_set_fund.txt'):
    line_one = line.split()
    id.append(line_one[0])

for line in open('train_set_fund.txt'):
    line_one = line.split()
    train_one = []
    # train_one.append(float(line_one[1]))
    train_one.append(float(line_one[2]))
    # train_one.append(float(line_one[3]))
    # train_one.append(float(line_one[7]))
    train_one.append(float(line_one[9]))
    # train_one.append(float(line_one[10]))
    # train_one.append(float(line_one[11]))
    # for i in range(1, len(line_one)):
    #     train_one.append(float(line_one[i]))
    X.append(train_one)

print X

y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X)
print y_pred

#  save and load model
# clf = KMeans(n_clusters=3, random_state=random_state)
# clf.fit(X)
# import pickle
# from sklearn.externals import joblib
# joblib.dump(clf, 'model_fund.pkl')
# clf1 = joblib.load('model_fund.pkl')
# y = clf1.predict(X)
# print y
# print s



for i in range(0, len(id)):
    fi.write(str(y_pred[i]))
    fi.write('\t')
    fi.write(str(id[i]))
    fi.write('\t')
    for v in X[i]:
        fi.write(str(v))
        fi.write('\t')
    fi.write('\n')

# drawing
x = map(list, zip(*X))

plt.scatter(x[0], x[1], c=y_pred)
plt.title("test")
plt.show()
