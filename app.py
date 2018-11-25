#!/usr/bin/env python3
# _*_ coding: utf8 _*_
#
# Foobar.py: Description of what foobar does.
# Sources :
#           Initial code without AI : https://www.ilemaths.net/sujet-taquin-en-python-771297.html
#

__author__ = "Anthony MARECHAL"
__copyright__ = "Copyright 2018, FuzeProg"
__credits__ = ["Anthony MARECHAL"]
__version__ = "1.0.1"
__maintainer__ = "Anthony MARECHAL"
__email__ = "anthony.marechal@etu.uphf.fr"
__status__ = "In product"

# *******************************************************************************
# IMPORT ***********************************************************************
# *******************************************************************************

# module de generation de nombres aleatoires
import random



# *******************************************************************************
# DEF **************************************************************************
# *******************************************************************************

# -- afficher_taquin ----------------------------------------------------------
#
# Description  : affichage du Taquin
#
# Parameters   :
#
# Return       :
#
# Notes        :
#                   --- --- ---
#                  | 0 | 1 | 2 |
#                   --- --- ---
#                  | 3 | 4 | 5 |
#                   --- --- ---
#                  | 6 | 7 | 8 |
#                   --- --- ---
#
def afficher_taquin():
    print("   --- --- ---")
    print("  |", l_case[0], "|", l_case[1], "|", l_case[2], "|")
    print("   --- --- ---")
    print("  |", l_case[3], "|", l_case[4], "|", l_case[5], "|")
    print("   --- --- ---")
    print("  |", l_case[6], "|", l_case[7], "|", l_case[8], "|")
    print("   --- --- ---")
    print(" ")


# -- echanger_cases ----------------------------------------------------------
#
# Description  : echange de 2 cases
#
# Parameters   :
#
# Return       :
#
# Notes        : aucunes cases echangées si pas possible
#
def echanger_cases(case1, case2):
    # echanges horizontaux

    # 0 <-> 1 ?
    if (case1 == 0 and case2 == 1) or (case1 == 1 and case2 == 0):

        l_case[0], l_case[1] = l_case[1], l_case[0]

    # 1 <-> 2 ?
    elif (case1 == 1 and case2 == 2) or (case1 == 2 and case2 == 1):

        l_case[1], l_case[2] = l_case[2], l_case[1]

    # 3 <-> 4 ?
    elif (case1 == 3 and case2 == 4) or (case1 == 4 and case2 == 3):

        l_case[3], l_case[4] = l_case[4], l_case[3]

    # 4 <-> 5 ?
    elif (case1 == 4 and case2 == 5) or (case1 == 5 and case2 == 4):

        l_case[4], l_case[5] = l_case[5], l_case[4]

    # 6 <-> 7 ?
    elif (case1 == 6 and case2 == 7) or (case1 == 7 and case2 == 6):

        l_case[6], l_case[7] = l_case[7], l_case[6]

    # 7 <-> 8
    elif (case1 == 7 and case2 == 8) or (case1 == 8 and case2 == 7):

        l_case[7], l_case[8] = l_case[8], l_case[7]

    # echanges verticaux

    # 0 <-> 3 ?
    elif (case1 == 0 and case2 == 3) or (case1 == 3 and case2 == 0):

        l_case[0], l_case[3] = l_case[3], l_case[0]

    # 3 <-> 6 ?
    elif (case1 == 3 and case2 == 6) or (case1 == 6 and case2 == 3):

        l_case[3], l_case[6] = l_case[6], l_case[3]

    # 1 <-> 4 ?
    elif (case1 == 1 and case2 == 4) or (case1 == 4 and case2 == 1):

        l_case[1], l_case[4] = l_case[4], l_case[1]

    # 4 <-> 7 ?
    elif (case1 == 4 and case2 == 7) or (case1 == 7 and case2 == 4):

        l_case[4], l_case[7] = l_case[7], l_case[4]

    # 2 <-> 5 ?
    elif (case1 == 2 and case2 == 5) or (case1 == 5 and case2 == 2):

        l_case[2], l_case[5] = l_case[5], l_case[2]

    # 5 <-> 8
    elif (case1 == 5 and case2 == 8) or (case1 == 8 and case2 == 5):

        l_case[5], l_case[8] = l_case[8], l_case[5]


# *******************************************************************************
# MAIN *************************************************************************
# *******************************************************************************



# initialisation du Taquin ----------------------------------------------------

# liste vide par defaut
l_case = []

i = 0

while i < 9:

    # chiffre aleatoire de 0 a 8
    chiffre = random.randrange(0, 9)

    # deja eu ?
    if chiffre not in l_case:
        # non : on le garde
        l_case.append(chiffre)

        i += 1

# jeu -------------------------------------------------------------------------

while (True):

    # affichage du Taquin
    afficher_taquin()

    # saisie
    numero = int(input(" Entrez le numero de la piece a bouger de 1 a 8 : "))

    # numero valide ?
    if 1 <= numero and numero <= 8:
        # oui : recherche de la case contenant le zero
        case_zero = l_case.index(0)

        # recherche de la case contenant le numero
        case_numero = l_case.index(numero)

        # echange (si possible)
        echanger_cases(case_zero, case_numero)
