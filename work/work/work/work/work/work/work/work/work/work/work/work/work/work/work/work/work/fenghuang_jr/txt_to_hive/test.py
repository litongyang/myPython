# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

# content = "请输入文件名，以逗号分隔:"
# content = raw_input("请输入文件名，以逗号分隔:")
# s = content.split(',')
# content1 = raw_input("请输入dt:")
# print s
# x = str(content1) + ".txt"
# print x

# for line in open("tm_outbound_2016_03_24.txt"):
#     lineone = line.split('\t')
#     print lineone[1].split(' ')[0].replace("/", "-")


import shutil
import os
if os.path.exists('./log_txt'):
    shutil.rmtree("./log_txt")
else:
    os.mkdir("./log_txt")
