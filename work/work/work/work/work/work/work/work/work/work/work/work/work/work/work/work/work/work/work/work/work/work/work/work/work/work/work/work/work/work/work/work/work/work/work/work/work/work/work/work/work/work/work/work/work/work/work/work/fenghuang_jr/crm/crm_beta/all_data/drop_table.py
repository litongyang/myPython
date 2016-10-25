# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import work.fenghuang_jr.crm.crm_beta.base_method.hive_command_method as hive_command_method
import logging
import logging.config


def drop_table():
    logger = logging.getLogger('start.drop_table')
    try:
        drop_table_sql_path = "./query_sql/drop_table.sql"
        hive_command_method.hive_command("-f", drop_table_sql_path)
        logger.info('drop table success !')
    except Exception, e:
        exception = Exception, e
        error_info = str(exception) + "--------->>" + "dropping table  fail !"
        logger.error(error_info)

