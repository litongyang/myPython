#__author__ = 'litongyang'
# -*- coding: utf-8 -*-

'''
贝叶斯算法
iris：训练数据
iris.data：训练数据的特征数据
iris.target：训练数据的标签数据（0，1，2）
target_pre:预测的标签
'''

from sklearn import datasets
from sklearn.naive_bayes import GaussianNB

iris = datasets.load_iris()
#print iris
gnb = GaussianNB()
target_pre = gnb.fit(iris.data, iris.target).predict(iris.data)
print target_pre
print iris.data
print("Number of mislabeled points out of a total %d points : %d"% (iris.data.shape[0],(iris.target != target_pre).sum()))