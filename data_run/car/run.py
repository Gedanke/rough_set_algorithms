# -*- coding: utf-8 -*-

from reduct import Reduct
from multiReduct import MReduct
from DealData import DealData
from Result import Result
import time

"""
car:
n_entradas= 6
n_clases= 4
n_arquivos= 1
fich1= car_R.dat
n_patrons1= 1728
n_patrons_entrena= 864
n_patrons_valida= 864
n_conxuntos= 1

数据集信息：
1728行,7列
"""

list_name = [
    "A1", "A2", "A3", "A4", "A5", "A6", "D"
]
pre_path = "../../data_set/car/"


def deal():
    path = pre_path + "car.txt"
    separator = " "
    global list_name
    d = DealData(path, separator, list_name)
    d.standard_data()


def split():
    path = pre_path + "car.csv"
    rate = 0.8
    attributes_num = list()
    Result(path, rate, attributes_num)


def result():
    train_path = pre_path + "car_train.csv"
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


if __name__ == "__main__":
    # deal()
    # split()
    result()
