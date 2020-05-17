# -*- coding: utf-8 -*-

from reduct import Reduct
from multiReduct import MReduct
from DealData import DealData
from Result import Result
import time

"""
n_entradas= 21
n_clases= 2
n_arquivos= 1
fich1= mushroom_R.dat
n_patrons1= 8124
n_patrons_entrena= 4062
n_patrons_valida= 4062
n_conxuntos= 1

8124行,23列
"""

'''注意该数据第一列为标签'''
list_name = ['D', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16',
             'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A1']
pre_path = "../../data_set/mushroom/"


def deal():
    path = pre_path + "mushroom.txt"
    separator = ","
    d = DealData(path, separator, list_name)
    d.standard_data()
    '''手动在csv文件中替换第一行和最后一列'''


def split():
    train_path = pre_path + "mushroom.csv"
    rate = 0.8
    attributes_num = list()
    Result(train_path, rate, attributes_num)


def result():
    train_path = pre_path + "mushroom_train.csv"
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
    # split()
    result()
