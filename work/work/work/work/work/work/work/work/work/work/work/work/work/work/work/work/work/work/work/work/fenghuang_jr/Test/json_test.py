# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import json
import chardet

fl = open("static.txt", 'a')
fl1 = open("coupon_logger.txt", 'a')
content = open("test.txt").read()
my_char= chardet.detect(content)
bian_ma = my_char['encoding']
content = content.decode(bian_ma, 'ignore').encode('utf-8')
json_data = json.loads(content)
for k, v in json_data.items():
    print "static_k", k, v
    # fl.write(content_static)
    # fl.write("\n")
    if k == 'fund':
        for fund_k, fund_v in v.items():
            print "fund_k:", fund_k, fund_v

            if fund_k == 'logger':
                if fund_v is None:
                    pass
                else:
                    print fund_v
    if k == 'coupon':
        for coupon_k, coupon_v in v.items():
            print "coupon_k:", coupon_k, coupon_v
            if coupon_k == 'logger':
                if coupon_v is None:
                    pass
                else:
                    for coupon_logger_k, coupon_logger_v in coupon_v[0].items():
                        print "coupon_logger_k", coupon_logger_k, coupon_logger_v
                    # print type(coupon_v[0])
                # for coupon_logger_k, v_coupon_logger in v.items():
                #     print "coupon_logger_k", coupon_logger_k
