#!/usr/bin/env python
import random

START_INTERVAL = 2
END_INTERVAL = 5


def introduction_to_game():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def ago_prime():
    number = random.randint(START_INTERVAL, END_INTERVAL)
    return number


def run_prime():
    number = ago_prime()
    for i in range(2, number):
        if number % i == 0 and number != i:
            return number, 'no'
    return number, 'yes'
