#!/usr/bin/env python3
# _*_ coding: utf8 _*_
#
# design.py: graphics
#

__author__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__copyright__ = "Copyright 2018, FuzeProg"
__credits__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__version__ = "1.0.1"
__maintainer__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__email__ = ["anthony.marechal@etu.uphf.fr", "ombeline.mozdzierz@etu.uphf.fr"]
__status__ = "In product"

class Design:
    
    def __init__(self, ligne_size, taquin):
        self.ligne_size = ligne_size
        self.taquin = taquin
    
    def ligne(self):

        for i in range(0, self.ligne_size):
            if i == 0:
                print("+", end='')
            for j in range(0, self.ligne_size):
                print("-", end='')
                if j == self.ligne_size - 1 and i == self.ligne_size - 1:
                    print("+")
                else:
                    if j == self.ligne_size - 1:
                        print("+", end='')

    def bloc(self, k):
        print("|", end='')

        for j in range(0, self.ligne_size):
            print("", self.taquin[k], end='')
            for l in range(0, (self.ligne_size - 1) - len(str(self.taquin[k]))):
                print(" ", end='')
            if j == self.ligne_size - 1:
                print("|")
            else:
                print("|", end='')
            k = k + 1
        return k