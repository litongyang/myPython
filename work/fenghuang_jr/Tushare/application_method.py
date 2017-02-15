# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import datetime
import shutil
import os
import file_dir_process

def read_file_content(path):
    try:
        content = open(path).read()
        return content
    except Exception, e:
        print "---read_file_content----"
        print Exception, ": ", e


# 获取文件夹的所有文件
def get_file_dir(file_path, filelist):
    try:
        if os.path.isfile(file_path):
            filelist.append(file_path)
        elif os.path.isdir(file_path):
            for file in os.listdir(file_path):
                new_path = os.path.join(file_path, file)
                get_file_dir(new_path, filelist)
    except Exception, e:
        print Exception, e


# noinspection PyBroadException
def move_log_file(file_name):
    try:
        datekey = datetime.date.today()
        file_dir = "logs/" + str(datekey)
        log_dir = "logs/" + str(datekey) + "/" + str(file_name)
        file_dir_process.is_exist_mkdir(file_dir)
        if os.path.exists(file_name):
            print log_dir
            if os.path.exists(log_dir):
                os.remove(log_dir)
        if not os.path.exists(log_dir):
            try:
                shutil.move(str(file_name), str(file_dir))
            except:
                pass
        else:
            print "log file is not exists !"
    except Exception, e:
        print Exception, e


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
# move_log_file("test.txt")

#  --test ---
# x =  time.strptime(str(datetime.datetime.today().date()), "%Y-%m-%d")
# print x.tm_mon
# file_list = []
# get_file_dir("query_sql", file_list)
# print file_list
