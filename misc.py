#!/usr/bin/python3

import sys
import pygame
import enemy_class

def enemy_player_collision(enemy, player):
    if enemy.__name__ in ['type1', 'type4']:
        if enemy.body[-1].x == player.body[2].x and enemy.body[-1].y >= player.body[2].y:
            print('yes')
    elif enemy.__name__ in ['type2', 'type3']:
        if (enemy.body[-1].x == player.body[2].x or enemy.body[-4].x == player.body[2].x) and enemy.body[-1].y >= player.body[2].y:
            print('yes')

def movements(event, player):
    if event.key == pygame.K_ESCAPE:
        pygame.quit(), sys.exit()
    elif event.key == pygame.K_LEFT:
        player.direction_vector = pygame.math.Vector2(-5, 0)
        player.move_aeroplane()
    elif event.key == pygame.K_RIGHT:
        player.direction_vector = pygame.math.Vector2(5, 0)
        player.move_aeroplane()
