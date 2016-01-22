# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# ------------ 非失信得分-----------

import numpy

class CreditRealScore:
    def __init__(self):
        self.fall_off_value = 0.8409  # 衰减值
        self.id = []
        self.brand_register_jingxinwei = []
        self.brand_register_jingxinwei_year = []
        self.credit_assess_guoshui = []
        self.credit_assess_guoshui_year = []
        self.credit_assess_yaojian = []
        self.credit_assess_yaojian_year = []
        self.credit_assess_jiaotong = []
        self.credit_assess_jiaotong_year = []
        self.credit_assess_zhijian = []
        self.credit_assess_zhijian_year = []
        self.credit_assess_dishui = []
        self.credit_assess_dishui_year = []
        self.credit_assess_wujia = []
        self.credit_assess_wujia_year = []
        self.credit_assess_yuanlin = []
        self.credit_assess_yuanlin_year = []
        self.credit_assess_tongji = []
        self.credit_assess_tongji_year = []
        self.credit_assess_lvyou = []
        self.credit_assess_lvyou_year = []
        self.credit_assess_anjian = []
        self.credit_assess_anjian_year = []
        self.credit_assess_shangwu = []
        self.credit_assess_shangwu_year = []
        self.credit_assess_jianshe = []
        self.credit_assess_jianshe_year = []

        self.certification_levels_gongshang = []
        self.brand_c_gongshang = []

        # 贯标
        self.brand_register = []
        self.brand_register_score = {}

        # 信用评定
        self.credit_assess = []
        self.credit_assess_score = {}

        # 工商认证等级
        self.certification_levels = []
        self.certification_levels_score = {}

        # C标
        self.brand_c = []
        self.brand_c_score = {}

    # 获取数据
    def get_data(self):
        for line in open("C:\\Users\\\Thinkpad\\Desktop\\feishixin.txt"):
            linone = line.split('\t')
            self.id.append(linone[0])
            self.brand_register_jingxinwei.append(linone[1])
            self.brand_register_jingxinwei_year.append(linone[2])
            self.credit_assess_guoshui.append(linone[4])
            self.credit_assess_guoshui_year.append(linone[5])
            self.credit_assess_yaojian.append(linone[6])
            self.credit_assess_yaojian_year.append(linone[7])
            self.credit_assess_jiaotong.append(linone[8])
            self.credit_assess_jiaotong_year.append(linone[9])
            self.credit_assess_zhijian.append(linone[10])
            self.credit_assess_zhijian_year.append(linone[11])
            self.credit_assess_dishui.append(linone[12])
            self.credit_assess_dishui_year.append(linone[13])
            self.credit_assess_wujia.append(linone[14])
            self.credit_assess_wujia_year.append(linone[15])
            self.credit_assess_yuanlin.append(linone[16])
            self.credit_assess_yuanlin_year.append(linone[17])
            self.credit_assess_tongji.append(linone[18])
            self.credit_assess_tongji_year.append(linone[19])
            self.credit_assess_lvyou.append(linone[20])
            self.credit_assess_lvyou_year.append(linone[21])
            self.credit_assess_anjian.append(linone[22])
            self.credit_assess_anjian_year.append(linone[23])
            self.credit_assess_shangwu.append(linone[24])
            self.credit_assess_shangwu_year.append(linone[25])
            self.credit_assess_jianshe.append(linone[26])
            self.credit_assess_jianshe_year.append(linone[27])

            self.certification_levels_gongshang.append(linone[28])
            self.brand_c_gongshang.append(linone[29])
        # for i in range(0, len(self.brand_c)):
        #     if  self.brand_c[i] != 'null':
        #         print self.brand_c[i]

    # data process
    def process_data(self):
        self.brand_register.append(self.id)
        self.brand_register.append(self.brand_register_jingxinwei)
        self.brand_register.append(self.brand_register_jingxinwei_year)
        self.brand_register = map(list, zip(*self.brand_register))

        self.credit_assess.append(self.id)
        self.credit_assess.append(self.credit_assess_guoshui)
        self.credit_assess.append(self.credit_assess_guoshui_year)
        self.credit_assess.append(self.credit_assess_yaojian)
        self.credit_assess.append(self.credit_assess_yaojian_year)
        self.credit_assess.append(self.credit_assess_jiaotong)
        self.credit_assess.append(self.credit_assess_jiaotong_year)
        self.credit_assess.append(self.credit_assess_zhijian)
        self.credit_assess.append(self.credit_assess_zhijian_year)
        self.credit_assess.append(self.credit_assess_dishui)
        self.credit_assess.append(self.credit_assess_dishui_year)
        self.credit_assess.append(self.credit_assess_wujia)
        self.credit_assess.append(self.credit_assess_wujia_year)
        self.credit_assess.append(self.credit_assess_yuanlin)
        self.credit_assess.append(self.credit_assess_yuanlin_year)
        self.credit_assess.append(self.credit_assess_tongji)
        self.credit_assess.append(self.credit_assess_tongji_year)
        self.credit_assess.append(self.credit_assess_lvyou)
        self.credit_assess.append(self.credit_assess_lvyou_year)
        self.credit_assess.append(self.credit_assess_anjian)
        self.credit_assess.append(self.credit_assess_anjian_year)
        self.credit_assess.append(self.credit_assess_shangwu)
        self.credit_assess.append(self.credit_assess_shangwu_year)
        self.credit_assess.append(self.credit_assess_jianshe)
        self.credit_assess.append(self.credit_assess_jianshe_year)
        self.credit_assess = map(list, zip(*self.credit_assess))

        self.certification_levels.append(self.id)
        self.certification_levels.append(self.certification_levels_gongshang)
        self.certification_levels = map(list, zip(*self.certification_levels))

        self.brand_c.append(self.id)
        self.brand_c.append(self.brand_c_gongshang)
        self.brand_c = map(list, zip(*self.brand_c))

        # for i in range(0, len(self.credit_assess)):
        #     if self.credit_assess[i][0] == '140644':
        #         print self.credit_assess[i]

        # print len(self.credit_assess)

    # noinspection PyBroadException
    # 贯标
    def compute_brand_register_score(self):
        cnt =0
        for i in range(0, len(self.brand_register)):
            self.brand_register_score[str(self.brand_register[i][0])] = 0
            for j in range(1, len(self.brand_register[i]),2):
                brand_str = self.brand_register[i][j].split(',')  # 贯标等级
                brand_year_str = self.brand_register[i][j+ 1].split('#')  # 年份
                brand_score = 0
                # print self.brand_register[i][0]
                # print brand_str
                # print brand_year_str
                for k in range(0, len(brand_str)):
                    if brand_str[k] == 'null':
                        brand_score += 0
                    elif brand_str[k] == '0':
                        try:
                            brand_score += pow(self.fall_off_value, (2015- int(brand_year_str[k])))
                        except:
                            brand_score += 1* self.fall_off_value
                    elif brand_str[k] == '市级':
                        try:
                            brand_score += 2 * pow(self.fall_off_value, (2015- int(brand_year_str[k])))
                        except:
                            brand_score += 2* self.fall_off_value
                    elif brand_str[k] == '省级':
                        try:
                            brand_score += 3 * pow(self.fall_off_value, (2015- int(brand_year_str[k])))
                        except:
                            brand_score += 3* self.fall_off_value
                    else:
                        brand_score += 0.5
                self.brand_register_score[str(self.brand_register[i][0])] += brand_score
        for k,v in self.brand_register_score.items():
            if v >0:
                cnt +=1
                print k,v
        print cnt

    # noinspection PyBroadException
    def compute_credit_score(self):
        cnt = 0
        for i in range(0,len(self.credit_assess)):
            self.credit_assess_score[str(self.credit_assess[i][0])] = 0
            for j in range(1, len(self.credit_assess[i]),2):
                # print self.credit_assess[i][j]
                credit_str = self.credit_assess[i][j].split(',')  # 评级内容
                credit_year_str = self.credit_assess[i][j+ 1].split('#')  # 评级年份
                credit_score = 0
                # print credit_year_str
                for k in range(0, len(credit_str)):
                    if credit_str[k] == 'AAA':
                        try:
                            credit_score += 6 * pow(self.fall_off_value, (2015- int(credit_year_str[k])))
                        except:
                            credit_score += 6* self.fall_off_value
                    elif credit_str[k] == 'AA':
                        try:
                            credit_score += 5 * pow(self.fall_off_value, (2015- int(credit_year_str[k])))
                        except:
                            credit_score += 5* self.fall_off_value
                    elif credit_str[k] == 'A':
                        try:
                            credit_score += 4 * pow(self.fall_off_value, (2015- int(credit_year_str[k])))
                        except:
                            credit_score += 4* self.fall_off_value
                    elif credit_str[k] == 'B':
                        try:
                            credit_score += 3 * pow(self.fall_off_value, (2015- int(credit_year_str[k])))
                        except:
                            credit_score += 3* self.fall_off_value
                    elif credit_str[k] == 'C':
                        try:
                            credit_score += 2 * pow(self.fall_off_value, (2015- int(credit_year_str[k])))
                        except:
                            credit_score += 2* self.fall_off_value
                    elif credit_str[k] == 'D':
                        try:
                            credit_score += pow(self.fall_off_value, (2015- int(credit_year_str[k])))
                        except:
                            credit_score += 1* self.fall_off_value
                    else:
                        credit_score = 0
                self.credit_assess_score[str(self.credit_assess[i][0])] += credit_score
        for k,v in self.credit_assess_score.items():
            if v !=0:
                cnt +=1
                print k,v
        print cnt

    #  工商认证等级
    # noinspection PyBroadException
    def compute_certification_levels_score(self):
        cnt = 0
        for i in range(0,len(self.certification_levels)):
            # print self.certification_levels[i]
            # if self.certification_levels[i][0] == 'CA9C4BEFE064453DB911594668681C1B':
            try:
                self.certification_levels_score[str(self.certification_levels[i][0])] = int(self.certification_levels[i][1])
            except:
                self.certification_levels_score[str(self.certification_levels[i][0])] = 0
        for k,v in self.certification_levels_score.items():
            if v >0:
                cnt +=1
                print k,v
        print cnt

    # C标
    # noinspection PyBroadException
    def compute_brand_c_score(self):
        cnt = 0
        for i in range(0,len(self.brand_c)):
            # print self.brand_c[i][0]
            try:
                self.brand_c_score[str(self.brand_c[i][0])] = int(self.brand_c[i][1])
            except:
                self.brand_c_score[str(self.brand_c[i][0])] = 0
        for k,v in self.brand_c_score.items():
            if v >0:
                cnt +=1
                print k,v
        print cnt

    # 分数规约处理
    def process_score(self,score_info):
        id_list = []
        score_list = []
        for k,v in score_info.items():
            id_list.append(k)
            score_list.append(float(v))
        mean_v = numpy.mean(score_list)
        var_v = numpy.var(score_list)
        # print mean_v
        # print var_v
        score_list = [(score_list[i]- mean_v) / var_v +1 for i in range(0, len(score_list))]
        # for i in range(0, len(score_list)):
        #     print score_list[i]
        for i in range(0, len(id_list)):
            score_info[id_list[i]] = score_list[i]
        for k, v in score_info.items():
            print k,':',v



if __name__ == '__main__':
    credit_real_score = CreditRealScore()
    credit_real_score.get_data()
    credit_real_score.process_data()
    credit_real_score.compute_brand_register_score()
    credit_real_score.compute_credit_score()
    credit_real_score.compute_certification_levels_score()
    credit_real_score.compute_brand_c_score()
    credit_real_score.process_score(credit_real_score.brand_register_score)
    credit_real_score.process_score(credit_real_score.credit_assess_score)
    credit_real_score.process_score(credit_real_score.certification_levels_score)
