import numpy as np
from utils.game_utils import *


class Board(object):

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.state = []
        self.state = np.ones((rows, columns)) * DEFAULT_VALUE


    def getState(self):
        return self.state
    

    def getValue(self, location):
        return self.state[location[0], location[1]]
    

    def setValue(self, location, value):
        self.state[location[0], location[1]] = value


    def getStart(self):
        for row in range(self.state.shape[0]):
            for col in range(self.state.shape[1]):
                if self.state[row, col] == START_VALUE:
                    return np.asarray([row, col])
                

    def getEnd(self):
        for row in range(self.state.shape[0]):
            for col in range(self.state.shape[1]):
                if self.state[row, col] == END_VALUE:
                    return np.asarray([row, col])
                

    def hasStart(self):
        for row in range(self.state.shape[0]):
            for col in range(self.state.shape[1]):
                if self.state[row, col] == START_VALUE:
                    return True
        return False


    def hasEnd(self):
        for row in range(self.state.shape[0]):
            for col in range(self.state.shape[1]):
                if self.state[row, col] == END_VALUE:
                    return True
        return False
                

    def getPath(self, start, stop):
        print(f"Finding path from: {start} -> {stop}")


    def clearExploredSquares(self):
        for row in range(self.state.shape[0]):
            for col in range(self.state.shape[1]):
                if self.state[row, col] == EXPLORED_VALUE:
                    self.state[row, col] = DEFAULT_VALUE


    def getLegalMoves(self, location):
        legal_moves = []
        for move in MOVE_DIRECTIONS:
            temp = location + move
            if temp[0] > -1 and temp[1] > -1 and temp[0] < NUM_ROWS and temp[1] < NUM_COLUMNS:
                if self.getValue(temp) != OBSTACLE_VALUE and self.getValue(temp) != EXPLORED_VALUE:
                    legal_moves.append(temp)
        return legal_moves

