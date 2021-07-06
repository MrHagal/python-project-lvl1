#!/usr/bin/env python

from brain_games.welcome_games import welcome_user
from brain_games.сongratulations_defeat import check_games


def count_algo_check(algo_games, introduction):
    count_all = 3  # определяем константу количество игр
    expression = 0  # счетчик игр
    name = welcome_user()  # приветствуем и вводим имя
    introduction()  # Краткое введение в игру
    while expression != count_all:
        result_answer = algo_games()  # функция алгорима передаваемая как аргумент
        expression = check_games(name, result_answer, count_all, expression)
