#!/usr/bin/env python

import random

START_INTERVAL = 1
END_INTERVAL = 10


def introduction_to_game():
    return 'Find the greatest common divisor of given numbers.'


def algo_gcd():
    number_1 = random.randint(START_INTERVAL, END_INTERVAL)
    number_2 = random.randint(START_INTERVAL, END_INTERVAL)
    random_numbers = f'{number_1} {number_2}'
    return random_numbers


def run_gcd():
    random_numbers = algo_gcd()
    while number_2 > 0:
        number_1, number_2 = number_2, number_1 % number_2
    return random_numbers, number_1
