# -*- coding: utf-8 -*-
import sys
sys.path.append("/root/intelligence_info/")
from pymongo import MongoClient


class GetMongoData(object):
    def __init__(self):
        self.client = MongoClient('10.10.202.25', 27017)
        self.datadb = self.client.spider
        self.search = {}
        self.data = []
    def get_mongo_data(self):
        self.data = self.datadb.eastmoney_zf.find(self.search).limit(10)


if __name__ == '__main__':
    test = GetMongoData()
    test.get_mongo_data()
    # for d in test.data:
    #     print(d['code'])
    #     print(d['p_date'])
    #     print('====')
