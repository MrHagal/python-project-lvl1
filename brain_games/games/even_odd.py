#!/usr/bin/env python

import random


def introduction_to_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def run_even():
    number = random.randint(1, 100)
    if number % 2 == 0:
        return [number], 'yes'
    return [number], 'no'
