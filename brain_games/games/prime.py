#!/usr/bin/env python
import random

START_INTERVAL = 2
END_INTERVAL = 100
MIN_PRIME = 2


def introduction_to_game():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def random_number():
    max_prime = random.randint(START_INTERVAL, END_INTERVAL)
    return max_prime


def check_prime():
    max_prime = random_number()
    for iterator_prime in range(MIN_PRIME, max_prime):
        if max_prime % iterator_prime == 0 and max_prime != iterator_prime:
            return max_prime, 'no'
    return max_prime, 'yes'
