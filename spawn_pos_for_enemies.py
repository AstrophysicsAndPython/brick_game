"""
Created on Nov 25 00:00:00 2021
"""

import random


def spawn_pos_of_enemy_type_1():
    rand_ = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])

    return 1 if rand_ in [1, 4, 7] else 6 if rand_ in [2, 5, 8] else 11


def spawn_pos_of_enemy_type_2():
    rand_ = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    return 1 if rand_ % 2 == 0 else 6


def spawn_pos_of_enemy_type_3():
    return 1
