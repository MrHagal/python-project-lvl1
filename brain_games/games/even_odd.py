#!/usr/bin/env python

import random

MIN_LENGTH = 1
MAX_LENGTH = 100
INTRODUCTION_TO_GAME =\
    'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    number = random.randint(MIN_LENGTH, MAX_LENGTH)
    if has_even(number) == 0:
        return number, 'yes'
    return number, 'no'


def has_even(number):
    return number % 2
