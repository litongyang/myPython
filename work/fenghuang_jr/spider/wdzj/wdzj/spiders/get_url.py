# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

"""
 获取url
"""

import sys
print sys.path[0]
sys.path.append('C:\\Users\\tongyang.li\\PycharmProjects\\myPython\\work\\fenghuang_jr\\spider\\wdzj')
import company_dict


class GetUrl:
    def __init__(self):
        self.preference_url_list = []
        self.preference_url_dict = {}
        self.basic_url_list = []
        self.basic_url_dict = {}
        self.archives_url_list = []
        self.archives_url_dict = {}
        self.preference_url_head = 'http://shuju.wdzj.com/preference-'
        self.basic_url_head = 'http://shuju.wdzj.com/basic-surface-'
        self.archives_url_head = 'http://shuju.wdzj.com/wdzj-archives-chart.html?wdzjPlatId='
        self.archives_type = [0, 1, 3]  # 0:利率/成交量;1:历史待还/净流入;3:投资人数/借款人数
        self.archives_status = [0]  # 0:日线
        self.company_dict_class = company_dict.CompanyDict()
        self.company_name_url_dict = {}  # 公司名称对应url字典

    def get_preference_url(self):
        for k, v in self.company_dict_class.company_dict.items():
            url = self.preference_url_head + str(v) + '.html'
            self.preference_url_dict[k] = url
            self.preference_url_list.append(url)
        return self.preference_url_list

    def get_basic_url(self):
        for k, v in self.company_dict_class.company_dict.items():
            url = self.basic_url_head + str(v) + '.html'
            self.company_name_url_dict[k] = url
            self.basic_url_dict[k] = url
            self.basic_url_list.append(url)
        return self.basic_url_list

    def get_archives_url(self):
        for k, v in self.company_dict_class.company_dict.items():
            for type_v in self.archives_type:
                for status_v in self.archives_status:
                    url = "%s%s&type=%s&status=%s" % (self.archives_url_head, v, type_v, status_v)
                    tmp_key = str(k) + '-' + str(type_v) + '-' + str(status_v)
                    self.archives_url_dict[tmp_key] = url
                    self.archives_url_list.append(url)
        return self.archives_url_list

    def test(self):
        for key, value in self.archives_url_dict.items():
            print value
            url_type = key.split('-')
            if str(url_type[1]) == str(0) and str(url_type[2]) == str(0):
                print url_type[0]

if __name__ == '__main__':
    test = GetUrl()
    x = test.get_preference_url()
    y = test.get_basic_url()
    print type(test.get_archives_url())
    test.test()



