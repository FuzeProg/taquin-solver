#!/usr/bin/env python3
# _*_ coding: utf8 _*_
#
# taquin.py: initial game
#

__author__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__copyright__ = "Copyright 2018, FuzeProg"
__credits__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__version__ = "1.0.1"
__maintainer__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__email__ = ["anthony.marechal@etu.uphf.fr", "ombeline.mozdzierz@etu.uphf.fr"]
__status__ = "In product"

import random
from math import sqrt
from design import Design

class Taquin:

    def __init__(self, state, size):
        self.state = state
        self.taquin = []

        if state == 'unsolved':
            i = 0
            while i < size:
                case = random.randrange(0, size)
                if case not in self.taquin:
                    self.taquin.append(case)
                    i = i+1

        elif state == 'solved':
            i = 0
            while i < size:
                self.taquin.append(i)
                i = i+1

    '''
    Display the grid
    :return nothing
    '''

    def display(self):
        k = 0
        ligne_size = int(sqrt(len(self.taquin)))
        d = Design(ligne_size, self.taquin)

        d.ligne()
        for i in range(0, ligne_size):
            k = d.bloc(k)
            d.ligne()

    '''
    Switch the empty case with an other case
    :return nothing
    '''
    def switch(self, emptyCase, case):

        if (emptyCase == 0 and case == 1) or (emptyCase == 1 and case == 0):
            self.taquin[0], self.taquin[1] = self.taquin[1], self.taquin[0]
        elif (emptyCase == 1 and case == 2) or (emptyCase == 2 and case == 1):
            self.taquin[1], self.taquin[2] = self.taquin[2], self.taquin[1]
        elif (emptyCase == 3 and case == 4) or (emptyCase == 4 and case == 3):
            self.taquin[3], self.taquin[4] = self.taquin[4], self.taquin[3]
        elif (emptyCase == 4 and case == 5) or (emptyCase == 5 and case == 4):
            self.taquin[4], self.taquin[5] = self.taquin[5], self.taquin[4]
        elif (emptyCase == 6 and case == 7) or (emptyCase == 7 and case == 6):
            self.taquin[6], self.taquin[7] = self.taquin[7], self.taquin[6]
        elif (emptyCase == 7 and case == 8) or (emptyCase == 8 and case == 7):
            self.taquin[7], self.taquin[8] = self.taquin[8], self.taquin[7]

        elif (emptyCase == 0 and case == 3) or (emptyCase == 3 and case == 0):
            self.taquin[0], self.taquin[3] = self.taquin[3], self.taquin[0]
        elif (emptyCase == 3 and case == 6) or (emptyCase == 6 and case == 3):
            self.taquin[3], self.taquin[6] = self.taquin[6], self.taquin[3]
        elif (emptyCase == 1 and case == 4) or (emptyCase == 4 and case == 1):
            self.taquin[1], self.taquin[4] = self.taquin[4], self.taquin[1]
        elif (emptyCase == 4 and case == 7) or (emptyCase == 7 and case == 4):
            self.taquin[4], self.taquin[7] = self.taquin[7], self.taquin[4]
        elif (emptyCase == 2 and case == 5) or (emptyCase == 5 and case == 2):
            self.taquin[2], self.taquin[5] = self.taquin[5], self.taquin[2]
        elif (emptyCase == 5 and case == 8) or (emptyCase == 8 and case == 5):
            self.taquin[5], self.taquin[8] = self.taquin[8], self.taquin[5]
