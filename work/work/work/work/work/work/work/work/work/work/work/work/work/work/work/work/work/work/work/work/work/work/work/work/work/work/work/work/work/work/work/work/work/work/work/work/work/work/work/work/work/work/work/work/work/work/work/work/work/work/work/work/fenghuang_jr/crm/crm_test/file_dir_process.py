# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import os
import error_log


class FileProcess:
    def __init__(self):
        self.error_log = error_log.ErrorLog()

    # 根据文件夹存在与否创建目录
    @staticmethod
    def is_exist_mkdir(file_path):
        try:
            if os.path.exists(file_path):
                print "%s is exists" % file_path
                # pass
            else:
                os.mkdir(file_path)
        except Exception, e:
            # error_info = Exception, ": ", e
            print Exception, ": ", e

    # 创建文件
    @staticmethod
    def create_file(file_path_name):
        open(file_path_name, 'w')

    # 写文件方法
    @staticmethod
    def wirte_file(file_name, content):
        try:
            fl = open(file_name, 'a')
            fl.write(str(content))
            fl.write("\n")
            # fl.close()
        except Exception, e:
            print Exception, ": ", e

if __name__ == '__main__':
    test = FileProcess()
