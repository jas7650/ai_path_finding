import pygame
import sys
from objects.Board import Board
import math
from utils.game_utils import *
import numpy as np
from objects.Q_Learning_Bot import Q_Learning_Bot
from objects.Node import Node
from objects.Game_Tile import Game_Tile


def main():
    global SCREEN, CLOCK
    global board
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    board = Board(NUM_ROWS, NUM_COLUMNS)
    value = OBSTACLE_VALUE
    tiles = []
    for row in range(NUM_ROWS):
        row_tiles = []
        for col in range(NUM_COLUMNS):
            row_tiles.append(Game_Tile(row, col, BLOCK_SIZE, BLOCK_SIZE, SCREEN))
        tiles.append(row_tiles)
    tiles = np.asarray(tiles).T
    for row_tiles in tiles:
        for tile in row_tiles:
            tile.process(DEFAULT_VALUE)
    pygame.display.update()

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
            if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                col = (int)(math.floor(pos[0]/BLOCK_SIZE))
                row = (int)(math.floor(pos[1]/BLOCK_SIZE))
                location = np.asarray([row, col])
                if row < NUM_ROWS and col < NUM_COLUMNS and row > -1 and col > -1:
                    if pygame.mouse.get_pressed()[0]:
                        if value == END_VALUE:
                            if board.hasEnd():
                                previous_stop = board.getEnd()
                                board.setValue(previous_stop, DEFAULT_VALUE)
                                tiles = update_tile(tiles, previous_stop)
                        elif value == START_VALUE:
                            if board.hasStart():
                                previous_start = board.getStart()
                                board.setValue(previous_start, DEFAULT_VALUE)
                                tiles = update_tile(tiles, previous_start)
                        board.setValue(location, value)
                        tiles = update_tile(tiles, location)
                        if board.hasStart() and board.hasEnd():
                            board.clearExploredSquares()
                            node = Node(board.getStart(), board, [], 0)
                            node.explore()
                            bestPath = node.getBestPath()
                            for location in bestPath:
                                if (location[0] != board.getEnd()[0] or location[1] != board.getEnd()[1]) and (location[0] != board.getStart()[0] or location[1] != board.getStart()[1]):
                                    board.setValue(location, EXPLORED_VALUE)
                                    update_tile(tiles, location)
                    elif pygame.mouse.get_pressed()[2]:
                        board.setValue(location, DEFAULT_VALUE)
                        tiles = update_tile(tiles, location)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def update_tile(tiles, location):
    tiles[location[0]][location[1]].process(board.getValue(location))
    return tiles

    # while True:
    #     drawGrid(board)
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_1:
    #                 value = OBSTACLE_VALUE
    #             if event.key == pygame.K_2:
    #                 value = END_VALUE
    #             if event.key == pygame.K_3:
    #                 value = START_VALUE
    #         if pygame.mouse.get_pressed():
    #             pos = pygame.mouse.get_pos()
    #             col = (int)(math.floor(pos[0]/BLOCK_SIZE))
    #             row = (int)(math.floor(pos[1]/BLOCK_SIZE))
    #             location = np.asarray([row, col])
    #             if pygame.mouse.get_pressed()[0]:
    #                 if row < NUM_ROWS and col < NUM_COLUMNS and row > -1 and col > -1:
    #                     if value == START_VALUE:
    #                         if board.getStart() != None:
    #                             previous_start = board.getStart()
    #                             board.clearExploredSquares()
    #                             board.setValue(previous_start, DEFAULT_VALUE)
    #                         board.setValue(location, value)
    #                         if board.getEnd() != None:
    #                             node = Node(location, board, [], 0)
    #                             node.explore()
    #                             bestPath = node.getBestPath()
    #                             for path_location in bestPath:
    #                                 if board.getValue(path_location) != END_VALUE and board.getValue(path_location) != START_VALUE:
    #                                     board.setValue(path_location, EXPLORED_VALUE)
    #                     elif value == END_VALUE:
    #                         if board.getEnd() != None:
    #                             previous_stop = board.getEnd()
    #                             board.clearExploredSquares()
    #                             board.setValue(previous_stop, DEFAULT_VALUE)
    #                         board.setValue(location, value)
    #                         if board.getStart() != None:
    #                             node = Node(board.getStart(), board, [], 0)
    #                             node.explore()
    #                             bestPath = node.getBestPath()
    #                             for path_location in bestPath:
    #                                 if board.getValue(path_location) != END_VALUE and board.getValue(path_location) != START_VALUE:
    #                                     board.setValue(path_location, EXPLORED_VALUE)
    #                     else:
    #                         board.setValue(location, value)
    #             if pygame.mouse.get_pressed()[2]:
    #                 if row < NUM_ROWS and col < NUM_COLUMNS and row > -1 and col > -1:
    #                     board.setValue(location, DEFAULT_VALUE)
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()

    #         for button in buttons:
    #             button.process()

    #     pygame.display.update()

def drawGrid(board):
    for row in range(0, NUM_ROWS):
        for col in range(0, NUM_COLUMNS):
            rect = pygame.Rect(col*BLOCK_SIZE, row*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, BROWN, rect, 1)


def clearBoard():
    global board
    board = Board(NUM_ROWS, NUM_COLUMNS)


if __name__ == "__main__":
    main()
