# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

import credit_score
import cx_Oracle
x= cx_Oracle.connect()

class Statistics:
    def __init__(self):
        self.credit_score_class = credit_score.CreditScore()
        self.statistics_data = {}

        self.statistics_area = {}

    # 获取企业信用分数数据
    def get_credit_score(self):
        self.credit_score_class.compute_base_score()
        self.credit_score_class.compute_cite_score()
        self.credit_score_class.compute_credit_real_score()
        self.credit_score_class.compute_dishonesty_score()
        self.credit_score_class.compute_credit_score()
        # self.credit_score_class.drawing()

        for id,v in self.credit_score_class.credit_score.items():
            self.statistics_data[id] = []
            if self.credit_score_class.base_class.area_info.has_key(id):
                self.statistics_data[id].append(v)
                self.statistics_data[id].append(str(self.credit_score_class.base_class.area_info[id]))
            else:
                self.statistics_data[id].append(v)
                self.statistics_data[id].append('null')

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
    statistics.get_credit_score()
    statistics.statistics_function()
    # print statistics.credit_score_class.credit_score