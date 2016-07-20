# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import logging
import logging.config
import os


# 根据文件夹存在与否创建目录
def is_exist_mkdir(file_path):
    # logger = logging.getLogger('crm.file_dir_process')
    try:
        if os.path.exists(file_path):
            print "%s is exists" % file_path
        else:
            os.mkdir(file_path)
    except Exception, e:
        exception = Exception, e
        error_info = str(exception) + "--------->>" + "create dir of %s is failed !" % file_path
        # logger.error(error_info)


# 创建文件
def create_file(file_path_name):
    open(file_path_name, 'w')


# 写文件方法
def wirte_file(file_name, content):
    try:
        fl = open(file_name, 'a')
        fl.write(str(content))
        fl.write("\n")
        # fl.close()
    except Exception, e:
        exception = Exception, e
        error_info = str(exception) + "--------->>" + "write  %s is failed !" % file_name
        # logger.error(error_info)


