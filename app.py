#!/usr/bin/env python3
# _*_ coding: utf8 _*_
#
# app.py: play the game played by your own
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

GAME = 3

size = 3
size = size*size
taquin = t(size, GAME)
solutions = s(taquin, GAME)

while (taquin.taquinUnsolved != taquin.taquinSolved):
    case_zero = taquin.taquinUnsolved.index(0)
    solutions.set_emptyCase(case_zero)
    taquin.display()
    #taquin.displaySolved()
    solutions.find_solutions()
    print("Liste des solutions disponibles : ", solutions.solutions)
    numero = int(input("Entrez une des solutions disponibles : "))

    if solutions.check_statment(numero):
        case_numero = taquin.taquinUnsolved.index(numero)
        taquin.switch(case_zero, case_numero)
        print("La case a bien été déplacée.")
    else:
        print("Saisie incorrecte")
