#!/usr/bin/env python

import random

START_INTERVAL_1 = 1
END_INTERVAL_2 = 50
START_INTERVAL_3 = 51
END_INTERVAL_4 = 100


def introduction_to_game():
    return 'What number is missing in the progression?'


def random_number_list():
    number_1 = random.randint(START_INTERVAL_1, END_INTERVAL_2)
    number_2 = random.randint(START_INTERVAL_3, END_INTERVAL_4)
    random_lists = []
    while len(random_lists) not in range(5, 10):
        step = random.randint(1, 20)
        i = iter(range(number_1, number_2, step))
        random_lists = list(i)
    return random_lists


def run_progression():
    random_lists = random_number_list()
    random_hidden_value = random.randint(0, len(random_lists) - 1)
    hidden_number = random_lists[random_hidden_value]
    random_lists[random_hidden_value] = '..'
    return random_lists, hidden_number
