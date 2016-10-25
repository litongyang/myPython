# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import logging
import logging.config
import work.fenghuang_jr.crm.crm_beta.schedule.invoke_schedule as invoke_schedule

invoke_schedule_class = invoke_schedule.InvokeSchedule()


def push_schedule_result(os_v, level, is_success, function_name):
    logger = logging.getLogger('crm.base_method.push_schedule_result')
    content_success = "run function of " + str(function_name) + " is successed !"
    content_fail = "run function of " + str(function_name) + " is failed !"
    # print type(push_schedule_result.__name__)
    if os_v == 0:
        logger.info(content_success)
        invoke_schedule_class.invoke_update_fun(level, 0, content_success, -1)
        is_success.append(1)
    else:
        logger.error(content_fail)
        invoke_schedule_class.invoke_update_fun(level, 1, content_fail, -1)
        is_success.append(0)


def push_schedule_result_es(os_v, level, is_success, function_name, cnt):
    logger = logging.getLogger('crm.base_method.push_schedule_result')
    content_success = "run function of " + str(function_name) + " is successed !"
    content_fail = "run function of " + str(function_name) + " is failed !"
    if os_v == 0:
        logger.info(content_success)
        invoke_schedule_class.invoke_update_fun(level, 0, content_success, cnt)
        is_success.append(1)
    else:
        logger.error(content_fail)
        invoke_schedule_class.invoke_update_fun(level, 1, content_fail, cnt)
        is_success.append(0)


def push_schedule_exception(exception, level, is_success, function_name):
    logger = logging.getLogger('crm.base_method.push_schedule_exception')
    exception_info = str(exception) + "--------->>" + "run  function of " + str(function_name) + "Exception !"
    logger.error(exception_info)
    invoke_schedule_class.invoke_update_fun(level, 2, exception_info, -1)
    is_success.append(0)




if __name__ == '__main__':
    # test
    push_schedule_result(0, 0, 0, 0)
