# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn.externals import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve
from sklearn.svm import SVC
from sklearn import datasets

iris = datasets.load_iris()
# print iris
X = iris.data[:, 0:2]  # we only take the first two features for visualization
y = iris.target


n_features = X.shape[1]
C = 1.0
#
# Create different classifiers. The logistic regression cannot do
# multiclass out of the box.

# penalty:惩罚种类
classifiers = {'L1 logistic': LogisticRegression(C=C, penalty='l1'),
               'L2 logistic (OvR)': LogisticRegression(C=C, penalty='l2'),
               'Linear SVC': SVC(kernel='linear', C=C, probability=True,
                                 random_state=0),
               'L2 logistic (Multinomial)': LogisticRegression(
                C=C, solver='lbfgs', multi_class='multinomial'
                )}

n_classifiers = len(classifiers)
# setting figure layout
plt.figure(figsize=(3 * 2, n_classifiers * 2))
plt.subplots_adjust(bottom=.2, top=.95)

# xx: rang(3,9), 100 numbers
# yy: rang(1,5), 100 numbers
xx = np.linspace(3, 9, 100)
yy = np.linspace(1, 5, 100).T

#  在 xx、yy 范围内采用三维网格数据
xx, yy = np.meshgrid(xx, yy)

# 合并xx、yy数据
Xfull = np.c_[xx.ravel(), yy.ravel()]

for index, (name, classifier) in enumerate(classifiers.items()):
    # 获取参数
    params = classifier.get_params()
    # 训练模型
    clf = classifier.fit(X, y)
    # print clf
    print name
    # 把模型保存到本地
    # joblib.dump(clf, 'model')

    y_pred = classifier.predict(X)
    # print y_pred

    # classif_rate：准确率
    classif_rate = np.mean(y_pred.ravel() == y.ravel()) * 100
    print('classif_rate for %s : %f ' % (name, classif_rate))

    # precision, recall, thresholds = precision_recall_curve(y, classifier.predict(X))
    # print "precision,recall,thresholds:",  precision, recall, thresholds

    # View probabilities
    # print Xfull
    probas = classifier.predict_proba(Xfull)
    print probas
    # n_classes:  number of kind of y_pred
    n_classes = np.unique(y_pred).size
    # print n_classes
    for k in range(n_classes):
        plt.subplot(n_classifiers, n_classes, index * n_classes + k + 1)
        plt.title("Class %d" % k)
        if k == 0:
            plt.ylabel(name)

        # probas[:, k].reshape((100, 100): 把probas[:, k]变成100行100列的数组
        imshow_handle = plt.imshow(probas[:, k].reshape((100, 100)),
                                   extent=(3, 9, 1, 5), origin='lower')  # extent：range
        plt.xticks(())
        plt.yticks(())

        idx = (y_pred == k)
        if idx.any():
            plt.scatter(X[idx, 0], X[idx, 1], marker='o', c='k')

ax = plt.axes([0.15, 0.04, 0.7, 0.05])
plt.title("Probability")
plt.colorbar(imshow_handle, cax=ax, orientation='horizontal')

plt.show()
