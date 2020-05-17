# -*- coding: utf-8 -*-

from reduct import Reduct
from multiReduct import MReduct
from DealData import DealData
from Result import Result
import time

"""
n_entradas= 42
n_clases= 2
n_arquivos= 1
fich1= connect-4_R.dat
n_patrons1= 67557
n_patrons_entrena= 33779
n_patrons_valida= 33778
n_conxuntos= 1

connect-4
"""

list_name = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16',
             'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27', 'A28', 'A29', 'A30',
             'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37', 'A38', 'A39', 'A40', 'A41', 'A42', "D"]
pre_path = "../../data_set/connect-4/"


def deal():
    path = pre_path + "connect-4.txt"
    separator = ","
    d = DealData(path, separator, list_name)
    d.standard_data()


def split():
    train_path = pre_path + "connect-4.csv"
    rate = 0.8
    attributes_num = list()
    Result(train_path, rate, attributes_num)


def result():
    train_path = pre_path + "connect-4_train.csv"
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
