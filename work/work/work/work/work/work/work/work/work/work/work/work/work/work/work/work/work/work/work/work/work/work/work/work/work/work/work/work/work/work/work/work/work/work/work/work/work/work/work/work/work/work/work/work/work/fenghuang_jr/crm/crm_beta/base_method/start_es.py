# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import logging
import logging.config
import application_method
import read_conf
import os


def implement_es(dir_name, attribute_index):
    namenode = read_conf.ReadConf().get_options("es_index_params", "namenode")
    ip = read_conf.ReadConf().get_options("es_index_params", "ip")
    index = read_conf.ReadConf().get_options("es_index_params", "index")
    type_index = read_conf.ReadConf().get_options("es_index_params", "type_index")
    data_file_list = []
    logger = logging.getLogger('crm.base_method.implement_es')
    try:
        os_flag = 0
        rank_cnt = 0
        application_method.get_file_dir(dir_name, data_file_list)
        if len(data_file_list) > 0:
            for file in data_file_list:
                if file.find("crc") < 0:
                    fi = open(file, "r")
                    lines = fi.readlines()
                    rank_cnt += len(lines)
                    fi.close()
                    logger.info(" rank_cnt of %s  is %s !" % (file, rank_cnt))
                    conmmand_content = "java -cp .:/data/ml/tongyang/lib/* com.fengjr.bigdata.es.tool.EsClientTool {0:s} {1:s} {2:s} 9300 {3:s} {4:s} 50000 500 48 {5:s} {6:s}" \
                        .format(file, namenode, ip, index, type_index, '\x01', attribute_index)
                    # print conmmand_content
                    logger.info(conmmand_content)
                    os_v = os.system(conmmand_content)
                    if os_v == 0:
                        logger.info("Import %s to es is successed !" % file)
                    else:
                        os_flag = 1
                        logger.error("Import %s to es is failed !" % file)
            return os_flag, rank_cnt
        else:
            logger.error("file of %s is not exist!" % dir_name)
        # logger.info("%s :implement_es is successed!" % dir_name)
    except Exception, e:
        exception = Exception, e
        error_info = str(exception) + "--------->>" + "%s :implement_es is Exception!" % dir_name
        logger.error(error_info)


