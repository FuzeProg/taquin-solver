#!/usr/bin/env python3
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
import copy

class Solver:
    F, G, H = 0, 1, 2

    def __init__(self, taquin, GAME):
        self.openList = []
        self.closedList = []
        self.solutions = []

        self.finalState = taquin.taquinSolved
        self.initialState = taquin.taquinUnsolved
        self.emptyCase = taquin.taquinUnsolved.index(0)
        self.size = taquin.size
        self.l_size = int(sqrt(self.size))

        self.GAME = GAME

        self.openList.append([0, 0, 0, taquin.taquinUnsolved, None])
        
    '''
    Find solutions for any size of grid (without the solver)
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
        if 0 <= (self.emptyCase + l_size) <= self.size and self.emptyCase <= self.size-4:
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

        while len(self.openList) > 0 :
            node = self.openList.pop(0)
            taquin = node[self.GAME]

            if node[self.GAME] == self.finalState:
                return node

            for case in range(0, self.size):
                print(taquin)
                print("case = ", case)
                if case > 0 and taquin[case] == self.emptyCase:
                    new_node = copy.deepcopy(taquin)
                    new_node[case], new_node[self.emptyCase] = new_node[self.emptyCase], new_node[case]
                    g = node[self.G]+1
                    h = self.heuristic(new_node)
                    print("if 1 ", new_node)
                    if not new_node in self.closedList:
                        i = self.openList_index(new_node)
                        print("i = ", i)
                        print("g + h ", g+h)
                        if i == -1:
                            self.openList.append([g+h, g, h, new_node, node])
                        elif g+h < self.openList[i][self.F] :
                            self.openList[i] = [g+h, h, new_node, node]

                if case < self.size - 1 and taquin[case] == self.emptyCase:
                    new_node = copy.deepcopy(taquin)
                    new_node[case], new_node[self.emptyCase] = new_node[self.emptyCase], new_node[case]
                    print("if 2 ", new_node)
                    g = node[self.G] + 1
                    h = self.heuristic(new_node)
                    if not new_node in self.closedList:
                        i = self.openList_index(new_node)
                        print("i =", i)
                        print("g + h ", g+h)
                        if i == -1:
                            self.openList.append([g + h, g, h, new_node, node])
                        elif g+h < self.openList[i][self.F] :
                            self.openList[i] = [g + h, h, new_node, node]
            self.openList.sort()
        print(None)


    '''
    Define the heuristic for the solver
    :return summ of invalid cases
    '''
    def heuristic(self, taquin):
        i = 0

        for case in range(0, self.size):
            if taquin[case] != self.finalState[case]:
                i = i+1

        return i

    '''
    Give the index in the open list
    :return i, index asked in the open list
    '''
    def openList_index(self, taquin):
        for i in range(0, len(self.openList)):
            if self.openList[i][3] == taquin:
                return i
        return -1