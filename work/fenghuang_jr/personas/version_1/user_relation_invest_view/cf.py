# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
协同过滤算法:基于pearson公式
"""
from math import sqrt


class Cf:
    # data：数据集，这里指users
    # k：表示得出最相近的k的近邻
    # metric：表示使用计算相似度的方法
    # n：表示推荐产品的个数
    def __init__(self, data, data_invest, data_view_no_invest, k=3, metric='pearson', n=12):

        self.k = k
        self.n = n
        self.username2id = {}
        self.userid2name = {}
        self.productid2name = {}
        self.data_view_no_invest = data_view_no_invest

        self.metric = metric
        if self.metric == 'pearson':
            self.fn = self.pearson
        if type(data).__name__ == 'dict' and type(data_invest).__name__ == 'dict':
            self.data = data
            self.data_invest = data_invest

    def convertProductID2name(self, id):
        if id in self.productid2name:
            return self.productid2name[id]
        else:
            return id

    # 定义的计算相似度的公式，用的是皮尔逊相关系数计算方法
    def pearson(self, rating1, rating2, username, instance):
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_y2 = 0
        n = 0
        for key in rating1:
            if key in rating2:
                n += 1
                x = rating1[key]
                y = rating2[key]
                sum_xy += x * y
                sum_x += x
                sum_y += y
                sum_x2 += pow(x, 2)
                sum_y2 += pow(y, 2)
        if n == 0:
            return 0

        # 皮尔逊相关系数计算公式
        denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
        if denominator == 0:
            return 0
        else:
            return (sum_xy - (sum_x * sum_y) / n) / denominator

    def computeNearestNeighbor(self, username):
        distances = []
        print username
        for instance in self.data:
            if instance != username:
                """ 不同用户feature间的距离计算 """
                distance = self.fn(self.data[username], self.data[instance], username, instance)
                distances.append((instance, distance))

        distances.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
        return distances

    # 推荐算法的主体函数
    def recommend(self, user):
        # 定义一个字典，用来存储推荐的用户id和feature
        recommendations = {}
        # 计算出user与所有其他用户的相似度，返回一个list
        nearest = self.computeNearestNeighbor(user)
        print "sss", len(nearest)
        userRatings = self.data[user]
        totalDistance = 0.0
        # 得住最近的k个近邻的总距离
        for i in range(self.k):
            totalDistance += nearest[i][1]
        if totalDistance == 0.0:
            totalDistance = 1.0

        # 将与user最相近的k个人中user没有买过的商品荐给user，并且这里又做了一个分数的计算排名
        for i in range(len(nearest)):

            # 第i个人的与user的相似度，转换到[0,1]之间
            weight = nearest[i][1] / totalDistance

            # 第i个人的name
            name = nearest[i][0]

            # 第i个用户买过的产品和相应的数量
            neighborRatings = self.data_invest[name]
            # print self.data[user]
            print neighborRatings

            if user not in self.data_view_no_invest:  # 浏览、投资用户的推荐
                for artist in neighborRatings:
                    if not artist in userRatings:
                        if artist not in recommendations:
                            recommendations[artist] = (neighborRatings[artist] * weight)
                        else:
                            recommendations[artist] = (recommendations[artist] + neighborRatings[artist] * weight)
            else:  # 只浏览不投资的用户推荐
                for artist in neighborRatings:
                    max_investcnt_tuple = max(neighborRatings.items(), key=lambda x: x[1])
                    recommendations[artist] = max_investcnt_tuple[0]

                # print "ss9999s", neighborRatings
                # max_cnt = 0
                # for invest_cnt in neighborRatings:
                #     if max_cnt < neighborRatings[invest_cnt]:
                #         max_cnt = neighborRatings[invest_cnt]
                # print max_cnt
                # print "*******"



        recommendations = list(recommendations.items())
        recommendations = [(self.convertProductID2name(k), v) for (k, v) in recommendations]

        # 做了一个排序
        recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse=True)

        return recommendations[:self.n], nearest