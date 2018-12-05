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


def afficher_taquin(l_case):
    print("   --- --- ---")
    print("  |", l_case[0], "|", l_case[1], "|", l_case[2], "|")
    print("   --- --- ---")
    print("  |", l_case[3], "|", l_case[4], "|", l_case[5], "|")
    print("   --- --- ---")
    print("  |", l_case[6], "|", l_case[7], "|", l_case[8], "|")
    print("   --- --- ---")
    print(" ")


def echanger_cases(case1, case2, l_case):
    if (case1 == 0 and case2 == 1) or (case1 == 1 and case2 == 0):

        l_case[0], l_case[1] = l_case[1], l_case[0]

    elif (case1 == 1 and case2 == 2) or (case1 == 2 and case2 == 1):

        l_case[1], l_case[2] = l_case[2], l_case[1]

    elif (case1 == 3 and case2 == 4) or (case1 == 4 and case2 == 3):

        l_case[3], l_case[4] = l_case[4], l_case[3]

    elif (case1 == 4 and case2 == 5) or (case1 == 5 and case2 == 4):

        l_case[4], l_case[5] = l_case[5], l_case[4]

    elif (case1 == 6 and case2 == 7) or (case1 == 7 and case2 == 6):

        l_case[6], l_case[7] = l_case[7], l_case[6]

    elif (case1 == 7 and case2 == 8) or (case1 == 8 and case2 == 7):

        l_case[7], l_case[8] = l_case[8], l_case[7]

    elif (case1 == 0 and case2 == 3) or (case1 == 3 and case2 == 0):

        l_case[0], l_case[3] = l_case[3], l_case[0]

    elif (case1 == 3 and case2 == 6) or (case1 == 6 and case2 == 3):

        l_case[3], l_case[6] = l_case[6], l_case[3]

    elif (case1 == 1 and case2 == 4) or (case1 == 4 and case2 == 1):

        l_case[1], l_case[4] = l_case[4], l_case[1]

    elif (case1 == 4 and case2 == 7) or (case1 == 7 and case2 == 4):

        l_case[4], l_case[7] = l_case[7], l_case[4]

    elif (case1 == 2 and case2 == 5) or (case1 == 5 and case2 == 2):

        l_case[2], l_case[5] = l_case[5], l_case[2]

    elif (case1 == 5 and case2 == 8) or (case1 == 8 and case2 == 5):

        l_case[5], l_case[8] = l_case[8], l_case[5]


def trouve_num(l_case):
    case_zero = l_case.index(0)
    taille_list = len(l_case)
    taille_ligne = int(sqrt(len(l_case)))
    list_num = []
        
    if 0 <= (case_zero-1) <= taille_list and case_zero % taille_ligne:
        list_num.append(l_case[case_zero - 1])
    if 0 <= (case_zero+1) <= taille_list and case_zero % taille_ligne != taille_ligne-1:
        list_num.append(l_case[case_zero + 1])
    if 0 <= (case_zero-taille_ligne) <= taille_list and case_zero >= taille_ligne:
        list_num.append(l_case[case_zero - taille_ligne])
    if 0 <= (case_zero+taille_ligne) <= taille_list and case_zero <= taille_list:
        list_num.append(l_case[case_zero + taille_ligne])

    print(list_num)
