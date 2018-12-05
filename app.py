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
import random



l_case = []
l_found = []
i = 0

while i < 9:
    chiffre = random.randrange(0, 9)

    if chiffre not in l_case:
        l_case.append(chiffre)
        i += 1
print(l_case)
while (True):
    afficher_taquin(l_case)
    trouve_num(l_case)
    numero = int(input(" Entrez le numero de la piece a bouger de 1 a 8 : "))

    if check_statment(numero, l_found):
        case_zero = l_case.index(0)
        case_numero = l_case.index(numero)
        switch(case_zero, case_numero, l_case)
        print("La case a bien été déplacée.")

