#!/usr/bin/env python
import prompt


def check_result_game(
        name_player, result_calculation_algo,
        NUMBER_GAMES, count_game_attempt):
    print('Question:', *result_calculation_algo[0])
    answer = prompt.string('Your answer: ')
    if str(result_calculation_algo[1]) == answer:
        count_game_attempt += 1
        if count_game_attempt == NUMBER_GAMES:
            print(f'Congratulations, {name_player}!')
            return count_game_attempt
        else:
            print('Correct!')
            return count_game_attempt
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{result_calculation_algo[1]}'."
              f"\n Let's try again, {name_player}!")
        count_game_attempt = NUMBER_GAMES
        return count_game_attempt
