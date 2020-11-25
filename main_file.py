#!/usr/bin/python3

import sys
import pygame
import random
import player_class
import enemy_class
import global_variables

pygame.init()

player = player_class.PLAYER()

# enemy_spawn_chance_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# enemy_spawn_chance = random.choice(enemy_spawn_chance_list)

enemy_spawn_chance = 2

if (enemy_spawn_chance % 2 == 0 and enemy_spawn_chance != 0) or enemy_spawn_chance in [1, 9]:
    enemy = enemy_class.ENEMY_TYPE_3()
else:
    enemy = enemy_class.ENEMY_TYPE_2()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(), sys.exit()
        if event.type == SCREEN_UPDATE:
            enemy.move_enemy()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit(), sys.exit()
            elif event.key == pygame.K_LEFT:
                player.direction_vector = pygame.math.Vector2(-5, 0)
                player.move_aeroplane()
            elif event.key == pygame.K_RIGHT:
                player.direction_vector = pygame.math.Vector2(5, 0)
                player.move_aeroplane()
            elif event.key == pygame.K_DOWN:
                pygame.time.set_timer(SCREEN_UPDATE, 100)

    global_variables.screen.fill(pygame.Color('gray'))
    player.draw_aeroplane()
    enemy.draw_enemy()
    pygame.display.update()
    global_variables.clock.tick(60)
