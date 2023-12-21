import pygame
from utils.game_utils import *

class Game_Tile(object):

    def __init__(self, row, col, width, height, screen):
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.screen = screen
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.row*self.width, self.col*self.height, self.width, self.height)


    def getValue(self):
        return self.value


    def process(self, value):
        self.value = value
        if self.value == START_VALUE:
            color = GREEN
        elif self.value == END_VALUE:
            color = RED
        elif self.value == OBSTACLE_VALUE:
            color = BLACK
        elif self.value == EXPLORED_VALUE:
            color = YELLOW
        else:
            color = WHITE
        self.surface.fill(color)
        self.screen.blit(self.surface, self.rect)
