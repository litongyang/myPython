# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import hive_command_method
import logging
import logging.config
import work.fenghuang_jr.crm.crm_beta.schedule.invoke_schedule as invoke_schedule


def drop_table(sql_path, is_success):
    invoke_schedule_class = invoke_schedule.InvokeSchedule()
    logger = logging.getLogger('crm.base_method.drop_table')
    try:
        invoke_schedule_class.invoke_level_fun(1, "drop_table", "drop_table is starting !")
        os_v = hive_command_method.hive_command("-f", sql_path)
        if os_v == 0:
            logger.info("drop_table is successed !")
            invoke_schedule_class.invoke_update_fun(1, 0, "drop_table is successed !", -1)
            is_success.append(1)
        else:
            logger.error("drop_table is failed !")
            invoke_schedule_class.invoke_update_fun(1, 1, "drop_table is failed !", -1)
            is_success.append(0)
    except Exception, e:
        exception = Exception, e
        error_info = str(exception) + "--------->>" + "dropping table is Exception !"
        logger.error(error_info)
        invoke_schedule_class.invoke_update_fun(1, 2, error_info, -1)
        is_success.append(0)
