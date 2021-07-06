#!/usr/bin/env python

import random


def introduction_question():
    print('What number is missing in the progression?')


def progression_up():  # генерируем лист
    random_list = []
    while len(random_list) not in range(5, 10):
        random_list = []
        number_1 = random.randint(1, 50)
        number_2 = random.randint(51, 100)
        step = random.randint(1, 20)  # шаг
        for i in range(number_1, number_2, step):  # формируем лист
            random_list.append(i)
    return random_list


def random_point():  # random index
    random_list = progression_up()
    random_point_list = random.randint(0, len(random_list) - 1)  # random index
    result = random_list[random_point_list]  # результат для сверки
    random_list[random_point_list] = '..'  # замена index на '..'
    return random_list, result
