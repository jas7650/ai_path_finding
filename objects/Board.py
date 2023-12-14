import numpy as np
from utils.game_utils import *


class Board(object):

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.state = np.ones((rows, columns))


    def getState(self):
        return self.state
    

    def getValue(self, row, column):
        return self.state[row, column]
    

    def setValue(self, row, column, value):
        self.state[row, column] = value


    def getStart(self):
        for row in range(self.state.shape[0]):
            for col in range(self.state.shape[1]):
                if self.state[row, col] == START_VALUE:
                    return row, col
                

    def getEnd(self):
        for row in range(self.state.shape[0]):
            for col in range(self.state.shape[1]):
                if self.state[row, col] == END_VALUE:
                    return row, col
