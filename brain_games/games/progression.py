#!/usr/bin/env python
import random

START_LENGTH = 5
END_LENGTH = 10
START_STEP = 2
END_STEP = 20
INTRODUCTION_TO_GAME = 'What number is missing in the progression?'


def hidden_value_progression():
    length = random.randint(START_LENGTH, END_LENGTH)
    step = random.randint(START_STEP, END_STEP)
    progression_lists = arithmetic_progression(length, step)
    random_hidden_value = random.randint(0, len(progression_lists) - 1)
    answer = progression_lists[random_hidden_value]
    progression_lists[random_hidden_value] = '..'
    question = ' '.join(list(map(str, progression_lists)))
    return question, answer


def arithmetic_progression(length, step):
    progression_lists = []
    for iterator in range(1, length + 1):
        iterator *= step
        progression_lists.append(iterator)
    return progression_lists
