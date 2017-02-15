# -*- encoding:utf-8 -*-
"""
#20170117
#author ruina
#用30days投资及基础信息，预测未来3,6,9,12月投资额度
"""
import sys
sys.path.append("/root/user_value_predict")
import logging
import logging.config
import numpy as np
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Imputer
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.ensemble import GradientBoostingClassifier
import model_train_base_method as model_train_base_method


class ModelTraining:
    def __init__(self):
        self.num_mat = [[]]  # 存储分段变量的转化结果
        self.data_set_label_last_n = 0  # 训练集分类变量最后一列下标
        self.label_encoding = ''  # 编码矩阵 
        # self.scaler = ''   # 归一化对象
        # self.model = GradientBoostingClassifier()  # 模型实例
        self.model = RandomForestClassifier()  # 模型实例
        self.model_name = ''
        # self.model_algorithm_name = 'GradientBoostingClassifier'
        self.model_algorithm_name = 'RandomForestClassifier'

    def pre_process_training(self, train_set, data_set_label_last_n, success):
        """ 
        :param success:
        :param train_set: X矩阵
        :param data_set_label_last_n: 
        :return: 
        """
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('user_predict.pre_process_training')
        try:
            # 预处理参数训练
            # step1，将部分字符型x_label 转 数值型x_value
            self.data_set_label_last_n = data_set_label_last_n
            print train_set
            # str_features = np.asarray(train_set[:, 0:data_set_label_last_n], dtype='str')
            value_features = train_set[:, data_set_label_last_n:]
            # self.label_encoding, num_features = model_train_base_method.train_mat_label_encoding(str_features)
            # train_set_result = np.asarray(np.column_stack((num_features, value_features)), dtype='float64')
            train_set_result = np.asarray(value_features)
            # step2，归一化
            train_set_result = Imputer().fit_transform(train_set_result)
            self.scaler = preprocessing.StandardScaler().fit(train_set_result)
            standar_train_set = np.nan_to_num(self.scaler.transform(train_set_result))
            success.append(1)
            return standar_train_set
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "pre_process_training is Exception !"
            logger.error(error_info)
            success.append(0)

    def process_predict_set(self, predict_set, success):
        """
        生成测试集
        :param success:
        :param predict_set:
        :return: 
        """
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('user_predict.process_predict_set')
        try:
            # str_features:离散化feature
            # str_features = np.asarray(predict_set[:, 0:self.data_set_label_last_n], dtype='str')
            value_features = predict_set[:, self.data_set_label_last_n:]
            # num_features = model_train_base_method.test_mat_label_encoding(self.label_encoding, str_features)
            # predict_set = np.asarray(np.column_stack((num_features, value_features)), dtype='float64')
            predict_set = np.asarray(value_features)
            predict_set = Imputer().fit_transform(predict_set)  # =>无需加self，因为该方法不会产生新参数，再次用到时，直接写函数名字调用
            standar_predict_set = np.nan_to_num(self.scaler.transform(predict_set))
            success.append(1)
            return standar_predict_set
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "process_predict_set is Exception !"
            logger.error(error_info)
            success.append(0)

    def model_training(self, model_name, model, model_algorithm_name, standar_train_set, label, success):
        """
        模型训练
        :param model_name:
        :param model_algorithm_name:
        :param model:
        :param standar_train_set:
        :param label:
        :return:
        """
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('user_predict.model_training')
        try:
            self.model_name, self.model_algorithm_name = model_name, model_algorithm_name
            self.model_train = Pipeline([("scale", StandardScaler()), (model_name, model)])
            self.model_train_object = self.model_train.fit(standar_train_set, np.asarray(label, dtype='int'))
            success.append(1)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "model_training is Exception !"
            logger.error(error_info)
            success.append(0)

    def model_predict(self, predict_standar_set, success):
        """
        模型预测
        :param success:
        :param predict_standar_set: 标准化后的测试集
        :return:
        """
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('user_predict.model_predict')
        try:
            self.predict_label = self.model_train_object.predict(predict_standar_set)
            success.append(1)
            return self.predict_label
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "model_predict is Exception !"
            logger.error(error_info)
            success.append(0)

    def save_result_file(self, user_id, predict_type, pre_label, ts, save_result_path, success):
        """
        存储预测结果:文件的形式
        :param ts: 存储时间戳
        :param predict_type: 预测类型
        :param success: 运行标识
        :param user_id:
        :param pre_label:
        :param save_result_path: 存储路径
        :return:
        """
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('user_predict.save_result_file')
        try:
            file_name = save_result_path + self.model_name + '_' + self.model_algorithm_name + 'result.txt'
            result = (np.column_stack((user_id, pre_label))).tolist()
            fw = open(file_name, 'w')
            for line in result:
                fw.write(str(line[0]))
                fw.write('\t')
                fw.write(str(predict_type))
                fw.write('\t')
                fw.write(str(line[1]))
                fw.write(str('\t'))
                fw.write(str(ts))
                fw.write('\n')
            fw.close()
            success.append(1)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "save_result_file is Exception !"
            logger.error(error_info)
            success.append(0)

    def model_report(self, true_label, pre_label, report_file, success):
        """
        产出模型效果报告
        :param report_file: 报告文件
        :param true_label: 真实label
        :param pre_label: 模型预测的label
        :return:
        """
        logging.config.fileConfig('../logger.conf')
        logger = logging.getLogger('user_predict.model_report')
        fw = open(report_file, 'aw')
        try:
            print self.model_name + '_' + self.model_algorithm_name + '_Report------------------------------------------'
            fw.write(str(self.model_name + '_' + self.model_algorithm_name + '_Report------------------------------------------'))
            fw.write('\n')
            report = metrics.classification_report(np.asarray(true_label, dtype='int'),
                                                   np.asarray(pre_label, dtype='int'))
            print report
            fw.write(str(report))
            success.append(1)
        except Exception, e:
            exception = Exception, e
            error_info = str(exception) + "--------->>" + "model_report is Exception !"
            logger.error(error_info)
            success.append(0)

if __name__ == '__main__':
    model_train = ModelTraining()


