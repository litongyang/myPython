# __author__ = 'litongyang'
# -*- coding: utf-8 -*

# 降为算法：PCA、LDA、NMF

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.lda import LDA
from sklearn.decomposition import NMF
import matplotlib.pyplot as plt


class DescebdingAlgorithm:
    def __init__(self):
        self.iris = datasets.load_iris()
        self.pca_result = ()
        self.lda_result = ()
        self.nmf_result = ()

    def pca(self):
        pca = PCA(n_components=2)
        self.pca_result = pca.fit_transform(self.iris.data, self.iris.target)
        # print self.pca_result

    def lda(self):
        lda = LDA(n_components=2)
        self.lda_result = lda.fit_transform(self.iris.data, self.iris.target)

    def nmf(self):
        nmf = NMF(n_components=2)
        self.nmf_result = nmf.fit_transform(self.iris.data)
        # print self.iris.target
        # print self.nmf_result
        # print self.nmf_result[self.iris.target==0, 0]

    def drawing(self):
        result = [self.pca_result, self.lda_result, self.nmf_result]
        title = ["PCA on iris", "LDA on iris", "NMF on iris"]
        for i in range(0, len(result)):
            # print result[i]
            plt.subplot(1, len(result), i+1)

            # result[i][self.iris.target == 0, 0]:得到数组result[i]与数组self.iris.target == 0一一对应的每个成员的第一个值
            plt.scatter(result[i][self.iris.target == 0, 0], result[i][self.iris.target == 0, 1], color='r')
            plt.scatter(result[i][self.iris.target == 1, 0], result[i][self.iris.target == 1, 1], color='g')
            plt.scatter(result[i][self.iris.target == 2, 0], result[i][self.iris.target == 2, 1], color='b')
            plt.title(str(title[i]))
        plt.show()
        # plt.subplot(1, 3, 1)
        # plt.scatter(self.pca_result[self.iris.target == 0, 0], self.pca_result[self.iris.target == 0, 1], color='r')
        # plt.scatter(self.pca_result[self.iris.target == 1, 0], self.pca_result[self.iris.target == 1, 1], color='g')
        # plt.scatter(self.pca_result[self.iris.target == 2, 0], self.pca_result[self.iris.target == 2, 1], color='b')
        # plt.title('PCA on iris')
        # plt.show()

if __name__ == '__main__':
    descebding_algorithm = DescebdingAlgorithm()
    descebding_algorithm.pca()
    descebding_algorithm.lda()
    descebding_algorithm.nmf()
    descebding_algorithm.drawing()

