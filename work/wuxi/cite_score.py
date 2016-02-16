# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# --- 表彰得分----

import numpy


class CiteScore:
    def __init__(self):
        self.fall_off_value = 0.8409  # 衰减值
        self.ID = []
        self.cite_gongshang = []  # 工商表彰
        self.cite_anjian = []
        self.cite_zhijian= []
        self.cite_xinxizhongxin = []
        self.cite_wujia= []
        self.cite_weisheng = []
        self.cite_renbaoju = []
        self.cite_nongwei = []
        self.cite_minzheng = []
        self.cite_lvyou= []
        self.cite_liangshi = []
        self.cite_keji = []
        self.cite_jiaotong = []
        self.cite_guojian = []
        self.cite_jianshe = []
        self.good_brand_cnt_gongshang = []
        self.good_brand_year_gongshang = []

        # 表彰
        self.cite = []
        self.score_biaozhang = {}  # 表彰得分(max:5.7 ,min:0,mean:0.0098)

        #  驰名商标
        self.good_brand = []
        self.good_brand_score = {}  # 驰名商标得分（max:13.69,min:0,mean:0.0016）


    # 获取数据
    def get_data(self):
        for line in open("C:\Users\Thinkpad\Desktop\wuxi-home\\biaozhang.txt"):
            linone = line.split()
            self.ID.append(linone[0])
            self.cite_gongshang.append(linone[1])
            self.cite_anjian.append(linone[2])
            self.cite_zhijian.append(linone[3])
            self.cite_xinxizhongxin.append(linone[4])
            self.cite_wujia.append(linone[5])
            self.cite_weisheng.append(linone[6])
            self.cite_renbaoju.append(linone[7])
            self.cite_nongwei.append(linone[8])
            self.cite_minzheng.append(linone[9])
            self.cite_lvyou.append(linone[10])
            self.cite_liangshi.append(linone[11])
            self.cite_keji.append(linone[12])
            self.cite_jiaotong.append(linone[13])
            self.cite_guojian.append(linone[14])
            self.cite_jianshe.append(linone[15])
            self.good_brand_cnt_gongshang.append(linone[16])
            self.good_brand_year_gongshang.append(linone[17])
        self.cite.append(self.ID)
        self.cite.append(self.cite_gongshang)
        self.cite.append(self.cite_anjian)
        self.cite.append(self.cite_zhijian)
        self.cite.append(self.cite_xinxizhongxin)
        self.cite.append(self.cite_wujia)
        self.cite.append(self.cite_weisheng)
        self.cite.append(self.cite_renbaoju)
        self.cite.append(self.cite_nongwei)
        self.cite.append(self.cite_minzheng)
        self.cite.append(self.cite_lvyou)
        self.cite.append(self.cite_liangshi)
        self.cite.append(self.cite_keji)
        self.cite.append(self.cite_jiaotong)
        self.cite.append(self.cite_guojian)
        self.cite.append(self.cite_jianshe)
        self.cite = map(list, zip(*self.cite))
        print len(self.cite)

        self.good_brand.append(self.ID)
        self.good_brand.append(self.good_brand_cnt_gongshang)
        self.good_brand.append(self.good_brand_year_gongshang)
        self.good_brand = map(list, zip(*self.good_brand))
        # for i in range(0, len(self.good_brand)):
        #     if self.good_brand[i][1] != '0':
        #         print self.good_brand[i][1]

    # data process
    # noinspection PyBroadException
    def compute_biaozhang_score(self):
        cnt = 0
        for i in range(0,len(self.cite)):
            self.score_biaozhang[str(self.cite[i][0])] = 0
            for j in range(1, len(self.cite[i])):
                score_one = 0
                Info_str = self.cite[i][j].split('#')
                if self.cite[i][j] != 'null':  # and self.cite[i][0] == '09E93D3FA8F94002B67315219B332A3D':
                    for k in range(0, len(Info_str)):
                        try:
                            score_one += pow(self.fall_off_value, (2015 - int(Info_str[k])))
                        except:
                            score_one += self.fall_off_value
                else:
                    score_one = 0
                self.score_biaozhang[str(self.cite[i][0])] += score_one
        for k,v in self.score_biaozhang.items():
            if v !=0:
                cnt +=1
                print k,v
        print cnt

    # 计算驰名商标的分数
    # noinspection PyBroadException
    def compute_good_brand_score(self):
        cnt = 0
        for i in range(0, len(self.good_brand)):
            score_one = 0
            # for j in range(1, len(self.good_brand[i]),2):
            cnt_str = self.good_brand[i][1].split('#')
            year_str = self.good_brand[i][2].split('#')
            if self.good_brand[i][1] != '0':
                for k in range(0, len(cnt_str)):
                    try:
                        score_one += int(cnt_str[k]) * pow(self.fall_off_value, (2015 - int(year_str[k])))
                    except:
                        score_one += 0
            else:
                score_one += 0
            self.good_brand_score[self.good_brand[i][0]] = score_one
        for k,v in self.good_brand_score.items():
            if v !=0:
                cnt +=1
            print k,v
        print cnt

    # 分数规约处理
    def process_score(self, score_info):
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
        for k,v in score_info.items():
            if score_info[k] == 1680.0:
                print k


if __name__ == '__main__':
    credit_score = CiteScore()
    credit_score.get_data()
    credit_score.compute_biaozhang_score()
    credit_score.compute_good_brand_score()

    credit_score.view_du(credit_score.score_biaozhang)  # max:5.7 ,min:0,mean:0.0098
    credit_score.view_du(credit_score.good_brand_score)  # max:13.69,min:0,mean:0.0016
    # credit_score.process_score(credit_score.score_biaozhang)
    # credit_score.process_score(credit_score.good_brand_score)