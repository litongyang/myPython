# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
得到公司名称和代码的映射字典
"""

import json


class GetCompanyDict:
    def __init__(self):
        self.company_code_file = file('company_code.json')
        self.company_name_list = []
        self.company_code_list = []

    def get_company_dict(self):
        company_code_list = json.load(self.company_code_file)
        for i in range(0, len(company_code_list)):
            for k, v in company_code_list[i].items():
                if k == str('name'):
                    self.company_name_list.append(v)
                if k == str('symbol'):
                    self.company_code_list.append(v)
        return self.company_code_list
        # print len(self.company_code_list)
        # print self.company_name_list[1]
        # print self.company_code_list[1]

if __name__ == '__main__':
    test = GetCompanyDict()
    test.get_company_dict()

