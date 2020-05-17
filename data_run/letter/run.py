# -*- coding: utf-8 -*-

from reduct import Reduct
from multiReduct import MReduct
from DealData import DealData
from Result import Result
import time

"""
n_entradas= 16
n_clases= 26
n_arquivos= 1
fich1= letter_R.dat
n_patrons1= 20000
n_patrons_entrena= 10000
n_patrons_valida= 10000
n_conxuntos= 1

数据集信息：
20000行,16列
"""

'''注意该数据第一列为标签'''
list_name = ['D', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11',
             'A12', 'A13', 'A14', 'A15', 'A16', 'A1']
pre_path = "../../data_set/letter/"


def deal():
    path = pre_path + "letter.txt"
    separator = " "
    d = DealData(path, separator, list_name)
    d.standard_data()
    '''手动在csv文件中替换第一行和最后一列'''


def split():
    train_path = pre_path + "letter.csv"
    rate = 0.8
    attributes_num = list()
    Result(train_path, rate, attributes_num)


def result():
    train_path = pre_path + "letter_train.csv"
    t1 = time.time()
    r = Reduct(train_path)
    r.gain_reduct()
    print("r:", time.time() - t1)
    print(r.reduct_list)
    """"""
    t2 = time.time()
    rm = MReduct(train_path, 3)
    rm.gain_multi_reduct()
    print("rm:", time.time() - t2)
    print(rm.reduct_all_list)


"""

"""

if __name__ == "__main__":
    # deal()
    # split()
    result()
