#!/usr/bin/python3

import pygame
import global_variables
from pygame.math import Vector2

class PLAYER:
    def __init__(self):
        self.body = [
            Vector2(1,17), Vector2(3,17), Vector2(5,17),
            Vector2(2,18), Vector2(3,18), Vector2(4,18),
            Vector2(3,19),
            Vector2(2,20), Vector2(3,20), Vector2(4,20),
            Vector2(1,21), Vector2(3,21), Vector2(5,21)
        ]
        self.direction_vector = Vector2(5, 0)

    def draw_aeroplane(self):
        for block in self.body:
            aeroplane_x_pos = int(block.x*global_variables.cell_size)
            aeroplane_y_pos = int(block.y*global_variables.cell_size)
            aeroplane_rect = pygame.Rect(aeroplane_x_pos, aeroplane_y_pos, global_variables.cell_size, global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), aeroplane_rect)

    def move_aeroplane(self):
        for block in self.body:
            block += self.direction_vector
