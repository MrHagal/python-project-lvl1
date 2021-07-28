#!/usr/bin/env python

import random

MIN_NUMBER = 1
MAX_NUMBER = 100
INTRODUCTION_TO_GAME =\
    'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    if has_even(number) == 0:
        return number, 'yes'
    return number, 'no'


def has_even(number):
    return number % 2
