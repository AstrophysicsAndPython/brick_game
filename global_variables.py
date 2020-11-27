#!/usr/bin/python3

import pygame

cell_number, cell_size = 56, 20
resolution = cell_number*cell_size
screen = pygame.display.set_mode([int(resolution/3.29), int(resolution/2)])
# use it for making high score or something
# screen = pygame.display.set_mode([int(resolution/1.57), int(resolution/2)])
clock = pygame.time.Clock()
