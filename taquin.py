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

    def __init__(self, size):
        self.taquinUnsolved = []
        self.taquinSolved = []
        self.size = size
        self.ligne_size = int(sqrt(self.size))

        i = 0
        while i < self.size:
            rand = random.randrange(0, self.size)
            if rand not in self.taquinUnsolved:
                self.taquinUnsolved.append(rand)
                self.taquinSolved.append(i)
                i = i+1

    '''
    Display the unsolved grid
    :return nothing
    '''

    def display(self):
        k = 0
        d = Design(self.ligne_size, self.taquinUnsolved)

        d.ligne()
        for i in range(0, self.ligne_size):
            k = d.bloc(k)
            d.ligne()

    '''
    Display the solved grid
    :return nothing
    '''

    def displaySolved(self):
        k = 0
        d = Design(self.ligne_size, self.taquinSolved)

        d.ligne()
        for i in range(0, self.ligne_size):
            k = d.bloc(k)
            d.ligne()

    '''
    Switch the empty case with an other case
    :return nothing
    '''
    def switch(self, emptyCase, case):
        if (case == emptyCase + 1) or (case == emptyCase - 1):
            self.taquinUnsolved[case], self.taquinUnsolved[emptyCase] = self.taquinUnsolved[emptyCase], self.taquinUnsolved[case]
        elif (case == emptyCase + self.ligne_size) or (case == emptyCase - self.ligne_size):
            self.taquinUnsolved[case], self.taquinUnsolved[emptyCase] = self.taquinUnsolved[emptyCase], self.taquinUnsolved[case]
