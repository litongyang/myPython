# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
基于用户投资行为的用户关系模型和产品推荐模型
"""
import sys
sys.path.append("/root/personas_fengjr/")
import logging
import logging.config
import get_user_relation_invest_view_train
import user_relation_invest_view_model_training
import save_user_relation_invest_view_result_data
import personas.version_1.base_method.application_method as application_method
import personas.version_1.base_method.read_conf as read_conf
import personas.version_1.base_method.send_mail as send_mail


class UserRelationInvestView:
    def __init__(self):
        self.get_train_set = get_user_relation_invest_view_train.GetRelationInvestViewTrain()
        self.model_training = user_relation_invest_view_model_training.UserRelationInvestViewModelTraining()
        self.save_hive = save_user_relation_invest_view_result_data.SaveUserRelationInvestViewResultData()
        self.is_success = []
        self.result_data_parent_path = read_conf.ReadConf().get_options("path_user_relation_invest_view", "input_user_relation_invest_view_result_data_parent_path")
        self.result_data_bid_path = read_conf.ReadConf().get_options("path_user_relation_invest_view", "input_user_relation_invest_view_bid_result_data_path")
        self.result_data_user_path = read_conf.ReadConf().get_options("path_user_relation_invest_view", "input_user_relation_invest_view_user_result_data_path")
        self.mail_tolist = read_conf.ReadConf().get_options("mail_send", "mail_tolist")
        self.mail_host = read_conf.ReadConf().get_options("mail_send", "mail_host")
        self.mail_user = read_conf.ReadConf().get_options("mail_send", "mail_user")
        self.mail_password = read_conf.ReadConf().get_options("mail_send", "mail_password")
        self.mail_postfix = read_conf.ReadConf().get_options("mail_send", "mail_postfix")

    def implement_process(self):
        logging.config.fileConfig('../logger.conf')
        root_logger = logging.getLogger('root')
        root_logger.debug('UserRelationInvestView start logger...')
        logger = logging.getLogger('personas.user_relation_invest_view')
        """ 得到训练集 """
        self.get_train_set.get_train_set(self.is_success)
        """ 模型训练 """
        self.model_training.get_train_data(self.is_success)
        self.model_training.compute_model_save_result_data(self.is_success)
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
            send_mail.send_mail(self.mail_tolist, self.mail_host, self.mail_user, self.mail_password, self.mail_postfix, "personas_UserRelationInvestView_error", "UserRelationInvest is error！")
        for v in self.is_success:
            if v == 0:
                flag = 0
                break
        if flag == 1:
            logger.info("success!")
        else:
            logger.error("error!")
            send_mail.send_mail(self.mail_tolist, self.mail_host, self.mail_user, self.mail_password, self.mail_postfix, "personas_UserRelationInvestView_error", "UserRelationInvest is error！")
        application_method.move_log_file("logs.log")
        application_method.move_file(self.result_data_parent_path, self.result_data_bid_path)
        application_method.move_file(self.result_data_parent_path, self.result_data_user_path)


if __name__ == '__main__':
    test = UserRelationInvestView()
    test.implement_process()