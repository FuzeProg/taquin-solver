#!/usr/bin/env python
# _*_ coding: utf8 _*_
#
# solver.py: class for the solver of taquin game.
#

__author__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__copyright__ = "Copyright 2018, FuzeProg"
__credits__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__version__ = "1.0.1"
__maintainer__ = ["Anthony MARECHAL", "Ombeline MOZDZIERZ"]
__email__ = ["anthony.marechal@etu.uphf.fr", "ombeline.mozdzierz@etu.uphf.fr"]
__status__ = "In product"

from math import sqrt

class Solver:

    def __init__(self, taquin):
        self.openList = []
        self.closedList = []
        self.solutions = []

        self.initialState = taquin
        self.size = len(taquin)
        
    '''
    Find solutions for any size of grid
    :return list of solutions possibles around the empty case
    '''
    def find_solutions(self, taquin):
        l_size = int(sqrt(self.size))
        self.solutions.clear()
        emptyCase = taquin.index(0)

        if 0 <= (emptyCase - 1) <= self.size and emptyCase % l_size:
            self.solutions.append(self.initialState[emptyCase - 1])
        if 0 <= (emptyCase + 1) <= self.size and emptyCase % l_size != l_size - 1:
            self.solutions.append(self.initialState[emptyCase + 1])
        if 0 <= (emptyCase - l_size) <= self.size and emptyCase >= l_size:
            self.solutions.append(self.initialState[emptyCase - l_size])
        if 0 <= (emptyCase + l_size) <= self.size and emptyCase <= l_size:
            self.solutions.append(self.initialState[emptyCase + l_size])


    '''
    Check if case is in list
    '''
    def check_statment(self, case):
        if case in self.solutions:
            return True
        return False

