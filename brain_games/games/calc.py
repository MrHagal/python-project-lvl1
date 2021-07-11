#!/usr/bin/env python

import operator
import random


def introduction_to_game():
    print('What is the result of the expression?')


def run_calc():
    operation_signs = \
        {'+': operator.add,
         '-': operator.sub,
         '*': operator.mul,
         }
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    sign = list(operation_signs.keys())
    random_chosen_sign = random.choice(sign)
    result_calculation = operation_signs[random_chosen_sign](number_1, number_2)
    arithmetic_operations = [number_1, random_chosen_sign, number_2]
    return arithmetic_operations, result_calculation
