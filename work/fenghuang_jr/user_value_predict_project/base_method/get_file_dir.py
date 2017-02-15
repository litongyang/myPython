# __author__ = 'lty'
# -*- coding: utf-8 -*-

import os


# 获取所以文件
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
