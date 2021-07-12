#!/usr/bin/env python

from brain_games.welcome_games import hello_player
from brain_games.check_result_games import check_result_game


def run_engine(run_game, introduction_to_game):
    NUMBER_GAMES = 3  # количество игр всего
    count_game_attempt = 0  # считаем попытки игры
    name_player = hello_player()
    introduction_to_game()  # краткое введение в игру
    while count_game_attempt != NUMBER_GAMES:
        result_calculation_algo = run_game()
        count_game_attempt = check_result_game(
            name_player, result_calculation_algo,
            NUMBER_GAMES, count_game_attempt)
