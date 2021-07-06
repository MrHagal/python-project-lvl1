#!/usr/bin/env python

import operator
import random


def introduction_question():
    print('What is the result of the expression?')


def calc_up():
    operation_sign = \
        {'+': operator.add,
         '-': operator.sub,
         '*': operator.mul,
         }
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    actions = list(operation_sign.keys())
    chosen = random.choice(actions)
    result = operation_sign[chosen](number_1, number_2)
    number_chosen = [number_1, chosen, number_2]
    return number_chosen, result
