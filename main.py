# -*- coding: utf-8 -*-

from reduct import Reduct
from multiReduct import MReduct
from DealData import DealData
from Result import Result

"""
connect-4
"""


def connect4_deal():
    path = "data_set/connect-4/connect-4.txt"
    separator = ","
    list_name = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16',
                 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27', 'A28', 'A29', 'A30',
                 'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37', 'A38', 'A39', 'A40', 'A41', 'A42', "D"]
    d = DealData(path, separator, list_name)
    d.standard_data()


def connect4_split():
    path = "data_set/connect-4/connect-4.csv"
    rate = 0.8
    attributes_num = list()
    Result(path, rate, attributes_num)


def connect4_reduct():
    """
    已经处理数据,注释前两个函数
    :return:
    """
    # connect4_deal()
    # connect4_split()
    path = "data_set/connect-4/connect-4_train.csv"
    # r = Reduct(path)
    # r.gain_reduct()
    '''['A1', 'A19', 'A37', 'A7', 'A31', 'A14', 'A8', 'A25', 'A2', 'A13', 'A38', 'A20', 'A32', 'A26', 'A15', 'A9', 'A3', 'A21', 'A39', 'A33', 'A27', 'A16', 
    'A10', 'A4', 'A22', 'A34', 'A28', 'A41']'''
    # print(r.reduct_list)
    rm = MReduct(path, 3)
    rm.gain_multi_reduct()
    print(rm.reduct_all_dict)


"""

"""

if __name__ == "__main__":
    # connect4_reduct()
    p = "data.csv"
    r = MReduct(p)
    r.gain_multi_reduct()
    print(r.reduct_all_dict)
    print(r.reduct_all_list)
    # L = {0: ['b'], 1: ['f'], 2: ['a']}
    # l = L[0]
    # for i in range(1, 3):
    #     l = list(set(l) ^ (set(L[i])))
    # print(l)
