# __author__ = 'lty'
# -*- coding: utf-8 -*-

from sklearn import linear_model
import numpy as np
clf = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
clf.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
print clf.predict(np.array([[0,2]]))