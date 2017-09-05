# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
得到门店的url
"""


class GetStoreUrl:
    def __init__(self):
        self.store_url_list = []
        self.url_head = 'https://www.zhouheiya.cn/wcs/Tpl/home/default/storejson/'
        self.url_tail = '.json'


    def get_url(self):
        for i in range(0, 20):  # i 代表省、直辖市
            for j in range(0, 20):  # j 代表市
                for k in range(0, 20):  # k 代表区
                    self.store_url_list.append(str(self.url_head) + str('0-') + str(i) + str('-') + str(j) + str('-') + str(k)
                                        + str(self.url_tail))

        return self.store_url_list


if __name__ == '__main__':
    test = GetStoreUrl()
    test.get_url()
