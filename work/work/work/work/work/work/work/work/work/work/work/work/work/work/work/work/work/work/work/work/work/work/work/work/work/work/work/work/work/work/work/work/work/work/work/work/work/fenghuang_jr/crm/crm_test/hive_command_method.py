# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import os


# 执行hive命令
def hive_command(params, content):
    try:
        hive_home = "$HIVE_HOME/bin/hive"
        command_content = hive_home + " " + params + " " + content
        os.system(command_content)
    except Exception, e:
        print Exception, e

