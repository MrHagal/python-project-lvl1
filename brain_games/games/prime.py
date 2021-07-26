#!/usr/bin/env python
import random

MIN_LENGTH = 2
MAX_LENGTH = 89
INTRODUCTION_TO_GAME =\
    'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_and_answer():
    max_prime = random.randint(MIN_LENGTH, MAX_LENGTH)
    if is_prime(max_prime):
        return max_prime, 'yes'
    return max_prime, 'no'


def is_prime(max_prime):
    for number in range(MIN_LENGTH, max_prime):
        if max_prime % number == 0:
            return False
    return True
