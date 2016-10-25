# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
将执行的hive_sql存入本地的数据,构造出训练集,存txt文件
"""
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


class GetTrainSet:
    def __init__(self):
        self.data_file_list = []

    def get_train_set(self, file_path, trans_path):
        fl = open(trans_path, 'w')
        get_file_dir(file_path, self.data_file_list)

        if len(self.data_file_list) > 0:
            for file in self.data_file_list:
                if file.find("crc") < 0:
                    fi = open(file, "r")
                    for line in fi:
                        fl.write(str(line))
        fl.close()

