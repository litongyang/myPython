# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# --- 表彰得分----


class CreditSorce:
    def __init__(self):
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

        self.cite = []
        self.sorce_biaozhang = {}  # 表彰得分
        self.fall_off_value = 0.8409  # 衰减值

    # 获取数据
    def get_data(self):
        for line in open("C:\\Users\\\Thinkpad\\Desktop\\biaozhang.txt"):
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
        self.cite.append(self.ID)
        self.cite.append(self.cite_gongshang)
        self.cite.append(self.cite_anjian)
        self.cite.append(self.cite_zhijian)
        self.cite.append(self.cite_xinxizhongxin)
        self.cite.append(self.cite_wujia)
        self.cite.append(self.cite_weisheng)
        self.cite = map(list, zip(*self.cite))
        print len(self.cite)

    # data process
    def process_biaozhang_data(self):
        cnt = 0
        for i in range(0,len(self.cite)):
            self.sorce_biaozhang[str(self.cite[i][0])] = 0
            for j in range(1, len(self.cite[i])):
                sorce_one = 0
                Info_str = self.cite[i][j].split(',')
                if self.cite[i][j] != 'null':  # and self.cite[i][0] == '09E93D3FA8F94002B67315219B332A3D':
                    for k in range(0, len(Info_str)):
                        try:
                            sorce_one += pow(self.fall_off_value, (2015 - int(Info_str[k])))
                        except:
                            sorce_one += self.fall_off_value
                else:
                    sorce_one = 0
                self.sorce_biaozhang[str(self.cite[i][0])] += sorce_one
        for k,v in self.sorce_biaozhang.items():
            if v !=0:
                cnt +=1
                print k,v
        print cnt


if __name__ == '__main__':
    credit_sorce = CreditSorce()
    credit_sorce.get_data()
    credit_sorce.process_biaozhang_data()