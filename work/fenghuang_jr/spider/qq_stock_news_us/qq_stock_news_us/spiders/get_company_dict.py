# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
得到公司名称和代码的映射字典
"""

import json
import time

class GetCompanyDict:
    def __init__(self):
        self.company_code_file = file('company_code.json')
        self.company_name_list = []
        self.company_code_list = []
        self.company_name_dict = {}

    """ 解析json获取公司字典 """
    def get_company_dict(self):
        time_stamp_tmp = time.time()
        time_array = time.localtime(time_stamp_tmp)
        time_satmp = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        print time_satmp
        company_code_list = json.load(self.company_code_file)
        for i in range(0, len(company_code_list)):
            for k, v in company_code_list[i].items():
                if k == str('name'):
                    self.company_name_list.append(v)
                if k == str('symbol'):
                    self.company_code_list.append(v)
        """ 构建公司名称和代码映射字典 """
        for i in range(0, len(self.company_name_list)):
            self.company_name_dict[self.company_name_list[i]] = self.company_code_list[i]

        # for k, v in self.company_name_dict.items():
        #     print k, v
        return self.company_name_dict, self.company_code_list


if __name__ == '__main__':
    test = GetCompanyDict()
    x= test.get_company_dict()
    # print x[1]

