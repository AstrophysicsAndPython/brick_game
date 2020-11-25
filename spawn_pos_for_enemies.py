#!/usr/bin/python3

import random
# import enemy_class

def spawn_pos_of_enemy_type_1():
    pos_list_for_type_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rand_pos_for_type_1 = random.choice(pos_list_for_type_1)

    if rand_pos_for_type_1 in [1, 4, 7]:
        rand_pos_for_type_1 = 1
    elif rand_pos_for_type_1 in [2, 5, 8]:
        rand_pos_for_type_1 = 6
    elif rand_pos_for_type_1 in [3, 6, 9]:
        rand_pos_for_type_1 = 11

    return rand_pos_for_type_1


def spawn_pos_of_enemy_type_2():
    pos_list_for_type_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    rand_pos_for_type_2 = random.choice(pos_list_for_type_2)

    if rand_pos_for_type_2 % 2 == 0:
        rand_pos_for_type_2 = 1
    else:
        rand_pos_for_type_2 = 6

    return rand_pos_for_type_2

def spawn_pos_of_enemy_type_3():
    return 1
