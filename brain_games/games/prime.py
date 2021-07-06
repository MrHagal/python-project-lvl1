#!/usr/bin/env python
import random


def introduction_question():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def prime_up():
    number = random.randint(2, 30)
    if number > 1:
        for i in range(2, number):
            if number % i == 0 and number != i:
                return [number], 'no'
        return [number], 'yes'
