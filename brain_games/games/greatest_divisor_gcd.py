#!/usr/bin/env python

import random


def introduction_to_game():
    print('Find the greatest common divisor of given numbers.')


def run_gcd():
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    random_numbers = [number_1, number_2]
    while number_2 > 0:
        number_1, number_2 = number_2, number_1 % number_2
    return random_numbers, number_1
