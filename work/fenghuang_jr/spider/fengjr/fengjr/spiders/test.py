# -*- coding: utf-8 -*-
import scrapy
from fengjr.items import *
import json
from scrapy.mail import MailSender
from scrapy.utils.project import get_project_settings  # 调用settings.py 文件方法


class TestSpider(scrapy.Spider):
    def __init__(self):
        self.mailer = MailSender.from_settings(get_project_settings())
    name = "test"
    allowed_domains = ["test.com"]
    start_urls = ['http://www.fengjr.com/api/v2/creditassign/filter?minRate=700&maxRate=5000&minLeftMonths=0&maxLeftMonths=40&repayMethod=all&status=OPEN&pageSize=15&page=1']

    def parse(self, response):
        try:
            item = FengjrItem()
            sites = json.loads(response.body_as_unicode())
            print sites
            for k, v in sites.items():
                if k == 'resultList':
                    if len(v) > 0:
                        for i in range(0, len(v)):
                            if v[i]['rate'] >= 700 and v[i]['leftMonths'] <= 3:
                                print "aaaa"
                                x = v[i]['title'].encode('utf-8')
                                self.mailer.send(to=["tongyang.li@fengjr.com"], subject="test!",
                                                 body=x, mimetype='text/plain')
                    else:
                        print "no res"

            # html = response.body_as_unicode()
            # root = etree.HTML(html)
            # print html
            # # print root
            # nodes = root.xpath('//div[@class="agency orange"]')
        except Exception, e:
            print Exception, e
