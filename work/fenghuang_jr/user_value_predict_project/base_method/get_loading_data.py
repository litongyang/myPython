# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
将执行的hive_sql存入本地的数据,构造出训练集,存txt文件
"""
import os
import get_file_dir


class GetLoadingData:
    def __init__(self):
        self.data_file_list = []

    def get_loading_data(self, file_path, trans_path):
        get_file_dir.get_file_dir(file_path, self.data_file_list)
        if len(self.data_file_list) > 0:
            fl = open(trans_path, 'w')
            for file in self.data_file_list:
                if file.find("crc") < 0:
                    fi = open(file, "r")
                    for line in fi:
                        fl.write(str(line))
            fl.close()
