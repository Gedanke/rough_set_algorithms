# -*- coding: utf-8 -*-

import operator
import pandas


class Reduct(object):
    def __init__(self, file_path, decision_num=1, precision=None):
        """
        基于知识粒度的经典启发式属性约简算法
        :param file_path: csv文件路径
        :param decision_num: 决策属性个数,默认为 1
        :param precision: 算法一中三个可能的参数(精度)
        """
        if precision is None:
            precision = [0, 1e-7, 0]
        '''信息系统,包含条件属性集和决策属性集'''
        self.data = pandas.read_csv(file_path)
        '''信息系统决策属性数'''
        self.decision_num = decision_num
        '''算法一中三个可能的参数(精度)'''
        self.precision = precision
        '''属性名,含决策属性'''
        self.conditions_decision_list = list(self.data)
        '''条件属性名,不含决策属性'''
        self.conditions_list = None
        '''约简集下标,含决策属性'''
        self.reduct_decision_list = list()
        '''约简集下标,不含决策属性'''
        self.reduct_list = list()
        '''对象数'''
        self.objects_num = len(self.data)
        '''属性个数，含决策属性'''
        self.attributes_num = len(self.conditions_decision_list)
        '''初始化函数'''
        self.init_data()

    def init_data(self):
        """
        初始化
        :return:
        """
        """
        在约简过程中,只添加属性名
        在内部属性重要度计算过程中:
        self.conditions_decision_list 相当于 C U D,C U D - {a}
        self.conditions_list 相当于 C,C - {a}
        在外部属性重要度计算过程中:
        self.reduct_decision_list 相当于 B U D,B U D - {a}
        self.reduct_list 相当于 B,B - {a}
        """
        index = self.attributes_num - self.decision_num
        self.conditions_list = self.conditions_decision_list[0:index]
        self.reduct_decision_list = self.conditions_decision_list[index:self.attributes_num]

    def gain_granularity(self, subscript):
        """
        https://blog.csdn.net/Dr_Guo/article/details/89670842
        获取一个 subscript 下标绝对的 DataFrame 的知识粒度
        :param subscript: 下标
        :return:
        """
        '''<class 'pandas.core.series.Series'>'''
        if len(subscript) == 0:
            return 0
        index = self.data.groupby(subscript).size()
        '''等价类内元素个数的列表,对其每个元素求平方后得到分子'''
        list_index = list(index)
        '''分子是各个等价类内元素的个数平方和,分母则是集合元素个数的平方'''
        molecule = sum(list(map(lambda num: num * num, list_index)))
        denominator = pow(self.objects_num, 2)
        return float(molecule / denominator)

    def gain_reduct(self):
        """
        属性约简过程
        :return:
        """
        """第一部分"""
        sub = self.gain_granularity(self.conditions_list) - self.gain_granularity(self.conditions_decision_list)
        '''遍历所有条件属性'''
        for a_j in self.conditions_list:
            '''此处可优化,暂时用该法,使用深拷贝的方式'''
            conditions_sub_aj = self.conditions_list[:]
            conditions_decision_sub_aj = self.conditions_decision_list[:]
            '''深拷贝后,从得到的副本上去除该条件属性'''
            conditions_sub_aj.remove(a_j)
            conditions_decision_sub_aj.remove(a_j)
            '''内部属性重要度'''
            result = self.gain_granularity(conditions_sub_aj) - self.gain_granularity(conditions_decision_sub_aj) - sub
            '''内部属性重要度值大于某一值认为其大于0'''
            if result > self.precision[0]:
                '''该元素加入约简集(不含决策属性)'''
                self.reduct_list.append(a_j)
                '''该元素加入约简集(含决策属性)'''
                self.reduct_decision_list.append(a_j)
        """第一部分"""
        """第二部分"""
        rules = self.conditions_list[:]
        '''求 C - B '''
        for a in self.reduct_list:
            rules.remove(a)
        '''差值大于某一值认为两者不相等'''
        while abs(self.gain_granularity(self.reduct_list) - self.gain_granularity(self.reduct_decision_list) - sub) >= \
                self.precision[1]:
            max_sig_outer = dict()
            for a_i in rules:
                pre_outer = self.gain_granularity(self.reduct_list) - self.gain_granularity(self.reduct_decision_list)
                '''使用深拷贝的方式'''
                reduct_add_ai = self.reduct_list[:]
                reduct_decision_add_ai = self.reduct_decision_list[:]
                '''深拷贝后,从得到的副本上增加该条件属性'''
                reduct_add_ai.append(a_i)
                reduct_decision_add_ai.append(a_i)
                '''外部属性重要度'''
                next_outer = self.gain_granularity(reduct_add_ai) - self.gain_granularity(reduct_decision_add_ai)
                max_sig_outer[a_i] = pre_outer - next_outer
            '''选择 C - B 中最大的条件属性'''
            max_sig_outer = sorted(max_sig_outer.items(), key=operator.itemgetter(1), reverse=True)
            a0 = max_sig_outer[0][0]
            '''该元素加入约简集(不含决策属性)'''
            self.reduct_list.append(a0)
            '''该元素加入约简集(含决策属性)'''
            self.reduct_decision_list.append(a0)
            '''原有的 C - B 中应该去除该条件属性'''
            rules.remove(a0)
        """第二部分"""
        """第三部分"""
        for a_i in self.reduct_list:
            '''深拷贝后,从得到的副本上去除该条件属性'''
            reduct_sub_ai = self.reduct_list[:]
            reduct_decision_sub_ai = self.reduct_decision_list[:]
            reduct_sub_ai.remove(a_i)
            reduct_decision_sub_ai.remove(a_i)
            '''差值在一定范围内认为是相等的'''
            if abs(self.gain_granularity(reduct_sub_ai) - self.gain_granularity(
                    reduct_decision_sub_ai) - sub) <= self.precision[2]:
                '''该元素移除约简集(不含决策属性)'''
                self.reduct_list.remove(a_i)
                '''该元素移除约简集(含决策属性)'''
                self.reduct_decision_list.remove(a_i)
        """第三部分"""
