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


def find_solutions(l_case):
    
    case_zero = l_case.index(0)
    list_size = len(l_case)
    line_size = int(sqrt(len(l_case)))
    list_num = []

    if 0 <= (case_zero - 1) <= list_size and case_zero % line_size:
        list_num.append(l_case[case_zero - 1])
    if 0 <= (case_zero + 1) <= list_size and case_zero % line_size != line_size - 1:
        list_num.append(l_case[case_zero + 1])
    if 0 <= (case_zero - line_size) <= list_size and case_zero >= line_size:
        list_num.append(l_case[case_zero - line_size])
    if 0 <= (case_zero + line_size) <= list_size and case_zero <= list_size:
        list_num.append(l_case[case_zero + line_size])

    return list_num


def check_statment(case, list):

    for i in range(0, len(list)):
        if list[i] == case:
            return True
    return False
