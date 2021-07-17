#!/usr/bin/env python

import prompt

from brain_games.welcome_games import hello_player

NUMBER_GAMES = 3  # количество игр всего



def run_engine(run_game, introduction_to_game):
    count_game_attempt = 0  # считаем попытки игры
    name_player = hello_player()
    print(introduction_to_game())  # краткое введение в игру
    while count_game_attempt != NUMBER_GAMES:
        result_calculation_algo = run_game()
        print(f"Question: {result_calculation_algo[0]}")
        answer = prompt.string('Your answer: ')
        if str(result_calculation_algo[1]) == answer:
            count_game_attempt += 1
            if count_game_attempt == NUMBER_GAMES:
                print(f'Congratulations, {name_player}!')
                return count_game_attempt
            else:
                print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result_calculation_algo[1]}'."
                  f"\n Let's try again, {name_player}!")
            count_game_attempt = NUMBER_GAMES