#!/usr/bin/env python

import prompt

NUMBER_GAMES = 3


def run_engine(create_question_answer, INTRODUCTION_TO_GAME):
    break_count_game = 0
    print('Welcome to the Brain Games!')
    name_player = prompt.string('May I have your name? ')
    print(f'Hello, {name_player}!')
    print(INTRODUCTION_TO_GAME)
    while break_count_game != NUMBER_GAMES:
        question, correct_answer = create_question_answer()
        print(f"Question: {question}")
        your_answer = prompt.string('Your answer: ')
        if str(correct_answer) == your_answer:
            break_count_game += 1
            if break_count_game == NUMBER_GAMES:
                print(f'Congratulations, {name_player}!')
                return break_count_game
            else:
                print('Correct!')
        else:
            print(f"'{your_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\n Let's try again, {name_player}!")
            break_count_game = NUMBER_GAMES
