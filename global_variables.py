#!/usr/bin/python3

import pygame

cell_number, cell_size = 44, 20
resolution = cell_number*cell_size
screen = pygame.display.set_mode([int(resolution/2.6), int(resolution/2)])
clock = pygame.time.Clock()
