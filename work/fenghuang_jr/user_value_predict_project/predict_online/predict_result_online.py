# -*- encoding: utf-8 -*-
import sys
sys.path.append("/root/user_value_predict")
import cPickle
import numpy as np
import pandas as pd
import logging
import logging.config
import time
import create_user_value_predict_result as mysqldb
import user_value_predict_project.base_method.save_result_db as save_result_db
import user_value_predict_project.base_method.read_conf as read_conf
import user_value_predict_project.get_data.get_predict_set as get_predict_set
import user_value_predict_project.base_method.send_mail as send_mail
import user_value_predict_project.base_method.application_method as application_method
from model_training import ModelTraining


class PredictOnline:
    def __init__(self):
        self.get_predict_set_class = get_predict_set.GetPredictSet()
        self.predict_set_file_from_1_path = read_conf.ReadConf().get_options('predict_set_file_path', 'predict_set_file_from_1_path')
        self.predict_set_file_from_30_path = read_conf.ReadConf().get_options('predict_set_file_path', 'predict_set_file_from_30_path')
        self.predict_set_file_from_60_path = read_conf.ReadConf().get_options('predict_set_file_path', 'predict_set_file_from_60_path')
        self.from_1_to_1_result_path = read_conf.ReadConf().get_options('first_invest_predict_result', 'from_1_to_1_result_path')
        self.predict_set_from_1_path = read_conf.ReadConf().get_options('predict_set_path', 'predict_set_from_1_path')
        self.predict_set_from_30_path = read_conf.ReadConf().get_options('predict_set_path', 'predict_set_from_30_path')
        self.predict_set_from_60_path = read_conf.ReadConf().get_options('predict_set_path', 'predict_set_from_60_path')
        self.model_from_1_to_1 = read_conf.ReadConf().get_options('model_pkl_path', 'model_from_1_to_1')
        self.model_from_1_to_3 = read_conf.ReadConf().get_options('model_pkl_path', 'model_from_1_to_3')
        self.model_from_1_to_6 = read_conf.ReadConf().get_options('model_pkl_path', 'model_from_1_to_6')
        self.model_from_1_to_9 = read_conf.ReadConf().get_options('model_pkl_path', 'model_from_1_to_9')
        self.model_from_1_to_12 = read_conf.ReadConf().get_options('model_pkl_path', 'model_from_1_to_12')
        self.model_from_30_to_3 = read_conf.ReadConf().get_options('model_pkl_path', 'model_from_30_to_3')
        self.model_from_30_to_6 = read_conf.ReadConf().get_options('model_pkl_path', 'model_from_30_to_6')
        self.model_from_30_to_9 = read_conf.ReadConf().get_options('model_pkl_path', 'model_from_30_to_9')
        self.model_from_30_to_12 = read_conf.ReadConf().get_options('model_pkl_path', 'model_from_30_to_12')
        self.model_from_60_to_3 = read_conf.ReadConf().get_options('model_pkl_path', 'model_from_60_to_3')
        self.model_from_60_to_6 = read_conf.ReadConf().get_options('model_pkl_path', 'model_from_60_to_6')
        self.model_from_60_to_9 = read_conf.ReadConf().get_options('model_pkl_path', 'model_from_60_to_9')
        self.model_from_60_to_12 = read_conf.ReadConf().get_options('model_pkl_path', 'model_from_60_to_12')
        self.from_1_to_1_result_path = read_conf.ReadConf().get_options('first_invest_predict_result', 'from_1_to_1_result_path')
        self.from_1_to_3_result_path = read_conf.ReadConf().get_options('first_invest_predict_result', 'from_1_to_3_result_path')
        self.from_1_to_6_result_path = read_conf.ReadConf().get_options('first_invest_predict_result', 'from_1_to_6_result_path')
        self.from_1_to_9_result_path = read_conf.ReadConf().get_options('first_invest_predict_result', 'from_1_to_9_result_path')
        self.from_1_to_12_result_path = read_conf.ReadConf().get_options('first_invest_predict_result', 'from_1_to_12_result_path')
        self.from_30_to_3_result_path = read_conf.ReadConf().get_options('first_invest_predict_result', 'from_30_to_3_result_path')
        self.from_30_to_6_result_path = read_conf.ReadConf().get_options('first_invest_predict_result', 'from_30_to_6_result_path')
        self.from_30_to_9_result_path = read_conf.ReadConf().get_options('first_invest_predict_result', 'from_30_to_9_result_path')
        self.from_30_to_12_result_path = read_conf.ReadConf().get_options('first_invest_predict_result', 'from_30_to_12_result_path')
        self.from_60_to_3_result_path = read_conf.ReadConf().get_options('first_invest_predict_result', 'from_60_to_3_result_path')
        self.from_60_to_6_result_path = read_conf.ReadConf().get_options('first_invest_predict_result', 'from_60_to_6_result_path')
        self.from_60_to_9_result_path = read_conf.ReadConf().get_options('first_invest_predict_result', 'from_60_to_9_result_path')
        self.from_60_to_12_result_path = read_conf.ReadConf().get_options('first_invest_predict_result', 'from_60_to_12_result_path')
        self.from_1_to_1_x_label_last_n = 0
        self.predict_set_dict = {}
        self.model_predict_set_dict_from_1 = {}  # 模型和预测集字典
        self.model_predict_set_dict_from_30 = {}  # 模型和预测集字典
        self.model_predict_set_dict_from_60 = {}  # 模型和预测集字典
        self.model_predict_type_dict = {}  # 模型和预测类型字典
        self.mysqldb = mysqldb.CreateTable()
        self.mail_tolist = read_conf.ReadConf().get_options("mail_send", "mail_tolist")
        self.mail_host = read_conf.ReadConf().get_options("mail_send", "mail_host")
        self.mail_user = read_conf.ReadConf().get_options("mail_send", "mail_user")
        self.mail_password = read_conf.ReadConf().get_options("mail_send", "mail_password")
        self.mail_postfix = read_conf.ReadConf().get_options("mail_send", "mail_postfix")
        self.is_success = []

    def predict_result(self):
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('user_predict.predict_result')
        try:
            self.model_predict_set_dict_from_1[self.model_from_1_to_1] = self.from_1_to_1_result_path
            self.model_predict_set_dict_from_1[self.model_from_1_to_3] = self.from_1_to_3_result_path
            self.model_predict_set_dict_from_1[self.model_from_1_to_6] = self.from_1_to_6_result_path
            self.model_predict_set_dict_from_1[self.model_from_1_to_9] = self.from_1_to_9_result_path
            self.model_predict_set_dict_from_1[self.model_from_1_to_12] = self.from_1_to_12_result_path
            self.model_predict_set_dict_from_30[self.model_from_30_to_3] = self.from_30_to_3_result_path
            self.model_predict_set_dict_from_30[self.model_from_30_to_6] = self.from_30_to_6_result_path
            self.model_predict_set_dict_from_30[self.model_from_30_to_9] = self.from_30_to_9_result_path
            self.model_predict_set_dict_from_30[self.model_from_30_to_12] = self.from_30_to_12_result_path
            self.model_predict_set_dict_from_60[self.model_from_60_to_3] = self.from_60_to_3_result_path
            self.model_predict_set_dict_from_60[self.model_from_60_to_6] = self.from_60_to_6_result_path
            self.model_predict_set_dict_from_60[self.model_from_60_to_9] = self.from_60_to_9_result_path
            self.model_predict_set_dict_from_60[self.model_from_60_to_12] = self.from_60_to_12_result_path

            self.model_predict_type_dict[self.model_from_1_to_1] = 'from_1_to_1'
            self.model_predict_type_dict[self.model_from_1_to_3] = 'from_1_to_3'
            self.model_predict_type_dict[self.model_from_1_to_6] = 'from_1_to_6'
            self.model_predict_type_dict[self.model_from_1_to_9] = 'from_1_to_9'
            self.model_predict_type_dict[self.model_from_1_to_12] = 'from_1_to_12'
            self.model_predict_type_dict[self.model_from_30_to_3] = 'from_30_to_3'
            self.model_predict_type_dict[self.model_from_30_to_6] = 'from_30_to_6'
            self.model_predict_type_dict[self.model_from_30_to_9] = 'from_30_to_9'
            self.model_predict_type_dict[self.model_from_30_to_12] = 'from_30_to_12'
            self.model_predict_type_dict[self.model_from_60_to_3] = 'from_60_to_3'
            self.model_predict_type_dict[self.model_from_60_to_6] = 'from_60_to_6'
            self.model_predict_type_dict[self.model_from_60_to_9] = 'from_60_to_9'
            self.model_predict_type_dict[self.model_from_60_to_12] = 'from_60_to_12'

            self.predict_set_dict[str(self.predict_set_from_1_path)] = self.model_predict_set_dict_from_1
            self.predict_set_dict[str(self.predict_set_from_30_path)] = self.model_predict_set_dict_from_30
            self.predict_set_dict[str(self.predict_set_from_60_path)] = self.model_predict_set_dict_from_60

            self.get_predict_set_class.load_data(self.is_success)
            self.get_predict_set_class.get_predict_set(self.predict_set_file_from_1_path, self.predict_set_from_1_path, self.is_success)
            self.get_predict_set_class.get_predict_set(self.predict_set_file_from_30_path, self.predict_set_from_30_path, self.is_success)
            self.get_predict_set_class.get_predict_set(self.predict_set_file_from_60_path, self.predict_set_from_60_path, self.is_success)
            for predict_set_path, model_predict_set_dict in self.predict_set_dict.items():
                try:
                    # 初始化模型对象，预处理X_train,X_test,赋初值y
                    predict_set_data = pd.read_table(predict_set_path, sep='\t').replace('\N', np.NaN)
                    user_id, predict_set = predict_set_data.iloc[:, 0], np.asarray(predict_set_data.iloc[:, 1:-1].fillna(0))
                    print predict_set.shape
                    for model_pkl_path, predict_set_result_path in model_predict_set_dict.items():
                        with open(model_pkl_path, 'r') as f:
                            model_object = cPickle.load(f)
                        standar_predict_x = model_object.process_predict_set(predict_set, self.is_success)
                        predict_y = model_object.model_predict(standar_predict_x, self.is_success)
                        print "#######", predict_set_result_path
                        predict_type = self.model_predict_type_dict[str(model_pkl_path)]
                        ts = time.strftime('%Y-%m-%d %X', time.localtime())
                        save_result_db.save_result_db(user_id, predict_type, predict_y, ts, self.mysqldb, self.is_success)
                        # model_object.save_result_file(user_id, predict_type, predict_y, ts, predict_set_result_path, self.is_success)
                        self.is_success.append(1)
                except Exception, e:
                    exception = Exception, e
                    error_info = str(exception) + "--------->>" + str(predict_set_path) + ":predict_result is Exception !"
                    logger.error(error_info)
                    self.is_success.append(0)
            self.is_success.append(1)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "predict_result is Exception !"
            logger.error(error_info)
            self.is_success.append(0)
        flag = 1
        for v in self.is_success:
            if v == 0:
                logger.error("predict_result is failed!")
                send_mail.send_mail(self.mail_tolist, self.mail_host, self.mail_user, self.mail_password,
                                    self.mail_postfix, "user_value_predict_error", "PredictOnline is error!")
                flag = 0
                break
        if flag == 1:
            logger.info("predict_result is successed!")
        application_method.move_log_file("logs.log")


if __name__ == "__main__":
    predict_online = PredictOnline()
    predict_online.predict_result()
