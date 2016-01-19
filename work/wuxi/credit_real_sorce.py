# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# ------------ 非失信得分-----------


class CreditRealScore:
    def __init__(self):
        self.fall_off_value = 0.8409  # 衰减值
        self.id = []
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

        # 信用评定
        self.credit_assess = []
        self.credit_assess_score = {}

    # 获取数据
    def get_data(self):
        for line in open("C:\\Users\\\Thinkpad\\Desktop\\feishixin.txt"):
            linone = line.split('\t')
            self.id.append(linone[0])
            self.credit_assess_guoshui.append(linone[4])
            self.credit_assess_guoshui_year.append(linone[5])
            self.credit_assess_yaojian.append(linone[6])
            self.credit_assess_yaojian_year.append(linone[7])
            self.credit_assess_jiaotong.append(linone[8])
            self.credit_assess_jiaotong_year.append(linone[9])
        # print self.credit_assess_guoshui

    # data process
    def process_data(self):
        self.credit_assess.append(self.id)
        self.credit_assess.append(self.credit_assess_guoshui)
        self.credit_assess.append(self.credit_assess_guoshui_year)
        self.credit_assess.append(self.credit_assess_yaojian)
        self.credit_assess.append(self.credit_assess_yaojian_year)
        self.credit_assess.append(self.credit_assess_jiaotong)
        self.credit_assess.append(self.credit_assess_jiaotong_year)
        self.credit_assess = map(list, zip(*self.credit_assess))
        # for i in range(0, len(self.credit_assess)):
        #     if self.credit_assess[i][0] == '140644':
        #         print self.credit_assess[i]

        print len(self.credit_assess)

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
                            credit_score += pow(6, (2015- int(credit_year_str[k])))
                        except:
                            credit_score += 6* self.fall_off_value
                    elif credit_str[k] == 'AA':
                        try:
                            credit_score += pow(5, (2015- int(credit_year_str[k])))
                        except:
                            credit_score += 5* self.fall_off_value
                    elif credit_str[k] == 'A':
                        try:
                            credit_score += pow(4, (2015- int(credit_year_str[k])))
                        except:
                            credit_score +=4* self.fall_off_value
                    elif credit_str[k] == 'B':
                        try:
                            credit_score += pow(3, (2015- int(credit_year_str[k])))
                        except:
                            credit_score += 3* self.fall_off_value
                    elif credit_str[k] == 'C':
                        try:
                            credit_score += pow(2, (2015- int(credit_year_str[k])))
                        except:
                            credit_score += 2* self.fall_off_value
                    elif credit_str[k] == 'D':
                        try:
                            credit_score += pow(1, (2015- int(credit_year_str[k])))
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

if __name__ == '__main__':
    credit_real_score = CreditRealScore()
    credit_real_score.get_data()
    credit_real_score.process_data()
    credit_real_score.compute_credit_score()

