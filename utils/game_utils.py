import pygame
import numpy as np

BLACK = pygame.Color('black')
WHITE = pygame.Color('grey')
GREEN = pygame.Color('green3')
RED = pygame.Color('red3')
YELLOW = pygame.Color('yellow3')
BROWN = pygame.Color('burlywood4')

UP = np.asarray([0, 1])
DOWN = np.asarray([0, -1])
LEFT = np.asarray([-1, 0])
RIGHT = np.asarray([1, 0])
MOVE_DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

OBSTACLE_VALUE = -100
START_VALUE = 0
END_VALUE = 1000
DEFAULT_VALUE = -1
EXPLORED_VALUE = 1

LEFT_CLICK = 1
RIGHT_CLICK = 2

GRID_SIZE = 7
NUM_ROWS = GRID_SIZE
NUM_COLUMNS = GRID_SIZE
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40

BLOCK_SIZE = 40

WINDOW_HEIGHT = NUM_ROWS * BLOCK_SIZE
WINDOW_WIDTH = NUM_COLUMNS * BLOCK_SIZE + BUTTON_WIDTH

def remove_duplicates(list):
    temp = []
    for value in list:
        if value not in temp:
            temp.append(value)
    return temp
