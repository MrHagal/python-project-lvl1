#!/usr/bin/env python

import operator
import random

MAX_RANDOM = 1
MIN_RANDOM = 10
INTRODUCTION_TO_GAME =\
    'What is the result of the expression?'

operation_signs = \
    {'+': operator.add,
     '-': operator.sub,
     '*': operator.mul,
     }


def question_answer():
    number_1 = random.randint(MAX_RANDOM, MIN_RANDOM)
    number_2 = random.randint(MAX_RANDOM, MIN_RANDOM)
    signs = tuple(operation_signs.items())
    operator_sign, action = random.choice(signs)
    question, answer = calculation_calc(
        number_1, number_2, operator_sign, action)
    return question, answer


def calculation_calc(number_1, number_2, operator_sign, action):
    result_calculation = action(number_1, number_2)
    game_question = f'{number_1} {operator_sign} {number_2}'
    return game_question, result_calculation
