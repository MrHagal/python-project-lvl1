#!/usr/bin/env python
import random

MAX_RANDOM = 2
MIN_RANDOM = 89
INTRODUCTION_TO_GAME =\
    'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime():
    max_prime = random.randint(MAX_RANDOM, MIN_RANDOM)
    if is_prime(max_prime):
        return max_prime, 'yes'
    return max_prime, 'no'


def is_prime(max_prime):
    for item in range(MAX_RANDOM, max_prime):
        if max_prime % item == 0:
            return False
    return True
