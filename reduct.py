# -*- coding: utf-8 -*-

import operator
import pandas
from collections import Counter


class Reduct(object):
    def __init__(self, file_path, decision_num=1, precision=[0, 1e-7, 0]):
        """
        基于知识粒度的经典启发式属性约简算法
        :param file_path: csv文件路径
        :param decision_num: 决策属性个数,默认为1
        :param precision: 算法一中三个可能的参数(精度)
        """
        '''信息系统,包含条件属性集和决策属性集'''
        self.data = pandas.read_csv(file_path)
        '''信息系统决策属性数'''
        self.decision_num = decision_num
        '''算法一中三个可能的参数(精度)'''
        self.precision = precision
        '''属性名,不含决策属性'''
        self.attributes_list = list(self.data)
        '''对象数'''
        self.objects_num = len(self.data)
        '''属性个数，含决策属性'''
        self.attributes_num = len(self.attributes_list)
        '''约简集下标'''
        self.reduct_list = list()
        '''决策属性集'''
        self.decisions_data = None
        '''条件属性集'''
        self.conditions_data = None
        '''初始化函数'''
        self.init_data()

    def init_data(self):
        """
        :return:
        """
        """切取决策属性"""
        start_index = self.attributes_num - self.decision_num
        index = list(range(start_index, self.attributes_num))
        self.decisions_data = self.data.iloc[:, index]
        """条件属性集"""
        index = list(range(start_index))
        self.conditions_data = self.data.iloc[:, index]

    def gain_granularity(self, frame):
        """
        https://blog.csdn.net/Dr_Guo/article/details/89670842
        res6_test = res6.groupby(['user_id', 'cate', 'shop_id']).size().sort_values(ascending=False)
        获取一个 DataFrame 的知识粒度
        :param frame:
        :return:
        """

    def gain_reduct(self):
        """
        属性约简过程
        :return:
        """
