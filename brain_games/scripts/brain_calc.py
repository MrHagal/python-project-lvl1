#!/usr/bin/env python
import random
import operator
from brain_games.scripts.brain_games import main2


def calc():
    name = main2()
    print('What is the result of the expression?')
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    operation_sign = \
        {'+': operator.add,
         '-': operator.sub,
         '*': operator.mul,
         }
    count = 0
    while count != 3:
        actions = list(operation_sign.keys())  # конвертируем dict в list для choice
        chosen = random.choice(actions)
        result = operation_sign[chosen](number_1, number_2)  # получаем результат от ариф. операции
        print(f'Question: {number_1} {chosen} {number_2}')
        answer = input('Your answer: ')
        if str(result) == answer:
            count += 1
            print('Correct!')
            if count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\n"
            f"Let's try again, {name}")
            break
