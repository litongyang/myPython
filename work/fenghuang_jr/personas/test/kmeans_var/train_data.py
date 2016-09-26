# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
对用户的投资方差进行聚类
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing


class TrainDdata:
    def __init__(self):
        self.fr = open('user_var.txt', 'r')
        self.fw = open('result_user_var.txt', 'wr')
        self.user_id = []
        self.var_list = []  # 方差list
        self.train_set = []  # 训练级
        self.pre_result_list = []  # 预测结果list

    def get_train_data(self):
        for line in self.fr:
            line_one = line.split()
            self.user_id.append(line_one[0])
            self.var_list.append(float(line_one[1]))
            tmp = [0, float(line_one[1])]
            self.train_set.append(tmp)

    def kmeans_var(self):
        train_data = np.array(self.train_set)
        print train_data[:, 1]
        random_state = 170
        y_pre = KMeans(n_clusters=3, random_state=random_state).fit_predict(train_data)
        self.pre_result_list = np.ndarray.tolist(y_pre)
        plt.scatter(train_data[:, 0], train_data[:, 1], c=self.pre_result_list)
        plt.title("test")
        # plt.show()
        print type(self.pre_result_list)

    def get_result(self):
        for i in range(0, len(self.user_id)):
            self.fw.write(self.user_id[i])
            self.fw.write('\t')
            self.fw.write(str(self.var_list[i]))
            self.fw.write('\t')
            self.fw.write(str(self.pre_result_list[i]))
            self.fw.write('\n')


if __name__ == '__main__':
    test = TrainDdata()
    test.get_train_data()
    test.kmeans_var()
    test.get_result()
"""
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
"""