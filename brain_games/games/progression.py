#!/usr/bin/env python
import random

MAX_RANDOM_LENGTH = 5
MIN_RANDOM_LENGTH = 10
MAX_RANDOM_STEP = 2
MIN_RANDOM_STEP = 20
INTRODUCTION_TO_GAME = 'What number is missing in the progression?'


def hidden_value_progression():
    length = random.randint(MAX_RANDOM_LENGTH, MIN_RANDOM_LENGTH)
    step = random.randint(MAX_RANDOM_STEP, MIN_RANDOM_STEP)
    progression_lists = arithmetic_progression(length, step)
    random_hidden_value = random.randint(0, len(progression_lists) - 1)
    answer = progression_lists[random_hidden_value]
    progression_lists[random_hidden_value] = '..'
    question = ' '.join(list(map(str, progression_lists)))
    return question, answer


def arithmetic_progression(length, step):
    progression_lists = []
    for item in range(1, length + 1):
        item *= step
        progression_lists.append(item)
    return progression_lists
