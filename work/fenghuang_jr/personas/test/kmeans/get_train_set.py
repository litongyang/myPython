# __author__ = 'lty'
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing
random_state = 170
train_set = []
user_id = []
age = []
gender = []
total_points = []

fl = open('train.txt', 'r')
for line in fl:
    line_one = line.split()
    user_id.append(line_one[0])
    age.append(line_one[1])
    gender.append(line_one[2])
    total_points.append(line_one[3])
for i in range(0, len(age)):
    tmp = [int(age[i]), int(gender[i]), int(total_points[i])]
    train_set.append(tmp)
# print train_set

X = np.array(train_set)

# X_n = preprocessing.scale(X)
# print X_n
# min_max_scaler = preprocessing.MinMaxScaler()
# X_n = min_max_scaler.fit_transform(X)
# print X_n

normalizer = preprocessing.Normalizer().fit(X)
X_n = normalizer.transform(X)
print X_n
y_pred = KMeans(n_clusters=5, random_state=random_state).fit_predict(X_n)
print y_pred
plt.scatter(X_n[:, 0], X_n[:, 2], c=y_pred)
plt.title("test")
plt.show()
fi = open('result.txt', 'w')
for i in range(0, len(age)):
    fi.write(str(user_id[i]))
    fi.write('\t')
    fi.write(str(age[i]))
    fi.write('\t')
    fi.write(str(gender[i]))
    fi.write('\t')
    fi.write(str(total_points[i]))
    fi.write('\t')
    fi.write(str(y_pred[i]))
    # for v in X[i]:
    #     fi.write(str(v))
    #     fi.write('\t')
    fi.write('\n')
fi.close()