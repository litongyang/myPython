# __author__ = 'lty'
# -*- coding: utf-8 -*-

import json


class GetUrl:
    def __init__(self):
        self.news_url_file = open('360_url1.json', 'r')
        self.news_url_list = []

    """ 得到新闻的发布时间和url的字典 """
    def get_news_time_url_dict(self):
        for line in self.news_url_file:
            json_data = eval(line)
            # json_data = json.load(self.news_url_file)
            for k, v in json_data.items():
                if k == str('url'):  # v:新闻的url:list
                    self.news_url_list.append(v)
                    # for i in range(0, len(v)):
                    #     self.news_url_list.append(v[i])
        return self.news_url_list


if __name__ == '__main__':
    test = GetUrl()
    print test.get_news_time_url_dict()
    # x = test.get_news_url()
    # print len(x)
    # test.get_news_time_url_dict()
