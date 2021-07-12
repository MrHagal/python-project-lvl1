#!/usr/bin/env python

import random


def introduction_to_game():
    print('What number is missing in the progression?')


def run_progression():
    random_lists = []
    while len(random_lists) not in range(5, 10):
        random_lists = []
        number_1 = random.randint(1, 50)
        number_2 = random.randint(51, 100)
        step = random.randint(1, 20)
        for i in range(number_1, number_2, step):
            random_lists.append(i)
    return random_lists


def random_point():
    random_lists = run_progression()
    random_hidden_value = random.randint(0, len(random_lists) - 1)
    hidden_number = random_lists[random_hidden_value]
    random_lists[random_hidden_value] = '..'
    return random_lists, hidden_number
