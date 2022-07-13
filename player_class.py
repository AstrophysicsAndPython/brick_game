"""
Created on Nov 25 00:00:00 2021
"""

import pygame
from pygame.math import Vector2

import global_variables


class Player:
    def __init__(self):
        final_block = int(global_variables.cell_number / 2) - 1
        self.body = [
            Vector2(1, final_block - 4), Vector2(3, final_block - 4),
            Vector2(5, final_block - 4),
            Vector2(2, final_block - 3), Vector2(3, final_block - 3),
            Vector2(4, final_block - 3),
            Vector2(3, final_block - 2),
            Vector2(2, final_block - 1), Vector2(3, final_block - 1),
            Vector2(4, final_block - 1),
            Vector2(1, final_block - 0), Vector2(3, final_block - 0),
            Vector2(5, final_block - 0)
            ]
        self.direction_vector = Vector2(5, 0)

    def draw_player(self):
        for block in self.body:
            player_x = int(block.x * global_variables.cell_size)
            player_y = int(block.y * global_variables.cell_size)
            player_rect = pygame.Rect(player_x, player_y,
                                      global_variables.cell_size,
                                      global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), player_rect)

    def move_player(self):
        for block in self.body:
            block += self.direction_vector
