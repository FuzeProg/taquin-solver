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

        self.initialState = taquin.taquin
        self.emptyCase = taquin.taquin.index(0)
        self.size = len(taquin.taquin)
        
    '''
    Find solutions for any size of grid
    :return list of solutions possibles around the empty case
    '''
    def find_solutions(self):
        l_size = int(sqrt(self.size))
        self.solutions.clear()

        if 0 <= (self.emptyCase - 1) <= self.size and self.emptyCase % l_size:
            self.solutions.append(self.initialState[self.emptyCase - 1])
        if 0 <= (self.emptyCase + 1) <= self.size and self.emptyCase % l_size != l_size - 1:
            self.solutions.append(self.initialState[self.emptyCase + 1])
        if 0 <= (self.emptyCase - l_size) <= self.size and self.emptyCase >= l_size:
            self.solutions.append(self.initialState[self.emptyCase - l_size])
        if 0 <= (self.emptyCase + l_size) <= self.size and self.emptyCase <= l_size:
            self.solutions.append(self.initialState[self.emptyCase + l_size])

    '''
    Update the emptyCase during the game
    '''
    def set_emptyCase(self, emptyCase):
        self.emptyCase = emptyCase

    '''
    Check if a number is in the solutions list
    '''
    def check_statment(self, number):
        if number in self.solutions:
            return True
        return False

    def resolve(self):
        print('Solver is running...')
