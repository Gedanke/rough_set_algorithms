# -*- coding: utf-8 -*-

from sklearn.preprocessing import MinMaxScaler
import os
import pandas


class Result(object):
    def __init__(self, path, rate, attributes_num):
        """
        :param path: 完全正确的csv文件绝对路径
        :param rate: 以该比例划分训练集和测试集
        :param attributes_num: 待归一化的特征,在属性约简中这个用的少
        """
        '''完全正确的csv文件绝对路径'''
        self.file_path = path
        '''以该比例划分训练集和测试集'''
        self.rate = rate
        '''全体数据集'''
        self.all_data = pandas.read_csv(self.file_path)
        '''待归一化的特征'''
        self.attributes_num = attributes_num
        '''训练集数据'''
        self.train_data = None
        '''训练集数据路径'''
        self.train_path = None
        '''测试集数据'''
        self.test_data = None
        '''测试集数据路径'''
        self.test_path = None
        '''所有样本的个数'''
        self.all_object_num = int(len(self.all_data))
        '''样本的属性数,包括了标签'''
        self.label_num = int(len(self.all_data.columns))
        '''划分训练集和测试集'''
        self.init_data()

    def gain_extension(self):
        """
        :return:
        @file_path : 返回文件路径
        @shot_name : 返回文件名
        @extension : 返回文件后缀
        """
        file_path, temp_filename = os.path.split(self.file_path)
        shot_name, extension = os.path.splitext(temp_filename)
        return file_path, shot_name, extension

    def init_data(self):
        """
        将self.all_data需要归一化处理的部分进行归一化处理
        使用DataFrame.sample函数：
        DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)
        n是选取的条数，frac是选取的比例，replace是可不可以重复选，weights是权重，random_state是随机种子，axis为0是选取行，为1是选取列。
        :return:
        """
        ss = MinMaxScaler()
        if len(self.attributes_num) != 0:
            self.all_data[self.attributes_num] = ss.fit_transform(self.all_data[self.attributes_num])
        self.train_data = self.all_data.sample(frac=self.rate, random_state=None, axis=0)
        self.test_data = self.all_data[~self.all_data.index.isin(self.train_data.index)]
        '''将数据写入csv文件中,与原文件同一路径,分别在文件名后加_train 和 _test'''
        _path, shot_name, extension = self.gain_extension()
        '''生成训练数据集的csv文件的完整路径'''
        '''生成测试数据集的csv文件的完整路径'''
        if _path != "":
            self.train_path = _path + '/' + shot_name + '_train' + '.csv'
            self.test_path = _path + '/' + shot_name + '_test' + '.csv'
        else:
            self.train_path = shot_name + '_train' + '.csv'
            self.test_path = shot_name + '_test' + '.csv'
        self.train_data.to_csv(self.train_path, index=False, sep=',')
        self.train_data = pandas.read_csv(self.train_path)
        self.test_data.to_csv(self.test_path, index=False, sep=',')
        self.test_data = pandas.read_csv(self.test_path)
