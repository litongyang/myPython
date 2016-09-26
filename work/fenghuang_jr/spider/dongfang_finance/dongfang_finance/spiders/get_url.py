# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

"""
 获取url
"""


class GetUrl:
    def __init__(self):
        self.notice_page_len = 2
        self.research_page_len = 10
        self.notice_url_head = 'http://data.eastmoney.com/Notice/Noticelist.aspx?type=0&market=all&date=&page='
        self.research_url_head = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var lty={"data":[(x)],"pages":"(pc)",' \
                                 '"update":"(ud)","count":"(count)"}&ps=5000&p=0'  # p=x :x 起始页码
        self.research_url_tail = '&mkt=0&stat=0&cmd=4&code='   # cmd =4:两年内数据
        self.notice_url_list = []  # 公告url的list
        self.research_url_list = []  # 研报url的list

    def get_notice_url(self):
        for i in range(1, self.notice_page_len):
            url = str(self.notice_url_head) + str(i)
            self.notice_url_list.append(url)
        # for i in self.notice_url_list:
        #     print i
        return self.notice_url_list

    def get_research_url(self):
        for i in range(1, self.research_page_len):
            url = str(self.research_url_head) + str(i) + str(self.research_url_tail)
            self.research_url_list.append(url)
        for i in self.research_url_list:
            print i
        return self.research_url_list

if __name__ == '__main__':
    test = GetUrl()
    test.get_notice_url()
    test.get_research_url()



