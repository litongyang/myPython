# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
实现模型训练过程
"""
import sys
sys.path.append("/root/user_value_predict")
import os
import logging
import logging.config
import numpy as np
import pandas as pd
import model_training as model_training
import model_train_base_method as model_train_base_method
import user_value_predict_project.base_method.read_conf as read_conf
import user_value_predict_project.base_method.application_method as application_method
# import work.fenghuang_jr.user_value_predict_project.base_method.read_conf as read_conf
# import work.fenghuang_jr.user_value_predict_project.base_method.application_method as application_method


class StartModelTraining:
    def __init__(self):
        self.model_training_class = model_training.ModelTraining()
        self.from_1_to_1_result_path = read_conf.ReadConf().get_options('train_path', 'first_invest_train_set_from_1')
        self.model_save_path = read_conf.ReadConf().get_options('model_save_path', 'model_save_path_from_1')
        self.report_file = read_conf.ReadConf().get_options('report_path', 'report_file')
        self.label_cut_threshold = map(int, (read_conf.ReadConf().get_options('cut_threshold', 'label_cut_threshold')).split(','))
        self.partiong_ratio = 0.7
        self.from_1_to_1_x_last_n = -5
        self.from_1_to_1_x_label_last_n = 0
        self.is_success = []

    def start_model_training(self, train_set_path, model_path):
        """
        文件格式：
        第1 列为 ID，
        2-I 列为 X_LABEL,   !!!X_label_last_n=I!!!
        I-J 列为 X_VALUE,   !!!X_last_n=倒数第几列都为y 最后五列为y，则此值为-5
        J-N 列为 Y_LABEL.
        :return:
        """
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('user_predict.start_model_training')
        try:
            #  删除报告文件
            if os.path.exists(self.report_file):
                os.remove(self.report_file)
            # 读入文件，去除空值'\N'替换为pandas格式空值
            # data = pd.read_csv(train_set_path, encoding='utf-8')  # test
            data = pd.read_table(train_set_path, sep='\t').replace('\N', np.NaN)
            # data = pd.DataFrame(np.random.shuffle(np.asarray(data)))
            print data.shape
            # cut_D,X补0，Y为空的label剔除
            userid_data_set, labels = data.iloc[:, 0:self.from_1_to_1_x_last_n].fillna(0), np.transpose(np.asarray(data.iloc[:, self.from_1_to_1_x_last_n:]))
            for i, label in enumerate(labels):
                the_model_name = 'The_' + str(i * 3) + 'y_label_model'
                print '\n\n\n' + the_model_name
                # 剔除y_null的samples，并且把y值转化为分段标签
                user_id, data_set, label = model_train_base_method.del_null_y_samples(userid_data_set, label, self.label_cut_threshold)

                # 数据分区,输出numpy矩阵
                user_id_train, user_id_test, data_set_train, data_set_test, train_true_label, test_true_label = model_train_base_method.partion_xy(user_id, data_set, label, self.partiong_ratio)
                # 初始化模型对象，预处理X_train,X_test,赋初值y
                standar_train_set = self.model_training_class.pre_process_training(data_set_train, self.from_1_to_1_x_label_last_n, self.is_success)
                standar_test_set = self.model_training_class.process_predict_set(data_set_test, self.is_success)
                self.model_training_class.model_training(the_model_name, self.model_training_class.model, self.model_training_class.model_algorithm_name, standar_train_set, train_true_label, self.is_success)
                model_train_base_method.save_pickle_dump(self.model_training_class, model_path + the_model_name + self.model_training_class.model_algorithm_name + '.pkl')
                train_pre_label = self.model_training_class.model_predict(standar_train_set, self.is_success)
                test_pre_label = self.model_training_class.model_predict(standar_test_set, self.is_success)
                self.model_training_class.model_report(train_true_label, train_pre_label, self.report_file, self.is_success)
                self.model_training_class.model_report(test_true_label, test_pre_label, self.report_file, self.is_success)
                self.is_success.append(1)
                flag = 1
                for v in self.is_success:
                    if v == 0:
                        logger.error("start_model_training is failed!")
                        flag = 0
                        break
                if flag == 1:
                    logger.info("start_model_training is successed!")
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "start_model_training is Exception !"
            logger.error(error_info)
            self.is_success.append(0)
        application_method.move_log_file("logs.log")
        

if __name__ == '__main__':
    start_model_training = StartModelTraining()
    start_model_training.start_model_training(start_model_training.from_1_to_1_result_path, start_model_training.model_save_path)
