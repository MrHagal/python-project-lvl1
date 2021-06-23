#!/usr/bin/env python
import random
from brain_games.scripts.brain_games import main2


def parity_check():
    count = 0
    name = main2()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count != 3:
        number = random.randint(1, 100)
        print('Question:', number)
        answer = input('Your answer: ')
        if number % 2 == 0 and answer == 'yes':
            count += 1
            print('Correct')
        elif number % 2 != 0 and answer == 'no':
            count += 1
            print('Correct')
        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'."
                  f"\nLet's try again, {name}!")
            break
        if count == 3:
            print(f'Congratulations, {name}!')
