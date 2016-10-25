# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

"""
将mysql表信息导入hive
"""

import logging
import logging.config
import os
import work.fenghuang_jr.crm.crm_beta.base_method.application_method as method


class SqoopFunction:
    def __init__(self):
        self.logger = ""
        pass

    # 全表导入hive(hive表已存在)
    @staticmethod
    def sqoop_table(host, user_name, password, table, table_name, target_dir, hive_table):
        logger = logging.getLogger('crm.base_method.sqoop_table')
        try:
            sqoop_content = "sqoop import --connect {0:s} --username {1:s} --password {2:s} --table {3:s}" \
                            " --class-name {4:s} --target-dir {5:s} --delete-target-dir  --hive-table {6:s} --hive-import -m 1 --as-textfile" \
                .format(host, user_name, password, table, table_name, target_dir, hive_table)
            # print sqoop_content
            os_v = os.system(sqoop_content)
            if os_v == 0:
                logger.info("sqoop %s is successed!" % table_name)
            else:
                logger.error("sqoop %s is failed!" % table_name)
            return os_v
            # logger.info("sqoop %s  is successed !" % table_name)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "sqoop sqoop_table is Exception !"
            logger.error(error_info)

    # 全量导入hive
    @staticmethod
    def sqoop_all(host, user_name, password, sql, table_name, target_dir, hive_table):
        logger = logging.getLogger('crm.base_method.sqoop_all')
        try:
            sql = "\"" + str(sql) + "\""
            sqoop_content = "sqoop import --connect {0:s} --username {1:s} --password {2:s} --create-hive-table --query {3:s}" \
                            " --class-name {4:s} --target-dir {5:s} --delete-target-dir  --hive-table {6:s} --hive-import -m 1 --as-textfile --split-by \",\"" \
                .format(host, user_name, password, sql, table_name, target_dir, hive_table)
            # print sqoop_content
            os_v = os.system(sqoop_content)
            if os_v == 0:
                logger.info("sqoop %s is successed!" % table_name)
            else:
                logger.error("sqoop %s is failed!" % table_name)
            return os_v
            # logger.info("sqoop %s is successed!" % table_name)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "sqoop 'sqoop_all' is Exception !"
            logger.error(error_info)

    # 导入指定hive分区表
    @staticmethod
    def sqoop_dt(dt_type, date, host, user_name, password, sql, table_name, target_dir, hive_table):
        logger = logging.getLogger('crm.base_method.sqoop_dt')
        try:
            sql = "\"" + str(sql) + "\""
            print date
            target_dir = str(target_dir + "\\" + method.compute_dt(dt_type, date))
            print target_dir
            sqoop_content = "sqoop import --connect {0:s} --username {1:s} --password {2:s} --create-hive-table --query {3:s}" \
                            " --class-name {4:s} --target-dir {5:s} --delete-target-dir  --hive-table {6:s} --hive-import -m 1 --as-textfile" \
                .format(host, user_name, password, sql, table_name, target_dir, hive_table)
            # print sqoop_content
            os.system(sqoop_content)
            logger.info("sqoop  is successed: %s !" % sqoop_content)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "sqoop sqoop_dt is failed !"
            logger.error(error_info)

    # 增量导入hive表
    @staticmethod
    def sqoop_append(host, user_name, password, sql, table_name, target_dir, hive_table, col_name,last_value):
        logger = logging.getLogger('crm.base_method.sqoop_append')
        try:
            sql = "\"" + str(sql) + "\""
            print sql
            sqoop_content = "sqoop import --connect {0:s} --username {1:s} --password {2:s} --create-hive-table --query {3:s}" \
                            " --class-name {4:s} --target-dir {5:s} --delete-target-dir  --hive-table {6:s} --hive-import " \
                            "--incremental lastmodified  --check-column {7:s} --last-value {8:s} -m 1 --as-textfile" \
                .format(host, user_name, password, sql, table_name, target_dir, hive_table, col_name, last_value)
            # print sqoop_content
            os.system(sqoop_content)
            logger.info("sqoop  is successed: %s !" % sqoop_content)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "sqoop sqoop_append is failed !"
            logger.error(error_info)


if __name__ == '__main__':
    test = SqoopFunction()
    # test.sqoop_fun('host', 'user_name', 'password', 'sql', 'table_name', 'target_dir', 'hive_table')
