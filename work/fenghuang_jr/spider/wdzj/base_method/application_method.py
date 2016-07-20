# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import datetime
import shutil
import os
import file_dir_process


# noinspection PyBroadException
# 将文件移到指定目录
def move_log_file(file_name, file_path):
    """

    :type spider_name: 蜘蛛名字
    :type file_name: 文件名称
    :type file_path: 文件路径

    """
    try:
        datekey = datetime.date.today()
        file_dir = "../log/" + str(datekey)
        log_dir = "../log/" + str(datekey) + "/" + str(file_name)
        file_dir_process.is_exist_mkdir(file_dir)
        if os.path.exists(file_path):
            print log_dir
            if os.path.exists(log_dir):
                os.remove(log_dir)
            if not os.path.exists(log_dir):
                try:
                    shutil.move(str(file_path), str(file_dir))
                except:
                    pass
        else:
            print "log file is not exists !"
    except Exception, e:
        print Exception, e


# 判断文件是否包含该字符串
def is_exist_string_file(file_path, string):
    flag = 0
    if os.path.exists(file_path):
        fileObj = open(file_path, 'r')
        for line in fileObj:
            if str(string) in str(line):
                flag = 1
                break
    return flag

