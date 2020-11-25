#!/usr/bin/python3

import sys
import pygame
import enemy_class
import player_class
import global_variables

pygame.init()

player = player_class.PLAYER()

enemy = enemy_class.enemy_type()

wall = enemy_class.WALL()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 35)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(), sys.exit()
        if event.type == SCREEN_UPDATE:
            enemy.move_enemy()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit(), sys.exit()
            elif event.key == pygame.K_LEFT:
                player.direction_vector = pygame.math.Vector2(-5, 0)
                player.move_aeroplane()
            elif event.key == pygame.K_RIGHT:
                player.direction_vector = pygame.math.Vector2(5, 0)
                player.move_aeroplane()
        if enemy.body[0].y == 22:
            enemy = enemy_class.enemy_type()


    global_variables.screen.fill(pygame.Color('gray'))
    player.draw_aeroplane()
    enemy.draw_enemy()
    wall.draw_wall()
    pygame.display.update()
    global_variables.clock.tick(60)
