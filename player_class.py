#!/usr/bin/python3

import pygame
import global_variables
from pygame.math import Vector2

class PLAYER:
    def __init__(self):
        final_block = int(global_variables.cell_number/2) - 1
        self.body = [
            Vector2(1,final_block-4), Vector2(3,final_block-4), Vector2(5,final_block-4),
            Vector2(2,final_block-3), Vector2(3,final_block-3), Vector2(4,final_block-3),
            Vector2(3,final_block-2),
            Vector2(2,final_block-1), Vector2(3,final_block-1), Vector2(4,final_block-1),
            Vector2(1,final_block-0), Vector2(3,final_block-0), Vector2(5,final_block-0)
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
