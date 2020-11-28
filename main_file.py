#!/usr/bin/python3

import sys
import misc
import pygame
import enemy_class
import player_class
import global_variables

pygame.init()

game_on, game_over, first_time = True, True, True

while game_on:
    for event in pygame.event.get():
        if game_over:
            game_over, first_time = misc.show_game_over_screen(game_over=game_over, first_time=first_time)

            score = []
            player = player_class.PLAYER()
            wall, enemy = enemy_class.WALL(), enemy_class.enemy_type()

            SCREEN_UPDATE = pygame.USEREVENT
            pygame.time.set_timer(SCREEN_UPDATE, 35)

        if event.type == pygame.QUIT:
            pygame.quit(), sys.exit()
        if event.type == SCREEN_UPDATE:
            enemy.move_enemy()
        if event.type == pygame.KEYDOWN:
            misc.key_press(event=event, player=player)
        if enemy.body[0].y == 28:
            score.append(misc.getting_current_score(enemy=enemy))
            enemy = enemy_class.enemy_type()
            if enemy.__name__ == 'type4':
                pygame.time.set_timer(SCREEN_UPDATE, 35)
            else:
                pygame.time.set_timer(SCREEN_UPDATE, 20)
        result = misc.enemy_player_collision(enemy=enemy, player=player)
        if result == 0:
            game_over = True
            if score != 0:
                misc.saving_score(score=score, mode='a')

    wall.draw_wall()
    enemy.draw_enemy()
    player.draw_aeroplane()
    misc.displaying_high_score()
    misc.displaying_score(score=score)

    pygame.display.update()
    global_variables.clock.tick(60)
    global_variables.screen.fill(pygame.Color('gray'))
