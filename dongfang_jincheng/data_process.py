# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

import default_customer_feature_analysis as Default
import no_default_customer_feature_analysis as No_default
import build_trainset as trainset_base_class


class DataProcess:
    def __init__(self):
        self.no_default_repayment_method_process = []
        self.default = Default.FEATURE_ANALYSIS()
        self.no_default = No_default.FIRSTDATA()
        self.trainset_base = trainset_base_class.BuildingTrainSet()

    def data_process_default(self):
        fl = open("C:\\Users\\\Thinkpad\\Desktop\\test.txt", 'a')
        self.default.get_data()
        self.no_default.get_data()
        self.trainset_base.building_no_default_trainset_base()
        self.trainset_base.building_default_trainset_base()
        # no_default process
        # print self.trainset_base.no_default_trainSet_base[0]
        repayment_method_set, test1 = set(self.trainset_base.no_default_trainSet_base[0][2]), set(self.no_default.companyType)
        for v in repayment_method_set:
            fl.write(str(v))
            fl.write("\n")
        # for i in range(0, len(self.no_default.repaymentMethod)):
        #     value = 0
        #     for v in repayment_method_set:
        #
        #         if self.no_default.repaymentMethod[i] == v:
        #             print "lty"
        #             # print v
        #             # print self.no_default.repaymentMethod[i]
        #             self.no_default_repayment_method_process.append(value)
        #         else:
        #             value += 1
        # print self.no_default_repayment_method_process


if __name__ == '__main__':
    dataProcess = DataProcess()
    dataProcess.data_process_default()