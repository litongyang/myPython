# __author__ = 'litongyang'
# -*- coding: utf-8 -*-


class DataInit:
    def __init__(self):
        # 每个指标的编码集合
        self.indexCode = [
            "A010101",
            "A010102",
            "A010103",
            "A010104",
            "A010105",
            "A010106",
            "A010401",
            "A010402",
            "A010403",
            "A010701",
            "A010801",
            "A010802",
            "A010803",

            "A0201",
            "A0202",
            "A020801",
            "A020802",
            "A020803",
            "A020804",
            "A020805",
            "A020806",

            "A0701",
            "A0702",
            "A0703",
            "A0704",
            "A0705",

            "A08",
            "A0901",
            "A0902",
            "A0A01",
            "A0B01"
        ]


        # ------价格指数------
        # 居民消费价格分类指数(上年同月=100)
        self.priceIdex1_1 = [[] for i in range(9)]  # 全国居民消费价格分类指数
        self.priceIdex1_2 = [[] for i in range(7)]  # 全国食品类居民消费价格指数
        self.priceIdex1_3 = [[] for i in range(9)]  # 城市居民消费价格分类指数(上年同月=100)
        self.priceIdex1_4 = [[] for i in range(7)]  # 食品类城市居民消费价格指数(上年同月=100)
        self.priceIdex1_5 = [[] for i in range(9)]  # 农村居民消费价格分类指数(上年同月=100
        self.priceIdex1_6 = [[] for i in range(7)]  # 食品类农村居民消费价格指数(上年同月=100)
        # 商品零售价格分类指数(上年同月=100)
        self.priceIdex4_1 = [[] for i in range(17)]  # 商品零售价格指数(上年同月=100)
        self.priceIdex4_2 = [[] for i in range(17)]  # 城市商品零售价格指数(上年同月=100)
        self.priceIdex4_3 = [[] for i in range(17)]  # 农村商品零售价格指数(上年同月=100)
        # 工业生产者购进价格指数
        self.priceIdex7_1 = [[] for i in range(10)]  # 工业生产者购进价格指数(上年同月=100)
        # 工业生产者出厂价格分类指数
        self.priceIdex8_1 = [[] for i in range(3)]  # 工业生产者出厂价格指数(上年同月=100)
        self.priceIdex8_2 = [[] for i in range(4)]  # 生产资料工业生产者出厂价格指数(上年同月=100)
        self.priceIdex8_3 = [[] for i in range(5)]  # 生活资料工业生产者出厂价格指数(上年同月=100)

        # 工业
        self.industry1 = [[] for i in range(2)]  # 工业增加值增长速度
        self.industry2 = [[] for i in range(12)]  # 按经济类型分工业增加值增长速度
        self.industry8_1 = [[] for i in range(4)]  # 天然原油
        self.industry8_2 = [[] for i in range(4)]  # 铁矿石原矿量
        self.industry8_3 = [[] for i in range(4)]  # 磷矿石
        self.industry8_4 = [[] for i in range(4)]  # 原盐
        self.industry8_5 = [[] for i in range(4)]  # 成品糖
        self.industry8_6 = [[] for i in range(4)]  # 软饮料

        # -----交通运输-----
        self.traffic7_1 = [[] for i in range(20)]  # 货物运输量
        self.traffic7_2 = [[] for i in range(20)]  # 货物周转量
        self.traffic7_3 = [[] for i in range(20)]  # 旅客运输量
        self.traffic7_4 = [[] for i in range(20)]  # 旅客周转量
        self.traffic7_5 = [[] for i in range(8)]  # 规模以上港口吞吐量

        # 邮电通信
        self.communication = [[] for i in range(84)]  # 邮电通信

        # 采购经理指数
        self.PMI9_1 = [[] for i in range(13)]  # 制造业采购经理指数
        self.PMI9_2 = [[] for i in range(10)]  # 非制造业采购经理指数

        # 财政
        self.finance = [[] for i in range(6)]  # 国家财政预算收入及支出完成情况

        # 金融
        self.money_supply = [[] for i in range(5)]  # 货币供应量

        self.data_dict = {
            "A010101":self.priceIdex1_1,
            "A010102":self.priceIdex1_2,
            "A010103":self.priceIdex1_3,
            "A010104":self.priceIdex1_4,
            "A010105":self.priceIdex1_5,
            "A010106":self.priceIdex1_6,
            "A010401":self.priceIdex4_1,
            "A010402":self.priceIdex4_2,
            "A010403":self.priceIdex4_3,
            "A010701":self.priceIdex7_1,
            "A010801":self.priceIdex8_1,
            "A010802":self.priceIdex8_2,
            "A010803":self.priceIdex8_3,

            "A0201": self.industry1,
            "A0202": self.industry2,
            "A020801": self.industry8_1,
            "A020802": self.industry8_2,
            "A020803": self.industry8_3,
            "A020804": self.industry8_4,
            "A020805": self.industry8_5,
            "A020806": self.industry8_6,

            "A0701":self.traffic7_1,
            "A0702":self.traffic7_2,
            "A0703":self.traffic7_3,
            "A0704":self.traffic7_4,
            "A0705":self.traffic7_5,

            "A08": self.communication,

            "A0901": self.PMI9_1,
            "A0902": self.PMI9_2,

            "A0A01": self.finance,
            "A0B01": self.money_supply
        }
