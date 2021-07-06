#!/usr/bin/env python
import prompt


def check_games(name, result_answer, count_all, expression):
    print('Question', *result_answer[0])
    answer = prompt.string('Your answer: ')
    if str(result_answer[1]) == answer:
        expression += 1
        if expression == count_all:
            print(f'Congratulations, {name}!')
            return expression
        else:
            print('Correct!')
            return expression
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{result_answer[1]}'.\n Let's try again, {name}!")
        expression = count_all
        return expression


# check_games('Andrey', ([5, 13, 21, 29, 37, '..', 53, 61], 45), 3, 0)
