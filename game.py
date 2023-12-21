import pygame
import sys
from objects.Board import Board
import math
from utils.game_utils import *
import numpy as np
from objects.Q_Learning_Bot import Q_Learning_Bot
from objects.Node import Node


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    board = Board(NUM_ROWS, NUM_COLUMNS)
    value = OBSTACLE_VALUE

    while True:
        drawGrid(board)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    value = OBSTACLE_VALUE
                if event.key == pygame.K_2:
                    value = END_VALUE
                if event.key == pygame.K_3:
                    value = START_VALUE
            if pygame.mouse.get_pressed():
                pos = pygame.mouse.get_pos()
                col = (int)(math.floor(pos[0]/BLOCK_SIZE))
                row = (int)(math.floor(pos[1]/BLOCK_SIZE))
                location = np.asarray([row, col])
                if pygame.mouse.get_pressed()[0]:
                    if row < NUM_ROWS and col < NUM_COLUMNS and row > -1 and col > -1:
                        if value == START_VALUE:
                            if board.getStart() != None:
                                previous_start = board.getStart()
                                board.clearExploredSquares()
                                board.setValue(previous_start, DEFAULT_VALUE)
                            board.setValue(location, value)
                            if board.getEnd() != None:
                                node = Node(location, board, [], 0)
                                node.explore()
                                bestPath = node.getBestPath()
                                for path_location in bestPath:
                                    if board.getValue(path_location) != END_VALUE and board.getValue(path_location) != START_VALUE:
                                        board.setValue(path_location, EXPLORED_VALUE)
                        elif value == END_VALUE:
                            if board.getEnd() != None:
                                previous_stop = board.getEnd()
                                board.clearExploredSquares()
                                board.setValue(previous_stop, DEFAULT_VALUE)
                            board.setValue(location, value)
                            if board.getStart() != None:
                                node = Node(board.getStart(), board, [], 0)
                                node.explore()
                                bestPath = node.getBestPath()
                                for path_location in bestPath:
                                    if board.getValue(path_location) != END_VALUE and board.getValue(path_location) != START_VALUE:
                                        board.setValue(path_location, EXPLORED_VALUE)
                        else:
                            board.setValue(location, value)
                if pygame.mouse.get_pressed()[2]:
                    if row < NUM_ROWS and col < NUM_COLUMNS and row > -1 and col > -1:
                        board.setValue(location, DEFAULT_VALUE)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid(board : Board):
    for row in range(0, NUM_ROWS):
        for col in range(0, NUM_COLUMNS):
            location = [row, col]
            value = board.getValue(location)
            if value == START_VALUE:
                color = GREEN
            elif value == END_VALUE:
                color = RED
            elif value == OBSTACLE_VALUE:
                color = BLACK
            elif value == EXPLORED_VALUE:
                color = YELLOW
            else:
                color = WHITE
            rect = pygame.Rect(col*BLOCK_SIZE, row*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, color, rect)
    for row in range(0, NUM_ROWS):
        for col in range(0, NUM_COLUMNS):
            rect = pygame.Rect(col*BLOCK_SIZE, row*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


if __name__ == "__main__":
    main()
