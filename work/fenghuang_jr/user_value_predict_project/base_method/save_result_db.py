# __author__ = 'lty'
# -*- coding: utf-8 -*-

import logging
import logging.config
import numpy as np


def save_result_db(user_id, predict_type, pre_label, ts, mysqldb, success):
    """
    存储预测结果:mysql
    :param user_id:
    :param predict_type:
    :param pre_label:
    :param ts:
    :param mysqldb:
    :param success:
    :return:
    """
    logging.config.fileConfig('../logger.conf')
    logger = logging.getLogger('user_predict.save_result_db')
    try:
        result = (np.column_stack((user_id, pre_label))).tolist()
        for line in result:
            insert_sql = '\'' + str(line[0]) + '\'' + ','
            insert_sql += '\'' + str(predict_type) + '\'' + ','
            insert_sql += '\'' + str(line[1]) + '\'' + ','
            insert_sql += '\'' + str(ts) + '\'' + ','
            insert_sql = insert_sql[0:-1]  # 去除最后一个逗号
            mysqldb.insert_data(mysqldb.user_value_predict_result, insert_sql)
        success.append(1)
    except Exception, e:
        exception = Exception, e
        error_info = str(exception) + "--------->>" + "save_result_db is Exception !"
        logger.error(error_info)
        success.append(0)