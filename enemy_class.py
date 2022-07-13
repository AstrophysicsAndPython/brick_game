"""
Created on Nov 25 00:00:00 2021
"""

import random

import pygame
from pygame.math import Vector2

import global_variables
import spawn_pos_for_enemies

wall_right = [Vector2(0, blocks) for blocks in range(global_variables.cell_number)]
wall_left = [Vector2(16, blocks) for blocks in range(global_variables.cell_number)]


class WALL:
    def __init__(self):
        self.__name__ = 'wall'
        self.wall_left = wall_left
        self.wall_right = wall_right

    def draw_wall(self):
        for block in self.wall_left:
            wall_left_x = int(block.x * global_variables.cell_size)
            wall_left_y = int(block.y * global_variables.cell_size)
            wall_left_rect = pygame.Rect(wall_left_x, wall_left_y,
                                         global_variables.cell_size,
                                         global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), wall_left_rect)

        for block in self.wall_right:
            wall_right_x = int(block.x * global_variables.cell_size)
            wall_right_y = int(block.y * global_variables.cell_size)
            wall_right_rect = pygame.Rect(wall_right_x, wall_right_y,
                                          global_variables.cell_size,
                                          global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'),
                             wall_right_rect)


class EnemyType1:
    def __init__(self):
        self.__name__ = 'type1'
        pos_type1 = spawn_pos_for_enemies.spawn_pos_of_enemy_type_1()
        self.body = [
            Vector2(pos_type1 + 0, -6), Vector2(pos_type1 + 2, -6),
            Vector2(pos_type1 + 4, -6),
            Vector2(pos_type1 + 1, -5), Vector2(pos_type1 + 2, -5),
            Vector2(pos_type1 + 3, -5),
            Vector2(pos_type1 + 2, -4),
            Vector2(pos_type1 + 1, -3), Vector2(pos_type1 + 2, -3),
            Vector2(pos_type1 + 3, -3),
            Vector2(pos_type1 + 0, -2), Vector2(pos_type1 + 2, -2),
            Vector2(pos_type1 + 4, -2)
            ]
        self.direction_vector = Vector2(0, 1)

    def draw_enemy(self):
        for block in self.body:
            enemy_x_pos = int(block.x * global_variables.cell_size)
            enemy_y_pos = int(block.y * global_variables.cell_size)
            enemy_rect = pygame.Rect(enemy_x_pos, enemy_y_pos, global_variables.cell_size,
                                     global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), enemy_rect)

    def move_enemy(self):
        for block in self.body:
            block += self.direction_vector


class EnemyType2:
    def __init__(self):
        self.__name__ = 'type2'
        pos_type2 = spawn_pos_for_enemies.spawn_pos_of_enemy_type_2()
        self.body = [
            Vector2(pos_type2 + 0, -6), Vector2(pos_type2 + 2, -6),
            Vector2(pos_type2 + 4, -6), Vector2(pos_type2 + 5, -6),
            Vector2(pos_type2 + 7, -6), Vector2(pos_type2 + 9, -6),
            Vector2(pos_type2 + 1, -5), Vector2(pos_type2 + 2, -5),
            Vector2(pos_type2 + 3, -5), Vector2(pos_type2 + 6, -5),
            Vector2(pos_type2 + 7, -5), Vector2(pos_type2 + 8, -5),
            Vector2(pos_type2 + 2, -4), Vector2(pos_type2 + 7, -4),
            Vector2(pos_type2 + 1, -3), Vector2(pos_type2 + 2, -3),
            Vector2(pos_type2 + 3, -3), Vector2(pos_type2 + 6, -3),
            Vector2(pos_type2 + 7, -3), Vector2(pos_type2 + 8, -3),
            Vector2(pos_type2 + 0, -2), Vector2(pos_type2 + 2, -2),
            Vector2(pos_type2 + 4, -2), Vector2(pos_type2 + 5, -2),
            Vector2(pos_type2 + 7, -2), Vector2(pos_type2 + 9, -2)
            ]
        self.direction_vector = Vector2(0, 1)

    def draw_enemy(self):
        for block in self.body:
            enemy_x_pos = int(block.x * global_variables.cell_size)
            enemy_y_pos = int(block.y * global_variables.cell_size)
            enemy_rect = pygame.Rect(enemy_x_pos, enemy_y_pos, global_variables.cell_size,
                                     global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), enemy_rect)

    def move_enemy(self):
        for block in self.body:
            block += self.direction_vector


class EnemyType3:
    def __init__(self):
        self.__name__ = 'type3'
        pos_type3 = spawn_pos_for_enemies.spawn_pos_of_enemy_type_3()
        self.body = [
            Vector2(pos_type3 + 0, -6), Vector2(pos_type3 + 2, -6),
            Vector2(pos_type3 + 4, -6), Vector2(pos_type3 + 10, -6),
            Vector2(pos_type3 + 12, -6), Vector2(pos_type3 + 14, -6),
            Vector2(pos_type3 + 1, -5), Vector2(pos_type3 + 2, -5),
            Vector2(pos_type3 + 3, -5), Vector2(pos_type3 + 11, -5),
            Vector2(pos_type3 + 12, -5), Vector2(pos_type3 + 13, -5),
            Vector2(pos_type3 + 2, -4), Vector2(pos_type3 + 12, -4),
            Vector2(pos_type3 + 1, -3), Vector2(pos_type3 + 2, -3),
            Vector2(pos_type3 + 3, -3), Vector2(pos_type3 + 11, -3),
            Vector2(pos_type3 + 12, -3), Vector2(pos_type3 + 13, -3),
            Vector2(pos_type3 + 0, -2), Vector2(pos_type3 + 2, -2),
            Vector2(pos_type3 + 4, -2), Vector2(pos_type3 + 10, -2),
            Vector2(pos_type3 + 12, -2), Vector2(pos_type3 + 14, -2)
            ]
        self.direction_vector = Vector2(0, 1)

    def draw_enemy(self):
        for block in self.body:
            enemy_x_pos = int(block.x * global_variables.cell_size)
            enemy_y_pos = int(block.y * global_variables.cell_size)
            enemy_rect = pygame.Rect(enemy_x_pos, enemy_y_pos, global_variables.cell_size,
                                     global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), enemy_rect)

    def move_enemy(self):
        for block in self.body:
            block += self.direction_vector


class EnemyType4:
    def __init__(self):
        self.__name__ = 'type4'
        pos_type1 = spawn_pos_for_enemies.spawn_pos_of_enemy_type_1()
        self.body = [
            Vector2(pos_type1 + 0, -6), Vector2(pos_type1 + 2, -6),
            Vector2(pos_type1 + 4, -6),
            Vector2(pos_type1 + 1, -5), Vector2(pos_type1 + 2, -5),
            Vector2(pos_type1 + 3, -5),
            Vector2(pos_type1 + 1, -4), Vector2(pos_type1 + 2, -4),
            Vector2(pos_type1 + 3, -4),
            Vector2(pos_type1 + 1, -3), Vector2(pos_type1 + 2, -3),
            Vector2(pos_type1 + 3, -3),
            Vector2(pos_type1 + 0, -2), Vector2(pos_type1 + 2, -2),
            Vector2(pos_type1 + 4, -2)
            ]
        self.move_down = Vector2(0, 1)
        self.move_down_right = Vector2(5, 1)
        self.move_down_left = Vector2(-5, 1)

    def draw_enemy(self):
        for block in self.body:
            enemy_x_pos = int(block.x * global_variables.cell_size)
            enemy_y_pos = int(block.y * global_variables.cell_size)
            enemy_rect = pygame.Rect(enemy_x_pos, enemy_y_pos, global_variables.cell_size,
                                     global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), enemy_rect)

    def move_enemy(self):
        move_pos_array = [2, 7, 12]
        for body1 in self.body:
            body1 += self.move_down
            if body1.x == 1 and body1.y in move_pos_array:
                for body2 in self.body:
                    body2 += self.move_down_right
            elif body1.x == 6 and body1.y in move_pos_array:
                rand_int = random.randint(0, 50)
                if rand_int % 2 == 0:
                    for body2 in self.body:
                        body2 += self.move_down_left
                else:
                    for body2 in self.body:
                        body2 += self.move_down_right
            elif body1.x == 11 and body1.y in move_pos_array:
                for body3 in self.body:
                    body3 += self.move_down_left


def pick_enemy_type():
    rand_ = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    if rand_ in [1, 5, 9]:
        return EnemyType1
    elif rand_ in [2, 6, 10]:
        return EnemyType2
    elif rand_ in [3, 7, 11]:
        return EnemyType3
    else:
        return EnemyType4
