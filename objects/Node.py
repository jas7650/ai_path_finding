import copy
import operator
from utils.game_utils import *


class Node(object):

    def __init__(self, location, board, explore_list, num_parents):
        self.best_child = None
        self.location = location
        self.board = copy.deepcopy(board)
        self.end_node = False
        self.num_parents = num_parents
        self.explore_list = explore_list
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
    

    def getExploreList(self):
        return self.explore_list
    

    def getNumParents(self):
        return self.num_parents
    

    def getIndentations(self):
        s = ""
        for i in range(self.num_parents):
            s += "    "
        return s


    def explore(self):
        legal_moves = self.board.getLegalMoves(self.location)
        if len(legal_moves) > 0:
            for move in legal_moves:
                node = Node(move, self.board, self.explore_list, self.num_parents+1)
                if self.potential_candidate(node):
                    self.explore_list.append(node)
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
                        self.explore_list.extend(node.getExploreList())
                        self.explore_list = remove_duplicates(self.explore_list)


    def potential_candidate(self, node):
        for n in self.explore_list:
            if n.getLocation()[0] == node.getLocation()[0] and n.getLocation()[1] == node.getLocation()[1]:
                if n.getNumParents() <= node.getNumParents():
                    return False
        return True
