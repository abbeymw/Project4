# Abbey Warren

import pygame 
import sys
import time
import random
from pygame.locals import *


FPS = 4
pygame.init()
fps_clock = pygame.time.Clock()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill(255, 20, 147)
clock = pygame.time.Clock()

pygame.key.set_repeat(1,40)

gridsize = 10
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

screen.blit(surface, (0,0))

