#!/usr/bin/env python

import random

MAX_RANDOM = 1
MIN_RANDOM = 100
INTRODUCTION_TO_GAME =\
    'Answer "yes" if the number is even, otherwise answer "no".'


def check_even():
    number = random.randint(MAX_RANDOM, MIN_RANDOM)
    if has_even(number) == 0:
        return number, 'yes'
    return number, 'no'


def has_even(number):
    return number % 2
