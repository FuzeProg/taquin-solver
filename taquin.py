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

    def __len__(self):
        return len(self.taquin)

    def index(self, index):
        return self.taquin.index(index)

    def __getitem__(self, item):
        return self.taquin[item]

    '''
    Display the grid
    :return nothing
    '''

    def display(self):
        ligne_size = int(sqrt(len(self.taquin)))
        d = Design(ligne_size, self.taquin)

        d.ligne()
        for i in range(0, ligne_size):
            d.bloc()
            d.ligne()

    '''
    
    '''
    def switch(self, case_zero, case_numero):

        if (case_zero == 0 and case_numero == 1) or (case_zero == 1 and case_numero == 0):
            self.taquin[0], self.taquin[1] = self.taquin[1], self.taquin[0]
        elif (case_zero == 1 and case_numero == 2) or (case_zero == 2 and case_numero == 1):
            self.taquin[1], self.taquin[2] = self.taquin[2], self.taquin[1]
        elif (case_zero == 3 and case_numero == 4) or (case_zero == 4 and case_numero == 3):
            self.taquin[3], self.taquin[4] = self.taquin[4], self.taquin[3]
        elif (case_zero == 4 and case_numero == 5) or (case_zero == 5 and case_numero == 4):
            self.taquin[4], self.taquin[5] = self.taquin[5], self.taquin[4]
        elif (case_zero == 6 and case_numero == 7) or (case_zero == 7 and case_numero == 6):
            self.taquin[6], self.taquin[7] = self.taquin[7], self.taquin[6]
        elif (case_zero == 7 and case_numero == 8) or (case_zero == 8 and case_numero == 7):
            self.taquin[7], self.taquin[8] = self.taquin[8], self.taquin[7]

        elif (case_zero == 0 and case_numero == 3) or (case_zero == 3 and case_numero == 0):
            self.taquin[0], self.taquin[3] = self.taquin[3], self.taquin[0]
        elif (case_zero == 3 and case_numero == 6) or (case_zero == 6 and case_numero == 3):
            self.taquin[3], self.taquin[6] = self.taquin[6], self.taquin[3]
        elif (case_zero == 1 and case_numero == 4) or (case_zero == 4 and case_numero == 1):
            self.taquin[1], self.taquin[4] = self.taquin[4], self.taquin[1]
        elif (case_zero == 4 and case_numero == 7) or (case_zero == 7 and case_numero == 4):
            self.taquin[4], self.taquin[7] = self.taquin[7], self.taquin[4]
        elif (case_zero == 2 and case_numero == 5) or (case_zero == 5 and case_numero == 2):
            self.taquin[2], self.taquin[5] = self.taquin[5], self.taquin[2]
        elif (case_zero == 5 and case_numero == 8) or (case_zero == 8 and case_numero == 5):
            self.taquin[5], self.taquin[8] = self.taquin[8], self.taquin[5]


