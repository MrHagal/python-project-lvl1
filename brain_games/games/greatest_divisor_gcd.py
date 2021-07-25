#!/usr/bin/env python
import random

START_INTERVAL = 1
END_INTERVAL = 10
INTRODUCTION_TO_GAME = 'Find the greatest common divisor of given numbers.'


def question_answer():
    number_1 = random.randint(START_INTERVAL, END_INTERVAL)
    number_2 = random.randint(START_INTERVAL, END_INTERVAL)
    question = f'{number_1} {number_2}'
    answer = has_gcd(number_1, number_2)
    return question, answer


def has_gcd(number_1, number_2):
    while number_2 > 0:
        number_1, number_2 = number_2, number_1 % number_2
    return number_1
