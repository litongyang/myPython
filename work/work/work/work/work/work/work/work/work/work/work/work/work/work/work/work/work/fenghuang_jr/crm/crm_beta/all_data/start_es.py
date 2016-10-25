# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import work.fenghuang_jr.crm.crm_beta.base_method.application_method as application_method
import os


class StartEs:
    def __init__(self):
        self.namenode = "bigdata-es"
        self.ip = "10.10.202.18:"
        self.index = "crm_index"
        self.type_index = "crm"

    def implement_es(self, dir_name, error_log_class):
        data_file_list = []
        try:
            application_method.get_file_dir(dir_name, data_file_list)
            for file in data_file_list:
                conmmand_content = "java -cp .:lib/* com.fengjr.bigdata.es.tool.EsClientTool {0:s} {1:s} {2:s} 9300 {3:s} {4:s} 50000 500 48 ${split} fund.logger" \
                    .format(file, self.namenode, self.ip, self.index, self.type_index)
                print conmmand_content
                os.system(conmmand_content)
        except Exception, e:
            error_info = Exception, e
            print error_info
            error_log_class.write_log(error_info)


if __name__ == '__main__':
    test = StartEs()
    # test.implement_es("query_sql")
