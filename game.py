import pygame
import sys
from objects.Board import Board
import math
from utils.game_utils import *
import numpy as np


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
                    value = START_VALUE
                if event.key == pygame.K_3:
                    value = END_VALUE
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                col = (int)(math.floor(pos[0]/BLOCK_SIZE))
                row = (int)(math.floor(pos[1]/BLOCK_SIZE))
                if row < NUM_ROWS and col < NUM_COLUMNS and row > -1 and col > -1:
                    if value == START_VALUE:
                        if board.getStart() == None:
                            board.setValue(row, col, value)
                    elif value == END_VALUE:
                        if board.getEnd() == None:
                            board.setValue(row, col, value)
                    else:
                        board.setValue(row, col, value)
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                col = (int)(math.floor(pos[0]/BLOCK_SIZE))
                row = (int)(math.floor(pos[1]/BLOCK_SIZE))
                if row < NUM_ROWS and col < NUM_COLUMNS and row > -1 and col > -1:
                    board.setValue(row, col, DEFAULT_VALUE)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid(board : Board):
    for row in range(0, NUM_ROWS):
        for col in range(0, NUM_COLUMNS):
            value = board.getValue(row, col)
            if value == END_VALUE:
                color = GREEN
            elif value == START_VALUE:
                color = RED
            elif value == OBSTACLE_VALUE:
                color = BLACK
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
