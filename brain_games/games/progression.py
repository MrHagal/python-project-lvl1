#!/usr/bin/env python
import random

MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_STEP = 2
MAX_STEP = 20
INTRODUCTION_TO_GAME = 'What number is missing in the progression?'


def generate_question_and_answer():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    step = random.randint(MIN_STEP, MAX_STEP)
    progression_lists = arithmetic_progression(length, step)
    random_hidden_value = random.randint(0, len(progression_lists) - 1)
    answer = progression_lists[random_hidden_value]
    progression_lists[random_hidden_value] = '..'
    question = ' '.join(list(map(str, progression_lists)))
    return question, answer


def arithmetic_progression(length, step):
    progression_lists = []
    for number in range(1, length + 1):
        number *= step
        progression_lists.append(number)
    return progression_lists
