# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import datetime
import time


def read_file_content(path):
    try:
        content = open(path).read()
        return content
    except Exception, e:
        print "---read_file_content----"
        print Exception, ": ", e


# 计算分区
def compute_dt(dt_type, date):
    if dt_type == 'd':  # 按天分区
        return str(date)
    if dt_type == 'm':  # 按月分区
        try:
            temp = str(date).split('-')
            dt = str(temp[0]) + '-' + str(temp[1])
            return dt
            # year = time.strptime(str(date), "%Y-%m-%d").tm_year
            # month = time.strptime(str(date), "%Y-%m-%d").tm_mon
            # dt = str(year) + '-' + str(month)
            # print dt
            # return str(year) + '-' + str(month)
        except Exception, e:
            print "---compute_dt----"
            print Exception, ": ", e


# #  得到sql语句
# def get_sql(sql_path):


#  --test ---
# x =  time.strptime(str(datetime.datetime.today().date()), "%Y-%m-%d")
# print x.tm_mon
