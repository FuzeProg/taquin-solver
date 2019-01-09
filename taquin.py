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
from solver import Solver

class Taquin:
    FATHER = 4

    def __init__(self, size, GAME):
        self.taquinUnsolved = []
        self.taquinSolved = []
        self.size = size
        self.line_size = int(sqrt(size))

        self.GAME = GAME

        i = 0
        while i < size:
            rand = random.randrange(0, size)
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
        d = Design(self.line_size, self.taquinUnsolved)

        d.ligne()
        for i in range(0, self.line_size):
            k = d.bloc(k)
            d.ligne()

    '''
    Display the solved grid
    :return nothing
    '''
    def displaySolved(self):
        k = 0
        d = Design(self.line_size, self.taquinSolved)

        d.ligne()
        for i in range(0, self.line_size):
            k = d.bloc(k)
            d.ligne()

    def etatFini(self):
        print('n'.join( ''.join(str(i)) for i in self.taquinSolved))

    '''
    Switch the empty case with an other case
    :return nothing
    '''
    def switch(self, emptyCase, case):
        if (case == emptyCase + 1) or (case == emptyCase - 1):
            self.taquinUnsolved[case], self.taquinUnsolved[emptyCase] = self.taquinUnsolved[emptyCase], self.taquinUnsolved[case]
        elif (case == emptyCase + self.line_size) or (case == emptyCase - self.line_size):
            self.taquinUnsolved[case], self.taquinUnsolved[emptyCase] = self.taquinUnsolved[emptyCase], self.taquinUnsolved[case]

    def resolve(self):
        solver = Solver(self, self.GAME)
        solution = solver.resolve()
        if solution == None:
            print("Ce taquin ne peut pas être résolu.")
            return
        print("Solution trouvée :")

        L = []
        while solution[self.FATHER] != None:
            L.append(solution[self.FATHER][self.GAME])
            solution = solution[self.FATHER]
        L.reverse()

        for elem in L:
            print('n' + 'n'.join( ''.join(str(i)) for i in elem))

        self.etatFini()
