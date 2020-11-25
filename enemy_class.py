#!/usr/bin/python3

import pygame
import global_variables
from pygame.math import Vector2
import spawn_pos_for_enemies

rand_pos_for_type_1 = spawn_pos_for_enemies.spawn_pos_of_enemy_type_1()
rand_pos_for_type_2 = spawn_pos_for_enemies.spawn_pos_of_enemy_type_2()
rand_pos_for_type_3 = spawn_pos_for_enemies.spawn_pos_of_enemy_type_3()

class ENEMY_TYPE_1:
    def __init__(self):
        self.body = [
            Vector2(rand_pos_for_type_1+0, 1), Vector2(rand_pos_for_type_1 +2, 1), Vector2(rand_pos_for_type_1+4, 1),
            Vector2(rand_pos_for_type_1+1, 2), Vector2(rand_pos_for_type_1 +2, 2), Vector2(rand_pos_for_type_1+3, 2),
            Vector2(rand_pos_for_type_1+2, 3),
            Vector2(rand_pos_for_type_1+1, 4), Vector2(rand_pos_for_type_1 +2, 4), Vector2(rand_pos_for_type_1+3, 4),
            Vector2(rand_pos_for_type_1+0, 5), Vector2(rand_pos_for_type_1 +2, 5), Vector2(rand_pos_for_type_1+4, 5)
        ]
        self.direction_vector = Vector2(0, 1)

    def draw_enemy(self):
        for block in self.body:
            enemy_x_pos = int(block.x*global_variables.cell_size)
            enemy_y_pos = int(block.y*global_variables.cell_size)
            enemy_rect = pygame.Rect(enemy_x_pos, enemy_y_pos,
                                     global_variables.cell_size, global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), enemy_rect)

    def move_enemy(self):
        for block in self.body:
            block += self.direction_vector


class ENEMY_TYPE_2:
    def __init__(self):
        self.body = [
            Vector2(rand_pos_for_type_2+0, 1), Vector2(rand_pos_for_type_2+2, 1), Vector2(rand_pos_for_type_2+4,1), Vector2(rand_pos_for_type_2+5, 1), Vector2(rand_pos_for_type_2+7, 1), Vector2(rand_pos_for_type_2+9, 1),
            Vector2(rand_pos_for_type_2+1, 2), Vector2(rand_pos_for_type_2+2, 2), Vector2(rand_pos_for_type_2+3,2), Vector2(rand_pos_for_type_2+6, 2), Vector2(rand_pos_for_type_2+7, 2), Vector2(rand_pos_for_type_2+8, 2),
            Vector2(rand_pos_for_type_2+2, 3), Vector2(rand_pos_for_type_2+7, 3),
            Vector2(rand_pos_for_type_2+1, 4), Vector2(rand_pos_for_type_2+2, 4), Vector2(rand_pos_for_type_2+3,4), Vector2(rand_pos_for_type_2+6, 4), Vector2(rand_pos_for_type_2+7, 4), Vector2(rand_pos_for_type_2+8, 4),
            Vector2(rand_pos_for_type_2+0, 5), Vector2(rand_pos_for_type_2+2, 5), Vector2(rand_pos_for_type_2+4,5), Vector2(rand_pos_for_type_2+5, 5), Vector2(rand_pos_for_type_2+7, 5), Vector2(rand_pos_for_type_2+9, 5)
        ]
        self.direction_vector = Vector2(0, 1)

    def draw_enemy(self):
        for block in self.body:
            enemy_x_pos = int(block.x*global_variables.cell_size)
            enemy_y_pos = int(block.y*global_variables.cell_size)
            enemy_rect = pygame.Rect(enemy_x_pos, enemy_y_pos,
                                     global_variables.cell_size, global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), enemy_rect)

    def move_enemy(self):
        for block in self.body:
            block += self.direction_vector


class ENEMY_TYPE_3:
    def __init__(self):
        self.body = [
            Vector2(rand_pos_for_type_3+0, 1), Vector2(rand_pos_for_type_3+2, 1), Vector2(rand_pos_for_type_3+4,1), Vector2(rand_pos_for_type_3+10, 1), Vector2(rand_pos_for_type_3+12, 1), Vector2(rand_pos_for_type_3+14, 1),
            Vector2(rand_pos_for_type_3+1, 2), Vector2(rand_pos_for_type_3+2, 2), Vector2(rand_pos_for_type_3+3,2), Vector2(rand_pos_for_type_3+11, 2), Vector2(rand_pos_for_type_3+12, 2), Vector2(rand_pos_for_type_3+13, 2),
            Vector2(rand_pos_for_type_3+2, 3), Vector2(rand_pos_for_type_3+12, 3),
            Vector2(rand_pos_for_type_3+1, 4), Vector2(rand_pos_for_type_3+2, 4), Vector2(rand_pos_for_type_3+3,4), Vector2(rand_pos_for_type_3+11, 4), Vector2(rand_pos_for_type_3+12, 4), Vector2(rand_pos_for_type_3+13, 4),
            Vector2(rand_pos_for_type_3+0, 5), Vector2(rand_pos_for_type_3+2, 5), Vector2(rand_pos_for_type_3+4,5), Vector2(rand_pos_for_type_3+10, 5), Vector2(rand_pos_for_type_3+12, 5), Vector2(rand_pos_for_type_3+14, 5)
        ]
        self.direction_vector = Vector2(0, 1)

    def draw_enemy(self):
        for block in self.body:
            enemy_x_pos = int(block.x*global_variables.cell_size)
            enemy_y_pos = int(block.y*global_variables.cell_size)
            enemy_rect = pygame.Rect(enemy_x_pos, enemy_y_pos,
                                     global_variables.cell_size, global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), enemy_rect)

    def move_enemy(self):
        for block in self.body:
            block += self.direction_vector
