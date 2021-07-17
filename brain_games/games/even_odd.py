#!/usr/bin/env python

import random

START_INTERVAL = 1
END_INTERVAL = 100


def introduction_to_game():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def run_even():
    number = random.randint(START_INTERVAL, END_INTERVAL)
    if number % 2 == 0:
        return number, 'yes'
    return number, 'no'
