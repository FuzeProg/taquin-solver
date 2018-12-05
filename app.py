#!/usr/bin/env python3
# _*_ coding: utf8 _*_
#
# app.py: play the game
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

from taquin import *
from solver import *
import random


size = 9
unsolved = []
solutions = []
solved = []
i = 0

while i < size:
    chiffre = random.randrange(0, size)

    if chiffre not in unsolved:
        unsolved.append(chiffre)
        solved.append(i)
        i = i+1

print(unsolved)
print(solved)

while (True):
    afficher_taquin(l_case)
    trouve_num(l_case)
    numero = int(input(" Entrez le numero de la piece a bouger de 1 a 8 : "))

    if check_statment(numero, solutions):
        case_zero = unsolved.index(0)
        case_numero = unsolved.index(numero)
        switch(case_zero, case_numero, unsolved)
        print("La case a bien été déplacée.")

