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
    def __init__(self, train_set1, train_set2, train_set3, user_id_view_invest, k=3, metric='pearson', n=12):

        self.k = k
        self.n = n
        self.username2id = {}
        self.userid2name = {}
        self.productid2name = {}
        # self.train_set1_view_no_invest = data_view_no_invest

        self.metric = metric
        if self.metric == 'pearson':
            self.fn = self.pearson
        if type(train_set1).__name__ == 'dict' and type(train_set2).__name__ == 'dict' and type(train_set3).__name__ == 'dict':
            self.train_set1 = train_set1
            self.train_set2 = train_set2
            self.train_set3 = train_set3
        if type(user_id_view_invest).__name__ == 'list':
            self.user_id_view_invest = user_id_view_invest

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
        for instance in self.train_set2:
            if instance != username:
                """ 不同用户feature间的距离计算 """
                distance = self.fn(self.train_set1[username], self.train_set2[instance], username, instance)
                distances.append((instance, distance))

        distances.sort(key=lambda artistTuple: artistTuple[1], reverse=True)  # list:每个成员是tuple(用户id, 距离值)
        return distances

    # 推荐算法的主体函数
    def recommend(self, user):
        # 定义一个字典，用来存储推荐的用户id和feature
        recommendations = {}
        recommendations_user = {}
        # 计算出user与所有其他用户的相似度，返回一个list
        nearest = self.computeNearestNeighbor(user)
        userRatings = self.train_set1[user]  # 用户对应的值
        totalDistance = 0.0
        # 得住最近的k个近邻的总距离
        for i in range(self.k):
            totalDistance += nearest[i][1]
        if totalDistance == 0.0:
            totalDistance = 1.0

        # 将与user最相近的k个人中user没有买过的商品荐给user，并且这里又做了一个分数的计算排名
        for i in range(self.k):
            weight = nearest[i][1] / totalDistance  #第i个人的与user的相似度，转换到[0,1]之间
            # 第i个人的name
            name = nearest[i][0]
            # 第i个用户买过的产品和相应的数量
            neighborRatings = self.train_set3[name]
            # print self.train_set1[user]
            for bid_type in neighborRatings:
                if bid_type in userRatings:  # 推荐浏览过类型bid产品
                    if bid_type not in recommendations:
                        recommendations[bid_type] = (neighborRatings[bid_type] * weight)
                    else:
                        recommendations[bid_type] = (recommendations[bid_type] + neighborRatings[bid_type] * weight)
            if len(recommendations) == 0:  # 购买过所有类型的产品
                for bid_type in neighborRatings:
                    recommendations[bid_type] = (neighborRatings[bid_type] * weight)

        recommendations = list(recommendations.items())
        recommendations = [(self.convertProductID2name(k), v) for (k, v) in recommendations]

        # 做了一个排序
        recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
        return recommendations[:self.n], nearest











############################TEST###########################
# class Cf:
#     # data：数据集，这里指users
#     # k：表示得出最相近的k的近邻
#     # metric：表示使用计算相似度的方法
#     # n：表示推荐产品的个数
#     def __init__(self, data, train_set2, user_id_view_invest, k=3, metric='pearson', n=12):
#
#         self.k = k
#         self.n = n
#         self.username2id = {}
#         self.userid2name = {}
#         self.productid2name = {}
#         # self.train_set1_view_no_invest = data_view_no_invest
#
#         self.metric = metric
#         if self.metric == 'pearson':
#             self.fn = self.pearson
#         if type(data).__name__ == 'dict' and type(train_set2).__name__ == 'dict':
#             self.train_set1 = data
#             self.train_set2 = train_set2
#         if type(user_id_view_invest).__name__ == 'list':
#             self.user_id_view_invest = user_id_view_invest
#
#     def convertProductID2name(self, id):
#         if id in self.productid2name:
#             return self.productid2name[id]
#         else:
#             return id
#
#     # 定义的计算相似度的公式，用的是皮尔逊相关系数计算方法
#     def pearson(self, rating1, rating2, username, instance):
#         sum_xy = 0
#         sum_x = 0
#         sum_y = 0
#         sum_x2 = 0
#         sum_y2 = 0
#         n = 0
#         for key in rating1:
#             if key in rating2:
#                 n += 1
#                 x = rating1[key]
#                 y = rating2[key]
#                 sum_xy += x * y
#                 sum_x += x
#                 sum_y += y
#                 sum_x2 += pow(x, 2)
#                 sum_y2 += pow(y, 2)
#         if n == 0:
#             return 0
#
#         # 皮尔逊相关系数计算公式
#         denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
#         if denominator == 0:
#             return 0
#         else:
#             return (sum_xy - (sum_x * sum_y) / n) / denominator
#
#     def computeNearestNeighbor(self, username):
#         distances = []
#         print username
#         for instance in self.train_set1:
#             if instance != username:
#                 """ 不同用户feature间的距离计算 """
#                 distance = self.fn(self.train_set1[username], self.train_set1[instance], username, instance)
#                 distances.append((instance, distance))
#
#         distances.sort(key=lambda artistTuple: artistTuple[1], reverse=True)  # list:每个成员是tuple(用户id, 距离值)
#         # print "distances", distances
#         return distances
#
#     # 推荐算法的主体函数
#     def recommend(self, user):
#         # 定义一个字典，用来存储推荐的用户id和feature
#         recommendations = {}
#         recommendations_user = {}
#         # 计算出user与所有其他用户的相似度，返回一个list
#         nearest = self.computeNearestNeighbor(user)
#         nearest_invest = []
#         for i in range(len(nearest)):
#             if nearest[i][0] in self.user_id_view_invest:
#                 nearest_invest.append(nearest[i])
#         print "rrrrr", nearest_invest
#         # print "nearest", nearest
#         # print "nearest_invest", nearest_invest
#         # print len(nearest)
#         # print len(nearest_invest)
#         userRatings = self.train_set1[user]  # 用户对应的值
#         totalDistance = 0.0
#         if user in self.user_id_view_invest:  # 浏览、投资用户的推荐
#             print "iiiiii"
#             # 得住最近的k个近邻的总距离
#             for i in range(self.k):
#                 totalDistance += nearest[i][1]
#             if totalDistance == 0.0:
#                 totalDistance = 1.0
#
#             # 将与user最相近的k个人中user没有买过的商品荐给user，并且这里又做了一个分数的计算排名
#             for i in range(self.k):
#                 # 第i个人的与user的相似度，转换到[0,1]之间
#                 weight = nearest[i][1] / totalDistance
#                 # 第i个人的name
#                 name = nearest[i][0]
#                 # 第i个用户买过的产品和相应的数量
#                 neighborRatings = self.train_set1[name]
#                 # print self.train_set1[user]
#                 for bid_type in neighborRatings:
#                     if not bid_type in userRatings:  # 推荐没有购买过类型bid产品
#                         if bid_type not in recommendations:
#                             recommendations[bid_type] = (neighborRatings[bid_type] * weight)
#                         else:
#                             recommendations[bid_type] = (recommendations[bid_type] + neighborRatings[bid_type] * weight)
#                 if len(recommendations) == 0:  # 购买过所有类型的产品
#                     for bid_type in neighborRatings:
#                         recommendations[bid_type] = (neighborRatings[bid_type] * weight)
#
#         else:  # 只浏览不投资的用户推荐
#             # 得住最近的k个近邻的总距离
#             for i in range(self.k):
#                 totalDistance += nearest_invest[i][1]
#             if totalDistance == 0.0:
#                 totalDistance = 1.0
#             # 将与user最相近的k个人中user没有买过的商品荐给user，并且这里又做了一个分数的计算排名
#             for i in range(self.k):
#                 # 第i个人的与user的相似度，转换到[0,1]之间
#                 weight = nearest_invest[i][1] / totalDistance
#                 # 第i个人的name
#                 name = nearest_invest[i][0]
#                 # 第i个用户买过的产品和相应的数量
#                 neighbor_bid_invest = self.train_set1[name]
#                 for bid_type in neighbor_bid_invest:
#                     if bid_type in userRatings:  # 推荐浏览过类型bid产品
#                         if bid_type not in recommendations:
#                             recommendations[bid_type] = (neighbor_bid_invest[bid_type] * weight)
#                         else:
#                             recommendations[bid_type] = (recommendations[bid_type] + neighbor_bid_invest[bid_type] * weight)
#                 if len(recommendations) == 0:  # 购买过所有类型的产品
#                     for bid_type in neighbor_bid_invest:
#                         recommendations[bid_type] = (neighbor_bid_invest[bid_type] * weight)
#         recommendations = list(recommendations.items())
#         recommendations = [(self.convertProductID2name(k), v) for (k, v) in recommendations]
#
#         # 做了一个排序
#         recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
#         return recommendations[:self.n], nearest
