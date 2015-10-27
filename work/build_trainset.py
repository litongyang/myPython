# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

# 构造训练集
import work.no_default_customer_feature_analysis as no_default
import work.default_customer_feature_analysis as Default
import random

class BuildingTrainSet:
    def __init__(self):
        self.trainSet_base = []
        self.no_default_trainSet_base = []
        self.default_trainSet_base = []

    def building_no_default_trainset_base(self):
        nodefault = no_default.FIRSTDATA()
        nodefault.get_data()
        print nodefault.inhbitancy_status
        for i in range(0, len(nodefault.loanAmount)):
            trainSet_base_one = []
            trainSet_base_one.append(0)
            trainSet_base_one.append(nodefault.code[i])
            trainSet_base_one.append(nodefault.repaymentMethod[i])
            trainSet_base_one.append(nodefault.guaranteeMethod[i])
            trainSet_base_one.append(nodefault.conderCd[i])
            trainSet_base_one.append(nodefault.marriageCd[i])
            trainSet_base_one.append(nodefault.degereeCd[i])
            trainSet_base_one.append(nodefault.maintainPersonNum[i])
            trainSet_base_one.append(nodefault.companyType[i])
            trainSet_base_one.append(nodefault.inhbitancy_status[i])
            trainSet_base_one.append(nodefault.employmentType[i])

            trainSet_base_one.append(nodefault.loanAmount[i])
            trainSet_base_one.append(nodefault.mortgageObject[i])
            trainSet_base_one.append(nodefault.familyTatalAsset[i])
            trainSet_base_one.append(-1)
            trainSet_base_one.append(-1)
            self.no_default_trainSet_base.append(trainSet_base_one)
        ratio = int(float(len(self.no_default_trainSet_base))*0.05)
        self.no_default_trainSet_base = random.sample(self.no_default_trainSet_base, ratio)
        self.trainSet_base.append(self.no_default_trainSet_base)
        # print len(self.no_default_trainSet_base)

    def building_default_trainset_base(self):
        default = Default.FEATURE_ANALYSIS()
        default.get_data()

        for i in range(0, len(default.loanAccount)):
            default_train_set_base_one = []
            default_train_set_base_one.append(1)
            default_train_set_base_one.append(default.default_code[i])
            default_train_set_base_one.append(default.repaymentMethod[i])
            default_train_set_base_one.append(default.guaranteeMethod[i])
            default_train_set_base_one.append(default.genderCd[i])
            default_train_set_base_one.append(default.marriageCd[i])
            default_train_set_base_one.append(default.degereeCd[i])
            default_train_set_base_one.append(default.maintainPersonNum[i])
            default_train_set_base_one.append(default.companyType[i])
            default_train_set_base_one.append(default.inhbitancy_status[i])
            default_train_set_base_one.append(default.employmentType[i])

            default_train_set_base_one.append(default.loanAccount[i])
            default_train_set_base_one.append(default.mortgageObject[i])
            default_train_set_base_one.append(default.familyTatalAsset[i])
            default_train_set_base_one.append(default.overdueDays[i])
            default_train_set_base_one.append(default.overdueAccount[i])
            self.default_trainSet_base.append(default_train_set_base_one)
        self.trainSet_base.append(self.default_trainSet_base)
        print self.default_trainSet_base
        # print len(self.trainSet_base)
        # print self.trainSet_base[0]

    def write_txt(self):
        fl = open("C:\\Users\\\Thinkpad\\Desktop\\test.txt", 'a')
        name = "IsDefault" + "\t" + "code" + "\t" + "repaymentMethod" + "\t" + "guaranteeMethod" + "\t" + "genderCd" + "\t"\
               + "marriageCd" + "\t" + "degereeCd" + "\t" + "maintainPersonNum" + "\t" + "companyType" + "\t"\
               + "inhbitancy_status" + "\t" + "employmentType" + "\t" + "loanAccount" + "\t" \
               + "mortgageObject" + "\t" + "familyTatalAsset" + "\t" + "overdueDays" + "\t" + "overdueAccount"
        fl.write(str(name))
        fl.write("\n")
        for i in range(0, len(self.no_default_trainSet_base)):
            for j in range(0, len(self.no_default_trainSet_base[i])):
                fl.write(str(self.no_default_trainSet_base[i][j]))
                fl.write("\t")
            fl.write("\n")
        for i in range(0, len(self.default_trainSet_base)):
            for j in range(0, len(self.default_trainSet_base[i])):
                fl.write(str(self.default_trainSet_base[i][j]))
                fl.write("\t")
            fl.write("\n")


if __name__ == '__main__':
    buildingTrainSet = BuildingTrainSet()
    buildingTrainSet.building_no_default_trainset_base()
    buildingTrainSet.building_default_trainset_base()
    buildingTrainSet.write_txt()