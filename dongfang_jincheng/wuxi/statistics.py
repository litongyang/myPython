# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

import credit_score
import cite_score


class Statistics:
    def __init__(self):
        self.credit_score_class = credit_score.CreditScore()
        self.cite_class = cite_score.CiteScore()
        self.hot_cite = {}
        self.statistics_data = {}
        self.statistics_data_two = {}

        self.statistics_area = {}


    # 获取企业信用分数数据
    def get_credit_score(self):
        self.credit_score_class.compute_base_score()
        self.credit_score_class.compute_cite_score()
        self.credit_score_class.compute_credit_real_score()
        self.credit_score_class.compute_dishonesty_score()
        self.credit_score_class.compute_credit_score()
        self.credit_score_class.company_score_label()
        # list = []
        # for k,v in self.credit_score_class.credit_score_info.items():
        #     list.append(v[4])
        # print max(list)


        for id,v in self.credit_score_class.credit_score_info.items():
            self.statistics_data[id] = []
            #  地域信息
            if self.credit_score_class.base_class.area_info.has_key(id):
                self.statistics_data[id].append(v)
                self.statistics_data[id].append(str(self.credit_score_class.base_class.area_info[id]))
            else:
                self.statistics_data[id].append(v)
                self.statistics_data[id].append('null')
            #  企业信息
            if self.credit_score_class.base_class.company_info.has_key(id):
                self.statistics_data[id].append(self.credit_score_class.base_class.company_info[id])
            else:
                self.statistics_data[id].append('null')
            # 企业类型得分
            if self.credit_score_class.base_class.type_score.has_key(id):
                self.statistics_data[id].append(self.credit_score_class.base_class.type_score[id])
            else:
                self.statistics_data[id].append('0')
            # 注册资本得分
            if self.credit_score_class.base_class.capital_score.has_key(id):
                self.statistics_data[id].append(self.credit_score_class.base_class.capital_score[id])
            else:
                self.statistics_data[id].append('0')
            # 表彰得分
            if self.credit_score_class.cite_class.score_biaozhang.has_key(id):
                self.statistics_data[id].append(self.credit_score_class.cite_class.score_biaozhang[id])
            else:
                self.statistics_data[id].append('0')
            # 驰名商标得分
            if self.credit_score_class.cite_class.good_brand_score.has_key(id):
                self.statistics_data[id].append(self.credit_score_class.cite_class.good_brand_score[id])
            else:
                self.statistics_data[id].append('0')
            # 贯标得分
            if self.credit_score_class.creditReal_class.brand_register_score.has_key(id):
                self.statistics_data[id].append(self.credit_score_class.creditReal_class.brand_register_score[id])
            else:
                self.statistics_data[id].append('0')
            # 信用评定得分
            if self.credit_score_class.creditReal_class.credit_assess_score.has_key(id):
                self.statistics_data[id].append(self.credit_score_class.creditReal_class.credit_assess_score[id])
            else:
                self.statistics_data[id].append('0')
            # 工商认证等级得分
            if self.credit_score_class.creditReal_class.certification_levels_score.has_key(id):
                self.statistics_data[id].append(self.credit_score_class.creditReal_class.certification_levels_score[id])
            else:
                self.statistics_data[id].append('0')
            # C标得分
            if self.credit_score_class.creditReal_class.brand_c_score.has_key(id):
                self.statistics_data[id].append(self.credit_score_class.creditReal_class.brand_c_score[id])
            else:
                self.statistics_data[id].append('0')
            # 公积金得分
            if self.credit_score_class.dishonesty_class.common_reserve_score.has_key(id):
                self.statistics_data[id].append(self.credit_score_class.dishonesty_class.common_reserve_score[id])
            else:
                self.statistics_data[id].append('0')
            # 欠税得分
            if self.credit_score_class.dishonesty_class.owing_taxes_score.has_key(id):
                self.statistics_data[id].append(self.credit_score_class.dishonesty_class.owing_taxes_score[id])
            else:
                self.statistics_data[id].append('0')
            # 行政处罚的得分
            if self.credit_score_class.dishonesty_class.penalty_score.has_key(id):
                self.statistics_data[id].append(self.credit_score_class.dishonesty_class.penalty_score[id])
            else:
                self.statistics_data[id].append('0')
            # 法院黑名单得分
            if self.credit_score_class.dishonesty_class.black_list_score.has_key(id):
                self.statistics_data[id].append(self.credit_score_class.dishonesty_class.black_list_score[id])
            else:
                self.statistics_data[id].append('0')
            # 人行不良得分
            if self.credit_score_class.dishonesty_class.bad_loan_score.has_key(id):
                self.statistics_data[id].append(self.credit_score_class.dishonesty_class.bad_loan_score[id])
            else:
                self.statistics_data[id].append('0')
            # 违法企业得分
            if self.credit_score_class.dishonesty_class.illegal_score.has_key(id):
                self.statistics_data[id].append(self.credit_score_class.dishonesty_class.illegal_score[id])
            else:
                self.statistics_data[id].append('0')


        fl = open("C:\\Users\\\Thinkpad\\Desktop\\company_data_info.txt", 'w')
        fl.write("id")
        fl.write("\t")
        fl.write("base_score")
        fl.write("\t")
        fl.write("credit_real_score")
        fl.write("\t")
        fl.write("dishonesty_score")
        fl.write("\t")
        fl.write("cite_score")
        fl.write("\t")
        fl.write("credit_score")
        fl.write("\t")
        fl.write("credit_label")
        fl.write("\t")
        fl.write("area_id")
        fl.write("\t")
        # fl.write("name")
        # fl.write("\t")
        fl.write("type")
        fl.write("\t")
        fl.write("industry_code")
        fl.write("\t")
        fl.write("type_score")
        fl.write("\t")
        fl.write("capital_score")
        fl.write("\t")
        fl.write("score_biaozhang")
        fl.write("\t")
        fl.write("good_brand_score")
        fl.write("\t")
        fl.write("brand_register_score")
        fl.write("\t")
        fl.write("credit_assess_score")
        fl.write("\t")
        fl.write("certification_levels_score")
        fl.write("\t")
        fl.write("brand_c_score")
        fl.write("\t")
        fl.write("common_reserve_score")
        fl.write("\t")
        fl.write("owing_taxes_score")
        fl.write("\t")
        fl.write("penalty_score")
        fl.write("\t")
        fl.write("black_list_score")
        fl.write("\t")
        fl.write("bad_loan_score")
        fl.write("\t")
        fl.write("illegal_score")
        fl.write("\n")
        for k,v in self.statistics_data.items():
            fl.write(str(k))
            fl.write("\t")
            for i in range(0, len(v[0])):
                fl.write(str(v[0][i]))
                fl.write("\t")
            fl.write(str(v[1]))
            fl.write(str("\t"))
            for i in range(0, len(v[2])):
                # fl.write(str(v[2][i].decode('gb2312', 'ignore').encode('utf-8')))
                fl.write(str(v[2][i]))
                fl.write(str("\t"))
            for j in range(3, len(v)):
                try:
                    fl.write(str(round(float(v[j]), 2)))
                except:
                    fl.write('0')
                fl.write(str("\t"))
            # fl.write(str(v[3]))
            # fl.write(str("\t"))
            # fl.write(str(v[4]))
            # fl.write(str("\t"))
            # fl.write(str(v[5]))
            # fl.write(str("\t"))
            # fl.write(str(v[6]))
            # fl.write(str("\t"))
            # fl.write(str(v[7]))
            # fl.write(str("\t"))
            # fl.write(str(v[8]))
            # fl.write(str("\t"))
            # fl.write(str(v[9]))
            # fl.write(str("\t"))
            # fl.write(str(v[10]))
            # fl.write(str("\t"))
            # fl.write(str(v[11]))
            fl.write("\n")
        for k,v in self.statistics_data.items():
            print k,v

        # 二级指标
        for id,v in self.credit_score_class.credit_score_info.items():
            self.statistics_data[id] = []
            if self.credit_score_class.base_class.area_info.has_key(id):
                self.statistics_data[id].append(v)
                self.statistics_data[id].append(str(self.credit_score_class.base_class.area_info[id]))
            else:
                self.statistics_data[id].append(v)
                self.statistics_data[id].append('null')

    def hot_info(self):
        self.cite_class.get_data()
        self.cite_class.compute_biaozhang_score()
        for id,v in self.cite_class.score_biaozhang.items():
            print id,v


    def statistics_function(self):
        area_code = []
        for id,v in self.statistics_data.items():
            if v[1] not in area_code:
                area_code.append(v[1])
        for i in range(0, len(area_code)):
            self.statistics_area[area_code[i]] = []
            for id ,v in self.statistics_data.items():
                if area_code[i] == v[1]:
                    self.statistics_area[area_code[i]].append(v[0])
        for k,v in self.statistics_area.items():
            print k,":",len(v)

if __name__ == '__main__':
    statistics = Statistics()
    statistics.hot_info()
    statistics.get_credit_score()


    # statistics.statistics_function()
    # print statistics.credit_score_class.credit_score