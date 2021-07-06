#!/usr/bin/env python

from brain_games.welcome_games import welcome_user
from brain_games.сongratulations_defeat import check_games


def count_algo_check(algo_games, introduction):
    # определяем константу количество игр
    count_all = 3
    # счетчик игр
    expression = 0
    # приветствуем и вводим имя
    name = welcome_user()
    # Краткое введение в игру
    introduction()
    while expression != count_all:
        # функция алгорима передаваемая как аргумент
        result_answer = algo_games()
        expression = check_games(name, result_answer, count_all, expression)
