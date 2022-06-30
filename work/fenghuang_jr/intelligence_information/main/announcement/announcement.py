# __author__ = 'lty'
# -*- coding: utf-8 -*-

import sys
sys.path.append("/root/intelligence_info/")
import logging
import logging.config
import intelligence_information.base_method.read_conf as read_conf
import intelligence_information.get_data.get_mongo_data as get_mongo_data
# import intelligence_information.get_data.get_hive_data as get_hive_data
import intelligence_information.get_data.get_data_set as get_data_set
import intelligence_information.base_method.save_result_data as save_result_data
import intelligence_information.base_method.application_method as application_method
import intelligence_information.base_method.send_mail as send_mail
import time
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

class GetPriceFinInfo:
    def __init__(self):
        self.get_hive_data = get_data_set.GetDataSet()
        self.save_result_data_class = save_result_data.SaveResultData()
        self.prices_all_file_path = read_conf.ReadConf().get_options('file_path', 'prices_all_file_path')
        self.prices_all_data_path = read_conf.ReadConf().get_options('data_path', 'prices_all_data_path')
        self.finace_result_file_path = read_conf.ReadConf().get_options('result_file_path', 'announcement_result_file_path')
        self.input_finance_price_announcement_result_sql_path = read_conf.ReadConf().get_options('finance_sql_path','input_finance_price_announcement_result_sql_path')
        self.mail_tolist = read_conf.ReadConf().get_options("mail_send", "mail_tolist")
        self.mail_host = read_conf.ReadConf().get_options("mail_send", "mail_host")
        self.mail_user = read_conf.ReadConf().get_options("mail_send", "mail_user")
        self.mail_password = read_conf.ReadConf().get_options("mail_send", "mail_password")
        self.mail_postfix = read_conf.ReadConf().get_options("mail_send", "mail_postfix")

        self.code = []
        self.short_name = []
        self.method = []
        self.total_count = []
        self.p_date = []
        self.list_date = []
        self.lock_date = []
        self.price = []
        self.trade_dt = []
        self.is_success = []

    def get_data(self):
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('intelligence_info.get_data')
        try:
            self.get_hive_data.load_data(self.is_success)
            self.get_hive_data.get_data_set(self.prices_all_file_path, self.prices_all_data_path, self.is_success)
            logger.info("get_data is successed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_data is Exception !"
            logger.error(error_info)
            self.is_success.append(0)

    def compute_price_range(self, n):
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('intelligence_info.compute_price_range')
        try:
            fw = open(str(self.finace_result_file_path), 'wr')
            test = get_mongo_data.GetMongoData()
            test.get_mongo_data()
            for data in test.data:
                self.code = []
                self.price = []
                self.trade_dt = []
                wr_code = ''
                for line in open(str(self.prices_all_data_path), 'r'):
                    line_one = line.split()
                    line_code = line_one[0].split('.')[0]
                    if line_code == data['code']:
                        line_time = time.strftime("%Y-%m-%d", time.strptime(line_one[2], "%Y%m%d"))
                        self.price.append(line_one[1])
                        self.trade_dt.append(line_time)
                        wr_code = line_one[0]

                if len(self.trade_dt) > 0:
                    for i in range(0, len(self.trade_dt)):
                        ##增发日期可能休市？
                        if self.trade_dt[i] == data['p_date']:
                            fw.write(str(wr_code))
                            fw.write('\t')
                            fw.write(str(data['short_name']))
                            fw.write('\t')
                            fw.write(str(data['method']))
                            fw.write('\t')
                            fw.write(str(data['total_count']))
                            fw.write('\t')
                            fw.write(str(data['p_date']))
                            fw.write('\t')
                            fw.write(str(data['list_date']))
                            fw.write('\t')
                            fw.write(str(data['lock_date']))
                            fw.write('\t')
                            fw.write(str(int(n)))
                            fw.write('\t')
                            if (i+n)<len(self.price):
                                fw.write(str((float(self.price[i]) - float(self.price[i + n])) / float(self.price[i])))
                            else:
                                fw.write('')
                            fw.write('\t')
                            if (i-n)>=0:
                                fw.write(str((float(self.price[i]) - float(self.price[i - n])) / float(self.price[i])))
                            else:
                                fw.write('')
                            fw.write('\n')
            self.is_success.append(1)
            logger.info("compute_price_range is successed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "compute_price_range is Exception !"
            logger.error(error_info)
            self.is_success.append(0)
    # 将结果存入hive

    def get_result(self):
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('intelligence_info.get_result')
        try:
            self.save_result_data_class.get_result_data(self.input_finance_price_announcement_result_sql_path, self.is_success)
            self.is_success.append(1)
            logger.info("get_result is successed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_result is Exception !"
            logger.error(error_info)
            self.is_success.append(0)

    # 监控
    def monitor(self):
        logging.config.fileConfig('../logger.conf')
        root_logger = logging.getLogger('root')
        root_logger.debug('UserRelationInvestView start logger...')
        logger = logging.getLogger('personas.user_relation_invest_view')
        flag = 1
        for v in self.is_success:
            if v == 0:
                flag = 0
                break
        if flag == 1:
            logger.info("get_price_finInfo is successed!")
        else:
            logger.error("get_price_finInfo is failed!")
            send_mail.send_mail(self.mail_tolist, self.mail_host, self.mail_user, self.mail_password,
                                self.mail_postfix,
                                "get_price_finInfo_error", "get_price_finInfo is failed！")
        application_method.move_log_file("logs.log")
if __name__ == '__main__':
    get_price_fin_info = GetPriceFinInfo()
    get_price_fin_info.get_data()
    # get_price_fin_info.compute_price_range(7)
    get_price_fin_info.compute_price_range(3)
    get_price_fin_info.get_result()
    get_price_fin_info.monitor()
