#!/usr/bin/env python

import random

START_INTERVAL = 1
END_INTERVAL = 100


def introduction_to_game():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def random_number():
    number = random.randint(START_INTERVAL, END_INTERVAL)
    return number


def check_even():
    number = random_number()
    if number % 2 == 0:
        return number, 'yes'
    return number, 'no'
