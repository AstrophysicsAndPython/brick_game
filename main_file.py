#!/usr/bin/python3

import sys
import misc
import pygame
import enemy_class
import player_class
import global_variables

pygame.init()

player = player_class.PLAYER()

enemy = enemy_class.enemy_type()
wall = enemy_class.WALL()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(), sys.exit()
        if event.type == SCREEN_UPDATE:
            enemy.move_enemy()
        if event.type == pygame.KEYDOWN:
            misc.movements(event=event, player=player)
        if enemy.body[0].y == 28:
            enemy = enemy_class.enemy_type()
            if enemy.__name__ == 'type4':
                pygame.time.set_timer(SCREEN_UPDATE, 65)
            else:
                pygame.time.set_timer(SCREEN_UPDATE, 40)
        misc.enemy_player_collision(enemy=enemy, player=player)

    global_variables.screen.fill(pygame.Color('gray'))
    player.draw_aeroplane()
    enemy.draw_enemy()
    wall.draw_wall()
    pygame.display.update()
    global_variables.clock.tick(60)
