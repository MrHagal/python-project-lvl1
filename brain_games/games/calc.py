#!/usr/bin/env python

import operator
import random

START_INTERVAL = 1
END_INTERVAL = 10
INTRODUCTION_TO_GAME =\
    'What is the result of the expression?'

operation_signs = \
    {'+': operator.add,
     '-': operator.sub,
     '*': operator.mul,
     }


def question_answer():
    number_1 = random.randint(START_INTERVAL, END_INTERVAL)
    number_2 = random.randint(START_INTERVAL, END_INTERVAL)
    signs = tuple(operation_signs.items())
    sign_operator, action = random.choice(signs)
    question, answer = calculation_calc(
        number_1, number_2, sign_operator, action)
    return question, answer


def calculation_calc(number_1, number_2, sign_operator, action):
    result_calculation = action(number_1, number_2)
    game_question = f'{number_1} {sign_operator} {number_2}'
    return game_question, result_calculation
