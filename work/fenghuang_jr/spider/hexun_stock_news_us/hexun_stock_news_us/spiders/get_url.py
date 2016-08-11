# __author__ = 'lty'
# -*- coding: utf-8 -*-

import json
import get_company_dict


class GetUrl:
    def __init__(self):
        self.news_url_file = open('news_url1.json', 'r')
        self.news_url_list = []
        self.news_time_list = []
        self.news_time_url_dict = {}  # 新闻的url和发表时间的映射字典
        self.company_news_url_head = 'http://stockdata.stock.hexun.com/us/news/'
        self.company_news_url_tail = '.shtml'
        self.company_news_url_head_hk = 'http://hkdata.stock.hexun.com/company/news/'
        self.company_news_url_tail_hk = '.shtml'
        self.company_news_url_list = []

    def get_company_news_url(self):
        """
        得到公司的新闻列表页
        :return:
        """
        get_company_dict_class = get_company_dict.GetCompanyDict()
        company_code_us_list = []
        company_code_hk_list = []
        for k, v in get_company_dict_class.get_code_name_hsymbol_dict().items():
            if v[1] == '':
                company_code_us_list.append(k)
            if v[1] != '':
                company_code_hk_list.append(v[1])
        for i in range(0, len(company_code_us_list)):  # 得到美股新闻url
            url_tmp = self.company_news_url_head + company_code_us_list[i] + self.company_news_url_tail
            self.company_news_url_list.append(url_tmp)
        for i in range(0, len(company_code_hk_list)):  # 得到港股新闻url
            url_tmp = self.company_news_url_head_hk + company_code_hk_list[i] + self.company_news_url_tail_hk
            self.company_news_url_list.append(url_tmp)
        # for i in range(0, len(self.company_news_url_list)):
        #     print self.company_news_url_list[i]
        return self.company_news_url_list

    def get_news_url(self):
        """ 得到新闻url """
        for line in self.news_url_file:
            try:
                json_data = eval(line)
                for k, v in json_data.items():
                    if k == str('news_url'):  # v:新闻的url:list
                        self.news_url_list.append(v)
            except:
                pass
        return self.news_url_list


if __name__ == '__main__':
    test = GetUrl()
    print test.get_company_news_url()
    print test.get_news_url()

