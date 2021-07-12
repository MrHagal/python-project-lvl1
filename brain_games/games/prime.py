#!/usr/bin/env python
import random


def introduction_to_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def run_prime():
    number = random.randint(2, 30)
    if number > 1:
        for i in range(2, number):
            if number % i == 0 and number != i:
                return [number], 'no'
        return [number], 'yes'
