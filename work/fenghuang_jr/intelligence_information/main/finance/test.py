# __author__ = 'lty'
# -*- coding: utf-8 -*-
import sys
sys.path.append("/root/intelligence_info/")
import logging
import logging.config
import intelligence_information.base_method.read_conf as read_conf
import intelligence_information.base_method.save_result_data as save_result_data
import intelligence_information.get_data.get_data_set as get_data_set
import intelligence_information.base_method.application_method as application_method
import intelligence_information.base_method.send_mail as send_mail


class GetPriceFinInfo:
    def __init__(self):
        self.get_predict_set_class = get_data_set.GetDataSet()
        self.save_result_data_class = save_result_data.SaveResultData()
        self.finance_prices_file_path = read_conf.ReadConf().get_options('file_path', 'finance_prices_file_path')
        self.finance_prices_data_path = read_conf.ReadConf().get_options('data_path', 'finance_prices_data_path')
        self.company_code_file_path = read_conf.ReadConf().get_options('file_path', 'company_code_file_path')
        self.company_code_data_path = read_conf.ReadConf().get_options('data_path', 'company_code_data_path')
        self.finace_result_file_path = read_conf.ReadConf().get_options('result_file_path', 'finace_result_file_path')
        self.input_finance_price_result_sql_path = read_conf.ReadConf().get_options('finance_sql_path', 'input_finance_price_result_sql_path')
        self.mail_tolist = read_conf.ReadConf().get_options("mail_send", "mail_tolist")
        self.mail_host = read_conf.ReadConf().get_options("mail_send", "mail_host")
        self.mail_user = read_conf.ReadConf().get_options("mail_send", "mail_user")
        self.mail_password = read_conf.ReadConf().get_options("mail_send", "mail_password")
        self.mail_postfix = read_conf.ReadConf().get_options("mail_send", "mail_postfix")
        self.company_code_list = []
        self.code = []
        self.price = []
        self.trade_dt = []
        self.ann_dt = []
        self.is_success = []

    def get_data(self):
        logging.config.fileConfig('../../logger.conf')
        logger = logging.getLogger('intelligence_info.get_data')
        try:
            #self.get_predict_set_class.load_data(self.is_success)
            self.get_predict_set_class.get_data_set(self.finance_prices_file_path, self.finance_prices_data_path, self.is_success)
            self.get_predict_set_class.get_data_set(self.company_code_file_path, self.company_code_data_path, self.is_success)
            for line in open(str(self.company_code_data_path), 'r'):
                line_one = line.split()
                self.company_code_list.append(line_one[0])
            self.is_success.append(1)
            logger.info("get_data is successed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_data is Exception !"
            logger.error(error_info)
            self.is_success.append(0)

    def compute_price_range(self, n):
        logging.config.fileConfig('../../logger.conf')
        logger = logging.getLogger('intelligence_info.compute_price_range')
        try:
            fw = open(str(self.finace_result_file_path), 'aw')
            for code in self.company_code_list:
                self.code = []
                self.price = []
                self.trade_dt = []
                self.ann_dt = []
                for line in open(str(self.finance_prices_data_path), 'r'):
                    line_one = line.split()
                    if line_one[0] == code:
                        self.price.append(line_one[1])
                        self.trade_dt.append(line_one[2])
                        self.ann_dt.append(line_one[3])
                if len(self.ann_dt) > 0:
                    for i in range(0, len(self.ann_dt)):
                        if self.ann_dt[i] != '\N':
                            if int(i + n) < 0 or int(i + n) >= len(self.ann_dt):
                                fw.write(str(code))
                                fw.write('\t')
                                fw.write(str(int(n)))
                                fw.write('\t')
                                fw.write(str(self.ann_dt[i]))
                                fw.write('\t')
                                fw.write(str(''))
                                fw.write('\n')
                                print code
                                print ''
                            else:
                                fw.write(str(code))
                                fw.write('\t')
                                fw.write(str(int(n)))
                                fw.write('\t')
                                fw.write(str(self.ann_dt[i]))
                                fw.write('\t')
                                price = self.price[i]
                                price_will = self.price[i + n]
                                if self.price[i] == '\N':
                                    for j in range(i - 1, -1, -1):
                                        if self.price[j] != '\N':
                                            price = self.price[j]
                                            break
                                if self.price[i + n] == '\N':
                                    for k in range(i + n - 1, -1, -1):
                                        if self.price[k] != '\N':
                                            price_will = self.price[k]
                                            break
                                if price == '\N' or price_will == '\N':
                                    fw.write(str(''))
                                else:
                                    fw.write(str((float(price) - float(price_will)) / float(price)))
                                fw.write('\n')
                                print code
                                print self.ann_dt[i]
                                #print self.trade_dt[i + n]
                                #print self.price[i + n]
                                #print (float(self.price[i]) - float(self.price[i + n])) / float(self.price[i])
                            print "********"
                            if int(i - n) < 0 or int(i - n) >= len(self.ann_dt):
                                fw.write(str(code))
                                fw.write('\t')
                                fw.write(str(int(-n)))
                                fw.write('\t')
                                fw.write(str(self.ann_dt[i]))
                                fw.write('\t')
                                fw.write(str(''))
                                fw.write('\n')
                                print code
                                print ''
                            else:
                                fw.write(str(code))
                                fw.write('\t')
                                fw.write(str(int(-n)))
                                fw.write('\t')
                                fw.write(str(self.ann_dt[i]))
                                fw.write('\t')
                                price1 = self.price[i]
                                price_pre = self.price[i - n]
                                if self.price[i] == '\N':
                                    for j1 in range(i-1, -1, -1):
                                        if self.price[j1] != '\N':
                                            price1 = self.price[j1]
                                            break
                                if self.price[i - n] == '\N':
                                    for k1 in range(i-n-1, -1, -1):
                                        if self.price[k1] != '\N':
                                            price_pre = self.price[k1]
                                            break
                                if price1 == '\N' or price_pre == '\N':
                                    fw.write(str(''))
                                else:
                                    fw.write(str((float(price1) - float(price_pre)) / float(price1)))
                                fw.write('\n')
                                print code
                                print self.ann_dt[i]
                                #print self.trade_dt[i - n]
                                #print self.price[i - n]
                                #print (float(self.price[i]) - float(self.price[i - n])) / float(self.price[i])
                            print "=============="
            self.is_success.append(1)
            logger.info("compute_price_range is successed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "compute_price_range is Exception !"
            logger.error(error_info)
            self.is_success.append(0)

    # 将结果存入hive
    def get_result(self):
        logging.config.fileConfig('../../logger.conf')
        logger = logging.getLogger('intelligence_info.get_result')
        try:
            self.save_result_data_class.get_result_data(self.input_finance_price_result_sql_path, self.is_success)
            self.is_success.append(1)
            logger.info("get_result is successed !")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "get_result is Exception !"
            logger.error(error_info)
            self.is_success.append(0)

    # 监控
    def monitor(self):
        logging.config.fileConfig('../../logger.conf')
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
            send_mail.send_mail(self.mail_tolist, self.mail_host, self.mail_user, self.mail_password, self.mail_postfix,
                                "get_price_finInfo_error", "get_price_finInfo is failed！")
        application_method.move_log_file("logs.log")

if __name__ == '__main__':
    get_price_fin_info = GetPriceFinInfo()
    get_price_fin_info.get_data()
    get_price_fin_info.compute_price_range(7)
    get_price_fin_info.compute_price_range(3)
    #get_price_fin_info.get_result()
    get_price_fin_info.monitor()
