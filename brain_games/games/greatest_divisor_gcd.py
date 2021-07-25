#!/usr/bin/env python
import random

MAX_RANDOM = 1
MIN_RANDOM = 10
INTRODUCTION_TO_GAME =\
    'Find the greatest common divisor of given numbers.'


def question_answer():
    number_1 = random.randint(MAX_RANDOM, MIN_RANDOM)
    number_2 = random.randint(MAX_RANDOM, MIN_RANDOM)
    question = f'{number_1} {number_2}'
    answer = has_gcd(number_1, number_2)
    return question, answer


def has_gcd(number_1, number_2):
    while number_2 > 0:
        number_1, number_2 = number_2, number_1 % number_2
    return number_1
