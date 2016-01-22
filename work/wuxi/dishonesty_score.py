# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# ----失信得分-----


class DeshonestyScore:
    def __init__(self):
        self.fall_off_value = 0.8409  # 衰减值
        self.id = []  # id
        self.common_reserve_funds_cnt = []  # 公积金欠缴月数
        self.owing_taxes_dishui = []  # 地税欠税记录
        self.owing_taxes_guoshui = []  # 国税...
        self.penalty_gongan = []  # 公安行政处罚失信信息
        self.penalty_anjian = []  # 安监行政处罚失信信息
        self.penalty_gongshang = []  # 工商行政处罚失信信息
        self.penalty_jiaotong = []  # 交通行政处罚失信信息
        self.penalty_huanbao = []  # 环保行政处罚失信信息
        self.penalty_guotu = []  # 国土行政处罚失信信息
        self.penalty_weisheng = []  # 国土行政处罚失信信息
        self.penalty_yuanlin = []  # 园林行政处罚失信信息
        self.penalty_wujia = []  # 物价行政处罚失信信息
        self.penalty_keji = []  # 科技行政处罚失信信息
        self.penalty_jiaoyu = []  # 教育行政处罚失信信息
        self.penalty_liangshi = []  # 粮食行政处罚失信信息
        self.penalty_nongwei = []  # 农委行政处罚失信信息
        self.penalty_minzheng = []  # 民政行政处罚失信信息
        self.penalty_tongji = []  # 统计行政处罚失信信息
        self.penalty_lvyou = []  # 旅游行政处罚失信信息

        self.black_list_fayuan = []
        self.bad_loan_renhang = []
        self.illegal_gongshang = []

        # 公积金欠缴月数
        self.common_reserve_funds = []
        self.common_reserve_score = {}

        # 欠税
        self.owing_taxes = []
        self.owing_taxes_score = {}  # 欠税分数

        # 行政处罚
        self.penalty = []  # 行政处罚
        self.penalty_score = {}  # 行政处罚分数

        # 法院黑名单
        self.black_list = []
        self.black_list_score = {}

        # 人行不良
        self.bad_loan = []
        self.bad_loan_score = {}

        # 违法企业
        self.illegal = []
        self.illegal_score = {}

    # 获取数据
    def get_data(self):
        for line in open("C:\\Users\\\Thinkpad\\Desktop\\shixin.txt"):
            linone = line.split()
            self.id.append(linone[0])
            self.common_reserve_funds_cnt.append(linone[1])
            self.owing_taxes_dishui.append(linone[2])
            self.owing_taxes_guoshui.append(linone[3])
            self.penalty_gongan.append(linone[4])
            self.penalty_anjian.append(linone[5])
            self.penalty_gongshang.append(linone[6])
            self.penalty_jiaotong.append(linone[7])
            self.penalty_huanbao.append(linone[8])
            self.penalty_guotu.append(linone[9])
            self.penalty_weisheng.append(linone[10])
            self.penalty_yuanlin.append(linone[11])
            self.penalty_wujia.append(linone[12])
            self.penalty_keji.append(linone[13])
            self.penalty_jiaoyu.append(linone[14])
            self.penalty_liangshi.append(linone[15])
            self.penalty_nongwei.append(linone[16])
            self.penalty_minzheng.append(linone[17])
            self.penalty_tongji.append(linone[18])
            self.penalty_lvyou.append(linone[19])
            self.black_list_fayuan.append(linone[20])
            self.bad_loan_renhang.append(linone[21])
            self.illegal_gongshang.append(linone[22])
            # for i in range(0,len(self.black_list_fayuan)):
            #     if self.black_list_fayuan[i] != '0':
            #         print self.black_list_fayuan[i]

    # data process
    def process_data(self):
        self.common_reserve_funds.append(self.id)
        self.common_reserve_funds.append(self.common_reserve_funds_cnt)
        self.common_reserve_funds = map(list, zip(*self.common_reserve_funds))
        # for i in range(0,len(self.common_reserve_funds)):
        #     print self.common_reserve_funds[i]

        self.owing_taxes.append(self.id)
        self.owing_taxes.append(self.owing_taxes_dishui)
        self.owing_taxes.append(self.owing_taxes_guoshui)
        self.owing_taxes = map(list, zip(*self.owing_taxes))

        self.penalty.append(self.id)
        self.penalty.append(self.penalty_gongan)
        self.penalty.append(self.penalty_anjian)
        self.penalty.append(self.penalty_gongshang)
        self.penalty.append(self.penalty_jiaotong)
        self.penalty.append(self.penalty_huanbao)
        self.penalty.append(self.penalty_guotu)
        self.penalty.append(self.penalty_weisheng)
        self.penalty.append(self.penalty_yuanlin)
        self.penalty.append(self.penalty_wujia)
        self.penalty.append(self.penalty_keji)
        self.penalty.append(self.penalty_jiaoyu)
        self.penalty.append(self.penalty_liangshi)
        self.penalty.append(self.penalty_nongwei)
        self.penalty.append(self.penalty_minzheng)
        self.penalty.append(self.penalty_tongji)
        self.penalty.append(self.penalty_lvyou)
        self.penalty = map(list, zip(*self.penalty))

        self.black_list.append(self.id)
        self.black_list.append(self.black_list_fayuan)
        self.black_list = map(list, zip(*self.black_list))

        self.bad_loan.append(self.id)
        self.bad_loan.append(self.bad_loan_renhang)
        self.bad_loan = map(list, zip(*self.bad_loan))

        self.illegal.append(self.id)
        self.illegal.append(self.illegal_gongshang)
        self.illegal = map(list, zip(*self.illegal))

    # 计算公积金分数
    def compute_gongjijin_score(self):
        cnt = 0
        for i in range(0, len(self.common_reserve_funds)):
            self.common_reserve_score[str(self.common_reserve_funds[i][0])] = 0
            for j in range(1, len(self.common_reserve_funds[i])):
                score_one = int(self.common_reserve_funds[i][j])
                self.common_reserve_score[str(self.common_reserve_funds[i][0])] += score_one
        for k, v in self.common_reserve_score.items():
            if v > 0:
                cnt += 1
                print k, v
        print cnt

    # 计算欠税分数
    def compute_qianshui_score(self):
        cnt = 0
        for i in range(0, len(self.owing_taxes)):
            self.owing_taxes_score[str(self.owing_taxes[i][0])] = 0
            for j in range(1, len(self.owing_taxes[i])):
                score_one = int(self.owing_taxes[i][j])
                self.owing_taxes_score[str(self.owing_taxes[i][0])] += score_one
        for k, v in self.owing_taxes_score.items():
            if v > 0:
                cnt += 1
                print k, v
        print cnt

    # 计算行政处罚分数
    def compute_penalty_score(self):
        cnt = 0
        for i in range(0, len(self.penalty)):
            self.penalty_score[str(self.penalty[i][0])] = 0
            for j in range(1, len(self.penalty[i])):
                score_one = int(self.penalty[i][j])
                self.penalty_score[str(self.penalty[i][0])] += score_one
        for k, v in self.penalty_score.items():
            if v > 0:
                cnt += 1
                print k, v
        print cnt

    # 计算黑名单分数
    # noinspection PyBroadException
    def compute_black_list_score(self):
        cnt = 0
        for i in range(0, len(self.black_list)):
            try:
                self.black_list_score[str(self.black_list[i][0])] = int(self.black_list[i][1])
            except:
                self.black_list_score[str(self.black_list[i][0])] = 0

        for k, v in self.black_list_score.items():
            if v != 0:
                cnt += 1
            print k, v
        print cnt

    # 计算不良贷款得分
    def compute_bad_loan_score(self):
        cnt = 0
        for i in range(0, len(self.bad_loan)):
            # self.bad_loan_score[str(self.bad_loan[i][0])] = 0
            bad_year_str = self.bad_loan[i][1].split('#')
            score_one = 0
            for j in range(0, len(bad_year_str)):
                if bad_year_str[j] != '0':
                    try:
                        score_one += pow(self.fall_off_value, (2015 - int(bad_year_str[j])))
                    except:
                        pass
                else:
                    score_one = 0
            self.bad_loan_score[str(self.bad_loan[i][0])] = score_one
        for k, v in self.bad_loan_score.items():
            if v > 1:
                cnt += 1
            print k, v
        print cnt


    # 计算企业违法得分
    def compute_illegal_score(self):
        cnt = 0
        for i in range(0, len(self.illegal)):
            illegal_year_str = self.illegal[i][1].split('#')
            # print illegal_year_str
            score_one = 0
            for j in range(0, len(illegal_year_str)):
                if illegal_year_str[j] != '0':
                    try:
                        score_one += pow(self.fall_off_value, (2015 - int(illegal_year_str[j])))
                    except:
                        pass
                else:
                    score_one = 0
            self.illegal_score[str(self.illegal[i][0])] = score_one
        for k, v in self.illegal_score.items():
            if v > 0:
                cnt += 1
            print k, v
        print cnt


if __name__ == '__main__':
    deshonesty_score = DeshonestyScore()
    deshonesty_score.get_data()
    deshonesty_score.process_data()
    deshonesty_score.compute_gongjijin_score()
    deshonesty_score.compute_qianshui_score()
    deshonesty_score.compute_penalty_score()
    deshonesty_score.compute_black_list_score()
    deshonesty_score.compute_bad_loan_score()
    deshonesty_score.compute_illegal_score()
