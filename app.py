#!/usr/bin/env python3
# _*_ coding: utf8 _*_
#
# app.py: play the game
#

__author__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__copyright__ = "Copyright 2018, FuzeProg"
__credits__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__version__ = "1.0.1"
__maintainer__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__email__ = ["anthony.marechal@etu.uphf.fr", "ombeline.mozdzierz@etu.uphf.fr"]
__status__ = "In product"

from taquin import Taquin as t
from solver import Solver as s


size = 3
size = size*size
unsolved = t('unsolved', size)
solved = t('solved', size)
solutions = s(unsolved)

while (True):
    unsolved.display()
    solutions.find_solutions()
    print("Liste des solutions disponibles : ", solutions.solutions)
    numero = int(input("Entrez une des solutions disponibles : "))

    if solutions.check_statment(numero):
        case_zero = unsolved.taquin.index(0)
        case_numero = unsolved.taquin.index(numero)
        unsolved.switch(case_zero, case_numero)
        print("La case a bien été déplacée.")
        input("Press any key to continue ...")
    else:
        print("Saisie incorrecte")
        input("Press any key to continue ...")
