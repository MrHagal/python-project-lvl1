#!/usr/bin/env python

import random


def introduction_question():
    print('Find the greatest common divisor of given numbers.')


def gcd_up():
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    question = [number_1, number_2]
    while number_2 > 0:
        number_1, number_2 = number_2, number_1 % number_2
    return question, number_1
