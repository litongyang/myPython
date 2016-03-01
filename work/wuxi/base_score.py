# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# -----基本信息得分-----

import numpy
import chardet


class BaseScore:
    def __init__(self):
        self.ID = []
        self.registered_code = []  # 工商注册号
        self.name = []
        self.type = []  # 企业类型
        self.registered_capital = []  # 注册资金
        self.cur_type = []  # 币种
        self.industry_code = []  # 行业代码

        self.company_info = {}

        # 区域代码
        self.ID_area_code = []
        self.area_code = []
        self.area_info = {}


        self.type_pro = []
        self.type_score = {}  # 企业类型得分(max:3,min:0)
        self.capital = []
        self.capital_score = {}  # 注册资本得分(max:5,min:0)

    # 获取数据
    def get_data(self):
        for line in open("C:\\Users\\Thinkpad\\Desktop\\wuxi-home\\base.txt"):
            linone = line.split('\t')
            self.ID.append(linone[0])
            self.registered_code.append(linone[1])
            self.name.append(linone[2].decode('gb2312', 'ignore').encode('utf-8'))
            self.type.append(linone[3])
            self.registered_capital.append(linone[4])
            self.cur_type.append(linone[5])
            self.industry_code.append(linone[8])
        for line in open("C:\Users\Thinkpad\Desktop\wuxi-home\\area_code.txt"):
            linone = line.split()
            self.ID_area_code.append(linone[0])
            if linone[1] == '320202' or linone[1] == '320203' or linone[1] == '320204':
                self.area_code.append('320215')
            else:
                self.area_code.append(linone[1])
        for i in range(0, len(self.ID_area_code)):
            self.area_info[self.ID_area_code[i]] = self.area_code[i]
        for i in range(0, len(self.ID)):
            # print self.ID[i]
            self.company_info[self.ID[i]] = []
            # self.company_info[self.ID[i]].append(self.name[i])
            self.company_info[self.ID[i]].append(self.type[i])
            self.company_info[self.ID[i]].append(self.industry_code[i])
        # print self.name[5]
        # my_char= chardet.detect(self.name[1])
        # bian_ma = my_char['encoding']
        # print bian_ma
        # content = self.name[1].decode(bian_ma, 'ignore').encode('utf-8')
        # print content



    # data process
    def process_data(self):
        self.type_pro.append(self.ID)
        self.type_pro.append(self.type)
        self.type_pro = map(list, zip(*self.type_pro))

        self.capital.append(self.ID)
        self.capital.append(self.registered_capital)
        self.capital.append(self.cur_type)
        self.capital = map(list, zip(*self.capital))

    # 计算企业性质得分
    # noinspection PyBroadException
    def compute_type_score(self):
        for i in range(0, len(self.type_pro)):
            try:
                score_one = int(self.type_pro[i][1])
            except:
                score_one = 0
            self.type_score[self.type_pro[i][0]] = score_one
        # for k,v in self.type_score.items():
        #     print k,":",v

    # 计算注册资金分数
    # noinspection PyBroadException
    def compute_register_capital_score(self):
        for i in range(0, len(self.capital)):
            try:
                score_one = float(self.capital[i][1]) * 10000 * float(self.capital[i][2])
                if 0< score_one <= 1000000:
                    score_one = 1
                elif 1000000< score_one <= 10000000:
                    score_one = 2
                elif 10000000< score_one <= 100000000:
                    score_one = 3
                elif 100000000< score_one <= 1000000000:
                    score_one = 4
                elif score_one > 1000000000:
                    score_one = 5
                else:
                    score_one = 0
            except:
                score_one = 0
            self.capital_score[self.capital[i][0]] = score_one
        # for k,v in self.capital_score.items():
        #     print k,":",v

    # 查看分布
    def view_du(self,score_info):
        score_list = []
        for k,v in score_info.items():
            score_list.append(float(v))
        max_v = max(score_list)
        min_v = min(score_list)
        mean_v = numpy.mean(score_list)
        var_v = numpy.var(score_list)
        print "max:",max_v
        print "min:",min_v
        print "mean:",mean_v

if __name__ == '__main__':
    base_score = BaseScore()
    base_score.get_data()
    base_score.process_data()
    base_score.compute_type_score()
    base_score.compute_register_capital_score()
    base_score.view_du(base_score.type_score)

