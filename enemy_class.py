#!/usr/bin/python3

import pygame
import random
import global_variables
import spawn_pos_for_enemies
from pygame.math import Vector2


wall_body_left, wall_body_right = [], []
for blocks in range(global_variables.cell_number):
    wall_body_left.append(Vector2(0, blocks))
    wall_body_right.append(Vector2(16, blocks))

class WALL:
    def __init__(self):
        self.__name__ = 'wall'
        self.body_left = wall_body_left
        self.body_right = wall_body_right

    def draw_wall(self):
        for block in self.body_left:
            wall_left_x_pos = int(block.x*global_variables.cell_size)
            wall_left_y_pos = int(block.y*global_variables.cell_size)
            wall_left_rect = pygame.Rect(wall_left_x_pos, wall_left_y_pos, global_variables.cell_size, global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), wall_left_rect)

        for block in self.body_right:
            wall_right_x_pos = int(block.x*global_variables.cell_size)
            wall_right_y_pos = int(block.y*global_variables.cell_size)
            wall_right_rect = pygame.Rect(wall_right_x_pos, wall_right_y_pos, global_variables.cell_size, global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), wall_right_rect)


class ENEMY_TYPE_1:
    def __init__(self):
        self.__name__ = 'type1'
        rand_pos_for_type_1 = spawn_pos_for_enemies.spawn_pos_of_enemy_type_1()
        self.body = [
            Vector2(rand_pos_for_type_1+0,-6), Vector2(rand_pos_for_type_1+2,-6), Vector2(rand_pos_for_type_1+4,-6),
            Vector2(rand_pos_for_type_1+1,-5), Vector2(rand_pos_for_type_1+2,-5), Vector2(rand_pos_for_type_1+3,-5),
            Vector2(rand_pos_for_type_1+2,-4),
            Vector2(rand_pos_for_type_1+1,-3), Vector2(rand_pos_for_type_1+2,-3), Vector2(rand_pos_for_type_1+3,-3),
            Vector2(rand_pos_for_type_1+0,-2), Vector2(rand_pos_for_type_1+2,-2), Vector2(rand_pos_for_type_1+4,-2)
        ]
        self.direction_vector = Vector2(0, 1)

    def draw_enemy(self):
        for block in self.body:
            enemy_x_pos = int(block.x*global_variables.cell_size)
            enemy_y_pos = int(block.y*global_variables.cell_size)
            enemy_rect = pygame.Rect(enemy_x_pos, enemy_y_pos, global_variables.cell_size, global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), enemy_rect)

    def move_enemy(self):
        for block in self.body:
            block += self.direction_vector


class ENEMY_TYPE_2:
    def __init__(self):
        self.__name__ = 'type2'
        rand_pos_for_type_2 = spawn_pos_for_enemies.spawn_pos_of_enemy_type_2()
        self.body = [
            Vector2(rand_pos_for_type_2+0,-6), Vector2(rand_pos_for_type_2+2,-6), Vector2(rand_pos_for_type_2+4,-6), Vector2(rand_pos_for_type_2+5,-6), Vector2(rand_pos_for_type_2+7,-6), Vector2(rand_pos_for_type_2+9,-6),
            Vector2(rand_pos_for_type_2+1,-5), Vector2(rand_pos_for_type_2+2,-5), Vector2(rand_pos_for_type_2+3,-5), Vector2(rand_pos_for_type_2+6,-5), Vector2(rand_pos_for_type_2+7,-5), Vector2(rand_pos_for_type_2+8,-5),
            Vector2(rand_pos_for_type_2+2,-4), Vector2(rand_pos_for_type_2+7,-4),
            Vector2(rand_pos_for_type_2+1,-3), Vector2(rand_pos_for_type_2+2,-3), Vector2(rand_pos_for_type_2+3,-3), Vector2(rand_pos_for_type_2+6,-3), Vector2(rand_pos_for_type_2+7,-3), Vector2(rand_pos_for_type_2+8,-3),
            Vector2(rand_pos_for_type_2+0,-2), Vector2(rand_pos_for_type_2+2,-2), Vector2(rand_pos_for_type_2+4,-2), Vector2(rand_pos_for_type_2+5,-2), Vector2(rand_pos_for_type_2+7,-2), Vector2(rand_pos_for_type_2+9,-2)
        ]
        self.direction_vector = Vector2(0, 1)

    def draw_enemy(self):
        for block in self.body:
            enemy_x_pos = int(block.x*global_variables.cell_size)
            enemy_y_pos = int(block.y*global_variables.cell_size)
            enemy_rect = pygame.Rect(enemy_x_pos, enemy_y_pos, global_variables.cell_size, global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), enemy_rect)

    def move_enemy(self):
        for block in self.body:
            block += self.direction_vector


class ENEMY_TYPE_3:
    def __init__(self):
        self.__name__ = 'type3'
        rand_pos_for_type_3 = spawn_pos_for_enemies.spawn_pos_of_enemy_type_3()
        self.body = [
            Vector2(rand_pos_for_type_3+0,-6), Vector2(rand_pos_for_type_3+2,-6), Vector2(rand_pos_for_type_3+4,-6), Vector2(rand_pos_for_type_3+10,-6), Vector2(rand_pos_for_type_3+12,-6), Vector2(rand_pos_for_type_3+14,-6),
            Vector2(rand_pos_for_type_3+1,-5), Vector2(rand_pos_for_type_3+2,-5), Vector2(rand_pos_for_type_3+3,-5), Vector2(rand_pos_for_type_3+11,-5), Vector2(rand_pos_for_type_3+12,-5), Vector2(rand_pos_for_type_3+13,-5),
            Vector2(rand_pos_for_type_3+2,-4), Vector2(rand_pos_for_type_3+12,-4),
            Vector2(rand_pos_for_type_3+1,-3), Vector2(rand_pos_for_type_3+2,-3), Vector2(rand_pos_for_type_3+3,-3), Vector2(rand_pos_for_type_3+11,-3), Vector2(rand_pos_for_type_3+12,-3), Vector2(rand_pos_for_type_3+13,-3),
            Vector2(rand_pos_for_type_3+0,-2), Vector2(rand_pos_for_type_3+2,-2), Vector2(rand_pos_for_type_3+4,-2), Vector2(rand_pos_for_type_3+10,-2), Vector2(rand_pos_for_type_3+12,-2), Vector2(rand_pos_for_type_3+14,-2)
        ]
        self.direction_vector = Vector2(0, 1)

    def draw_enemy(self):
        for block in self.body:
            enemy_x_pos = int(block.x*global_variables.cell_size)
            enemy_y_pos = int(block.y*global_variables.cell_size)
            enemy_rect = pygame.Rect(enemy_x_pos, enemy_y_pos, global_variables.cell_size, global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), enemy_rect)

    def move_enemy(self):
        for block in self.body:
            block += self.direction_vector


class ENEMY_TYPE_4:
    def __init__(self):
        self.__name__ = 'type4'
        rand_pos_for_type_1 = spawn_pos_for_enemies.spawn_pos_of_enemy_type_1()
        self.body = [
            Vector2(rand_pos_for_type_1+0,-6), Vector2(rand_pos_for_type_1+2,-6), Vector2(rand_pos_for_type_1+4,-6),
            Vector2(rand_pos_for_type_1+1,-5), Vector2(rand_pos_for_type_1+2,-5), Vector2(rand_pos_for_type_1+3,-5),
            Vector2(rand_pos_for_type_1+1,-4), Vector2(rand_pos_for_type_1+2,-4), Vector2(rand_pos_for_type_1+3,-4),
            Vector2(rand_pos_for_type_1+1,-3), Vector2(rand_pos_for_type_1+2,-3), Vector2(rand_pos_for_type_1+3,-3),
            Vector2(rand_pos_for_type_1+0,-2), Vector2(rand_pos_for_type_1+2,-2), Vector2(rand_pos_for_type_1+4,-2)
        ]
        self.move_down = Vector2(0, 1)
        self.move_down_right = Vector2(5,1)
        self.move_down_left = Vector2(-5, 1)

    def draw_enemy(self):
        for block in self.body:
            enemy_x_pos = int(block.x*global_variables.cell_size)
            enemy_y_pos = int(block.y*global_variables.cell_size)
            enemy_rect = pygame.Rect(enemy_x_pos, enemy_y_pos, global_variables.cell_size, global_variables.cell_size)
            pygame.draw.rect(global_variables.screen, pygame.Color('red'), enemy_rect)

    def move_enemy(self):
        move_pos_array = [2, 7, 12]
        for block in self.body:
            block += self.move_down
            if block.x == 1 and block.y in move_pos_array:
                for block in self.body:
                    block += self.move_down_right
            elif block.x == 6 and block.y in move_pos_array:
                rand_int = random.randint(0, 50)
                if rand_int%2 == 0:
                    for block in self.body:
                        block += self.move_down_left
                else:
                    for block in self.body:
                        block += self.move_down_right
            elif block.x == 11 and block.y in move_pos_array:
                for block in self.body:
                    block += self.move_down_left

def enemy_type():
    enemy_spawn_chance_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    enemy_spawn_chance = random.choice(enemy_spawn_chance_list)

    if enemy_spawn_chance in [1, 5, 9]:
        enemy = ENEMY_TYPE_1()
    elif enemy_spawn_chance in [2, 6, 10]:
        enemy = ENEMY_TYPE_2()
    elif enemy_spawn_chance in [3, 7, 11]:
        enemy = ENEMY_TYPE_3()
    elif enemy_spawn_chance in [4, 8, 12]:
        enemy = ENEMY_TYPE_4()

    return enemy
