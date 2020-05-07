# -*- coding: utf-8 -*-

from reduct import Reduct
from multiReduct import MReduct
from DealData import DealData
from Result import Result


def connect4_deal():
    path = "data_set/connect-4/connect-4.txt"
    separator = ","
    list_name = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16',
                 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27', 'A28', 'A29', 'A30',
                 'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37', 'A38', 'A39', 'A40', 'A41', 'A42', "D"]
    d = DealData(path, separator, list_name)
    d.standard_data()


def connect_4_split():
    path = "data_set/connect-4/connect-4.csv"
    rate = 0.8
    attributes_num = list()
    Result(path, rate, attributes_num)


def connect_4():
    path = "data_set/connect-4/connect-4_train.csv"
    r = Reduct(path)


if __name__ == "__main__":
    connect_4()
