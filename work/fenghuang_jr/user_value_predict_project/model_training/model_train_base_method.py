# __author__ = 'ruina'
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn import preprocessing
import cPickle


def del_null_y_samples(id_x, y, y_cut_threshold):
    """
    删除y为null的样本数据,并将连续型y值转化为label分类
    :param id_x:
    :param y_cut_threshold: 分段阈值
    :return: 返回清洗过y_null的有效样本集
    """

    data_pd = pd.DataFrame(np.column_stack((id_x, y)))
    data = np.asarray(data_pd.dropna(axis=0))
    print 'After del_nullY_samples:', data.shape

    user_id, data_set, label = data[:, 0], data[:, 1:-1], list_cut(data[:, -1], y_cut_threshold)
    return user_id, data_set, label


def partion_xy(user_id, data_set, label, ratio):
    """
    将数据集切分成训练集和测试集
    :param user_id:
    :param data_set: X数据集
    :param label: Y
    :param ratio: 切分训练集占比
    :return: 分区后的user_id,data_set,label
    """
    user_id, data_set, label = np.asarray(user_id), np.asarray(data_set), np.asarray(label)
    n_train = int(len(data_set) * ratio)

    user_id_train, user_id_test, data_train, data_test, label_train, label_test = user_id[0:n_train], user_id[n_train:], data_set[0:n_train, :], data_set[n_train:, :], label[0:n_train], label[n_train:]
    return user_id_train, user_id_test, data_train, data_test, label_train, label_test


def list_cut(continue_value, cut_threshold):
    """
    将连续值的一列list, 转化为分段label,主要用于 将连续型y值转化为分类标签
    :param continue_value: 输入需要进行离散化的一维数组[0,0,2,4,14,17,19,31]
    :param cut_threshold: 输入分段阈值 如[0,10,20,30]
    :return:
    """
    continue_value = pd.Series(continue_value.astype('float64'))
    segment_matrix = pd.cut(continue_value, cut_threshold)
    segment_matrix = np.asarray(pd.get_dummies(segment_matrix))
    segment_value = np.dot(segment_matrix, np.asarray(cut_threshold[1:]))
    return np.asarray(segment_value, dtype='int')


def train_mat_label_encoding(str_mat):

    """
    :param str_mat: 字符型分类变量矩阵
    :return: 整型分类变量矩阵
    """

    num_mat = []
    le = []
    features = np.transpose(np.asarray(str_mat))
    for i, f in enumerate(features):
        # print 'Training distinct x_label',set(f),'\n'
        le.append(preprocessing.LabelEncoder().fit(f))
        num_f = list(le[i].transform(f))
        num_mat.append(num_f)
    num_mat = np.transpose(num_mat)
    return le, num_mat


def test_mat_label_encoding(label_encoding_trained, str_mat):

    """
    使用训练集分段变量的编码序列,对测试集或预测集进行编码
    :param label_encoding_trained:
    :param str_mat: 字符型分类变量矩阵
    :return: 整型分类变量矩阵
    """
    num_mat = []
    le = label_encoding_trained
    features = np.transpose(np.asarray(str_mat))
    for i, f in enumerate(features):
        print 'Processing the ' + str(i + 1) + 'X_label_Dimension ...'
        # print 'Predict distinct x_label',set(f),'\n'
        num_f = list(le[i].transform(f))

        num_mat.append(num_f)
    num_mat = np.transpose(num_mat)
    return num_mat


def save_pickle_dump(model_object, file_name):
    """
    存储训练过程的参数对象
    :param model_object: 需存储的对象、变量
    :param file_name: pickle文件名
    :return:
    """
    with open(file_name, 'wb') as f:
        cPickle.dump(model_object, f)

