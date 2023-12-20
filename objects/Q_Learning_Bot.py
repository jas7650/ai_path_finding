from utils.game_utils import *
import random

class Q_Learning_Bot(object):

    def __init__(self, board):
        self.board = board


    def find_path(self):
        start = self.board.getStart()
        stop = self.board.getEnd()


    def getNextLocation(self, board, current_location):
        print(f"Finding next move from: {current_location}")
        legal_moves = board.getLegalMoves(current_location)
        print(f"Legal moves: {legal_moves}")
        if len(legal_moves) > 0:
            next_move = random.choice(legal_moves)
            for move in legal_moves:
                if board.getValue(move) == END_VALUE:
                    next_move = move
        print(f"Next move: {next_move}")
        return next_move
