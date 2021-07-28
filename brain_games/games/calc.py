#!/usr/bin/env python

import operator
import random

MIN_NUMBER = 1
MAX_NUMBER = 100
INTRODUCTION_TO_GAME =\
    'What is the result of the expression?'

operation_signs = \
    {'+': operator.add,
     '-': operator.sub,
     '*': operator.mul,
     }


def generate_question_and_answer():
    number_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    signs = tuple(operation_signs.items())
    operator_sign, action = random.choice(signs)
    question, answer = calculation_calc(
        number_1, number_2, operator_sign, action)
    return question, answer


def calculation_calc(number_1, number_2, operator_sign, action):
    result_calculation = action(number_1, number_2)
    arithmetic_action = f'{number_1} {operator_sign} {number_2}'
    return arithmetic_action, result_calculation
