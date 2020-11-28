#!/usr/bin/python3

import os
import sys
import pygame
import enemy_class
import global_variables


def enemy_player_collision(enemy, player):
    if enemy.__name__ in ['type1', 'type4']:
        if enemy.body[-1].x == player.body[2].x and enemy.body[-1].y >= player.body[2].y:
            return 0
    elif enemy.__name__ in ['type2', 'type3']:
        if (enemy.body[-1].x == player.body[2].x or enemy.body[-4].x == player.body[2].x) and enemy.body[-1].y >= player.body[2].y:
            return 0


def key_press(event, player):
    if event.key == pygame.K_ESCAPE:
        pygame.quit(), sys.exit()
    elif event.key in [pygame.K_LEFT, pygame.K_a] and player.body[0].x != 1:
        player.direction_vector = pygame.math.Vector2(-5, 0)
        player.move_aeroplane()
    elif event.key in [pygame.K_RIGHT, pygame.K_d] and player.body[0].x != 11:
        player.direction_vector = pygame.math.Vector2(5, 0)
        player.move_aeroplane()


def display_text(font_size, text_to_display, text_color, pos_x, pos_y, display_position):
    font = pygame.font.Font('Font/inconsolata.ttf', font_size)
    text = str('%s' %(text_to_display))
    text_surface = font.render(text, True, pygame.Color('%s' %(text_color)))
    text_x, text_y = int(pos_x), int(pos_y)
    if display_position == 'center':
        text_surface_rect = text_surface.get_rect(center=(text_x, text_y))
    elif display_position == 'topright':
        text_surface_rect = text_surface.get_rect(topright=(text_x, text_y))
    global_variables.screen.blit(text_surface, text_surface_rect)


def show_game_over_screen(game_over, first_time):

    if first_time:
        global_variables.screen.fill(pygame.Color('gray'))
        display_text(font_size=72, text_to_display='WELCOME!', text_color='red', pos_x=global_variables.resolution/4.5, pos_y=global_variables.resolution/8, display_position='center')

        display_text(font_size=18, text_to_display='Press Left/Right arrow keys or A/D to move', text_color='red', pos_x=global_variables.resolution/4.5, pos_y=global_variables.resolution/4.25, display_position='center')

        display_text(font_size=18, text_to_display='Press the Spacebar key to start the game', text_color='red', pos_x=global_variables.resolution/4.5, pos_y=global_variables.resolution/3, display_position='center')
    else:
        global_variables.screen.fill(pygame.Color('black'))
        display_text(font_size=72, text_to_display='GAME OVER', text_color='red', pos_x=global_variables.resolution/4.5, pos_y=global_variables.resolution/8, display_position='center')

        display_text(font_size=18, text_to_display='Press Left/Right arrow keys or A/D to move', text_color='red', pos_x=global_variables.resolution/4.5, pos_y=global_variables.resolution/4.25, display_position='center')

        display_text(font_size=18, text_to_display='Press r or Spacebar key to restart the game', text_color='red', pos_x=global_variables.resolution/4.5, pos_y=global_variables.resolution/3, display_position='center')

    display_text(font_size=22, text_to_display='Press Esc key or [Alt+F4] to quit', text_color='red', pos_x=global_variables.resolution/4.5, pos_y=global_variables.resolution/6, display_position='center')

    pygame.display.flip()

    while game_over:
        global_variables.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(), sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(), sys.exit()
                if first_time:
                    if event.key == pygame.K_SPACE:
                        game_over, first_time = False, False
                else:
                    if event.key in [pygame.K_r, pygame.K_SPACE]:
                        game_over, first_time = False, False

    return game_over, first_time


def displaying_score(score):

    display_text(
        font_size=24, text_to_display='CURRENT SCORE', text_color='green',
        pos_x=global_variables.width, pos_y=50,
        display_position='topright'
        )

    display_text(
        font_size=32, text_to_display=sum(score), text_color='green',
        pos_x=global_variables.width, pos_y=70,
        display_position='topright'
        )


def getting_current_score(enemy):
    if enemy.__name__ == 'type1':
        this_score = 10
    elif enemy.__name__ in ['type2', 'type3']:
        this_score = 20
    elif enemy.__name__ == 'type4':
        this_score = 25

    return this_score


def saving_score(score, mode):
    high_score_file = open('high_score_file.txt', '%s' %(mode))
    high_score_file.write(str(sum(score))+'\n')
    high_score_file.close()


def displaying_high_score():
    try:
        read_high_score_file = open('high_score_file.txt', 'r')
        num_list = [float(num) for num in read_high_score_file.read().split()]
        max_val = max(num_list)
    except FileNotFoundError:
        max_val = 0

    display_text(
        font_size=24, text_to_display='HIGH SCORE', text_color='green',
        pos_x=global_variables.resolution/2.25, pos_y=0,
        display_position='topright'
        )

    display_text(
        font_size=32, text_to_display=int(max_val), text_color='green',
        pos_x=global_variables.resolution/2.25, pos_y=20,
        display_position='topright'
        )
