# __author__ = 'lty'
# -*- coding: utf-8 -*-

import logging
import logging.config
import os


# 执行hive命令
def hive_command(params, content):
    logger = logging.getLogger('crm.base_method.hive_command')
    try:
        hive_home = "$HIVE_HOME/bin/hive"
        command_content = hive_home + " " + params + " " + content
        # print command_content
        # os.system(command_content)
        os_v = os.system(command_content)
        if os_v == 0:
            logger.info("run hive command is successed !")
        else:
            logger.error("run hive command is failed !")
        return os_v
    except Exception, e:
        exception = Exception, e
        error_info = str(exception) + "--------->>" + "run  function of hive_command is Exception !"
        logger.error(error_info)