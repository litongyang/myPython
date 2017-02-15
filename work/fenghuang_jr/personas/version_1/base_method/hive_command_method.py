# __author__ = 'lty'
# -*- coding: utf-8 -*-

import logging
import logging.config
import os


# 执行hive命令
def hive_command(params, content):
    logger = logging.getLogger('personas.base_method.hive_command')
    try:
        os.system("kinit -k -t  /data/key/hdfs.keytab hdfs@hadoop_edw")
        hive_home = "hive"
        command_content = hive_home + " " + params + " " + content
        # print command_content
        os_v1 = os.system("set hive.exec.compress.output=false")
        os_v = os.system(command_content)
        return os_v
    except Exception, e:
        exception = Exception, e
        error_info = str(exception) + "--------->>" + "run  function of hive_command is Exception !"
        logger.error(error_info)