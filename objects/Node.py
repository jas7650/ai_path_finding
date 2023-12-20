import copy
import operator
from utils.game_utils import *


class Node(object):

    def __init__(self, location, board):
        self.best_child = None
        self.location = location
        self.board = copy.deepcopy(board)
        self.end_node = False
        if self.board.getValue(location) == END_VALUE:
            self.end_node = True
        if not self.end_node:
            self.board.setValue(location, EXPLORED_VALUE)


    def getBestPath(self):
        if self.end_node:
            return []
        if self.best_child.getEndNode():
            return [self.best_child.getLocation()]
        children = [self.best_child.getLocation()]
        children.extend(self.best_child.getBestPath())
        return children


    def getLocation(self):
        return self.location


    def getEndNode(self):
        return self.end_node


    def foundEnd(self):
        if self.getEndNode():
            return True
        if self.best_child != None:
            return self.best_child.foundEnd()
        return False


    def explore(self):
        legal_moves = self.board.getLegalMoves(self.location)
        if len(legal_moves) > 0:
            for move in legal_moves:
                node = Node(move, self.board)
                if node.getEndNode():
                    self.best_child = node
                else:
                    node.explore()
                    if node.foundEnd():
                        if self.best_child == None:
                            self.best_child = node
                        else:
                            if len(node.getBestPath()) < len(self.best_child.getBestPath()):
                                self.best_child = node
