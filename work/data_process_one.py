# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

import default_customer_feature_analysis as Default
import no_default_customer_feature_analysis as No_default
import build_trainset as trainset_base_class


class DataProcess:
    def __init__(self):
        self.is_default = []
        self.code = []

        self.repayment_method = []
        self.repayment_method_set = []
        self.repayment_method_process = []

        self.guaranteeMethod = []
        self.guaranteeMethod_set = []
        self.guaranteeMethod_process = []

        self.genderCd = []
        self.genderCd_set = []
        self.genderCd_process = []

        self.marriageCd = []
        self.marriageCd_set = []
        self.marriageCd_process = []

        self.degereeCd = []
        self.degereeCd_set = []
        self.degereeCd_process = []

        self.maintainPersonNum = []
        self.maintainPersonNum_set = []
        self.maintainPersonNum_process = []

        self.companyType = []
        self.companyType_set = []
        self.companyType_process = []

        self.inhbitancy_status = []
        self.inhbitancy_status_set = []
        self.inhbitancy_status_process = []

        self.employmentType = []
        self.employmentType_set = []
        self.employmentType_process = []

        self.trainSet_one = []

    def get_data_set(self):
        for line in open("C:\\Users\\\Thinkpad\\Desktop\\trainSet_base.txt"):
            linone = line.split()
            self.is_default.append(linone[0])
            self.code.append(linone[1])
            self.repayment_method.append(linone[2])
            self.guaranteeMethod.append(linone[3])
            self.genderCd.append(linone[4])
            self.marriageCd.append(linone[5])
            self.degereeCd.append(linone[6])
            self.maintainPersonNum.append(linone[7])
            self.companyType.append(linone[8])
            self.inhbitancy_status.append(linone[9])
            self.employmentType.append(linone[10])
        self.repayment_method_set = set(self.repayment_method)
        self.guaranteeMethod_set = set(self.guaranteeMethod)
        self.genderCd_set = set(self.genderCd)
        self.marriageCd_set = set(self.marriageCd)
        self.degereeCd_set = set(self.degereeCd)
        self.maintainPersonNum_set = set(self.maintainPersonNum)
        self.companyType_set = set(self.companyType)
        self.inhbitancy_status_set = set(self.inhbitancy_status)
        self.employmentType_set = set(self.employmentType)

        fl = open("C:\\Users\\\Thinkpad\\Desktop\\set_log.txt", 'a')
        fl.write("repayment_method:")
        fl.write("\n")
        for v in self.repayment_method_set:
            fl.write(str(v))
            fl.write("\n")
        fl.write("genderCd:")
        fl.write("\n")
        for v in self.genderCd_set:
            fl.write(str(v))
            fl.write("\n")
        fl.write("marriageCd:")
        fl.write("\n")
        for v in self.marriageCd_set:
            fl.write(str(v))
            fl.write("\n")
        # fl.write("degereeCd:")
        # fl.write("\n")
        # for v in self.degereeCd_set:
        #     fl.write(str(v))
        #     fl.write("\n")

    def data_process_one(self, feature, feature_set, feature_process):
        for i in range(0, len(feature)):
            value = 0
            # print self.repayment_method[1]
            for v in feature_set:
                if feature[i] == 'null':
                    feature_process.append(-1)
                    break
                elif feature[i] == v:
                    feature_process.append(value)
                else:
                    value += 1
        # print feature_process

    def data_process_special_num(self, feature, num, feature_process):
        for i in range(0, len(feature)):
            if feature[i] != 'null':
                try:
                    if int(feature[i]) <= num:
                        feature_process.append(int(feature[i]))
                    else:
                        feature_process.append(num+1)
                except:
                    feature_process.append(-1)
            else:
                feature_process.append(-1)
        # print feature_process

    def data_process_guaranteeMethod(self):
        for i in range(0, len(self.guaranteeMethod)):
            if self.guaranteeMethod[i] != 'null':
                if self.guaranteeMethod[i] == '保证':
                    self.guaranteeMethod_process.append(0)
                elif self.guaranteeMethod[i] == '信用' or self.guaranteeMethod[i] == '信用,':
                    self.guaranteeMethod_process.append(1)
                else:
                    self.guaranteeMethod_process.append(2)
            else:
                self.guaranteeMethod_process.append(-1)
        # print self.guaranteeMethod_process

    def build_trainSet_one(self):
        self.trainSet_one.append(self.is_default)
        self.trainSet_one.append(self.code)
        self.trainSet_one.append(self.repayment_method_process)
        self.trainSet_one.append(self.guaranteeMethod_process)
        self.trainSet_one.append(self.genderCd_process)
        self.trainSet_one.append(self.marriageCd_process)
        self.trainSet_one.append(self.degereeCd_process)
        self.trainSet_one.append(self.maintainPersonNum_process)
        self.trainSet_one.append(self.companyType_process)
        self.trainSet_one.append(self.inhbitancy_status_process)
        self.trainSet_one.append(self.employmentType_process)
        self.trainSet_one = map(list, zip(*self.trainSet_one))  # 训练集转置操作，每一行就是一个训练集
        print self.trainSet_one

    def write_file_trainSet_one(self):
        fl = open("C:\\Users\\\Thinkpad\\Desktop\\trainSet_one.txt", 'a')
        name = "IsDefault" + "\t" + "code" + "\t" + "repaymentMethod" + "\t" + "guaranteeMethod" + "\t" + "genderCd" + "\t"\
               + "marriageCd" + "\t" + "degereeCd" + "\t" + "maintainPersonNum" + "\t" + "companyType" + "\t"\
               + "inhbitancy_status" + "\t" + "employmentType"
        fl.write(str(name))
        fl.write("\n")
        for rowNum in range(0, len(self.trainSet_one)):
            for colNum in range(0, len(self.trainSet_one[rowNum])):
                fl.write(str(self.trainSet_one[rowNum][colNum]))
                fl.write("\t")
            fl.write("\n")

if __name__ == '__main__':
    dataProcess = DataProcess()
    dataProcess.get_data_set()
    dataProcess.data_process_one(dataProcess.repayment_method, dataProcess.repayment_method_set,
                                 dataProcess.repayment_method_process)
    dataProcess.data_process_one(dataProcess.genderCd, dataProcess.genderCd_set,
                                 dataProcess.genderCd_process)
    dataProcess.data_process_one(dataProcess.marriageCd, dataProcess.marriageCd_set,
                                 dataProcess.marriageCd_process)
    # dataProcess.data_process_one(dataProcess.degereeCd, dataProcess.degereeCd_set,
    #                              dataProcess.degereeCd_process)
    dataProcess.data_process_special_num(dataProcess.degereeCd, 9, dataProcess.degereeCd_process)
    dataProcess.data_process_special_num(dataProcess.maintainPersonNum, 4, dataProcess.maintainPersonNum_process)
    dataProcess.data_process_special_num(dataProcess.companyType, 9, dataProcess.companyType_process)
    dataProcess.data_process_special_num(dataProcess.inhbitancy_status, 6, dataProcess.inhbitancy_status_process)
    dataProcess.data_process_special_num(dataProcess.employmentType, 4, dataProcess.employmentType_process)
    dataProcess.data_process_guaranteeMethod()
    dataProcess.build_trainSet_one()
    dataProcess.write_file_trainSet_one()