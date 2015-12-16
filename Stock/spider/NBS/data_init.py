# __author__ = 'litongyang'
# -*- coding: utf-8 -*-


class DataInit:
    def __init__(self):
        # ------价格指数------
        # 居民消费价格分类指数(上年同月=100)
        self.priceIdex1_1 = [[] for i in range(9)]  # 全国居民消费价格分类指数(上年同月=100)
        self.priceIdex1_2 = [[] for i in range(7)]  # 全国食品类居民消费价格指数(上年同月=100)
        self.priceIdex1_3 = [[] for i in range(9)]  # 城市居民消费价格分类指数(上年同月=100)
        self.priceIdex1_4 = [[] for i in range(7)]  # 食品类城市居民消费价格指数(上年同月=100)
        self.priceIdex1_5 = [[] for i in range(9)]  # 农村居民消费价格分类指数(上年同月=100）
        self.priceIdex1_6 = [[] for i in range(7)]  # 食品类农村居民消费价格指数(上年同月=100)
        # 居民消费价格分类指数(上年同期=100)
        self.priceIdex2_1 = [[] for i in range(9)]  # 全国居民消费价格分类指数(上年同期=100)
        self.priceIdex2_2 = [[] for i in range(7)]  # 全国食品类居民消费价格指数(上年同期=100)
        self.priceIdex2_3 = [[] for i in range(9)]  # 城市居民消费价格分类指数(上年同期=100)
        self.priceIdex2_4 = [[] for i in range(7)]  # 食品类城市居民消费价格指数(上年同期=100)
        self.priceIdex2_5 = [[] for i in range(9)]  # 农村居民消费价格分类指数(上年同期=100)
        self.priceIdex2_6 = [[] for i in range(7)]  # 食品类农村居民消费价格指数(上年同期=100)
        # 居民消费价格分类指数((上月=100)
        self.priceIdex3_1 = [[] for i in range(9)]  # 全国居民消费价格分类指数(上月=100)
        self.priceIdex3_2 = [[] for i in range(7)]  # 全国食品类居民消费价格指数(上月=100)
        self.priceIdex3_3 = [[] for i in range(9)]  # 城市居民消费价格分类指数(上月=100)
        self.priceIdex3_4 = [[] for i in range(7)]  # 食品类城市居民消费价格指数(上月=100)
        self.priceIdex3_5 = [[] for i in range(9)]  # 农村居民消费价格分类指数(上月=100)
        self.priceIdex3_6 = [[] for i in range(7)]  # 食品类农村居民消费价格指数(上月=100)
        # 商品零售价格分类指数(上年同月=100)
        self.priceIdex4_1 = [[] for i in range(17)]  # 商品零售价格指数(上年同月=100)
        self.priceIdex4_2 = [[] for i in range(17)]  # 城市商品零售价格指数(上年同月=100)
        self.priceIdex4_3 = [[] for i in range(17)]  # 农村商品零售价格指数(上年同月=100)
        # 商品零售价格分类指数(上年同期=100)
        self.priceIdex5_1 = [[] for i in range(17)]  # 商品零售价格指数(上年同期=100)
        self.priceIdex5_2 = [[] for i in range(17)]  # 城市商品零售价格指数(上年同期=100)
        self.priceIdex5_3 = [[] for i in range(17)]  # 农村商品零售价格指数(上年同期=100)
        # 商品零售价格分类指数(上月=100)
        self.priceIdex6_1 = [[] for i in range(17)]  # 商品零售价格指数(上月=100)
        self.priceIdex6_2 = [[] for i in range(17)]  # 城市商品零售价格指数(上月=100)
        self.priceIdex6_3 = [[] for i in range(17)]  # 农村商品零售价格指数(上月=100)
        # 工业生产者购进价格指数
        self.priceIdex7_1 = [[] for i in range(10)]  # 工业生产者购进价格指数(上年同月=100)
        self.priceIdex7_2 = [[] for i in range(10)]  # 工业生产者购进价格指数(上年同期=100)
        self.priceIdex7_3 = [[] for i in range(10)]  # 工业生产者购进价格指数(上月=100)
        # 工业生产者出厂价格分类指数
        self.priceIdex8_1 = [[] for i in range(3)]  # 工业生产者出厂价格指数(上年同月=100)
        self.priceIdex8_2 = [[] for i in range(4)]  # 生产资料工业生产者出厂价格指数(上年同月=100)
        self.priceIdex8_3 = [[] for i in range(5)]  # 生活资料工业生产者出厂价格指数(上年同月=100)
        self.priceIdex8_4 = [[] for i in range(3)]  # 工业生产者出厂价格指数(上年同期=100)
        self.priceIdex8_5 = [[] for i in range(4)]  # 生产资料工业生产者出厂价格指数(上年同期=100)
        self.priceIdex8_6 = [[] for i in range(5)]  # 生活资料工业生产者出厂价格指数(上年同期=100)
        self.priceIdex8_7 = [[] for i in range(3)]  # 工业生产者出厂价格指数(上月=100)
        self.priceIdex8_8 = [[] for i in range(4)]  # 生产资料工业生产者出厂价格指数(上月=100)
        self.priceIdex8_9 = [[] for i in range(5)]  # 生活资料工业生产者出厂价格指数(上月=100)
        # 分行业工业生产者出厂价格指数(上年同月=100)(2007-2013)
        self.priceIdex9 = [[] for i in range(42)]  # 分行业工业生产者出厂价格指数(上年同月=100)(2007-2013)
        # 分行业工业生产者出厂价格指数(上年同月=100)(2014-至今)
        self.priceIdexA = [[] for i in range(42)]  # 分行业工业生产者出厂价格指数(上年同月=100)(2014-至今)

        # ------工业-------
        self.industry1 = [[] for i in range(2)]  # 工业增加值增长速度
        self.industry2 = [[] for i in range(12)]  # 按经济类型分工业增加值增长速度
        self.industry4_2011 = [[] for i in range(12)]  # 工业分大类行业增加值增长速度(2003-2011)
        self.industry5_now = [[] for i in range(12)]  # 工业分大类行业增加值增长速度(2012-至今)

        self.industry8_1 = [[] for i in range(4)]  # 天然原油
        self.industry8_2 = [[] for i in range(4)]  # 铁矿石原矿量
        self.industry8_3 = [[] for i in range(4)]  # 磷矿石
        self.industry8_4 = [[] for i in range(4)]  # 原盐
        self.industry8_5 = [[] for i in range(4)]  # 成品糖
        self.industry8_6 = [[] for i in range(4)]  # 软饮料
        self.industry8_7 = [[] for i in range(4)]  # 纱
        self.industry8_8 = [[] for i in range(4)]  # 布
        self.industry8_9 = [[] for i in range(4)]  # 蚕丝及交织机织物(含蚕量≧50%)
        self.industry8_A = [[] for i in range(4)]  # 机制纸及纸板
        self.industry8_B = [[] for i in range(4)]  # 新闻纸
        self.industry8_C = [[] for i in range(4)]  # 汽油
        self.industry8_D = [[] for i in range(4)]  # 煤油
        self.industry8_E = [[] for i in range(4)]  # 机制纸及纸板

        # -----固定资产投资(不含农户)-----
        self.FAI1 = [[] for i in range(34)]  # 固定资产投资情况
        self.FAI4 = [[] for i in range(18)]  # 固定资产投资资金来源情况
        # 分行业固定资产投资情况(2004-2011)
        self.FAI6_1_2011 = [[] for i in range(4)]  # 农林牧渔业固定资产投资额
        self.FAI6_2_2011 = [[] for i in range(14)]  # 采矿业固定资产投资额
        self.FAI6_3_2011 = [[] for i in range(62)]  # 制造业固定资产投资额
        # 分行业固定资产投资情况(2012-至今)
        self.FAI7_1_now = [[] for i in range(4)]  # 农林牧渔业固定资产投资额
        self.FAI7_2_now = [[] for i in range(14)]  # 采矿业固定资产投资额
        self.FAI7_3_now = [[] for i in range(62)]  # 制造业固定资产投资额
        #  -----
        self.FAI8 = [[] for i in range(58)]  # 按登记注册类型分的固定资产投资情况
        self.FAI9 = [[] for i in range(6)]   # 固定资产投资住宅建设情况
        self.FAIA = [[] for i in range(6)]   # 固定资产投资项目情况
        self.FAIB = [[] for i in range(4)]   # 固定资产投资项目计划总投资
        self.FAIC = [[] for i in range(8)]   # 民间固定资产投资
        self.FAID = [[] for i in range(60)]  # 按行业分民间固定资产投资

        # -------国内贸易------
        self.tradeHome1 = [[] for i in range(8)]  # 社会消费品零售总额
        self.tradeHome2 = [[] for i in range(8)]  # 按经营地分社会消费品零售总额
        self.tradeHome3 = [[] for i in range(16)]  # 按消费形态分社会消费品零售总额
        # 限上单位商品零售类值
        self.tradeHome5_1 = [[] for i in range(24)]  # 粮油、食品、饮料、烟酒类
        self.tradeHome5_2 = [[] for i in range(8)]  # 服装鞋帽、针、纺织品类
        self.tradeHome5_3 = [[] for i in range(4)]  # 化妆品类
        self.tradeHome5_4 = [[] for i in range(4)]  # 金银珠宝类
        self.tradeHome5_5 = [[] for i in range(4)]  # 日用品类
        self.tradeHome5_6 = [[] for i in range(4)]  # 体育、娱乐用品类
        self.tradeHome5_7 = [[] for i in range(4)]  # 书报杂志类
        self.tradeHome5_8 = [[] for i in range(4)]  # 家用电器和音像器材类
        self.tradeHome5_9 = [[] for i in range(4)]  # 中西药品类
        self.tradeHome5_A = [[] for i in range(4)]  # 文化办公用品类
        self.tradeHome5_B = [[] for i in range(4)]  # 家具类
        self.tradeHome5_C = [[] for i in range(4)]  # 通讯器材类
        self.tradeHome5_D = [[] for i in range(4)]  # 石油及制品类
        self.tradeHome5_E = [[] for i in range(4)]  # 建筑及装潢材料类
        self.tradeHome5_F = [[] for i in range(4)]  # 汽车类
        self.tradeHome5_G = [[] for i in range(4)]  # 其他

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


        # ----------------每个指标的编码集合---------------------
        self.indexCode = [
            "A010101",
            "A010102",
            "A010103",
            "A010104",
            "A010105",
            "A010106",
            "A010201",
            "A010202",
            "A010203",
            "A010204",
            "A010205",
            "A010206",
            "A010301",
            "A010302",
            "A010303",
            "A010304",
            "A010305",
            "A010306",
            "A010401",
            "A010402",
            "A010403",
            "A010501",
            "A010502",
            "A010503",
            "A010601",
            "A010602",
            "A010603",
            "A010701",
            "A010702",
            "A010703",
            "A010801",
            "A010802",
            "A010803",
            "A010804",
            "A010805",
            "A010806",
            "A010807",
            "A010808",
            "A010809",
            "A0109",
            "A010A",

            "A0201",
            "A0202",
            "A0204",
            "A0205",
            "A020801",
            "A020802",
            "A020803",
            "A020804",
            "A020805",
            "A020806",

            "A0301",
            "A0304",
            "A030601",
            "A030602",
            "A030603",
            "A030701",
            "A030702",
            "A030703",
            "A0308",
            "A0309",
            "A030A",
            "A030B",
            "A030C",
            "A030D",

            "A0501",
            "A0502",
            "A0503",
            "A050501",
            "A050502",
            "A050503",
            "A050504",
            "A050505",
            "A050506",
            "A050507",
            "A050508",
            "A050509",
            "A05050A",
            "A05050B",
            "A05050C",
            "A05050D",
            "A05050E",
            "A05050F",
            "A05050G",

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


        self.data_dict = {
            "A010101":self.priceIdex1_1,
            "A010102":self.priceIdex1_2,
            "A010103":self.priceIdex1_3,
            "A010104":self.priceIdex1_4,
            "A010105":self.priceIdex1_5,
            "A010106":self.priceIdex1_6,
            "A010201":self.priceIdex2_1,
            "A010202":self.priceIdex2_2,
            "A010203":self.priceIdex2_3,
            "A010204":self.priceIdex2_4,
            "A010205":self.priceIdex2_5,
            "A010206":self.priceIdex2_6,
            "A010301":self.priceIdex3_1,
            "A010302":self.priceIdex3_2,
            "A010303":self.priceIdex3_3,
            "A010304":self.priceIdex3_4,
            "A010305":self.priceIdex3_5,
            "A010306":self.priceIdex3_6,
            "A010401":self.priceIdex4_1,
            "A010402":self.priceIdex4_2,
            "A010403":self.priceIdex4_3,
            "A010501":self.priceIdex5_1,
            "A010502":self.priceIdex5_2,
            "A010503":self.priceIdex5_3,
            "A010601":self.priceIdex6_1,
            "A010602":self.priceIdex6_2,
            "A010603":self.priceIdex6_3,

            "A010701":self.priceIdex7_1,
            "A010702":self.priceIdex7_2,
            "A010703":self.priceIdex7_3,
            "A010801":self.priceIdex8_1,
            "A010802":self.priceIdex8_2,
            "A010803":self.priceIdex8_3,
            "A010804":self.priceIdex8_4,
            "A010805":self.priceIdex8_5,
            "A010806":self.priceIdex8_6,
            "A010807":self.priceIdex8_7,
            "A010808":self.priceIdex8_8,
            "A010809":self.priceIdex8_9,
            "A0109":self.priceIdex9,
            "A010A":self.priceIdexA,

            "A0201": self.industry1,
            "A0202": self.industry2,
            "A020801": self.industry8_1,
            "A020802": self.industry8_2,
            "A020803": self.industry8_3,
            "A020804": self.industry8_4,
            "A020805": self.industry8_5,
            "A020806": self.industry8_6,

            "A0301": self.FAI1,
            "A0304": self.FAI4,
            "A030601": self.FAI6_1_2011,
            "A030602": self.FAI6_2_2011,
            "A030603": self.FAI6_3_2011,
            "A030701": self.FAI7_1_now,
            "A030702": self.FAI7_2_now,
            "A030703": self.FAI7_3_now,
            "A0308": self.FAI8,
            "A0309": self.FAI9,
            "A030A": self.FAIA,
            "A030B": self.FAIB,
            "A030C": self.FAIC,
            "A030D": self.FAID,

            "A0501": self.tradeHome1,
            "A0502": self.tradeHome2,
            "A0503": self.tradeHome3,
            "A050501": self.tradeHome5_1,
            "A050502": self.tradeHome5_2,
            "A050503": self.tradeHome5_3,
            "A050504": self.tradeHome5_4,
            "A050505": self.tradeHome5_5,
            "A050506": self.tradeHome5_6,
            "A050507": self.tradeHome5_7,
            "A050508": self.tradeHome5_8,
            "A050509": self.tradeHome5_9,
            "A05050A": self.tradeHome5_A,
            "A05050B": self.tradeHome5_B,
            "A05050C": self.tradeHome5_C,
            "A05050D": self.tradeHome5_D,
            "A05050E": self.tradeHome5_E,
            "A05050F": self.tradeHome5_F,
            "A05050G": self.tradeHome5_G,

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
