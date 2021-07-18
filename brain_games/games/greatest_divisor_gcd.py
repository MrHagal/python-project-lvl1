#!/usr/bin/env python

import random

START_INTERVAL = 1
END_INTERVAL = 10


def introduction_to_game():
    return 'Find the greatest common divisor of given numbers.'


def random_number():
    number_1 = random.randint(START_INTERVAL, END_INTERVAL)
    number_2 = random.randint(START_INTERVAL, END_INTERVAL)
    game_question = f'{number_1} {number_2}'
    return game_question


def check_gcd():
    game_question = random_number()
    while number_2 > 0:
        number_1, number_2 = number_2, number_1 % number_2
    return game_question, number_1
