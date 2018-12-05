#!/usr/bin/env python
# _*_ coding: utf8 _*_
#
# Foobar.py: Description of what foobar does.
#

__author__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__copyright__ = "Copyright 2018, FuzeProg"
__credits__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__version__ = "1.0.1"
__maintainer__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__email__ = ["anthony.marechal@etu.uphf.fr", "ombeline.mozdzierz@etu.uphf.fr"]
__status__ = "In product"

from math import sqrt


def find_case(l_case):

    found = []
    index_zero = l_case.index(0)
    len_case = int(sqrt(len(l_case)))

    if index_zero == 0:
        found.append(l_case[(index_zero) + 1])
        found.append(l_case[(index_zero) + (len_case)])

    if index_zero == 1:
        found.append(l_case[(index_zero) - 1])
        found.append(l_case[(index_zero) + 1])
        found.append(l_case[(index_zero) + (len_case)])

    if index_zero == 2:
        found.append(l_case[(index_zero) - 1])
        found.append(l_case[(index_zero) + (len_case)])

    if index_zero == 3:
        found.append(l_case[(index_zero) - (len_case)])
        found.append(l_case[(index_zero) + 1])
        found.append(l_case[(index_zero) + (len_case)])

    if index_zero == 4:
        found.append(l_case[(index_zero) - (len_case)])
        found.append(l_case[(index_zero) - 1])
        found.append(l_case[(index_zero) + (len_case)])
        found.append(l_case[(index_zero) + 1])

    if index_zero == 5:
        found.append(l_case[(index_zero) - (len_case)])
        found.append(l_case[(index_zero) - 1])
        found.append(l_case[(index_zero) + (len_case)])

    if index_zero == 6:
        found.append(l_case[(index_zero) - (len_case)])
        found.append(l_case[(index_zero) + 1])

    if index_zero == 7:
        found.append(l_case[(index_zero) - (len_case)])
        found.append(l_case[(index_zero) - 1])
        found.append(l_case[(index_zero) + 1])

    if index_zero == 8:
        found.append(l_case[(index_zero) - (len_case)])
        found.append(l_case[(index_zero) - 1])

    return found


def check_statment(case, list):

    for i in range(0, len(list)):
        if list[i] == case:
            return True
    return False
