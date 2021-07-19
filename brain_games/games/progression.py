#!/usr/bin/env python
import random

START_INTERVAL_1 = 1
END_INTERVAL_2 = 50
START_INTERVAL_3 = 51
END_INTERVAL_4 = 100


def introduction_to_game():
    return 'What number is missing in the progression?'


def arithmetic_progression():
    min_number_1 = random.randint(START_INTERVAL_1, END_INTERVAL_2)
    max_number_2 = random.randint(START_INTERVAL_3, END_INTERVAL_4)
    progression_lists = []
    while len(progression_lists) not in range(5, 10):
        step = random.randint(1, 20)
        generating_progression = iter(range(min_number_1, max_number_2, step))
        progression_lists = list(generating_progression)
    return progression_lists


def hidden_value_progression():
    progression_lists = arithmetic_progression()
    random_hidden_value = random.randint(0, len(progression_lists) - 1)
    answer_game = progression_lists[random_hidden_value]
    progression_lists[random_hidden_value] = '..'
    game_question = ' '.join(list(map(str, progression_lists)))
    return game_question, answer_game
