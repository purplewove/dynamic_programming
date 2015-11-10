from collections import namedtuple
from enum import Enum
'''
Created on Nov 10, 2015

@author: templetonc
'''

Cell = namedtuple("Cell", "cost parent")

class Edits(Enum):
    MATCH = 0
    INSERT = 1
    DELETE = 2

class Editor():
    def __init__(self, string1, string2):
        self.p = string1
        self.t = string2
        self.table = []
        
    def __iter__(self):
        self.table.append([j for j in range(len(self.t))])
        for i in len(self.p):
            self.table.append([i])
            for j in len(self.t):
                self.table.append(self.__cell__(i,j))
                    
    def __cell__(self, i, j):
        costs = {}
        costs[Edits.MATCH] = self.table[i-1, j-1] + self.__match__(i, j)
        costs[Edits.INSERT] = self.table[i, j-1] + self.__indel__(j)
        costs[Edits.DELETE] = self.table[i-1, j] + self.__indel__(i)
        cost = costs[Edits.MATCH]
        parent = Edits.Match
        for edit_type in list(Edits):
            if costs[edit_type] < cost:
                cost = costs[edit_type]
                parent = edit_type
        return Cell(cost, parent)
     
