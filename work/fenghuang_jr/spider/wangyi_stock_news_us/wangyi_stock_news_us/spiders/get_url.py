# __author__ = 'lty'
# -*- coding: utf-8 -*-

import json
import get_company_dict


class GetUrl:
    def __init__(self):
        self.news_url_list = []
        self.news_time_list = []
        self.news_time_url_dict = {}  # 新闻的url和发表时间的映射字典
        self.company_news_url_head = 'http://quotes.money.163.com/usstock/'
        self.company_news_url_tail = '_news.html?page=0'
        self.company_news_url_head_hk = 'http://quotes.money.163.com/hkstock/'
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
            url_tmp = self.company_news_url_head_hk + company_code_hk_list[i] + '.html'
            self.company_news_url_list.append(url_tmp)
        # for i in range(0, len(self.company_news_url_list)):
        #     print self.company_news_url_list[i]
        return self.company_news_url_list

    # def get_news_url_lately(self):
    # """ 得到新闻url """
    # def get_news_url(self):
    #     # null_cnt = 0
    #     for line in self.news_url_file:
    #         json_data = eval(line)
    #         for k, v in json_data.items():
    #             if k == str('news_url'):  # v:新闻的url:list
    #                 # if len(v) == 0:
    #                 #     null_cnt += 1
    #                 for i in range(0, len(v)):
    #                     self.news_url_list.append(v[i])
    #             if k == str('news_time'):
    #                 for i in range(0, len(v)):
    #                     self.news_time_list.append(v[i])
    #     # print null_cnt
    #     return self.news_url_list

    # """ 得到新闻的发布时间和url的字典 """
    # def get_news_time_url_dict(self):
    #     for line in self.news_url_file:
    #         json_data = eval(line)
    #         # json_data = json.load(self.news_url_file)
    #         for k, v in json_data.items():
    #             if k == str('news_url'):  # v:新闻的url:list
    #                 for i in range(0, len(v)):
    #                     self.news_url_list.append(v[i])
    #             if k == str('news_time'):
    #                 for j in range(0, len(v)):
    #                     self.news_time_list.append(v[j])
    #     # print self.news_url_list[0]
    #     tmp = zip(self.news_url_list, self.news_time_list)
    #     self.news_time_url_dict = dict(
    #         (self.news_url_list, self.news_time_list) for self.news_url_list, self.news_time_list in tmp)
    #     return self.news_time_url_dict


if __name__ == '__main__':
    test = GetUrl()
    print test.get_company_news_url()
    # x = test.get_news_url()
    # print len(x)
    # test.get_news_time_url_dict()
