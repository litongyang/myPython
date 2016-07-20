# __author__ = 'litongyang'
# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(console=["test.py"])

# options = {"py2exe":
#             {"compressed": 1,
#              "optimize": 2,
#              "bundle_files": 1   # <span style="color: rgb(255, 128, 0); line-height: 15px; white-space: pre; background-color: rgb(253, 253, 253); ">所有文件打包成一个exe文件</span>
#             }
#           }
# setup(
#     version = "1.0.0",
#     description = "description for your exe",
#     name = "name for your exe",
#     options = options,
#     zipfile = None, # 不生成zip库文件
#     console = [{"script": "Test.py", "icon_resources": [(1, "Test.ico")] }],
#     )