#!/usr/bin/env python
import random

MIN_NUMBER = 1
MAX_NUMBER = 10
INTRODUCTION_TO_GAME =\
    'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    number_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{number_1} {number_2}'
    answer = has_gcd(number_1, number_2)
    return question, answer


def has_gcd(number_1, number_2):
    while number_2 > 0:
        number_1, number_2 = number_2, number_1 % number_2
    return number_1
