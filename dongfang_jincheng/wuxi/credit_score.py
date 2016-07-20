#  __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# ------企业信用模型-------

import work.wuxi.base_score as base  # 基本信息
import work.wuxi.cite_score as cite  # 表彰
import work.wuxi.credit_real_score as credit_real  # 非失信
import work.wuxi.dishonesty_score as dishonesty  # 失信
import numpy
import math
import matplotlib.pylab as plt
import seaborn as sns


# noinspection PyBroadException
class CreditScore:
    def __init__(self):
        self.base_class = base.BaseScore()
        self.cite_class = cite.CiteScore()
        self.creditReal_class = credit_real.CreditRealScore()
        self.dishonesty_class = dishonesty.DeshonestyScore()
        self.weight_type = 0.5  # 企业类型权重
        self.weight_register_captail = 0.5  # 注册资本权重
        self.weight_cite = 0.5  # 表彰权重
        self.weight_good_brand = 0.5  # 驰名商标权重
        self.weight_brand_register = 0.1634  # 贯标权重
        self.weight_credit = 0.3952  # 信用评定等级权重
        self.weight_certification_levels = 0.2781  # 工商认证等级权重
        self.weight_brand_c = 0.1634  # C标权重
        self.weight_gongjijin = 0.0951  # 公积金权重
        self.weight_owe = 0.0668  # 欠税权重
        self.weight_penalty = 0.1235  # 行政处罚权重
        self.weight_blackList = 0.1382  # 黑名单权重
        self.weight_bad_loan = 0.2012  # 不良贷款权重
        self.weight_illegal = 0.3083  # 企业违法权重

        self.weight_cite = 1  # 表彰权重
        self.weight_base = 2  # 基本信息权重
        self.weight_credit_real = 1  # 非失信权重
        self.weight_dishonesty = 2  # 失信权重

        self.base_score = {}
        self.cite_score = {}
        self.credit_real_score = {}
        self.dishonesty_score = {}
        self.credit_score = {}
        self.credit_score_info = {}
        self.credit_lable_info = {}

    # 计算基本信息得分
    def compute_base_score(self):
        cnt = 0
        self.base_class.get_data()
        self.base_class.process_data()
        self.base_class.compute_type_score()
        self.base_class.compute_register_capital_score()
        self.base_class.type_score = {key: float(value) * self.weight_type for key, value in
                                      self.base_class.type_score.items()}
        self.base_class.capital_score = {key: float(value) * self.weight_register_captail for key, value in
                                         self.base_class.capital_score.items()}
        for id, value in self.base_class.type_score.items():
            score_one = value
            if self.base_class.capital_score.has_key(id):
                score_one += self.base_class.capital_score[id]
            self.base_score[id] = score_one *2

        for k, v in self.base_score.items():
            if v != 0:
                cnt += 1
            print k, v
        print cnt

    # 计算表彰得分
    def compute_cite_score(self):
        cnt = 0
        self.cite_class.get_data()
        self.cite_class.compute_biaozhang_score()
        self.cite_class.compute_good_brand_score()

        self.cite_class.score_biaozhang = {key: float(value) * self.weight_brand_register for key, value in
                                           self.cite_class.score_biaozhang.items()}
        self.cite_class.good_brand_score = {key: float(value) * self.weight_good_brand for key, value in
                                            self.cite_class.good_brand_score.items()}
        for id, value in self.cite_class.score_biaozhang.items():
            score_one = value
            if self.cite_class.good_brand_score.has_key(id):
                score_one += self.cite_class.good_brand_score[id]
            self.cite_score[id] = score_one * 2
        for k, v in self.cite_score.items():
            if v != 0:
                cnt += 1
            print k, v
        print cnt

    # 计算非失信得分
    # noinspection PyBroadException
    def compute_credit_real_score(self):
        cnt = 0
        self.creditReal_class.get_data()
        self.creditReal_class.process_data()
        self.creditReal_class.compute_brand_register_score()
        self.creditReal_class.compute_credit_score()
        self.creditReal_class.compute_certification_levels_score()
        self.creditReal_class.compute_brand_c_score()
        # self.creditReal_class.process_score(self.creditReal_class.brand_register_score)
        # self.creditReal_class.process_score(self.creditReal_class.credit_assess_score)
        # self.creditReal_class.process_score(self.creditReal_class.certification_levels_score)

        # print len(self.creditReal_class.brand_register_score)
        self.creditReal_class.brand_register_score = {key: float(value) * self.weight_brand_register for key, value in
                                                      self.creditReal_class.brand_register_score.items()}
        self.creditReal_class.credit_assess_score = {key: float(value) * self.weight_credit for key, value in
                                                     self.creditReal_class.credit_assess_score.items()}
        self.creditReal_class.certification_levels_score = {key: float(value) * self.weight_certification_levels for
                                                            key, value in
                                                            self.creditReal_class.certification_levels_score.items()}
        self.creditReal_class.brand_c_score = {key: float(value) * self.weight_brand_c for key, value in
                                               self.creditReal_class.brand_c_score.items()}
        # for k,v in self.creditReal_class.brand_register_score.items():
        #     if v != 0:
        #         print v
        for id, value in self.creditReal_class.credit_assess_score.items():
            score_one = value
            # print score_one
            if self.creditReal_class.brand_register_score.has_key(id):
                score_one += self.creditReal_class.brand_register_score[id]
            if self.creditReal_class.certification_levels_score.has_key(id):
                score_one += self.creditReal_class.certification_levels_score[id]
            if self.creditReal_class.brand_c_score.has_key(id):
                score_one += self.creditReal_class.brand_c_score[id]
            self.credit_real_score[id] = score_one * 2

            # # 查看非信用的得分数量
            # if x != score_one:
            #     cnt +=1
            # print cnt

        for k, v in self.credit_real_score.items():
            if v > 0:
                cnt += 1
            print k, ':', v
        print cnt

    # 计算失信得分
    def compute_dishonesty_score(self):
        cnt = 0
        self.dishonesty_class.get_data()
        self.dishonesty_class.process_data()
        self.dishonesty_class.compute_gongjijin_score()
        self.dishonesty_class.compute_qianshui_score()
        self.dishonesty_class.compute_penalty_score()
        self.dishonesty_class.compute_black_list_score()
        self.dishonesty_class.compute_bad_loan_score()
        self.dishonesty_class.compute_illegal_score()
        # print len(self.dishonesty_class.common_reserve_score)
        self.dishonesty_class.common_reserve_score = {key: float(value) * self.weight_gongjijin for key, value in
                                                      self.dishonesty_class.common_reserve_score.items()}
        self.dishonesty_class.owing_taxes_score = {key: float(value) * self.weight_owe for key, value in
                                                   self.dishonesty_class.owing_taxes_score.items()}
        self.dishonesty_class.penalty_score = {key: float(value) * self.weight_penalty for key, value in
                                               self.dishonesty_class.penalty_score.items()}
        self.dishonesty_class.black_list_score = {key: float(value) * self.weight_blackList for key, value in
                                                  self.dishonesty_class.black_list_score.items()}
        self.dishonesty_class.bad_loan_score = {key: float(value) * self.weight_bad_loan for key, value in
                                                self.dishonesty_class.bad_loan_score.items()}
        self.dishonesty_class.illegal_score = {key: float(value) * self.weight_illegal for key, value in
                                               self.dishonesty_class.illegal_score.items()}
        for id, value in self.dishonesty_class.penalty_score.items():
            score_one = self.weight_penalty * value
            if self.dishonesty_class.common_reserve_score.has_key(id):
                score_one += self.dishonesty_class.common_reserve_score[id]
            if self.dishonesty_class.owing_taxes_score.has_key(id):
                score_one += self.dishonesty_class.owing_taxes_score[id]
            if self.dishonesty_class.black_list_score.has_key(id):
                score_one += self.dishonesty_class.black_list_score[id]
            if self.dishonesty_class.bad_loan_score.has_key(id):
                score_one += self.dishonesty_class.bad_loan_score[id]
            if self.dishonesty_class.illegal_score.has_key(id):
                score_one += self.weight_illegal * self.dishonesty_class.illegal_score[id]
            self.dishonesty_score[id] = score_one * 6 *2
        for k, v in self.dishonesty_score.items():
            if v != 0:
                cnt += 1
            print k, ':', v
        print cnt

    # 计算企业的信用得分
    def compute_credit_score(self):
        cnt = 0
        for id, value in self.base_score.items():
            try:
                self.credit_score_info[id] = []
                score_one = self.weight_base * value
                self.credit_score_info[id].append(value)
                if self.credit_real_score.has_key(id):
                    score_one += self.weight_credit_real * self.credit_real_score[id]
                    self.credit_score_info[id].append(self.credit_real_score[id])
                if self.dishonesty_score.has_key(id):
                    score_one -= self.weight_dishonesty * self.dishonesty_score[id]
                    self.credit_score_info[id].append(self.dishonesty_score[id])
                if self.cite_score.has_key(id):
                    score_one += self.weight_cite * self.cite_score[id]
                    self.credit_score_info[id].append(self.cite_score[id])
                # if self.credit_score.has_key(id):
                #     score_one += self.weight_credit * self.credit_score[id]
                self.credit_score[id] = 60 + score_one
                self.credit_score_info[id].append(self.credit_score[id])
            except:
                pass
        for k, v in self.credit_score_info.items():
            cnt += 1
            print k, v
        print cnt

    # 按信用分数将企业分类信息
    def company_score_label(self):
        for id,v in self.credit_score.items():
            if float(v) >= 80 :
                self.credit_lable_info[id] = 'A'
            elif 70<= float(v) <80:
                self.credit_lable_info[id] = 'B'
            elif 66<= float(v) <70:
                self.credit_lable_info[id] = 'C'
            elif 60<= float(v) <66:
                self.credit_lable_info[id] = 'D'
            elif float(v) <60:
                self.credit_lable_info[id] = 'E'
        # for k,v in self.credit_lable_info.items():
        #     print v
        for id,v in self.credit_score_info.items():
            if self.credit_lable_info.has_key(id):
                self.credit_score_info[id].append(self.credit_lable_info[id])
            else:
                self.credit_score_info[id].append('null')



    def drawing(self):
        data = []
        fl = open("C:\\Users\\\Thinkpad\\Desktop\\data_score.txt", 'w')
        for k,v in self.credit_score.items():
            # if float(v) <10:
            # fl.write(str(k))
            # fl.write("\t")
            fl.write(str(v))
            fl.write('\n')
            data.append(v)

        # sns.distplot(data, kde=True, color="#FF0000", rug=True, hist=True)
        # plt.show()

    # 查看分布
    @staticmethod
    def view_du(score_info):
        score_list = []
        for k,v in score_info.items():
            if float(v) != 0.0:
                score_list.append(float(v))
        max_v = max(score_list)
        min_v = min(score_list)
        mean_v = numpy.mean(score_list)
        # var_v = numpy.var(score_list)
        print "max:",max_v
        print "min:",min_v
        print "mean:",mean_v
        print "cnt:",len(score_list)

if __name__ == '__main__':
    credit_score = CreditScore()
    credit_score.compute_base_score()
    credit_score.compute_cite_score()
    credit_score.compute_credit_real_score()
    credit_score.compute_dishonesty_score()
    credit_score.compute_credit_score()
    credit_score.company_score_label()
    credit_score.drawing()
    print "dishonesty_score:"
    credit_score.view_du(credit_score.dishonesty_score)
    print "#############"
    print "base_score:"
    credit_score.view_du(credit_score.base_score)
    print "#############"
    print "credit_real_score:"
    credit_score.view_du(credit_score.credit_real_score)
    print "#############"
    print "cite_score:"
    credit_score.view_du(credit_score.cite_score)
    print "#############"
    print "credit_score:"
    credit_score.view_du(credit_score.credit_score)
    print "#############"
