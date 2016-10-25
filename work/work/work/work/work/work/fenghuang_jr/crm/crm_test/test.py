# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import os
import time
import datetime

# c = "echo lty!"
# os.system(c)
# print int(time.time())
# # time.ctime('1970-01-01 00:00:00')
# x = '1971-01-01 00:00:00'
# d = time.strptime(x, '%Y-%m-%d %H:%M:%S')
# print time.mktime(d)


# import ConfigParser
# cf = ConfigParser.ConfigParser()
# cf.read("crm.conf")
# opts = cf.options("is_all")
# kvs = cf.items("is_all")
# print type(kvs)
# cf.set("cycle_all","content","all")
# cf.write(open("crm.conf",'w'))

import logging
import logging.handlers
LOG_FILE = 'tst.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
fmt = "%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s"

formatter = logging.Formatter(fmt)   # 实例化formatter
handler.setFormatter(formatter)      # 为handler添加formatter

logger = logging.getLogger('tst')    # 获取名为tst的logger
logger.addHandler(handler)           # 为logger添加handler
logger.setLevel(logging.DEBUG)

logger.info('first info message')
logger.debug('first debug message')