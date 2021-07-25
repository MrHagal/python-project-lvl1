#!/usr/bin/env python
import random

START_INTERVAL = 2
END_INTERVAL = 89
INTRODUCTION_TO_GAME =\
    'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime():
    max_prime = random.randint(START_INTERVAL, END_INTERVAL)
    if is_prime(max_prime):
        return max_prime, 'yes'
    return max_prime, 'no'


def is_prime(max_prime):
    for iterator_prime in range(START_INTERVAL, max_prime):
        if max_prime % iterator_prime == 0:
            return False
    return True
