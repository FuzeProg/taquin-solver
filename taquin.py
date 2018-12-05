#!/usr/bin/env python3
# _*_ coding: utf8 _*_
#
# taquin.py: display the game
# Sources :
#           Initial code without AI : https://www.ilemaths.net/sujet-taquin-en-python-771297.html
#

__author__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__copyright__ = "Copyright 2018, FuzeProg"
__credits__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__version__ = "1.0.1"
__maintainer__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__email__ = ["anthony.marechal@etu.uphf.fr", "ombeline.mozdzierz@etu.uphf.fr"]
__status__ = "In product"

from math import sqrt

def display(l_case):
    print("   --- --- ---")
    print("  |", l_case[0], "|", l_case[1], "|", l_case[2], "|")
    print("   --- --- ---")
    print("  |", l_case[3], "|", l_case[4], "|", l_case[5], "|")
    print("   --- --- ---")
    print("  |", l_case[6], "|", l_case[7], "|", l_case[8], "|")
    print("   --- --- ---")
    print(" ")


def switch(case_zero, case_numero, l_case):

    # echanges horizontaux
    if (case_zero == 0 and case_numero == 1) or (case_zero == 1 and case_numero == 0):

        l_case[0], l_case[1] = l_case[1], l_case[0]

    elif (case_zero == 1 and case_numero == 2) or (case_zero == 2 and case_numero == 1):

        l_case[1], l_case[2] = l_case[2], l_case[1]

    elif (case_zero == 3 and case_numero == 4) or (case_zero == 4 and case_numero == 3):

        l_case[3], l_case[4] = l_case[4], l_case[3]

    elif (case_zero == 4 and case_numero == 5) or (case_zero == 5 and case_numero == 4):

        l_case[4], l_case[5] = l_case[5], l_case[4]

    elif (case_zero == 6 and case_numero == 7) or (case_zero == 7 and case_numero == 6):

        l_case[6], l_case[7] = l_case[7], l_case[6]

    elif (case_zero == 7 and case_numero == 8) or (case_zero == 8 and case_numero == 7):

        l_case[7], l_case[8] = l_case[8], l_case[7]

    # echanges verticaux
    elif (case_zero == 0 and case_numero == 3) or (case_zero == 3 and case_numero == 0):

        l_case[0], l_case[3] = l_case[3], l_case[0]

    elif (case_zero == 3 and case_numero == 6) or (case_zero == 6 and case_numero == 3):

        l_case[3], l_case[6] = l_case[6], l_case[3]

    elif (case_zero == 1 and case_numero == 4) or (case_zero == 4 and case_numero == 1):

        l_case[1], l_case[4] = l_case[4], l_case[1]

    elif (case_zero == 4 and case_numero == 7) or (case_zero == 7 and case_numero == 4):

        l_case[4], l_case[7] = l_case[7], l_case[4]

    elif (case_zero == 2 and case_numero == 5) or (case_zero == 5 and case_numero == 2):

        l_case[2], l_case[5] = l_case[5], l_case[2]

    elif (case_zero == 5 and case_numero == 8) or (case_zero == 8 and case_numero == 5):

        l_case[5], l_case[8] = l_case[8], l_case[5]


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
