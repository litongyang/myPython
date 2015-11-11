# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

from sklearn.externals import joblib
from sklearn import datasets

# Test data
iris = datasets.load_iris()
X = iris.data[:, 0:2]
y = iris.target

clf = joblib.load('model')
print clf.predict(X)

