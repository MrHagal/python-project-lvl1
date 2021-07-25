#!/usr/bin/env python

import random

START_INTERVAL = 1
END_INTERVAL = 100
INTRODUCTION_TO_GAME =\
    'Answer "yes" if the number is even, otherwise answer "no".'


def check_even():
    number = random.randint(START_INTERVAL, END_INTERVAL)
    if has_even(number) == 0:
        return number, 'yes'
    return number, 'no'


def has_even(number):
    return number % 2
