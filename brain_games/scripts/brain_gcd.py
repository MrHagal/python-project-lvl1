#!/usr/bin/env python
import random
from brain_games.scripts.brain_games import main2


def nod():
    name = main2()
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count != 3:
        number_1 = random.randint(1, 10)
        number_2 = random.randint(1, 10)
        print(f'Question: {number_1} {number_2}')
        # НОД
        while number_2 > 0:
            number_1, number_2 = number_2, number_1 % number_2
        result = number_1
        # НОД
        answer = input('Your answer: ')
        if str(result) == answer:
            count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\n"
                  f"Let's try again, {name}!")
            break
        if count == 3:
            print(f'Congratulations, {name}!')

