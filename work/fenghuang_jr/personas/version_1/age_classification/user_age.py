# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
用户投资稳定性分类模型
"""
import sys
sys.path.append("/root/personas_fengjr")
import logging
import logging.config
import personas.version_1.base_method.application_method as application_method
import save_user_age_result_data
import user_age_model_training
import get_age_trans_set
import personas.version_1.base_method.read_conf as read_conf
import personas.version_1.base_method.send_mail as send_mail


class AgeClassification:
    def __init__(self):
        self.get_train_set = get_age_trans_set.GetAgeTransSet()
        self.model_training = user_age_model_training.UserAgeModelTraining()
        self.save_hive = save_user_age_result_data.SaveUserAgeResultData()
        self.is_success = []  # 每一步运行成功或者失败的标记
        self.result_data_path = read_conf.ReadConf().get_options("path_user_age", "input_user_age_result_data_path")
        self.result_data_parent_path = read_conf.ReadConf().get_options("path_user_age", "input_user_age_result_data_parent_path")
        self.mail_tolist = read_conf.ReadConf().get_options("mail_send", "mail_tolist")
        self.mail_host = read_conf.ReadConf().get_options("mail_send", "mail_host")
        self.mail_user = read_conf.ReadConf().get_options("mail_send", "mail_user")
        self.mail_password = read_conf.ReadConf().get_options("mail_send", "mail_password")
        self.mail_postfix = read_conf.ReadConf().get_options("mail_send", "mail_postfix")

    def implement_process(self):
        logging.config.fileConfig('../logger.conf')
        root_logger = logging.getLogger('root')
        root_logger.debug('AgeClassification start logger...')
        logger = logging.getLogger('personas.age_classification')
        """ 得到训练集 """
        self.get_train_set.get_train_set(self.is_success)

        """ 模型训练 """
        self.model_training.get_train_data(self.is_success)
        self.model_training.kmeans_age(self.is_success)
        self.model_training.get_classification_result(self.is_success)
        self.model_training.get_result(self.is_success)

        """ 将训练好的数据存入hive表 """
        flag = 1
        for v in self.is_success:
            if v == 0:
                flag = 0
                break
        if flag == 1:
            self.save_hive.get_result_data(self.is_success)
        else:
            logger.error("error!")
            send_mail.send_mail(self.mail_tolist, self.mail_host, self.mail_user, self.mail_password, self.mail_postfix, "personas_AgeClassification_error", "AgeClassification is error！")
        for v in self.is_success:
            if v == 0:
                flag = 0
                break
        if flag == 1:
            logger.info("success!")
        else:
            logger.error("error!")
            send_mail.send_mail(self.mail_tolist, self.mail_host, self.mail_user, self.mail_password, self.mail_postfix, "personas_AgeClassification_error", "AgeClassification is error！")
        application_method.move_log_file("logs.log")
        application_method.move_file(self.result_data_parent_path, self.result_data_path)

if __name__ == '__main__':
    test = AgeClassification()
    test.implement_process()
