# -*- coding: utf-8 -*-

import os
import csv
import pandas

"""
数据的预处理：
根据txt文件的绝对路径和txt文件内容的分隔符,手动添加属性列名,将txt文件转化为 同一路径下 的csv文件
在进行下一步操作之前,必须保证数据的正确性
首先必须是正常的csv文件,文件的编码为utf-8
在csv文件中
第一行是属性列名,最后一列是标签,其余列是特征
特征的属性值必须是整数,浮点数,字符(串)
不应该有缺失属性值,即为完备数据集,当含有字符(串)时,一定要保证编码,以及是否完整读到DataFrame里面
"""


class DealData(object):
    def __init__(self, path, separator, list_name):
        """
        :param path: txt文件的绝对路径(str)
        :param separator: txt文件内容之间的分隔符(str)
        :param list_name: 每个列的属性名(list)
        """
        '''txt文件绝对路径'''
        self.file_path = path
        '''文件内容之间的分隔符'''
        self.separator = separator
        '''每个属性的名称'''
        self.list_name = list_name

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

    def mine_data(self):
        _path, shot_name, extension = self.gain_extension()
        '''生成的csv文件的完整路径'''
        new_path = _path + '/' + shot_name + '.csv'
        new_file = open(new_path, 'w+', newline='')
        writer = csv.writer(new_file)
        '''先将列名写入'''
        writer.writerow(self.list_name)
        data = open(self.file_path)
        lines = data.readlines()
        for index in range(len(lines)):
            lines[index] = lines[index].strip('\n')
            lines[index] = lines[index].strip('"')
            line = lines[index].split(self.separator)
            writer.writerow(line)
        data.close()
        new_file.close()
        self.file_path = new_path

    def standard_data(self):
        data = pandas.read_table(
            self.file_path, sep=self.separator, names=self.list_name)
        _path, shot_name, extension = self.gain_extension()
        '''生成的csv文件的完整路径'''
        new_path = _path + '/' + shot_name + '.csv'
        data.to_csv(new_path, index=0)
        self.file_path = new_path
